from __future__ import annotations

import base64
import hashlib
import json
import os
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI
from PIL import Image, ImageOps, UnidentifiedImageError

from .config import GenerationOptions, output_paths, validate_size


class GenerationError(RuntimeError):
    """Falha local de geração ou validação."""


@dataclass(frozen=True)
class GenerationResult:
    output_paths: list[Path]
    metadata_paths: list[Path]
    partial_paths: list[Path]
    request_id: str | None
    usage: dict[str, Any] | None


def load_api_key(root: Path) -> str:
    env_path = root / ".env"
    load_dotenv(env_path if env_path.exists() else None, override=False)
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise GenerationError(
            f"OPENAI_API_KEY não encontrada. Crie {root / '.env'} "
            "a partir de .env.example."
        )
    return api_key


def build_client(api_key: str, options: GenerationOptions) -> OpenAI:
    return OpenAI(
        api_key=api_key,
        timeout=options.timeout,
        max_retries=options.max_retries,
    )


def check_authentication(client: OpenAI, model: str) -> str:
    result = client.models.retrieve(model)
    return result.id


def load_prompt(path: Path) -> str:
    if not path.exists():
        raise GenerationError(f"Prompt não encontrado: {path}")
    if not path.is_file():
        raise GenerationError(f"O caminho do prompt não é um arquivo: {path}")
    prompt = path.read_text(encoding="utf-8").strip()
    if not prompt:
        raise GenerationError(f"O prompt está vazio: {path}")
    return prompt


def _decode_base64(value: str) -> bytes:
    if not value:
        raise GenerationError("A API retornou uma imagem vazia.")
    try:
        return base64.b64decode(value, validate=True)
    except (ValueError, TypeError) as exc:
        raise GenerationError("A API retornou base64 inválido.") from exc


def _normalize_pillow_format(value: str | None) -> str:
    normalized = (value or "").lower()
    if normalized == "jpg":
        normalized = "jpeg"
    return normalized


def validate_image_bytes(
    data: bytes,
    expected_format: str,
    expected_size: str,
) -> tuple[int, int, str]:
    try:
        with Image.open(BytesIO(data)) as image:
            actual_format = _normalize_pillow_format(image.format)
            width, height = image.size
            image.verify()
    except (UnidentifiedImageError, OSError, SyntaxError) as exc:
        raise GenerationError("Os bytes recebidos não formam uma imagem válida.") from exc
    if actual_format != expected_format:
        raise GenerationError(
            f"A API retornou {actual_format or 'formato desconhecido'}, "
            f"mas foi solicitado {expected_format}."
        )
    requested = validate_size(expected_size)
    if requested and (width, height) != requested:
        raise GenerationError(
            f"A API retornou {width}x{height}, mas foi solicitado {expected_size}."
        )
    return width, height, actual_format


def _atomic_write_bytes(path: Path, data: bytes, overwrite: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        raise GenerationError(
            f"A saída já existe: {path}. Use --forcar para substituir."
        )
    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temp_path = Path(handle.name)
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, path)
    finally:
        if temp_path and temp_path.exists():
            temp_path.unlink()


