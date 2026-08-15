from __future__ import annotations

import io
import json
import unittest
import urllib.error
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from gerador_imagens.config import ConfigError, GenerationOptions
from gerador_imagens.core import GenerationError, build_client, generate_image
from gerador_imagens.openrouter import (
    OpenRouterClient,
    OpenRouterError,
    json_request,
)


API_KEY = "sk-or-CHAVE-SECRETA-DE-TESTE"


def _options(**overrides) -> GenerationOptions:
    base = {
        "model": "qwen/qwen-image-3-pro",
        "size": "auto",
        "quality": "medium",
        "output_format": "png",
        "background": "auto",
        "moderation": "auto",
        "aspect_ratio": "2:3",
        "resolution": "2k",
        "timeout": 5.0,
        "max_retries": 0,
    }
    base.update(overrides)
    return GenerationOptions(**base)


class FakeResponse(io.BytesIO):
    def __init__(self, body: bytes, headers: dict[str, str] | None = None) -> None:
        super().__init__(body)
        self.headers = headers or {}

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *args) -> None:
        self.close()


class JsonRequestTest(unittest.TestCase):
    """A API pode responder 200 com corpo que não é JSON."""

    def test_corpo_nao_json_com_status_200_vira_openrouter_error(self) -> None:
        with patch(
            "urllib.request.urlopen",
            return_value=FakeResponse(b"<html>manutencao</html>"),
        ):
            with self.assertRaises(OpenRouterError) as ctx:
                json_request(
                    "POST",
                    "https://openrouter.ai/api/v1/images",
                    api_key=API_KEY,
                    payload={"model": "qwen/qwen-image-3-pro"},
                    timeout=5.0,
                )
        self.assertIn("resposta inválida", str(ctx.exception).lower())

    def test_corpo_vazio_com_status_200_nao_quebra(self) -> None:
        with patch("urllib.request.urlopen", return_value=FakeResponse(b"")):
            parsed, _ = json_request(
                "GET",
                "https://openrouter.ai/api/v1/key",
                api_key=API_KEY,
                timeout=5.0,
            )
        self.assertEqual(parsed, {})

    def test_chave_nunca_aparece_na_mensagem_de_erro(self) -> None:
        vazamento = json.dumps(
            {"error": {"message": f"No auth credentials found: Bearer {API_KEY}"}}
        ).encode("utf-8")
        erro = urllib.error.HTTPError(
            "https://openrouter.ai/api/v1/images",
            401,
            "Unauthorized",
            {},
            io.BytesIO(vazamento),
        )
        with patch("urllib.request.urlopen", side_effect=erro):
            with self.assertRaises(OpenRouterError) as ctx:
                json_request(
                    "POST",
                    "https://openrouter.ai/api/v1/images",
                    api_key=API_KEY,
                    payload={},
                    timeout=5.0,
                )
        mensagem = str(ctx.exception)
        self.assertNotIn(API_KEY, mensagem)
        self.assertIn("[REDIGIDO]", mensagem)


class BaseUrlTest(unittest.TestCase):
    """A chave viaja no header; o destino precisa ser confiável."""

    def test_base_url_sem_https_e_recusada(self) -> None:
        with self.assertRaises(OpenRouterError):
            OpenRouterClient(
                API_KEY,
                _options(),
                base_url="http://openrouter.ai/api/v1",
            )

    def test_host_nao_autorizado_e_recusado(self) -> None:
        with self.assertRaises(OpenRouterError):
            OpenRouterClient(
                API_KEY,
                _options(),
                base_url="https://coletor-de-chaves.example/api/v1",
            )

    def test_host_oficial_e_aceito(self) -> None:
        cliente = OpenRouterClient(
            API_KEY,
            _options(),
            base_url="https://openrouter.ai/api/v1/",
        )
        self.assertEqual(cliente.base_url, "https://openrouter.ai/api/v1")

    def test_build_client_recusa_base_url_do_ambiente_insegura(self) -> None:
        with patch.dict(
            "os.environ",
            {"OPENROUTER_BASE_URL": "http://interno.example/v1"},
            clear=False,
        ):
            with self.assertRaises((OpenRouterError, GenerationError)):
                build_client(API_KEY, _options(), "openrouter", root=Path("."))


