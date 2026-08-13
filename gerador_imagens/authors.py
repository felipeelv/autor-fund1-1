from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from .config import ConfigError


@dataclass(frozen=True)
class AuthorProfile:
    id: str
    name: str
    discipline: str | None = None
    prompt_prefix: str = ""
    prompt_suffix: str = ""
    default_renderer: str = "texto"
    formats: tuple[str, ...] = ()
    active: bool = True
    parameters: dict[str, Any] | None = None


def _author_path(root: Path, author_id: str) -> Path:
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", author_id):
        raise ConfigError(
            "ID de autor inválido. Use letras minúsculas, números, hífen ou underscore."
        )
    return root / "autores" / author_id / "autor.yaml"


def load_author(root: Path, author_id: str) -> AuthorProfile:
    path = _author_path(root, author_id)
    if not path.exists():
        raise ConfigError(f"Autor não encontrado: {author_id} ({path})")
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        raise ConfigError(f"YAML inválido no autor {author_id}: {exc}") from exc
    data = raw.get("autor", raw)
    formats = data.get("formatos") or data.get("formats") or []
    if not isinstance(formats, list):
        raise ConfigError(f"formatos em {path} precisa ser uma lista.")
    profile = AuthorProfile(
        id=str(data.get("id") or author_id),
        name=str(data.get("nome") or data.get("name") or author_id),
        discipline=data.get("disciplina") or data.get("discipline"),
        prompt_prefix=str(data.get("prompt_prefixo") or data.get("prompt_prefix") or "").strip(),
        prompt_suffix=str(data.get("prompt_sufixo") or data.get("prompt_suffix") or "").strip(),
        default_renderer=str(
            data.get("renderizador_padrao")
            or data.get("default_renderer")
            or "texto"
        ),
        formats=tuple(str(item) for item in formats),
        active=bool(data.get("ativo", data.get("active", True))),
        parameters=data.get("parametros_api") or data.get("parameters") or {},
    )
    if profile.id != author_id:
        raise ConfigError(
            f"O ID dentro de {path} precisa ser igual ao nome da pasta ({author_id})."
        )
    if not profile.active:
        raise ConfigError(f"O autor '{author_id}' está desativado.")
    return profile


def aplicar_autor(
    root: Path,
    author_id: str | None,
    prompt: str,
) -> tuple[str, AuthorProfile | None]:
    if not author_id:
        return prompt, None
    author = load_author(root, author_id)
    parts = [part for part in (author.prompt_prefix, prompt.strip(), author.prompt_suffix) if part]
    return "\n\n".join(parts), author


def listar_autores(root: Path) -> list[AuthorProfile]:
    author_root = root / "autores"
    if not author_root.exists():
        return []
    profiles: list[AuthorProfile] = []
    for path in sorted(author_root.glob("*/autor.yaml")):
        if path.parent.name.startswith("_"):
            continue
        try:
            profile = load_author(root, path.parent.name)
        except ConfigError:
            continue
        profiles.append(profile)
    return profiles