def _atomic_write_json(path: Path, payload: dict[str, Any], overwrite: bool) -> None:
    encoded = (
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    _atomic_write_bytes(path, encoded, overwrite)


def save_image(
    path: Path,
    data: bytes,
    options: GenerationOptions,
    overwrite: bool,
    expected_size: str | None = None,
) -> dict[str, Any]:
    width, height, actual_format = validate_image_bytes(
        data,
        options.output_format,
        expected_size or options.size,
    )
    _atomic_write_bytes(path, data, overwrite)
    return {
        "path": str(path),
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "width": width,
        "height": height,
        "format": actual_format,
    }


def _serialize(value: Any) -> Any:
    if value is None:
        return None
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")
    if isinstance(value, dict):
        return value
    return str(value)


def _request_kwargs(prompt: str, options: GenerationOptions) -> dict[str, Any]:
    kwargs: dict[str, Any] = {
        "model": options.model,
        "prompt": prompt,
        "size": options.size,
        "quality": options.quality,
        "output_format": options.output_format,
        "background": options.background,
        "moderation": options.moderation,
        "n": options.n,
    }
    if options.output_compression is not None:
        kwargs["output_compression"] = options.output_compression
    if options.stream:
        kwargs["stream"] = True
        kwargs["partial_images"] = options.partial_images
    return kwargs


def _metadata_payload(
    *,
    prompt: str,
    prompt_source: Path | None,
    author_id: str | None,
    project_source: Path | None,
    options: GenerationOptions,
    image_info: dict[str, Any],
    request_id: str | None,
    usage: dict[str, Any] | None,
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "provider": "openai",
        "model": options.model,
        "parameters": {
            "size": options.size,
            "quality": options.quality,
            "output_format": options.output_format,
            "output_compression": options.output_compression,
            "background": options.background,
            "moderation": options.moderation,
            "quantity": options.n,
            "stream": options.stream,
            "partial_images": options.partial_images,
            "timeout": options.timeout,
            "max_retries": options.max_retries,
        },
        "prompt": {
            "source": str(prompt_source) if prompt_source else None,
            "sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
            "characters": len(prompt),
            "words": len(prompt.split()),
        },
        "author": author_id,
        "project_source": str(project_source) if project_source else None,
        "request_id": request_id,
        "usage": usage,
        "image": image_info,
    }


def _save_metadata(
    output_path: Path,
    payload: dict[str, Any],
    overwrite: bool,
) -> Path:
    metadata_path = output_path.with_name(f"{output_path.stem}.metadata.json")
    _atomic_write_json(metadata_path, payload, overwrite)
    return metadata_path


def _metadata_path(output_path: Path) -> Path:
    return output_path.with_name(f"{output_path.stem}.metadata.json")


def _protect_planned_paths(paths: list[Path], overwrite: bool) -> None:
    occupied = [path for path in paths if path.exists()]
    if occupied and not overwrite:
        raise GenerationError(
            "Saída(s) já existente(s): "
            + ", ".join(str(path) for path in occupied)
            + ". Use --forcar para substituir."
        )


def _generate_regular(
    client: OpenAI,
    prompt: str,
    output: Path,
    options: GenerationOptions,
    overwrite: bool,
    prompt_source: Path | None,
    author_id: str | None,
    project_source: Path | None,
) -> GenerationResult:
    paths = output_paths(output, options.n, options.output_format)
    planned = list(paths)
    if options.write_metadata:
        planned.extend(_metadata_path(path) for path in paths)
    _protect_planned_paths(planned, overwrite)
    response = client.images.generate(**_request_kwargs(prompt, options))
    data = list(response.data or [])
    if len(data) != options.n:
        raise GenerationError(
            f"A API retornou {len(data)} imagem(ns); eram esperadas {options.n}."
        )
    request_id = getattr(response, "_request_id", None)
    usage = _serialize(getattr(response, "usage", None))
    decoded = [_decode_base64(getattr(item, "b64_json", "")) for item in data]
    for image_bytes in decoded:
        validate_image_bytes(image_bytes, options.output_format, options.size)
    metadata_paths: list[Path] = []
    for image_bytes, path in zip(decoded, paths, strict=True):
        image_info = save_image(path, image_bytes, options, overwrite)
        if options.write_metadata:
            payload = _metadata_payload(
                prompt=prompt,
                prompt_source=prompt_source,
                author_id=author_id,
                project_source=project_source,
                options=options,
                image_info=image_info,
                request_id=request_id,
                usage=usage,
            )
            metadata_paths.append(_save_metadata(path, payload, overwrite))
    return GenerationResult(paths, metadata_paths, [], request_id, usage)


def _generate_streaming(
    client: OpenAI,
    prompt: str,
    output: Path,
    options: GenerationOptions,
    overwrite: bool,
    prompt_source: Path | None,
    author_id: str | None,
    project_source: Path | None,
) -> GenerationResult:
    final_path = output_paths(output, 1, options.output_format)[0]
    planned = [final_path]
    if options.write_metadata:
        planned.append(_metadata_path(final_path))
    planned.extend(
        final_path.with_name(
            f"{final_path.stem}-parcial-{index:02d}{final_path.suffix}"
        )
        for index in range(1, options.partial_images + 1)
    )
    _protect_planned_paths(planned, overwrite)
    partial_paths: list[Path] = []
    final_bytes: bytes | None = None
    usage: dict[str, Any] | None = None
    request_id: str | None = None
    stream = client.images.generate(**_request_kwargs(prompt, options))
    for event in stream:
        request_id = (
            getattr(event, "_request_id", None)
            or getattr(event, "request_id", None)
            or request_id
        )
        event_type = getattr(event, "type", "")
        if event_type == "image_generation.partial_image":
            index = int(getattr(event, "partial_image_index", len(partial_paths))) + 1
            partial_path = final_path.with_name(
                f"{final_path.stem}-parcial-{index:02d}{final_path.suffix}"
            )
            partial_bytes = _decode_base64(getattr(event, "b64_json", ""))
            save_image(
                partial_path,
                partial_bytes,
                options,
                overwrite,
                expected_size="auto",
            )
            partial_paths.append(partial_path)
        elif event_type == "image_generation.completed":
            final_bytes = _decode_base64(getattr(event, "b64_json", ""))
            usage = _serialize(getattr(event, "usage", None))
    if final_bytes is None:
        raise GenerationError("O streaming terminou sem uma imagem final.")
    image_info = save_image(final_path, final_bytes, options, overwrite)
    metadata_paths: list[Path] = []
    if options.write_metadata:
        payload = _metadata_payload(
            prompt=prompt,
            prompt_source=prompt_source,
            author_id=author_id,
            project_source=project_source,
            options=options,
            image_info=image_info,
            request_id=request_id,
            usage=usage,
        )
        metadata_paths.append(_save_metadata(final_path, payload, overwrite))
    return GenerationResult(
        [final_path],
        metadata_paths,
        partial_paths,
        request_id,
        usage,
    )


def generate_image(
    *,
    client: OpenAI,
    prompt: str,
    output: Path,
    options: GenerationOptions,
    overwrite: bool = False,
    prompt_source: Path | None = None,
    author_id: str | None = None,
    project_source: Path | None = None,
) -> GenerationResult:
    prompt = prompt.strip()
    if not prompt:
        raise GenerationError("O prompt está vazio.")
    options = options.validated()
    if options.stream:
        return _generate_streaming(
            client,
            prompt,
            output,
            options,
            overwrite,
            prompt_source,
            author_id,
            project_source,
        )
    return _generate_regular(
        client,
        prompt,
        output,
        options,
        overwrite,
        prompt_source,
        author_id,
        project_source,
    )


def create_pdf(
    image_paths: list[Path],
    output_path: Path,
    overwrite: bool,
    dpi: int = 300,
) -> None:
    if not image_paths:
        raise GenerationError("Nenhuma imagem foi fornecida para o PDF.")
    if not 72 <= dpi <= 600:
        raise GenerationError("O DPI do PDF precisa estar entre 72 e 600.")
    if output_path.exists() and not overwrite:
        raise GenerationError(
            f"O PDF já existe: {output_path}. Use --forcar para substituir."
        )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pages: list[Image.Image] = []
    temp_path: Path | None = None
    try:
        for path in image_paths:
            if not path.exists():
                raise GenerationError(f"Imagem ausente para o PDF: {path}")
            with Image.open(path) as image:
                portrait = image.height >= image.width
                a4_portrait = (
                    round((210 / 25.4) * dpi),
                    round((297 / 25.4) * dpi),
                )
                canvas_size = (
                    a4_portrait if portrait else (a4_portrait[1], a4_portrait[0])
                )
                converted = image.convert("RGB")
                fitted = ImageOps.contain(
                    converted,
                    canvas_size,
                    method=Image.Resampling.LANCZOS,
                )
                converted.close()
                canvas = Image.new("RGB", canvas_size, "white")
                position = (
                    (canvas_size[0] - fitted.width) // 2,
                    (canvas_size[1] - fitted.height) // 2,
                )
                canvas.paste(fitted, position)
                fitted.close()
                pages.append(canvas)
        with tempfile.NamedTemporaryFile(
            dir=output_path.parent,
            prefix=f".{output_path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temp_path = Path(handle.name)
        first, *rest = pages
        first.save(
            temp_path,
            format="PDF",
            save_all=True,
            append_images=rest,
            resolution=dpi,
        )
        os.replace(temp_path, output_path)
    finally:
        for page in pages:
            page.close()
        if temp_path and temp_path.exists():
            temp_path.unlink()
