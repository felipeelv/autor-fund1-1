"""Leitura de fonte bruta e rascunho de prompt.

A fonte bruta é o material didático recebido, versionado dentro do autor. Este
módulo faz duas coisas e apenas duas:

1. lê a fonte e descreve a sua estrutura, para que uma pessoa escolha o recorte;
2. monta o **rascunho** de um prompt, transportando texto literal da fonte e
   marcando explicitamente o que exige decisão editorial.

O que este módulo nunca faz: escrever conteúdo que não esteja na fonte. O
recorte, a hierarquia visual e a redação final são trabalho humano — o rascunho
existe para eliminar o trabalho mecânico, não para substituir a reescrita.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

__all__ = [
    "PENDING_DECISION",
    "Section",
    "approve_draft",
    "build_prompt_draft",
    "clean_export_escapes",
    "parse_source",
    "prompt_state",
    "section_literals",
    "split_front_matter",
]

# O Google Docs exporta markdown escapando pontuação: "\-", "\!", "\=".
_ESCAPED_PUNCTUATION = re.compile(r"\\([-!=+*_#\[\]().:;,\"'>])")
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_ILLUSTRATION = re.compile(r"\[\s*ilustra[çc][ãa]o", re.IGNORECASE)
_TABLE_SEPARATOR = re.compile(r"^[\s|:-]+$")
_LIST_ITEM = re.compile(r"^[-*+]\s+(.*)$")
_EMPHASIS = re.compile(r"[*_`]+")

# Um literal muito longo não é texto de página: é parágrafo de apostila.
_MAX_LITERAL = 160

# Marca deixada pelo rascunho onde uma pessoa precisa decidir.
PENDING_DECISION = "<<DECISÃO EDITORIAL"

_DRAFT_SUFFIX = "-rascunho"
_FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_DRAFT_NOTICE = re.compile(
    r"^> \*\*RASCUNHO.*?(?=\n[^>\n])", re.DOTALL | re.MULTILINE
)


def clean_export_escapes(text: str) -> str:
    """Remove o escape de pontuação que a exportação do Docs insere."""
    return _ESCAPED_PUNCTUATION.sub(r"\1", text)


def _strip_emphasis(text: str) -> str:
    return _EMPHASIS.sub("", text).strip()


@dataclass
class Section:
    """Um trecho da fonte delimitado por um cabeçalho markdown."""

    index: int
    level: int
    title: str
    body: str
    start_line: int
    end_line: int
    illustrations: int = 0
    has_table: bool = False
    literals: list[str] = field(default_factory=list)

    @property
    def line_range(self) -> str:
        return f"{self.start_line}-{self.end_line}"


def parse_source(text: str) -> list[Section]:
    """Divide a fonte em seções, uma por cabeçalho com título real.

    Cabeçalhos vazios — comuns no fim de arquivos exportados do Docs — são
    ignorados, e o corpo de cada seção vai até o cabeçalho seguinte.
    """
    lines = text.splitlines()
    marks: list[tuple[int, int, str]] = []
    for number, line in enumerate(lines, start=1):
        match = _HEADING.match(line)
        if not match:
            continue
        title = _strip_emphasis(clean_export_escapes(match.group(2)))
        if not title:
            continue
        marks.append((number, len(match.group(1)), title))

    sections: list[Section] = []
    for position, (start, level, title) in enumerate(marks):
        end = marks[position + 1][0] - 1 if position + 1 < len(marks) else len(lines)
        body = clean_export_escapes("\n".join(lines[start:end])).strip()
        section = Section(
            index=position + 1,
            level=level,
            title=title,
            body=body,
            start_line=start,
            end_line=end,
            illustrations=len(_ILLUSTRATION.findall(body)),
            has_table=any(line.lstrip().startswith("|") for line in body.splitlines()),
        )
        section.literals = section_literals(section)
        sections.append(section)
    return sections


def section_literals(section: Section) -> list[str]:
    """Texto da seção que pode ser transportado literalmente para o prompt.

    Recolhe itens de lista, células de tabela e frases curtas. Descarta
    marcação de ilustração, separador de tabela e parágrafo longo, que é texto
    de apostila e não cabe numa página-imagem.
    """
    found: list[str] = []
    seen: set[str] = set()

    def keep(raw: str) -> None:
        value = _strip_emphasis(raw)
        if not value or len(value) > _MAX_LITERAL:
            return
        if _ILLUSTRATION.search(value) or _TABLE_SEPARATOR.match(value):
            return
        if value in seen:
            return
        seen.add(value)
        found.append(value)

    for line in section.body.splitlines():
        stripped = line.strip()
        if not stripped or _ILLUSTRATION.search(stripped):
            continue
        if stripped.startswith("|"):
            if _TABLE_SEPARATOR.match(stripped):
                continue
            for cell in stripped.strip("|").split("|"):
                keep(cell)
            continue
        item = _LIST_ITEM.match(stripped)
        if item:
            keep(item.group(1))
            continue
        if stripped.startswith(">"):
            keep(stripped.lstrip("> "))
            continue
        if stripped.startswith("#"):
            continue
        keep(stripped)
    return found


def build_prompt_draft(
    *,
    author: str,
    discipline: str,
    school_year: str,
    year_label: str,
    unit: str,
    page_number: int,
    page_title: str,
    sections: list[Section],
    source_path: str,
    visual_system: str,
    locks: str,
) -> str:
    """Monta o rascunho do prompt de uma página.

    Preenche o que é derivável — cabeçalho, sistema visual, textos literais e
    travas do autor — e marca com `<<DECISÃO EDITORIAL>>` o que precisa de uma
    pessoa: o pedido da página e a composição.
    """
    literals: list[str] = []
    seen: set[str] = set()
    for section in sections:
        for literal in section.literals:
            if literal not in seen:
                seen.add(literal)
                literals.append(literal)

    origem = ", ".join(f"{s.title} (linhas {s.line_range})" for s in sections)
    texts = "\n".join(f"- {literal}" for literal in literals) or "- (sem literal extraído)"

    return f"""Use case: scientific-educational
