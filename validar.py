from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from dataclasses import asdict
from pathlib import Path
from typing import Any, Mapping

import yaml

from gerador_imagens.core import load_prompt
from gerador_imagens.quality import (
    analyze_prompt,
    compare_ocr_text,
    extract_expected_text,
    run_tesseract,
    validate_image_file,
    validate_yaml_file,
)
from gerador_imagens.renderers import render_prompt
from gerador_imagens.storage import load_storage
from gerador_imagens.version_indices import (
    discover_prompt_snapshots,
    discover_render_resources,
    discover_operational_yaml_snapshots,
    discover_image_snapshots,
    discover_version_indices,
)


ROOT = Path(__file__).resolve().parent
INTERNAL_ID_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*", re.ASCII)
PROJECT_SUFFIXES = frozenset({".yaml", ".yml"})


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Auditoria local de prompts, imagens, YAML e OCR."
    )
    parser.add_argument(
        "--acervo",
        action="store_true",
        help="Valida todos os prompts, YAMLs e a ausência de imagens no projeto.",
    )
    parser.add_argument(
        "--revisao",
        action="store_true",
        help="Também valida as imagens existentes na área externa de revisão.",
    )
    parser.add_argument("--saida-root", help="Sobrescreve a raiz externa configurada.")
    parser.add_argument("--prompt", action="append", default=[], help="Prompt específico.")
    parser.add_argument("--imagem", action="append", default=[], help="Imagem específica.")
    parser.add_argument("--ocr", help="Imagem que será submetida ao OCR.")
    parser.add_argument("--esperado", help="Prompt com bloco de textos obrigatórios.")
    parser.add_argument("--idioma", default="por", help="Idioma do Tesseract.")
    parser.add_argument("--json", action="store_true", help="Exibe o relatório em JSON.")
    parser.add_argument("--relatorio", help="Também salva o relatório JSON neste arquivo.")
    return parser