class GenerateImageTravasTest(unittest.TestCase):
    """As travas do AGENTS.md não podem valer só no carregador de projeto."""

    def _cliente_falso(self):
        return SimpleNamespace(
            images=SimpleNamespace(
                generate=lambda **kwargs: self.fail(
                    "A API não pode ser chamada quando a configuração é inválida."
                )
            )
        )

    def _gerar(self, tmp: Path, **overrides):
        return generate_image(
            client=self._cliente_falso(),
            prompt="prompt de teste",
            output=tmp / "saida.png",
            options=_options(**overrides),
            provider="openrouter",
        )

    def test_resolucao_ausente_nao_e_inventada(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as raw:
            with self.assertRaises(GenerationError):
                self._gerar(Path(raw), resolution=None)

    def test_proporcao_ausente_e_recusada(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as raw:
            with self.assertRaises(GenerationError):
                self._gerar(Path(raw), aspect_ratio=None)

    def test_formato_diferente_de_png_e_recusado(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as raw:
            with self.assertRaises(GenerationError):
                self._gerar(Path(raw), output_format="jpeg")

    def test_tamanho_precisa_ser_auto(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as raw:
            with self.assertRaises(GenerationError):
                self._gerar(Path(raw), size="1024x1536")

    def test_quantidade_acima_de_seis_e_recusada(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as raw:
            with self.assertRaises(GenerationError):
                self._gerar(Path(raw), n=7)


class ImagesResponseTest(unittest.TestCase):
    def _cliente(self) -> OpenRouterClient:
        return OpenRouterClient(API_KEY, _options())

    def test_data_ausente_vira_erro_tratado(self) -> None:
        with patch(
            "urllib.request.urlopen",
            return_value=FakeResponse(json.dumps({"id": "x"}).encode("utf-8")),
        ):
            with self.assertRaises(OpenRouterError):
                self._cliente().images.generate(model="qwen/qwen-image-3-pro")

    def test_linha_sem_b64_json_vira_erro_tratado(self) -> None:
        corpo = json.dumps({"data": [{"url": "https://exemplo/imagem.png"}]})
        with patch(
            "urllib.request.urlopen",
            return_value=FakeResponse(corpo.encode("utf-8")),
        ):
            with self.assertRaises(OpenRouterError):
                self._cliente().images.generate(model="qwen/qwen-image-3-pro")

    def test_caminho_feliz_devolve_itens_e_request_id(self) -> None:
        corpo = json.dumps({"data": [{"b64_json": "QUJD"}], "usage": {"cost": 1}})
        with patch(
            "urllib.request.urlopen",
            return_value=FakeResponse(
                corpo.encode("utf-8"),
                {"x-request-id": "req-123"},
            ),
        ):
            resposta = self._cliente().images.generate(
                model="qwen/qwen-image-3-pro",
            )
        self.assertEqual(len(resposta.data), 1)
        self.assertEqual(resposta.data[0].b64_json, "QUJD")
        self.assertEqual(resposta._request_id, "req-123")


class CheckImageModelTest(unittest.TestCase):
    def test_modelo_divergente_e_recusado(self) -> None:
        respostas = [
            FakeResponse(json.dumps({"data": {"label": "chave"}}).encode("utf-8")),
            FakeResponse(
                json.dumps(
                    {"id": "outro/modelo", "endpoints": [{"name": "e"}]}
                ).encode("utf-8")
            ),
        ]
        with patch("urllib.request.urlopen", side_effect=respostas):
            cliente = OpenRouterClient(API_KEY, _options())
            with self.assertRaises(OpenRouterError):
                cliente.check_image_model("qwen/qwen-image-3-pro")

    def test_modelo_confirmado(self) -> None:
        respostas = [
            FakeResponse(json.dumps({"data": {"label": "chave"}}).encode("utf-8")),
            FakeResponse(
                json.dumps(
                    {
                        "id": "qwen/qwen-image-3-pro",
                        "endpoints": [{"name": "e"}],
                    }
                ).encode("utf-8")
            ),
        ]
        with patch("urllib.request.urlopen", side_effect=respostas):
            cliente = OpenRouterClient(API_KEY, _options())
            self.assertEqual(
                cliente.check_image_model("qwen/qwen-image-3-pro"),
                "qwen/qwen-image-3-pro",
            )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