Asset type: página {page_number} de uma sequência didática de {discipline} do {year_label}

> **RASCUNHO gerado por `preparar.py`.** Não é prompt aprovado.
>
> Fonte: `{source_path}`
> Trechos: {origem}
> Autor: `{author}` · ano: `{school_year}` · unidade: {unit}
>
> Antes de gerar imagem: resolver os pontos marcados como decisão editorial,
> conferir os textos exatos contra a fonte e salvar como `-v1` sem o aviso.

## PEDIDO

<<DECISÃO EDITORIAL: descrever em duas ou três frases o que esta página faz —
o recorte, a intenção pedagógica principal e o que fica de fora. O rascunho não
decide isso porque a escolha depende de como a unidade foi dividida em páginas.>>

Título previsto: {page_title}

## SISTEMA VISUAL

{visual_system}

## COMPOSIÇÃO E TÍTULO

<<DECISÃO EDITORIAL: definir a hierarquia da página — o que é protagonista, em
quantos recortes o conteúdo se distribui, onde entra cada texto e qual elemento
carrega o sentido. É aqui que entram também as correções nascidas de defeitos
já observados na produção, que nenhum template consegue prever.>>

## TEXTOS EXATOS

Extraídos literalmente da fonte. Revisar: remover o que não cabe na página,
ajustar a ordem e condensar onde a leitura pedir — sem trocar número, nome
próprio, unidade ou termo técnico.

{texts}

## TRAVAS

{locks}
"""


def split_front_matter(text: str) -> tuple[dict, str]:
    """Separa o front matter YAML do corpo do prompt.

    O front matter guarda estado, revisor e data. Ele nunca é enviado à API:
    quem lê o prompt para gerar recebe apenas o corpo.
    """
    import yaml  # local: mantém o módulo utilizável sem carregar YAML à toa

    match = _FRONT_MATTER.match(text)
    if not match:
        return {}, text
    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise ValueError(f"front matter inválido no prompt: {exc}") from exc
    if meta is None:
        meta = {}
    if not isinstance(meta, dict):
        raise ValueError("front matter do prompt deve ser um mapa YAML.")
    return meta, text[match.end():]


def prompt_state(path, meta: dict) -> str:
    """Estado do prompt: 'rascunho' ou 'aprovado'.

    O nome do arquivo manda. Um arquivo `-rascunho` continua rascunho mesmo que
    o front matter diga o contrário, para que renomear seja o ato deliberado de
    aprovar. Prompt legado, sem front matter e sem sufixo, conta como aprovado.
    """
    from pathlib import Path as _Path

    if _Path(path).stem.endswith(_DRAFT_SUFFIX):
        return "rascunho"
    if str(meta.get("estado", "aprovado")).strip().lower() == "rascunho":
        return "rascunho"
    return "aprovado"


def approve_draft(draft_path, *, reviewer: str, approved_at: str):
    """Promove um rascunho a prompt aprovado `-v1`.

    Recusa aprovar enquanto houver decisão editorial pendente. O rascunho é
    preservado: a aprovação cria um arquivo novo, nunca sobrescreve.
    """
    from pathlib import Path as _Path

    source = _Path(draft_path)
    text = source.read_text(encoding="utf-8")
    if PENDING_DECISION in text:
        raise ValueError(
            "há decisão editorial pendente no rascunho; resolva antes de aprovar."
        )
    if not source.stem.endswith(_DRAFT_SUFFIX):
        raise ValueError(f"não é um rascunho: {source.name}")

    destination = source.with_name(
        f"{source.stem[: -len(_DRAFT_SUFFIX)]}-v1{source.suffix}"
    )
    if destination.exists():
        raise ValueError(f"já existe: {destination.name}")

    _, body = split_front_matter(text)
    body = _DRAFT_NOTICE.sub("", body).lstrip()
    header = (
        "---\n"
        "estado: aprovado\n"
        f"revisor: {reviewer}\n"
        f"aprovado_em: {approved_at}\n"
        f"origem: {source.name}\n"
        "---\n"
    )
    destination.write_text(header + body, encoding="utf-8")
    return destination
