from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any

from .config import GenerationOptions


DEFAULT_OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
ALLOWED_OPENROUTER_HOSTS = frozenset({"openrouter.ai"})


class OpenRouterError(RuntimeError):
    """Falha HTTP da Image API do OpenRouter."""


def redact(text: str, api_key: str) -> str:
    """Remove a credencial de qualquer texto vindo do upstream."""

    key = (api_key or "").strip()
    if not key:
        return text
    return text.replace(key, "[REDIGIDO]")


def validate_base_url(base_url: str) -> str:
    """A credencial viaja no header; só destinos confiáveis são aceitos."""

    candidate = (base_url or "").strip().rstrip("/")
    if not candidate:
        raise OpenRouterError("A base URL da OpenRouter não pode ser vazia.")
    parsed = urllib.parse.urlparse(candidate)
    if parsed.scheme != "https":
        raise OpenRouterError(
            f"A base URL da OpenRouter precisa usar https: {candidate}"
        )
    if parsed.hostname not in ALLOWED_OPENROUTER_HOSTS:
        permitidos = ", ".join(sorted(ALLOWED_OPENROUTER_HOSTS))
        raise OpenRouterError(
            f"Host não autorizado para a OpenRouter: {parsed.hostname}. "
            f"Hosts permitidos: {permitidos}."
        )
    return candidate


def _error_message(status: int, payload: Any) -> str:
    detail = ""
    if isinstance(payload, dict):
        error = payload.get("error")
        if isinstance(error, dict):
            detail = str(error.get("message") or "").strip()
        elif isinstance(error, str):
            detail = error.strip()
        elif payload.get("message"):
            detail = str(payload["message"]).strip()
    if status == 401:
        base = "Chave OpenRouter inválida ou ausente."
    elif status == 402:
        base = "Créditos insuficientes na OpenRouter."
    elif status == 404:
        base = "Modelo de imagem não encontrado na OpenRouter."
    else:
        base = f"A OpenRouter respondeu HTTP {status}."
    return f"{base} {detail}".strip()


def json_request(
    method: str,
    url: str,
    *,
    api_key: str,
    payload: dict[str, Any] | None = None,
    timeout: float,
) -> tuple[Any, str | None]:
    data = None
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "User-Agent": "autor-gerador/1.0",
        "HTTP-Referer": "https://local.autor-fund1",
        "X-Title": "Autores Fundamental I",
    }
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            request_id = response.headers.get("x-request-id")
            if not raw.strip():
                return {}, request_id
            try:
                parsed = json.loads(raw)
            except json.JSONDecodeError as exc:
                trecho = redact(raw[:300], api_key)
                raise OpenRouterError(
                    f"A OpenRouter devolveu resposta inválida, fora de JSON: {trecho}"
                ) from exc
            return parsed, request_id
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(raw) if raw.strip() else {}
        except json.JSONDecodeError:
            parsed = {"error": {"message": raw[:300]}}
        mensagem = redact(_error_message(exc.code, parsed), api_key)
        raise OpenRouterError(mensagem) from exc
    except urllib.error.URLError as exc:
        motivo = redact(str(exc.reason), api_key)
        raise OpenRouterError(f"Falha de rede na OpenRouter: {motivo}") from exc
    except TimeoutError as exc:
        raise OpenRouterError("Timeout na OpenRouter.") from exc


@dataclass
class OpenRouterImageItem:
    b64_json: str


@dataclass
class OpenRouterImageResponse:
    data: list[OpenRouterImageItem]
    usage: dict[str, Any] | None
    _request_id: str | None


class OpenRouterImages:
    def __init__(self, client: "OpenRouterClient") -> None:
        self._client = client

    def generate(self, **kwargs: Any) -> OpenRouterImageResponse:
        payload, request_id = self._client.request(
            "POST",
            "/images",
            payload=kwargs,
        )
        rows = payload.get("data") if isinstance(payload, dict) else None
        if not isinstance(rows, list):
            raise OpenRouterError("A OpenRouter não devolveu a lista data de imagens.")
        items: list[OpenRouterImageItem] = []
        for row in rows:
            if not isinstance(row, dict) or not row.get("b64_json"):
                raise OpenRouterError("A OpenRouter devolveu uma imagem sem b64_json.")
            items.append(OpenRouterImageItem(b64_json=str(row["b64_json"])))
        usage = payload.get("usage") if isinstance(payload.get("usage"), dict) else None
        return OpenRouterImageResponse(
            data=items,
            usage=usage,
            _request_id=request_id or (
                str(payload["id"]) if isinstance(payload.get("id"), str) else None
            ),
        )


class OpenRouterClient:
    def __init__(
        self,
        api_key: str,
        options: GenerationOptions,
        base_url: str = DEFAULT_OPENROUTER_BASE_URL,
    ) -> None:
        self.api_key = api_key
        self.timeout = options.timeout
        self.max_retries = options.max_retries
        self.base_url = validate_base_url(base_url)
        self.images = OpenRouterImages(self)

    def request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
    ) -> tuple[Any, str | None]:
        url = f"{self.base_url}{path}"
        attempts = self.max_retries + 1
        last_error: OpenRouterError | None = None
        for attempt in range(attempts):
            try:
                return json_request(
                    method,
                    url,
                    api_key=self.api_key,
                    payload=payload,
                    timeout=self.timeout,
                )
            except OpenRouterError as exc:
                last_error = exc
                retryable = "HTTP 429" in str(exc) or "HTTP 5" in str(exc)
                if not retryable or attempt + 1 >= attempts:
                    raise
                time.sleep(0.4 * (attempt + 1))
        assert last_error is not None
        raise last_error

    def check_image_model(self, model: str) -> str:
        key_payload, _ = self.request("GET", "/key")
        if not isinstance(key_payload, dict) or "data" not in key_payload:
            raise OpenRouterError("A OpenRouter não confirmou a chave em /key.")
        model_path = "/images/models/" + "/".join(
            part for part in model.split("/") if part
        )
        model_payload, _ = self.request("GET", f"{model_path}/endpoints")
        if not isinstance(model_payload, dict):
            raise OpenRouterError("A OpenRouter não devolveu o modelo de imagem.")
        model_id = str(model_payload.get("id") or "").strip()
        endpoints = model_payload.get("endpoints")
        if not isinstance(endpoints, list) or not endpoints:
            raise OpenRouterError(
                f"A OpenRouter não listou endpoint de imagem para {model}."
            )
        if model_id and model_id != model:
            raise OpenRouterError(
                f"A OpenRouter devolveu o modelo {model_id}, não {model}."
            )
        return model_id or model