def resolve_local(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = ROOT / path
    return path.resolve()


def prompt_report(path: Path, prompt_text: str | None = None) -> dict[str, Any]:
    try:
        prompt = prompt_text if prompt_text is not None else load_prompt(path)
    except Exception as exc:
        return {"path": str(path), "valid": False, "error": str(exc), "findings": []}
    findings = [
        {
            "severity": item.severity,
            "code": item.code,
            "message": item.message,
        }
        for item in analyze_prompt(prompt)
    ]
    return {
        "path": str(path),
        "valid": not any(item["severity"] == "error" for item in findings),
        "characters": len(prompt),
        "words": len(prompt.split()),
        "findings": findings,
    }


def rendering_report(
    author_id: str,
    path: Path,
    renderer: str,
    prompt_text: str | None = None,
    resource_texts: dict[str, dict[str, str]] | None = None,
) -> dict[str, Any]:
    try:
        prompt = render_prompt(
            ROOT,
            path,
            renderer,
            prompt_text=prompt_text,
            resource_texts=resource_texts,
        )
    except Exception as exc:
        return {
            "path": str(path),
            "author": author_id,
            "valid": False,
            "error": str(exc),
        }
    return {
        "path": str(path),
        "author": author_id,
        "renderer": renderer,
        "valid": True,
        "characters": len(prompt),
        "words": len(prompt.split()),
        "error": None,
    }


def image_files(root: Path) -> list[Path]:
    snapshots, _reports = discover_image_snapshots(root)
    return [snapshot.path for snapshot in snapshots]


def prompt_files(author_root: Path) -> list[Path]:
    lexical = _lexical_absolute(author_root)
    if lexical.name != "autores":
        return []
    snapshots, _reports = discover_prompt_snapshots(
        lexical.parent,
        require_author_profile=False,
    )
    return [snapshot.path for snapshot in snapshots]


def project_yaml_files(root: Path) -> list[Path]:
    project_files, _, _ = _project_inventory(root)
    return project_files


def transversal_project_reports(root: Path) -> list[dict[str, Any]]:
    """Relata violações da coleção transversal sem ler alvos simbólicos."""

    _, reports = _transversal_project_inventory(root)
    return reports


def _valid_internal_id(value: object) -> bool:
    return isinstance(value, str) and bool(INTERNAL_ID_PATTERN.fullmatch(value))


def _lexical_absolute(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def _safe_collection_root(root: Path, name: str) -> tuple[Path | None, str | None]:
    lexical_root = _lexical_absolute(root)
    if lexical_root.is_symlink():
        return None, "A raiz do projeto não pode ser um link simbólico."
    try:
        real_root = lexical_root.resolve(strict=True)
    except OSError as exc:
        return None, f"A raiz do projeto não pôde ser resolvida: {exc}"

    collection = lexical_root / name
    if collection.is_symlink():
        return None, f"A pasta {name}/ não pode ser um link simbólico."
    if not collection.is_dir():
        return None, f"A pasta {name}/ não é um diretório regular."
    try:
        real_collection = collection.resolve(strict=True)
    except OSError as exc:
        return None, f"A pasta {name}/ não pôde ser resolvida: {exc}"
    if real_collection.parent != real_root:
        return None, f"A pasta {name}/ escapa da raiz do projeto."
    return collection, None


def _safe_identifier_directory(
    root: Path,
    collection_name: str,
    identifier: object,
) -> tuple[Path | None, str | None]:
    if not _valid_internal_id(identifier):
        return None, "O identificador interno é inválido."
    collection, collection_error = _safe_collection_root(root, collection_name)
    if collection_error or collection is None:
        return None, collection_error
    directory = collection / identifier
    if directory.is_symlink():
        return None, "A pasta identificada não pode ser um link simbólico."
    if not directory.is_dir():
        return None, "A pasta identificada não é um diretório regular."
    try:
        real_directory = directory.resolve(strict=True)
        real_collection = collection.resolve(strict=True)
    except OSError as exc:
        return None, f"A pasta identificada não pôde ser resolvida: {exc}"
    if real_directory.parent != real_collection:
        return None, "A pasta identificada escapa da coleção interna."
    return directory, None


def _safe_regular_file(
    directory: Path,
    name: str,
) -> tuple[Path | None, str | None]:
    path = directory / name
    if path.is_symlink():
        return None, f"{name} não pode ser um link simbólico."
    if not path.is_file():
        return None, f"{name} não é um arquivo regular."
    try:
        real_path = path.resolve(strict=True)
        real_directory = directory.resolve(strict=True)
    except OSError as exc:
        return None, f"{name} não pôde ser resolvido: {exc}"
    if real_path.parent != real_directory:
        return None, f"{name} escapa da pasta autorizada."
    return path, None


def kit_yaml_files(root: Path) -> list[Path]:
    kits_root, root_error = _safe_collection_root(root, "kits")
    if root_error or kits_root is None:
        return []
    contracts: list[Path] = []
    try:
        entries = sorted(kits_root.iterdir(), key=lambda item: item.name)
    except OSError:
        return []
    for entry in entries:
        if not _valid_internal_id(entry.name):
            continue
        kit_root, kit_error = _safe_identifier_directory(root, "kits", entry.name)
        if kit_error or kit_root is None:
            continue
        contract, contract_error = _safe_regular_file(kit_root, "kit.yaml")
        if not contract_error and contract is not None:
            contracts.append(contract)
    return contracts


def _load_yaml_mapping(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    if path.is_symlink():
        return None, "O arquivo YAML não pode ser um link simbólico."
    if not path.is_file():
        return None, "Arquivo YAML regular não encontrado."
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        return None, str(exc)
    if not isinstance(value, dict):
        return None, "A raiz do YAML não é um objeto."
    return value, None


def _load_yaml_mapping_text(
    content: str,
) -> tuple[dict[str, Any] | None, str | None]:
    """Carrega um snapshot YAML já lido; nunca consulta seu caminho de origem."""

    try:
        value = yaml.safe_load(content)
    except (UnicodeError, yaml.YAMLError, ValueError, TypeError) as exc:
        return None, str(exc)
    if not isinstance(value, dict):
        return None, "A raiz do YAML não é um objeto."
    return value, None


def _snapshot_yaml_mapping(
    snapshot_map: Mapping[str, str],
    relative_path: str,
) -> tuple[dict[str, Any] | None, str | None]:
    """Obtém referência semântica estritamente do inventário seguro fornecido."""

    try:
        content = snapshot_map[relative_path]
    except KeyError:
        return None, f"Snapshot seguro ausente para {relative_path}."
    if not isinstance(content, str):
        return None, f"Snapshot seguro inválido para {relative_path}."
    return _load_yaml_mapping_text(content)


def _invalid_report(path: Path, error: str) -> dict[str, Any]:
    return {
        "path": str(path),
        "valid": False,
        "error": error,
    }


def _safe_optional_collection_root(
    root: Path,
    name: str,
) -> tuple[Path | None, str | None]:
    """Resolve uma coleção opcional sem aceitar links ou fuga da raiz."""

    lexical_root = _lexical_absolute(root)
    if lexical_root.is_symlink():
        return None, "A raiz do projeto não pode ser um link simbólico."
    try:
        real_root = lexical_root.resolve(strict=True)
    except OSError as exc:
        return None, f"A raiz do projeto não pôde ser resolvida: {exc}"

    collection = lexical_root / name
    if collection.is_symlink():
        return None, f"A pasta {name}/ não pode ser um link simbólico."
    if not collection.exists():
        return None, None
    if not collection.is_dir():
        return None, f"A pasta {name}/ não é um diretório regular."
    try:
        real_collection = collection.resolve(strict=True)
    except OSError as exc:
        return None, f"A pasta {name}/ não pôde ser resolvida: {exc}"
    if real_collection.parent != real_root:
        return None, f"A pasta {name}/ escapa da raiz do projeto."
    return collection, None


def _internal_author_collection_path(
    author_root: Path,
    value: object,
    *,
    field: str,
) -> tuple[Path | None, str | None]:
    """Valida um caminho interno declarado, mesmo quando ainda não existe."""

    if not isinstance(value, str) or not value:
        return None, f"{field} deve ser um caminho relativo não vazio."

    # A forma portátil precisa anteceder qualquer decisão lexical ou criação
    # de Path. Caracteres de compatibilidade podem esconder barras, dois-pontos,
    # contrabarras, til ou segmentos de travessia em sua grafia original.
    portable_value = unicodedata.normalize("NFKC", value)
    if (
        value != value.strip()
        or portable_value != portable_value.strip()
        or "\x00" in portable_value
    ):
        return None, f"{field} contém caracteres inválidos."
    if (
        portable_value.startswith(("~", "/"))
        or "\\" in portable_value
        or re.match(r"^[A-Za-z]:", portable_value)
        or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", portable_value)
    ):
        return None, f"{field} deve ser relativo e interno ao autor."

    portable_parts = portable_value.split("/")
    if any(part in {"", ".", ".."} for part in portable_parts):
        return None, f"{field} deve permanecer interno ao autor."

    # Preserve a grafia declarada para localizar uma pasta legítima no sistema
    # atual, depois de a representação NFKC ter sido integralmente validada.
    parts = value.split("/")

    try:
        real_author_root = author_root.resolve(strict=True)
    except OSError as exc:
        return None, f"A pasta do autor não pôde ser resolvida: {exc}"

    candidate = author_root
    for part in parts:
        candidate /= part
        if candidate.is_symlink():
            return None, f"{field} não pode atravessar links simbólicos."
        if not candidate.exists():
            continue
        if not candidate.is_dir():
            return None, f"{field} não aponta para um diretório regular."
        try:
            real_candidate = candidate.resolve(strict=True)
        except OSError as exc:
            return None, f"{field} não pôde ser resolvido: {exc}"
        if not real_candidate.is_relative_to(real_author_root):
            return None, f"{field} escapa da pasta do autor."
    return candidate, None


def _portable_path_parts(path: Path, boundary: Path) -> tuple[str, ...]:
    """Cria uma chave portátil com Unicode NFKC + casefold.

    Normalizar o caminho POSIX inteiro antes de separar os componentes também
    cobre separadores e caracteres de compatibilidade. A segunda NFKC recompõe
    o resultado do ``casefold``. Assim, a comparação independe de caixa, forma
    canônica e largura tipográfica, inclusive quando o caminho ainda não existe.
    """

    relative = path.relative_to(boundary).as_posix()
    portable = unicodedata.normalize(
        "NFKC",
        unicodedata.normalize("NFKC", relative).casefold(),
    )
    return tuple(portable.split("/"))


def _parts_contain(
    possible_parent: tuple[str, ...],
    possible_child: tuple[str, ...],
) -> bool:
    return (
        len(possible_parent) <= len(possible_child)
        and possible_child[: len(possible_parent)] == possible_parent
    )


def _production_area_conflict(
    author_root: Path,
    projects_directory: Path,
    records_directory: Path,
) -> str | None:
    """Detecta sobreposição lexical portátil e física entre as áreas."""

    projects_key = _portable_path_parts(projects_directory, author_root)
    records_key = _portable_path_parts(records_directory, author_root)
    if projects_key == records_key:
        return (
            "producao.projetos e producao.registros devem ser distintos: "
            "suas chaves portáteis (Unicode NFKC + casefold) coincidem."
        )
    if _parts_contain(projects_key, records_key) or _parts_contain(
        records_key,
        projects_key,
    ):
        return (
            "producao.projetos e producao.registros devem ser distintos e "
            "disjuntos: uma área não pode conter a outra, segundo suas chaves "
            "portáteis (Unicode NFKC + casefold)."
        )

    if not projects_directory.exists() or not records_directory.exists():
        return None
    try:
        if os.path.samefile(projects_directory, records_directory):
            return (
                "producao.projetos e producao.registros devem ser distintos e "
                "disjuntos: as áreas existentes apontam para o mesmo diretório."
            )
        real_projects = projects_directory.resolve(strict=True)
        real_records = records_directory.resolve(strict=True)
    except OSError as exc:
        return f"As áreas de producao não puderam ser comparadas fisicamente: {exc}"

    if real_projects.is_relative_to(real_records) or real_records.is_relative_to(
        real_projects
    ):
        return (
            "producao.projetos e producao.registros devem ser distintos e "
            "disjuntos: uma área existente contém fisicamente a outra."
        )
    return None


def _production_reserved_conflict(
    author_root: Path,
    projects_directory: Path,
    records_directory: Path,
) -> str | None:
    """Impede que áreas de produção escondam qualquer parte de ``anos/**``."""

    years_directory = author_root / "anos"
    years_key = ("anos",)
    for field, directory in (
        ("producao.projetos", projects_directory),
        ("producao.registros", records_directory),
    ):
        area_key = _portable_path_parts(directory, author_root)
        if _parts_contain(area_key, years_key) or _parts_contain(
            years_key,
            area_key,
        ):
            return f"{field} não pode sobrepor a árvore reservada anos/**."

    if not years_directory.exists():
        return None
    try:
        real_years = years_directory.resolve(strict=True)
        for field, directory in (
            ("producao.projetos", projects_directory),
            ("producao.registros", records_directory),
        ):
            if not directory.exists():
                continue
            if os.path.samefile(directory, years_directory):
                return f"{field} aponta fisicamente para a árvore reservada anos/**."
            real_area = directory.resolve(strict=True)
            if real_area.is_relative_to(real_years) or real_years.is_relative_to(
                real_area
            ):
                return f"{field} sobrepõe fisicamente a árvore reservada anos/**."
    except OSError as exc:
        return f"As áreas de produção e anos/** não puderam ser comparadas: {exc}"
    return None


def _safe_project_files(
    directory: Path,
    boundary: Path,
    *,
    field: str,
) -> tuple[list[Path], list[str]]:
    """Percorre YAMLs reais sem seguir nenhum link simbólico."""

    if not directory.exists():
        return [], []
    try:
        real_boundary = boundary.resolve(strict=True)
    except OSError as exc:
        return [], [f"{field}: limite interno inválido: {exc}"]

    files: list[Path] = []
    errors: list[str] = []
    pending = [directory]
    while pending:
        current = pending.pop()
        try:
            entries = sorted(current.iterdir(), key=lambda item: item.name)
        except OSError as exc:
            errors.append(f"{field}: não foi possível listar {current}: {exc}")
            continue
        child_directories: list[Path] = []
        for entry in entries:
            try:
                relative = entry.relative_to(boundary).as_posix()
            except ValueError:
                errors.append(f"{field}: entrada lexical fora do limite: {entry}")
                continue
            if entry.is_symlink():
                errors.append(
                    f"{field}: link simbólico não permitido em {relative}."
                )
                continue
            if entry.is_dir():
                try:
                    real_entry = entry.resolve(strict=True)
                except OSError as exc:
                    errors.append(f"{field}: {relative} não pôde ser resolvido: {exc}")
                    continue
                if not real_entry.is_relative_to(real_boundary):
                    errors.append(f"{field}: {relative} escapa do limite interno.")
                    continue
                child_directories.append(entry)
                continue
            if not entry.is_file():
                errors.append(f"{field}: entrada não regular em {relative}.")
                continue
            if entry.suffix.lower() not in PROJECT_SUFFIXES:
                continue
            try:
                real_entry = entry.resolve(strict=True)
            except OSError as exc:
                errors.append(f"{field}: {relative} não pôde ser resolvido: {exc}")
                continue
            if not real_entry.is_relative_to(real_boundary):
                errors.append(f"{field}: {relative} escapa do limite interno.")
                continue
            files.append(entry)
        pending.extend(reversed(child_directories))
    return sorted(files), errors


def _author_production_inventory(
    root: Path,
) -> tuple[list[Path], list[dict[str, Any]]]:
    authors_root, authors_error = _safe_collection_root(root, "autores")
    if authors_error or authors_root is None:
        return [], [
            _invalid_report(
                _lexical_absolute(root) / "autores",
                authors_error or "A pasta autores/ é inválida.",
            )
        ]

    try:
        entries = sorted(authors_root.iterdir(), key=lambda item: item.name)
    except OSError as exc:
        return [], [
            _invalid_report(authors_root, f"A pasta autores/ não pôde ser lida: {exc}")
        ]

    project_files: list[Path] = []
    reports: list[dict[str, Any]] = []
    for entry in entries:
        if entry.name.startswith((".", "_")):
            continue
        if entry.is_symlink():
            reports.append(
                _invalid_report(
                    entry / "manifesto.yaml",
                    "A pasta identificada não pode ser um link simbólico.",
                )
            )
            continue
        if not entry.is_dir():
            continue
        manifest_label = entry / "manifesto.yaml"
        if not _valid_internal_id(entry.name):
            reports.append(
                _invalid_report(
                    manifest_label,
                    "O identificador da pasta do autor é inválido.",
                )
            )
            continue
        author_root, author_error = _safe_identifier_directory(
            root,
            "autores",
            entry.name,
        )
        if author_error or author_root is None:
            reports.append(
                _invalid_report(
                    manifest_label,
                    author_error or "A pasta do autor é inválida.",
                )
            )
            continue

        manifest_path, manifest_path_error = _safe_regular_file(
            author_root,
            "manifesto.yaml",
        )
        if manifest_path_error or manifest_path is None:
            reports.append(
                _invalid_report(
                    manifest_label,
                    manifest_path_error or "manifesto.yaml é inválido.",
                )
            )
            continue
        manifest, manifest_error = _load_yaml_mapping(manifest_path)
        if manifest_error or manifest is None:
            reports.append(
                _invalid_report(
                    manifest_path,
                    manifest_error or "manifesto.yaml é inválido.",
                )
            )
            continue

        errors: list[str] = []
        production = manifest.get("producao")
        if not isinstance(production, dict):
            errors.append("producao deve ser um objeto YAML.")
            production = {}

        declared_paths: dict[str, Path] = {}
        for key in ("projetos", "registros"):
            field = f"producao.{key}"
            declared, declared_error = _internal_author_collection_path(
                author_root,
                production.get(key),
                field=field,
            )
            if declared_error or declared is None:
                errors.append(declared_error or f"{field} é inválido.")
                continue
            declared_paths[key] = declared

        if len(declared_paths) != 2:
            declared_paths.clear()
        else:
            area_conflict = _production_area_conflict(
                author_root,
                declared_paths["projetos"],
                declared_paths["registros"],
            )
            if area_conflict:
                errors.append(area_conflict)
                declared_paths.clear()
            else:
                reserved_conflict = _production_reserved_conflict(
                    author_root,
                    declared_paths["projetos"],
                    declared_paths["registros"],
                )
                if reserved_conflict:
                    errors.append(reserved_conflict)
                    declared_paths.clear()

        projects_directory = declared_paths.get("projetos")
        if projects_directory is not None:
            discovered, discovery_errors = _safe_project_files(
                projects_directory,
                author_root,
                field="producao.projetos",
            )
            project_files.extend(discovered)
            errors.extend(discovery_errors)

        reports.append(
            {
                "path": str(manifest_path),
                "valid": not errors,
                "error": "; ".join(errors) if errors else None,
            }
        )
    return sorted(set(project_files)), reports


def author_production_reports(root: Path) -> list[dict[str, Any]]:
    """Relata o contrato `producao` de cada manifesto sem exigir pasta vazia."""

    _, reports = _author_production_inventory(root)
    return reports


def _transversal_project_inventory(
    root: Path,
) -> tuple[list[Path], list[dict[str, Any]]]:
    projects_root, projects_error = _safe_optional_collection_root(root, "projetos")
    if projects_error:
        return [], [
            _invalid_report(_lexical_absolute(root) / "projetos", projects_error)
        ]
    if projects_root is None:
        return [], []
    project_files, errors = _safe_project_files(
        projects_root,
        _lexical_absolute(root),
        field="projetos transversais",
    )
    if not errors:
        return project_files, []
    return project_files, [
        _invalid_report(projects_root, "; ".join(errors))
    ]


def _project_inventory(
    root: Path,
) -> tuple[list[Path], list[dict[str, Any]], list[dict[str, Any]]]:
    author_projects, author_reports = _author_production_inventory(root)
    transversal_projects, transversal_reports = _transversal_project_inventory(root)
    return (
        sorted(set(author_projects) | set(transversal_projects)),
        author_reports,
        transversal_reports,
    )


def _internal_kit_path(
    kit_root: Path,
    value: object,
    *,
    expected_kind: str,
) -> tuple[Path | None, str | None]:
    if not isinstance(value, str) or not value:
        return None, "O caminho deve ser uma string relativa não vazia."
    relative = Path(value)
    if (
        relative.is_absolute()
        or value.startswith("~")
        or "\\" in value
        or any(part in {"", ".", ".."} for part in relative.parts)
    ):
        return None, "O caminho deve permanecer relativo e interno ao kit."

    candidate = kit_root
    for part in relative.parts:
        candidate /= part
        if candidate.is_symlink():
            return None, "O caminho interno não pode atravessar links simbólicos."

    if expected_kind == "file" and not candidate.is_file():
        return None, "O caminho não aponta para um arquivo regular."
    if expected_kind == "directory" and not candidate.is_dir():
        return None, "O caminho não aponta para um diretório regular."
    try:
        real_candidate = candidate.resolve(strict=True)
        real_kit_root = kit_root.resolve(strict=True)
    except OSError as exc:
        return None, f"O caminho interno não pôde ser resolvido: {exc}"
    if not real_candidate.is_relative_to(real_kit_root):
        return None, "O caminho interno escapa da pasta do kit."
    return candidate, None


def kit_contract_report(
    root: Path,
    path: Path,
    *,
    yaml_text: str | None = None,
    snapshot_map: Mapping[str, str] | None = None,
) -> dict[str, Any]:
    """Valida um kit; com snapshots, nenhuma referência YAML é reaberta.

    A forma sem snapshots é mantida para chamadas isoladas legadas. Na
    auditoria do acervo, ``yaml_text`` e ``snapshot_map`` são obrigatoriamente
    fornecidos em conjunto e qualquer referência ausente falha fechado, sem
    fallback para o disco.
    """

    errors: list[str] = []
    snapshot_mode = yaml_text is not None or snapshot_map is not None
    if snapshot_mode and (yaml_text is None or snapshot_map is None):
        return {
            "path": str(path),
            "valid": False,
            "error": "yaml_text e snapshot_map devem ser fornecidos em conjunto.",
        }
    lexical_root = _lexical_absolute(root)
    if snapshot_mode:
        kits_root, kits_error = lexical_root / "kits", None
    else:
        kits_root, kits_error = _safe_collection_root(root, "kits")
    lexical_path = _lexical_absolute(path)
    if kits_error or kits_root is None:
        return {
            "path": str(path),
            "valid": False,
            "error": kits_error,
        }
    if (
        lexical_path.name != "kit.yaml"
        or lexical_path.parent.parent != kits_root
        or not _valid_internal_id(lexical_path.parent.name)
    ):
        return {
            "path": str(path),
            "valid": False,
            "error": "O contrato não está em kits/<id>/kit.yaml.",
        }

    if snapshot_mode:
        kit_root = lexical_path.parent
        contract_path = lexical_path
        contract, load_error = _load_yaml_mapping_text(yaml_text)
    else:
        kit_root, kit_error = _safe_identifier_directory(
            root,
            "kits",
            lexical_path.parent.name,
        )
        if kit_error or kit_root is None:
            return {
                "path": str(path),
                "valid": False,
                "error": kit_error,
            }
        contract_path, contract_path_error = _safe_regular_file(kit_root, "kit.yaml")
        if contract_path_error or contract_path is None:
            return {
                "path": str(path),
                "valid": False,
                "error": contract_path_error,
            }
        contract, load_error = _load_yaml_mapping(contract_path)
    if load_error:
        errors.append(load_error)
    if contract is None:
        return {
            "path": str(path),
            "valid": False,
            "error": "; ".join(errors),
        }

    if contract.get("schema") != 1:
        errors.append("O campo schema deve ser 1.")

    kit_id = contract.get("id")
    if not _valid_internal_id(kit_id):
        errors.append("O id do kit deve ser um identificador interno simples.")
    elif kit_id != kit_root.name:
        errors.append("O id do kit deve corresponder ao nome da pasta.")
    if contract.get("estado") != "ativo":
        errors.append("O estado do kit deve ser ativo.")

    author_id = contract.get("autor")
    valid_author_id = _valid_internal_id(author_id)
    if not valid_author_id:
        errors.append("O campo autor deve ser um identificador interno simples.")

    formats = contract.get("formatos")
    if (
        not isinstance(formats, list)
        or not formats
        or any(not _valid_internal_id(item) for item in formats)
        or len(set(formats)) != len(formats)
    ):
        errors.append(
            "formatos deve ser uma lista não vazia de identificadores internos "
            "simples e únicos."
        )
        format_ids: list[str] = []
    else:
        format_ids = formats

    documents = contract.get("documentos")
    if not isinstance(documents, dict) or not documents:
        errors.append("documentos deve ser um objeto não vazio.")
    else:
        for name, declared_path in documents.items():
            _, error = _internal_kit_path(
                kit_root,
                declared_path,
                expected_kind="file",
            )
            if error:
                errors.append(f"documentos.{name}: {error}")

    if "modelos" in contract:
        models_root, error = _internal_kit_path(
            kit_root,
            contract["modelos"],
            expected_kind="directory",
        )
        if error:
            errors.append(f"modelos: {error}")
        elif models_root is not None:
            for model_path in models_root.rglob("*"):
                if model_path.is_symlink():
                    errors.append(
                        f"modelos: link simbólico não permitido em {model_path}."
                    )
                elif not (model_path.is_file() or model_path.is_dir()):
                    errors.append(
                        f"modelos: entrada não regular encontrada em {model_path}."
                    )

    if valid_author_id:
        author_root = lexical_root / "autores" / author_id
        if snapshot_mode:
            assert snapshot_map is not None
            profile, profile_error = _snapshot_yaml_mapping(
                snapshot_map,
                f"autores/{author_id}/autor.yaml",
            )
        else:
            safe_author_root, author_root_error = _safe_identifier_directory(
                root,
                "autores",
                author_id,
            )
            if author_root_error or safe_author_root is None:
                errors.append(f"Perfil do autor inválido: {author_root_error}")
                return {
                    "path": str(path),
                    "valid": False,
                    "error": "; ".join(errors),
                }
            author_root = safe_author_root
            profile_path, profile_path_error = _safe_regular_file(
                author_root,
                "autor.yaml",
            )
            if profile_path_error or profile_path is None:
                profile, profile_error = None, profile_path_error
            else:
                profile, profile_error = _load_yaml_mapping(profile_path)
        author_profile = profile.get("autor") if profile else None
        if profile_error or not isinstance(author_profile, dict):
            profile_reason = profile_error or "autor ausente"
            errors.append(f"Perfil do autor inválido: {profile_reason}")
        else:
            if author_profile.get("id") != author_id:
                errors.append("O id do perfil do autor não corresponde ao contrato.")
            author_formats = author_profile.get("formatos")
            if not isinstance(author_formats, list):
                errors.append("O perfil do autor não declara formatos válidos.")
                author_formats = []
            for format_id in format_ids:
                if format_id not in author_formats:
                    errors.append(
                        f"O autor {author_id} não autoriza o formato {format_id}."
                    )

        if snapshot_mode:
            assert snapshot_map is not None
            manifest, manifest_error = _snapshot_yaml_mapping(
                snapshot_map,
                f"autores/{author_id}/manifesto.yaml",
            )
        else:
            manifest_path, manifest_path_error = _safe_regular_file(
                author_root,
                "manifesto.yaml",
            )
            if manifest_path_error or manifest_path is None:
                manifest, manifest_error = None, manifest_path_error
            else:
                manifest, manifest_error = _load_yaml_mapping(manifest_path)
        configuration = manifest.get("configuracao") if manifest else None
        declared_kit = (
            configuration.get("kit") if isinstance(configuration, dict) else None
        )
        if manifest_error:
            errors.append(f"Manifesto do autor inválido: {manifest_error}")
        elif not isinstance(declared_kit, str):
            errors.append(
                "O manifesto do autor não declara configuracao.kit corretamente."
            )
        else:
            manifest_target = _lexical_absolute(author_root / declared_kit)
            expected_target = _lexical_absolute(kit_root)
            if manifest_target != expected_target:
                errors.append("configuracao.kit não aponta para o próprio kit.")

        for format_id in format_ids:
            if snapshot_mode:
                assert snapshot_map is not None
                format_data, format_error = _snapshot_yaml_mapping(
                    snapshot_map,
                    f"formatos/{format_id}/formato.yaml",
                )
            else:
                format_root, format_root_error = _safe_identifier_directory(
                    root,
                    "formatos",
                    format_id,
                )
                if format_root_error or format_root is None:
                    errors.append(
                        f"Contrato do formato {format_id} inválido: "
                        f"{format_root_error}"
                    )
                    continue
                format_path, format_path_error = _safe_regular_file(
                    format_root,
                    "formato.yaml",
                )
                if format_path_error or format_path is None:
                    format_data, format_error = None, format_path_error
                else:
                    format_data, format_error = _load_yaml_mapping(format_path)
            format_profile = format_data.get("formato") if format_data else None
            if format_error or not isinstance(format_profile, dict):
                errors.append(
                    f"Contrato do formato {format_id} inválido: "
                    f"{format_error or 'formato ausente'}"
                )
                continue
            if format_profile.get("id") != format_id:
                errors.append(f"O id do formato {format_id} é inconsistente.")
            format_authors = format_profile.get("autores")
            if not isinstance(format_authors, list) or author_id not in format_authors:
                errors.append(
                    f"O formato {format_id} não autoriza o autor {author_id}."
                )

    return {
        "path": str(path),
        "valid": not errors,
        "error": "; ".join(errors) if errors else None,
    }


def audit_collection(include_review: bool, output_root: str | None) -> dict[str, Any]:
    prompt_snapshots, prompt_discovery_reports = discover_prompt_snapshots(ROOT)
    render_resources, render_resource_reports = discover_render_resources(
        ROOT,
        set(),
    )
    image_snapshots = []
    image_discovery_reports = []
    if include_review:
        storage = load_storage(ROOT, output_root)
        # Não use ``area_root`` aqui: ele resolve links antes que o leitor por
        # descritores possa rejeitá-los. A auditoria preserva o caminho lexical.
        storage_root = (
            _lexical_absolute(Path(output_root).expanduser())
            if output_root is not None
            else storage.root
        )
        review_root = _lexical_absolute(storage_root / storage.areas["revisao"])
        if review_root.exists() or review_root.is_symlink():
            image_snapshots, image_discovery_reports = discover_image_snapshots(
                review_root
            )
    forbidden_snapshots, forbidden_discovery_reports = discover_image_snapshots(
        ROOT,
        ignored_top_level=frozenset({".git", ".venv", "__pycache__"}),
    )
    project_yamls, manifest_reports, project_discovery_reports = _project_inventory(
        ROOT
    )
    kit_yamls = kit_yaml_files(ROOT)
    kit_yaml_set = set(kit_yamls)
    yaml_snapshots, yaml_discovery_reports = discover_operational_yaml_snapshots(
        ROOT,
        [*project_yamls, *kit_yamls],
    )
    yaml_snapshot_map = {
        snapshot.path.relative_to(ROOT).as_posix(): snapshot.text
        for snapshot in yaml_snapshots
    }
    manifest_report_paths = {
        _lexical_absolute(Path(item["path"])) for item in manifest_reports
    }
    version_indices, version_index_reports = discover_version_indices(ROOT)
    rendering = []
    for snapshot in prompt_snapshots:
        if snapshot.renderer != "texto" and snapshot.renderer not in render_resources:
            continue
        rendering.append(
            rendering_report(
                snapshot.autor,
                snapshot.path,
                snapshot.renderer,
                prompt_text=snapshot.text,
                resource_texts=render_resources,
            )
        )
    prompt_reports = [
        prompt_report(snapshot.path, prompt_text=snapshot.text)
        for snapshot in prompt_snapshots
    ]
    return {
        "prompts": prompt_reports,
        "relatorios_descoberta_prompts": [
            asdict(item) for item in prompt_discovery_reports
        ],
        "relatorios_recursos_renderizacao": [
            asdict(item) for item in render_resource_reports
        ],
        "relatorios_descoberta_yaml": [
            asdict(item) for item in yaml_discovery_reports
        ],
        "relatorios_descoberta_imagens": [
            asdict(item)
            for item in [*image_discovery_reports, *forbidden_discovery_reports]
        ],
        "rendering": rendering,
        "images": [
            validate_image_file(snapshot.path, image_bytes=snapshot.data)
            for snapshot in image_snapshots
        ],
        "yaml": [
            kit_contract_report(
                ROOT,
                snapshot.path,
                yaml_text=snapshot.text,
                snapshot_map=yaml_snapshot_map,
            )
            if snapshot.path in kit_yaml_set
            else validate_yaml_file(snapshot.path, yaml_text=snapshot.text)
            for snapshot in yaml_snapshots
            if snapshot.path not in manifest_report_paths
        ]
        + manifest_reports
        + project_discovery_reports,
        # Índices são metadados editoriais: não entram na contagem dos YAMLs
        # operacionais e não alteram projetos nem a geração.
        "indices_versao": len(version_indices),
        "indices_versao_invalidos": sum(
            1 for item in version_index_reports if not item.valid
        ),
        "contratos_indices_versao": [asdict(item) for item in version_indices],
        "relatorios_indices_versao": [
            asdict(item) for item in version_index_reports
        ],
        "forbidden_images": [
            str(snapshot.path) for snapshot in forbidden_snapshots
        ],
    }


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    report: dict[str, Any] = {"root": str(ROOT)}
    if args.acervo or not any((args.prompt, args.imagem, args.ocr)):
        report.update(audit_collection(args.revisao, args.saida_root))
    else:
        report["prompts"] = [prompt_report(resolve_local(item)) for item in args.prompt]
        report["images"] = [
            validate_image_file(resolve_local(item)) for item in args.imagem
        ]
        report["yaml"] = []
    if args.ocr:
        image_path = resolve_local(args.ocr)
        expected_path = resolve_local(args.esperado) if args.esperado else None
        ocr_text = run_tesseract(image_path, args.idioma)
        expected = extract_expected_text(load_prompt(expected_path)) if expected_path else []
        report["ocr"] = {
            "image": str(image_path),
            "expected_source": str(expected_path) if expected_path else None,
            "recognized_characters": len(ocr_text),
            "comparison": compare_ocr_text(ocr_text, expected) if expected else None,
        }
    return report


def report_errors(report: dict[str, Any]) -> int:
    invalid = 0
    for section in ("prompts", "rendering", "images", "yaml"):
        invalid += sum(1 for item in report.get(section, []) if not item.get("valid"))
    invalid += sum(
        1
        for item in report.get("relatorios_indices_versao", [])
        if not item.get("valid")
    )
    for section in (
        "relatorios_descoberta_prompts",
        "relatorios_recursos_renderizacao",
        "relatorios_descoberta_yaml",
        "relatorios_descoberta_imagens",
    ):
        invalid += sum(
            1 for item in report.get(section, []) if not item.get("valid")
        )
    invalid += len(report.get("forbidden_images", []))
    return invalid


def print_human(report: dict[str, Any]) -> None:
    prompts = report.get("prompts", [])
    images = report.get("images", [])
    yamls = report.get("yaml", [])
    rendering = report.get("rendering", [])
    invalid = report_errors(report)
    warnings = sum(
        1
        for prompt in prompts
        for finding in prompt.get("findings", [])
        if finding["severity"] in {"warning", "review"}
    )
    print(f"Prompts: {len(prompts)}")
    print(f"Renderizações validadas: {len(rendering)}")
    print(f"Imagens: {len(images)}")
    print(f"YAMLs: {len(yamls)}")
    print(f"Índices de versão: {report.get('indices_versao', 0)}")
    print(
        "Índices de versão inválidos: "
        f"{report.get('indices_versao_invalidos', 0)}"
    )
    print(f"Imagens proibidas no projeto: {len(report.get('forbidden_images', []))}")
    print(f"Erros: {invalid}")
    print(f"Avisos para revisão humana: {warnings}")
    for prompt in prompts:
        for finding in prompt.get("findings", []):
            print(
                f"[{finding['severity'].upper()}] {prompt['path']}: "
                f"{finding['message']}"
            )
        if not prompt.get("valid") and prompt.get("error"):
            print(f"[ERRO] {prompt['path']}: {prompt['error']}")
    for section in (
        "relatorios_descoberta_prompts",
        "relatorios_recursos_renderizacao",
        "relatorios_descoberta_yaml",
        "relatorios_descoberta_imagens",
    ):
        for item in report.get(section, []):
            if not item.get("valid"):
                print(
                    f"[ERRO] {item.get('path', '<recurso sem caminho>')}: "
                    f"{item.get('error') or 'recurso inválido'}"
                )
    for item in report.get("relatorios_indices_versao", []):
        if not item.get("valid"):
            print(
                f"[ERRO] {item.get('path', '<índice sem caminho>')}: "
                f"{item.get('error') or 'índice de versão inválido'}"
            )
    if report.get("ocr"):
        comparison = report["ocr"].get("comparison")
        if comparison:
            print(
                "OCR:",
                f"{comparison['present_count']}/{comparison['expected_count']} "
                "trechos encontrados.",
            )


def main() -> int:
    args = build_parser().parse_args()
    try:
        report = build_report(args)
    except Exception as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 2
    encoded = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.relatorio:
        path = resolve_local(args.relatorio)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(encoded, encoding="utf-8")
        print(f"Relatório salvo em: {path}", file=sys.stderr)
    if args.json:
        print(encoded, end="")
    else:
        print_human(report)
    return 1 if report_errors(report) else 0


if __name__ == "__main__":
    raise SystemExit(main())
