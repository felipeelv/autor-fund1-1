from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

import yaml
from dotenv import load_dotenv

from .config import ConfigError


DEFAULT_AREAS = {
    "revisao": "_revisao",
    "aprovadas": "aprovadas",
    "historico": "historico-importado",
}


@dataclass(frozen=True)
class StorageSettings:
    root: Path
    areas: Mapping[str, str]

    def area_root(self, area: str) -> Path:
        if area not in self.areas:
            raise ConfigError(
                f"Área de saída desconhecida: {area}. "
                f"Opções: {', '.join(sorted(self.areas))}."
            )
        return (self.root / self.areas[area]).resolve()


def _mapping(value: Any, label: str) -> Mapping[str, Any]:
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise ConfigError(f"{label} precisa ser um objeto YAML.")
    return value


def _load_local_config(root: Path) -> Mapping[str, Any]:
    path = root / "config.local.yaml"
    if not path.exists():
        return {}
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        raise ConfigError(f"config.local.yaml inválido: {exc}") from exc
    return _mapping(data, "config.local.yaml")


def _outside_project(project_root: Path, storage_root: Path) -> Path:
    project_root = project_root.resolve()
    storage_root = storage_root.resolve()
    if storage_root == project_root or storage_root.is_relative_to(project_root):
        raise ConfigError(
            "A raiz de saída precisa ficar fora da pasta do projeto."
        )
    return storage_root


def load_storage(
    project_root: Path,
    root_override: str | Path | None = None,
) -> StorageSettings:
    project_root = project_root.resolve()
    load_dotenv(project_root / ".env", override=False)
    local = _load_local_config(project_root)
    storage_config = _mapping(local.get("armazenamento"), "armazenamento")
    root_value = (
        root_override
        or os.getenv("GERADOR_IMAGENS_SAIDA", "").strip()
        or storage_config.get("raiz")
    )
    if not root_value:
        raise ConfigError(
            "Destino externo não configurado. Defina GERADOR_IMAGENS_SAIDA "
            "ou armazenamento.raiz em config.local.yaml."
        )
    storage_root = _outside_project(
        project_root,
        Path(str(root_value)).expanduser(),
    )
    if not storage_root.is_dir():
        raise ConfigError(
            f"A raiz de saída externa não está disponível: {storage_root}"
        )
    configured_areas = _mapping(storage_config.get("areas"), "armazenamento.areas")
    areas = {
        key: str(configured_areas.get(key) or value)
        for key, value in DEFAULT_AREAS.items()
    }
    for key, relative in areas.items():
        path = Path(relative)
        if path.is_absolute() or ".." in path.parts:
            raise ConfigError(
                f"armazenamento.areas.{key} precisa ser um caminho relativo seguro."
            )
    return StorageSettings(root=storage_root, areas=areas)


def resolve_external_output(
    settings: StorageSettings,
    value: str | Path,
    area: str = "revisao",
) -> Path:
    storage_root = settings.root.resolve()
    raw = Path(value).expanduser()
    if raw.is_absolute():
        resolved = raw.resolve()
    else:
        resolved = (settings.area_root(area) / raw).resolve()
    if not resolved.is_relative_to(storage_root):
        raise ConfigError(
            f"A saída precisa ficar dentro da raiz externa: {storage_root}"
        )
    if not raw.is_absolute() and not resolved.is_relative_to(settings.area_root(area)):
        raise ConfigError(f"Caminho de saída inseguro: {value}")
    return resolved
