from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping


class ConfigError(ValueError):
    """Configuração inválida informada antes de qualquer chamada à API."""


PRESETS: dict[str, str] = {
    "quadrado": "1024x1024",
    "retrato": "1024x1536",
    "paisagem": "1536x1024",
    "a4": "2160x3056",
    "2k-quadrado": "2048x2048",
    "4k-paisagem": "3840x2160",
    "4k-retrato": "2160x3840",
}

FORMAT_EXTENSIONS: dict[str, tuple[str, ...]] = {
    "png": (".png",),
    "jpeg": (".jpg", ".jpeg"),
    "webp": (".webp",),
}

ALIASES: dict[str, str] = {
    "modelo": "model",
    "tamanho": "size",
    "qualidade": "quality",
    "formato": "output_format",
    "compressao": "output_compression",
    "compressão": "output_compression",
    "fundo": "background",
    "moderacao": "moderation",
    "moderação": "moderation",
    "quantidade": "n",
    "parciais": "partial_images",
    "imagens_parciais": "partial_images",
    "tentativas": "max_retries",
    "metadados": "write_metadata",
    "proporcao": "aspect_ratio",
    "proporção": "aspect_ratio",
    "resolucao": "resolution",
    "resolução": "resolution",
}


@dataclass(frozen=True)
class GenerationOptions:
    model: str = "gpt-image-2"
    size: str = "1024x1536"
    quality: str = "auto"
    output_format: str = "png"
    output_compression: int | None = None
    background: str = "auto"
    moderation: str = "auto"
    n: int = 1
    stream: bool = False
    partial_images: int = 0
    timeout: float = 180.0
    max_retries: int = 2
    write_metadata: bool = True
    aspect_ratio: str | None = None
    resolution: str | None = None

    def validated(self) -> "GenerationOptions":
        validate_size(self.size)
        output_format = normalize_format(self.output_format)
        if self.quality not in {"auto", "low", "medium", "high"}:
            raise ConfigError(f"Qualidade inválida: {self.quality}")
        if self.background not in {"auto", "opaque"}:
            raise ConfigError(
                "Fundo inválido. GPT Image 2 aceita apenas 'auto' ou 'opaque'."
            )
        if self.moderation not in {"auto", "low"}:
            raise ConfigError("Moderação deve ser 'auto' ou 'low'.")
        if not 1 <= self.n <= 10:
            raise ConfigError("A quantidade deve estar entre 1 e 10.")
        if self.output_compression is not None:
            if output_format not in {"jpeg", "webp"}:
                raise ConfigError("--compressao só pode ser usada com JPEG ou WebP.")
            if not 0 <= self.output_compression <= 100:
                raise ConfigError("A compressão deve estar entre 0 e 100.")
        if not 0 <= self.partial_images <= 3:
            raise ConfigError("O número de imagens parciais deve estar entre 0 e 3.")
        if self.partial_images and not self.stream:
            raise ConfigError("--parciais exige --stream.")
        if self.stream and self.n != 1:
            raise ConfigError("Streaming exige quantidade igual a 1.")
        if self.timeout <= 0:
            raise ConfigError("O timeout precisa ser maior que zero.")
        if not 0 <= self.max_retries <= 10:
            raise ConfigError("Retries deve estar entre 0 e 10.")
        if not self.model.strip():
            raise ConfigError("O modelo não pode estar vazio.")
        if self.aspect_ratio is not None and not re.fullmatch(
            r"(?:1:1|16:9|9:16|4:3|3:4|3:2|2:3|2:1|1:2|19\.5:9|9:19\.5|20:9|9:20|auto)",
            str(self.aspect_ratio),
        ):
            raise ConfigError(f"Proporção inválida: {self.aspect_ratio}")
        if self.resolution is not None and self.resolution not in {"1k", "2k"}:
            raise ConfigError("Resolução do provedor deve ser '1k' ou '2k'.")
        if output_format != self.output_format:
            return GenerationOptions(
                **{**asdict(self), "output_format": output_format}
            )
        return self


def normalize_format(value: str) -> str:
    normalized = str(value).strip().lower()
    if normalized == "jpg":
        normalized = "jpeg"
    if normalized not in FORMAT_EXTENSIONS:
        raise ConfigError(f"Formato inválido: {value}")
    return normalized


def validate_size(value: str) -> tuple[int, int] | None:
    if value == "auto":
        return None
    match = re.fullmatch(r"(\d+)x(\d+)", value.strip().lower())
    if not match:
        raise ConfigError("Tamanho deve usar WIDTHxHEIGHT, por exemplo 1024x1536.")
    width, height = (int(match.group(1)), int(match.group(2)))
    if width > 3840 or height > 3840:
        raise ConfigError("Nenhuma borda pode ultrapassar 3840 px.")
    if width % 16 or height % 16:
        raise ConfigError("As duas dimensões precisam ser múltiplas de 16 px.")
    short, long = sorted((width, height))
    if long / short > 3:
        raise ConfigError("A proporção entre a borda longa e a curta não pode passar de 3:1.")
    pixels = width * height
    if not 655_360 <= pixels <= 8_294_400:
        raise ConfigError(
            "O total de pixels precisa ficar entre 655.360 e 8.294.400."
        )
    return width, height


def options_from_mapping(
    mapping: Mapping[str, Any] | None = None,
    base: GenerationOptions | None = None,
) -> GenerationOptions:
    values = asdict(base or GenerationOptions())
    for raw_key, value in (mapping or {}).items():
        key = ALIASES.get(str(raw_key), str(raw_key))
        if key not in values:
            raise ConfigError(f"Parâmetro de API desconhecido: {raw_key}")
        if value is not None:
            values[key] = value
    return GenerationOptions(**values).validated()


def normalize_output_path(path: Path, output_format: str) -> Path:
    output_format = normalize_format(output_format)
    suffix = path.suffix.lower()
    accepted = FORMAT_EXTENSIONS[output_format]
    if not suffix:
        return path.with_suffix(accepted[0])
    if suffix not in accepted:
        expected = " ou ".join(accepted)
        raise ConfigError(
            f"A extensão de {path.name} não corresponde ao formato "
            f"{output_format}; use {expected}."
        )
    return path


def output_paths(path: Path, count: int, output_format: str) -> list[Path]:
    normalized = normalize_output_path(path, output_format)
    if count == 1:
        return [normalized]
    return [
        normalized.with_name(f"{normalized.stem}-{index:02d}{normalized.suffix}")
        for index in range(1, count + 1)
    ]
