#!/usr/bin/env python3
"""Lê a fonte bruta e prepara rascunhos de prompt.

Este script é o passo anterior ao `gerar.py`. Ele não chama API, não consome
crédito e não decide conteúdo: transporta texto literal da fonte para a
estrutura de prompt já validada pelos autores `matematica` e `ingles`, e marca
o que exige decisão editorial.

    uv run preparar.py --inventario <fonte.md>
    uv run preparar.py --recorte <recorte.yaml> [--forcar]

O inventário lista as seções da fonte com índice, para escolher o recorte. O
recorte declara quais seções alimentam cada página e gera um rascunho por
página, com o sufixo `-rascunho`: prompt aprovado é sempre `-vN`, escrito por
uma pessoa a partir do rascunho.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

from gerador_imagens.config import ConfigError
from gerador_imagens.sources import build_prompt_draft, parse_source

ROOT = Path(__file__).resolve().parent

YEAR_LABELS = {
    "infantil4": "Infantil 4",
    "infantil5": "Infantil 5",
    "1ano": "1º ano",
    "2ano": "2º ano",
    "3ano": "3º ano",
}


def draft_path(
    root: Path, author: str, school_year: str, year_label: str, bimester: str,
    unit: str, page_number: int, slug: str,
) -> Path:
    """Caminho do rascunho, na área de prompts do autor."""
    return (
        root / "autores" / author / "anos" / school_year / "prompts" / year_label
        / bimester / f"{unit}-p{page_number:02d}-{slug}-rascunho.md"
    )


def _read(path: Path, label: str) -> str:
    if not path.is_file():
        raise ConfigError(f"{label} não encontrado: {path}")
    return path.read_text(encoding="utf-8")


def _author_visual_system(root: Path, author: str, school_year: str) -> str:
    """Referência ao padrão visual do ano, sem inventar direção."""
    ordinal = school_year[0] if school_year and school_year[0].isdigit() else school_year
    relative = f"direcao/PADRAO-VISUAL-{ordinal}ANO.md"
    path = root / "autores" / author / relative
    if path.is_file():
        return (
            f"Seguir integralmente `autores/{author}/{relative}`, em especial o DNA\n"
            "visual, a paleta com um papel fixo por cor e a densidade de núcleos do ano.\n"
            "Condensar aqui, ao revisar, o parágrafo que descreve o sistema visual desta\n"
            "página específica."
        )
    return f"Padrão visual do ano não encontrado em `{relative}`. Declarar antes de gerar."


def _author_locks(root: Path, author: str, school_year: str) -> str:
    rules = f"autores/{author}/anos/{school_year}/REGRAS.md"
    exists = (root / rules).is_file()
    base = (
        f"Valem as travas de `{rules}` e o `prompt_sufixo` do autor, que o gerador\n"
        "injeta automaticamente."
        if exists
        else f"Regras do ano não encontradas em `{rules}`. Escrever antes de gerar."
    )
    return (
        f"{base}\n\n"
        "Invioláveis, independentes de ano: não inventar número, nome próprio, data,\n"
        "lugar, povo ou termo ausente da fonte; renderizar cada texto literal exatamente\n"
        "uma vez; nenhum texto além da lista de TEXTOS EXATOS."
    )


def run_inventory(source: Path) -> int:
    sections = parse_source(_read(source, "fonte"))
    print(f"Fonte: {source}")
    print(f"Seções: {len(sections)}\n")
    print(f"{'#':>4}  {'nív':>3}  {'linhas':>11}  {'lit':>4}  {'ilu':>4}  título")
    for section in sections:
        marks = "T" if section.has_table else " "
        print(
            f"{section.index:>4}  {section.level:>3}  {section.line_range:>11}  "
            f"{len(section.literals):>4}  {section.illustrations:>4}{marks} {section.title}"
        )
    print("\nlit = literais extraíveis · ilu = marcações de ilustração · T = tem tabela")
    return 0


def run_recorte(recorte_path: Path, forcar: bool) -> int:
    raw: Any = yaml.safe_load(_read(recorte_path, "recorte"))
    if not isinstance(raw, dict):
        raise ConfigError("recorte deve conter objeto YAML.")
    cut = raw.get("recorte")
    pages = raw.get("paginas")
    if not isinstance(cut, dict) or not isinstance(pages, list) or not pages:
        raise ConfigError("recorte exige o mapa 'recorte' e a lista 'paginas'.")

    for key in ("autor", "ano", "ano_letivo", "bimestre", "unidade", "fonte", "disciplina"):
        if not cut.get(key):
            raise ConfigError(f"recorte.{key} é obrigatório.")

    author = str(cut["autor"])
    school_year = str(cut["ano"])
    if school_year not in YEAR_LABELS:
        raise ConfigError(f"ano fora das etapas canônicas: {school_year}")
    if not (ROOT / "autores" / author / "autor.yaml").is_file():
        raise ConfigError(f"autor inexistente: {author}")

    source_rel = str(cut["fonte"])
    sections = parse_source(_read(ROOT / source_rel, "fonte"))
    by_index = {section.index: section for section in sections}

    visual = _author_visual_system(ROOT, author, school_year)
    locks = _author_locks(ROOT, author, school_year)
    written: list[Path] = []

    for page in pages:
        if not isinstance(page, dict):
            raise ConfigError("cada página deve ser um mapa.")
        for key in ("numero", "slug", "titulo", "secoes"):
            if page.get(key) in (None, "", []):
                raise ConfigError(f"página exige '{key}'.")
        chosen = []
        for index in page["secoes"]:
            if index not in by_index:
                raise ConfigError(
                    f"seção {index} não existe na fonte (use --inventario)."
                )
            chosen.append(by_index[index])

        destination = draft_path(
            ROOT, author, school_year, str(cut["ano_letivo"]), str(cut["bimestre"]),
            str(cut["unidade"]), int(page["numero"]), str(page["slug"]),
        )
        if destination.exists() and not forcar:
            raise ConfigError(f"rascunho já existe: {destination}. Use --forcar.")

        draft = build_prompt_draft(
            author=author,
            discipline=str(cut["disciplina"]),
            school_year=school_year,
            year_label=YEAR_LABELS[school_year],
            unit=str(cut["unidade"]),
            page_number=int(page["numero"]),
            page_title=str(page["titulo"]),
            sections=chosen,
            source_path=source_rel,
            visual_system=visual,
            locks=locks,
        )
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(draft, encoding="utf-8")
        written.append(destination)
        print(f"Rascunho: {destination.relative_to(ROOT)}")

    print(f"\n{len(written)} rascunho(s). Nenhuma imagem foi gerada e nenhuma API foi chamada.")
    print("Revise cada um, resolva as decisões editoriais e salve como -v1.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Lê a fonte bruta e prepara rascunhos de prompt."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--inventario", metavar="FONTE", help="Lista as seções da fonte.")
    group.add_argument("--recorte", metavar="YAML", help="Gera rascunhos a partir do recorte.")
    parser.add_argument("--forcar", action="store_true", help="Sobrescreve rascunho existente.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.inventario:
            return run_inventory(Path(args.inventario))
        return run_recorte(Path(args.recorte), args.forcar)
    except ConfigError as error:
        print(f"Erro: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
