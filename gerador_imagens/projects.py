from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

import yaml

from .authors import load_author
from .config import (
    ConfigError,
    GenerationOptions,
    normalize_output_path,
    options_from_mapping,
)
from .storage import StorageSettings, resolve_external_output


@dataclass(frozen=True)
class ProjectTask:
    label: str
    prompt_path: Path
    output_path: Path
    options: GenerationOptions
    author_id: str | None = None


@dataclass(frozen=True)
class ProjectPlan:
    title: str
    source: Path
    tasks: list[ProjectTask]
    pdf_path: Path | None = None
    pdf_dpi: int = 300


def _inside_root(root: Path, path: Path, label: str) -> Path:
    root = root.resolve()
    resolved = path.resolve()
    if not resolved.is_relative_to(root):
        raise ConfigError(f"{label} precisa ficar dentro da pasta do gerador: {path}")
    return resolved


def _resolve_prompt(root: Path, project_path: Path, value: str) -> Path:
    raw = Path(value).expanduser()
    candidates = [raw] if raw.is_absolute() else [project_path.parent / raw, root / raw]
    for candidate in candidates:
        resolved = _inside_root(root, candidate, "O prompt")
        if resolved.exists():
            return resolved
    raise ConfigError(f"Prompt do projeto não encontrado: {value}")


def _resolve_output(
    storage: StorageSettings,
    value: str,
    area: str,
) -> Path:
    return resolve_external_output(storage, value, area)


def _mapping(value: Any, label: str) -> Mapping[str, Any]:
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise ConfigError(f"{label} precisa ser um objeto YAML.")
    return value


def _validate_four_page_series(
    project_info: Mapping[str, Any],
    images: list[Any],
    author_id: Any,
) -> None:
    if str(project_info.get("tipo") or "") != "serie-editorial-4-paginas":
        return
    if str(author_id or "") != "estudos-sociais":
        raise ConfigError(
            "serie-editorial-4-paginas exige projeto.autor=estudos-sociais."
        )
    if len(images) != 4:
        raise ConfigError(
            "A série editorial de Estudos Sociais exige exatamente 4 imagens."
        )

    expected_parent: Path | None = None
    valid_years = {f"{year}ano" for year in range(4, 10)}
    for index, item in enumerate(images, start=1):
        if not isinstance(item, dict) or not item.get("saida"):
            raise ConfigError(f"imagens[{index}] precisa de saida.")
        output = Path(str(item["saida"]))
        if output.is_absolute() or ".." in output.parts or len(output.parts) != 4:
            raise ConfigError(
                "Saídas da série precisam seguir "
                "estudos-sociais/<ano>/capitulo-<numero>-<tema>/pN-<funcao>.png."
            )
        discipline, year, chapter, filename = output.parts
        if (
            discipline != "estudos-sociais"
            or year not in valid_years
            or not chapter.startswith("capitulo-")
            or not filename.startswith(f"p{index}-")
        ):
            raise ConfigError(
                "Saídas da série precisam seguir a disciplina, o ano, o capítulo "
                "e a ordem p1, p2, p3, p4."
            )
        if expected_parent is None:
            expected_parent = output.parent
        elif output.parent != expected_parent:
            raise ConfigError(
                "As quatro páginas da série precisam usar a mesma pasta de capítulo."
            )


def load_project(
    root: Path,
    project_path: Path,
    storage: StorageSettings,
    overrides: Mapping[str, Any] | None = None,
    author_override: str | None = None,
) -> ProjectPlan:
    project_path = _inside_root(root, project_path, "O projeto")
    if not project_path.exists():
        raise ConfigError(f"Projeto YAML não encontrado: {project_path}")
    try:
        raw = yaml.safe_load(project_path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        raise ConfigError(f"Projeto YAML inválido: {exc}") from exc
    if not isinstance(raw, dict):
        raise ConfigError("O arquivo de projeto precisa conter um objeto YAML.")

    project_info = _mapping(raw.get("projeto"), "projeto")
    model_info = _mapping(raw.get("modelo"), "modelo")
    provider = str(model_info.get("provider", "openai")).lower()
    if provider != "openai":
        raise ConfigError("Esta pasta autônoma aceita apenas provider=openai.")

    global_parameters = dict(_mapping(raw.get("parametros_api"), "parametros_api"))
    if model_info.get("id"):
        global_parameters["model"] = model_info["id"]
    output_info = _mapping(raw.get("saida"), "saida")
    default_area = str(output_info.get("area") or "revisao")

    global_author = author_override or project_info.get("autor") or raw.get("autor")
    author_defaults = GenerationOptions()
    if global_author:
        author = load_author(root, str(global_author))
        if author.parameters:
            author_defaults = options_from_mapping(author.parameters, author_defaults)
    global_options = options_from_mapping(global_parameters, author_defaults)

    images = raw.get("imagens")
    if not isinstance(images, list) or not images:
        raise ConfigError("O projeto precisa declarar ao menos um item em imagens.")
    _validate_four_page_series(project_info, images, global_author)

    tasks: list[ProjectTask] = []
    for index, item in enumerate(images, start=1):
        if not isinstance(item, dict):
            raise ConfigError(f"imagens[{index}] precisa ser um objeto YAML.")
        prompt_value = item.get("prompt")
        output_value = item.get("saida")
        if not prompt_value or not output_value:
            raise ConfigError(f"imagens[{index}] precisa de prompt e saida.")
        author_id = author_override or item.get("autor") or global_author
        options = global_options
        if author_id and str(author_id) != str(global_author or ""):
            author = load_author(root, str(author_id))
            author_defaults = GenerationOptions()
            if author.parameters:
                author_defaults = options_from_mapping(
                    author.parameters,
                    author_defaults,
                )
            options = options_from_mapping(global_parameters, author_defaults)
        options = options_from_mapping(
            _mapping(item.get("parametros_api"), f"imagens[{index}].parametros_api"),
            options,
        )
        options = options_from_mapping(overrides, options)
        output_path = normalize_output_path(
            _resolve_output(
                storage,
                str(output_value),
                str(item.get("area") or default_area),
            ),
            options.output_format,
        )
        tasks.append(
            ProjectTask(
                label=str(item.get("nome") or item.get("tipo") or f"imagem-{index}"),
                prompt_path=_resolve_prompt(root, project_path, str(prompt_value)),
                output_path=output_path,
                options=options,
                author_id=str(author_id) if author_id else None,
            )
        )

    pdf_path: Path | None = None
    pdf_dpi = int(output_info.get("dpi_pdf", 300))
    if not 72 <= pdf_dpi <= 600:
        raise ConfigError("saida.dpi_pdf precisa estar entre 72 e 600.")
    if output_info.get("gerar_pdf"):
        pdf_value = output_info.get("arquivo_pdf")
        if not pdf_value:
            raise ConfigError("saida.gerar_pdf exige saida.arquivo_pdf.")
        pdf_path = _resolve_output(storage, str(pdf_value), default_area)
        if pdf_path.suffix.lower() != ".pdf":
            raise ConfigError("O arquivo PDF precisa terminar em .pdf.")

    return ProjectPlan(
        title=str(project_info.get("titulo") or project_path.stem),
        source=project_path,
        tasks=tasks,
        pdf_path=pdf_path,
        pdf_dpi=pdf_dpi,
    )
