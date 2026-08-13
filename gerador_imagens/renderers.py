from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Mapping

import yaml

from .config import ConfigError
from .core import load_prompt


RENDERERS = {
    "texto",
}

COLAGEM_MASTERS = {
    "capa": "MASTER-CAPA.md",
    "conteudo": "MASTER-CONTEUDO.md",
}


def _mapping(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, dict):
        raise ConfigError(f"{label} precisa ser um objeto YAML.")
    return value


def _list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        raise ConfigError(f"{label} precisa ser uma lista YAML.")
    return value


def _load_yaml(path: Path, resource_text: str | None = None) -> Mapping[str, Any]:
    if resource_text is None:
        text = path.read_text(encoding="utf-8")
    else:
        text = resource_text
    try:
        value = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        raise ConfigError(f"YAML inválido em {path}: {exc}") from exc
    return _mapping(value, str(path))


def _frontmatter(
    path: Path,
    prompt_text: str | None = None,
) -> tuple[Mapping[str, Any], str] | None:
    text = prompt_text if prompt_text is not None else load_prompt(path)
    if not text.startswith("---"):
        return None
    match = re.match(r"\A---[ \t]*\n(.*?)\n---[ \t]*(?:\n|\Z)(.*)\Z", text, re.DOTALL)
    if not match:
        raise ConfigError(f"Frontmatter YAML incompleto em {path}.")
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise ConfigError(f"Frontmatter YAML inválido em {path}: {exc}") from exc
    return _mapping(data, f"frontmatter de {path}"), match.group(2).strip()


def _master_template(path: Path, resource_text: str | None = None) -> str:
    text = resource_text if resource_text is not None else path.read_text(encoding="utf-8")
    match = re.search(r"```(?:text)?[ \t]*\n(.*?)\n```", text, re.DOTALL)
    if not match:
        raise ConfigError(f"Bloco de prompt não encontrado em {path}.")
    return match.group(1)


def _replace_placeholders(template: str, values: Mapping[str, Any]) -> str:
    prompt = template
    for key, value in values.items():
        prompt = prompt.replace("{{" + key + "}}", str(value))
    unresolved = sorted(set(re.findall(r"\{\{[a-zA-Z0-9_]+\}\}", prompt)))
    if unresolved:
        raise ConfigError(
            "Placeholders não preenchidos: " + ", ".join(unresolved)
        )
    return prompt


def _bullets(items: Any, label: str) -> str:
    values = _list(items, label)
    return "\n     • ".join([""] + [str(item) for item in values]).strip()


def _editorial_vocabulary(items: Any) -> str:
    values = _list(items, "vocab_termos")
    if len(values) != 6:
        raise ConfigError(
            f"O vocabulário editorial exige 6 termos; recebeu {len(values)}."
        )
    lines = []
    for index, item in enumerate(values, start=1):
        data = _mapping(item, f"vocab_termos[{index}]")
        lines.append(
            f'{data["termo"]} (pictogram: {data["icone"]}) — '
            f'"{data["definicao"]}"'
        )
    return "; ".join(lines)


def _editorial_summary(items: Any) -> str:
    values = _list(items, "resumo_visual")
    if len(values) != 6:
        raise ConfigError(
            f"O resumo visual editorial exige 6 etapas; recebeu {len(values)}."
        )
    return " → ".join(
        f'{_mapping(item, "etapa do resumo")["icone"]}: '
        f'"{_mapping(item, "etapa do resumo")["legenda"]}"'
        for item in values
    )


def _render_editorial(
    content: Mapping[str, Any],
    discipline: Mapping[str, Any],
    series: Mapping[str, Any],
    template: str,
) -> str:
    reflections = _list(content["reflexoes"], "reflexoes")
    if len(reflections) != 3:
        raise ConfigError("reflexoes precisa conter exatamente 3 itens.")
    box2_legend = _list(content["box2_legenda"], "box2_legenda")
    organize_by_lessons = bool(content.get("organizar_por_aulas", False))
    opening_author = str(content.get("citacao_abertura_autor", "")).strip()
    closing_author = str(content.get("citacao_fechamento_autor", "")).strip()
    summary_title = str(content.get("resumo_titulo", "RESUMO VISUAL")).strip()
    opening_attribution = (
        f'Attribution in smaller caps: "— {opening_author}".'
        if opening_author
        else "NO ATTRIBUTION: render nothing beneath the opening quotation."
    )
    closing_attribution = (
        f'Render the attribution in smaller caps: "— {closing_author}".'
        if closing_author
        else "NO ATTRIBUTION: render nothing beneath the closing quotation."
    )
    summary_header = (
        f'Render a "{summary_title}" pill header on a dark teal ribbon, '
        "anchored on the left."
        if summary_title
        else (
            "DO NOT render any title, label or ribbon for this strip. "
            "Begin directly with the six icons and their captions."
        )
    )
    vocabulary_rendered = _editorial_vocabulary(content["vocab_termos"])
    summary_rendered = _editorial_summary(content["resumo_visual"])
    lesson_headers = {
        index: (
            f"AULA {index} · {content[f'box{index}_titulo']}"
            if organize_by_lessons
            else f"{index}. {content[f'box{index}_titulo']}"
        )
        for index in range(1, 5)
    }
    box5_type = str(content.get("box5_tipo", "vocabulario")).strip()
    if box5_type == "aula":
        box5_header = (
            f"AULA 5 · {content['box5_titulo']}"
            if organize_by_lessons
            else f"5. {content['box5_titulo']}"
        )
        box5_instruction = (
            "BOX 5 — Lower right — LESSON CARD, visually equal to boxes 1–4, "
            "not a vocabulary grid.\n"
            f'   Header: "{box5_header}" in bold editorial serif caps.\n'
            "   Body: 4 short factual icon-bullets using "
            f"{content['box5_icons']}.\n"
            "   Inset: "
            f"{content['box5_inset_descricao']}.\n"
            f'   Handwritten caption: "{content["box5_caption"]}".'
        )
    elif box5_type == "vocabulario":
        box5_instruction = (
            "BOX 5 — Lower right — VOCABULARY GRID (always 6 cards, "
            "3 columns × 2 rows, NEVER 2×3 NEVER 3×3):\n"
            f'   Header: "5. {content.get("vocab_titulo", "VOCABULÁRIO ESSENCIAL")}" '
            "in bold caps.\n"
            "   Six dark-navy cards, each with a large mustard pictogram, "
            "ALL-CAPS mustard term and two-line cream definition.\n"
            f"   The six terms are: {vocabulary_rendered}."
        )
    else:
        raise ConfigError(
            "box5_tipo precisa ser 'vocabulario' ou 'aula'."
        )
    footer_mode = str(content.get("rodape_modo", "resumo")).strip()
    if footer_mode == "conceitos":
        footer_title = str(
            content.get("rodape_titulo", "PARA NÃO ESQUECER")
        ).strip()
        footer_instruction = (
            f'Render the heading "{footer_title}" as a compact dark-teal '
            "editorial label on the left. To its right, create SIX compact "
            "white concept chips in one horizontal row, separated by thin "
            "mustard dividers. Each chip has one mustard pictogram, one "
            "dark-teal all-caps term and a one-line definition. Do not connect "
            "these chips with arrows. The six concepts are: "
            f"{vocabulary_rendered}. The label \"RESUMO VISUAL\" must not appear."
        )
    elif footer_mode == "resumo":
        footer_instruction = (
            f"{summary_header} Arrange SIX small circular icons horizontally "
            "across the usable width and connect them with thin mustard arrows. "
            "Each circle has one pictogram and a short caption. The six steps "
            f"are: {summary_rendered}."
        )
    else:
        raise ConfigError("rodape_modo precisa ser 'resumo' ou 'conceitos'.")
    values = {
        "tema_principal": content["tema_principal"],
        "credito_curto": content["credito_curto"],
        "titulo_linha1": content.get("titulo_linha1", ""),
        "titulo_linha2": content.get("titulo_linha2", ""),
        "titulo_linha3": content.get("titulo_linha3", ""),
        "subtitulo_hook": content["subtitulo_hook"],
        "citacao_abertura": content["citacao_abertura"],
        "citacao_abertura_atribuicao": opening_attribution,
        "hero_descricao": content["hero_descricao"],
        "hero_tratamento": content.get("hero_tratamento")
        or discipline["hero_tratamento_default"],
        "hero_caption": content["hero_caption"],
        "badge_icon": content.get("badge_icon") or discipline["badge_icon_default"],
        "badge_formato": content.get(
            "badge_formato",
            (
                "black circular badge with mustard pictogram, mustard title, "
                "cream body text and three mustard-star bullets"
            ),
        ),
        "badge_titulo": content["badge_titulo"],
        "badge_subtitulo": content.get("badge_subtitulo", ""),
        "badge_fato_1": content["badge_fato_1"],
        "badge_fato_2": content["badge_fato_2"],
        "badge_fato_3": content["badge_fato_3"],
        "badge_conectores_instrucao": content.get(
            "badge_conectores_instrucao",
            "A thin hand-drawn arrow curves out from the bottom of the badge.",
        ),
        "box1_titulo": content["box1_titulo"],
        "box1_cabecalho": lesson_headers[1],
        "box1_icons": content["box1_icons"],
        "box1_inset_descricao": content["box1_inset_descricao"],
        "box1_caption": content["box1_caption"],
        "box2_titulo": content["box2_titulo"],
        "box2_cabecalho": lesson_headers[2],
        "box2_bullets_estilo": content["box2_bullets_estilo"],
        "box2_visual": content["box2_visual"],
        "box2_legenda": "; ".join(str(item) for item in box2_legend),
        "box2_caption": content["box2_caption"],
        "box3_titulo": content["box3_titulo"],
        "box3_cabecalho": lesson_headers[3],
        "box3_termos": content["box3_termos"],
        "box3_inset_descricao": content["box3_inset_descricao"],
        "box3_caption": content["box3_caption"],
        "box4_titulo": content["box4_titulo"],
        "box4_cabecalho": lesson_headers[4],
        "box4_icons": content["box4_icons"],
        "box4_inset_descricao": content["box4_inset_descricao"],
        "box4_caption": content["box4_caption"],
        "box5_conteudo_instrucao": box5_instruction,
        "vocab_termos_lista": vocabulary_rendered,
        "vocab_titulo": content.get(
            "vocab_titulo", "VOCABULÁRIO ESSENCIAL"
        ),
        "reflexao_1": reflections[0],
        "reflexao_2": reflections[1],
        "reflexao_3": reflections[2],
        "resumo_visual_etapas": summary_rendered,
        "resumo_cabecalho_instrucao": summary_header,
        "rodape_conteudo_instrucao": footer_instruction,
        "citacao_fechamento": content["citacao_fechamento"],
        "citacao_fechamento_atribuicao": closing_attribution,
        "tom_disciplina": discipline["tom_disciplina"],
        "cor_destaque": discipline["cor_destaque"],
        "cor_secundaria_escura": discipline["cor_secundaria_escura"],
        "hero_estilo_renderizacao": discipline["hero_estilo_renderizacao"],
        "emblema_final": discipline["emblema_final"],
        "permitir_cristao": str(discipline["permitir_cristao"]).lower(),
        "atmosfera_capitulo": content.get(
            "atmosfera_capitulo",
            "(não definida — use atmosfera coerente com o tema)",
        ),
        "paleta_acessoria_capitulo": content.get(
            "paleta_acessoria_capitulo",
            "(não definida — use a paleta canônica da disciplina)",
        ),
        "iconografia_capitulo": content.get(
            "iconografia_capitulo",
            "(não definida — use iconografia da disciplina)",
        ),
        "layout_variant": content.get("layout_variant", "hero-central"),
        "galeria_central_instruction": content.get(
            "galeria_central_instruction",
            (
                "NO central badge / identity card — instead, use a thin "
                "horizontal divider strip between the top row and bottom row "
                "of boxes, with a small theme-glyph centered on the divider"
            ),
        ),
        "titulo_tratamento": content.get(
            "titulo_tratamento",
            (
                "CANONICAL: use the three-layer condensed-serif hierarchy "
                "with irregular chalk-brush strokes described in section 1"
            ),
        ),
        "tipografia_conteudo": content.get(
            "tipografia_conteudo",
            (
                "CANONICAL: medium-weight editorial serif for body text, "
                "condensed serif caps for section headers and handwritten "
                "italic only for short captions"
            ),
        ),
        "titulo_cor_protagonista": content.get(
            "titulo_cor_protagonista", discipline["cor_destaque"]
        ),
        "titulo_cor_chalk": content.get(
            "titulo_cor_chalk", "rich black ink #1A1A1A"
        ),
        "titulo_cor_letras_cream": content.get(
            "titulo_cor_letras_cream", "cream off-white #F2EBDB"
        ),
        "faixa_etaria": series["faixa_etaria"],
        "densidade_pedagogica": (
            f"{series['densidade_pedagogica']} | "
            f"TONE ADJUSTMENT: {series['ajustes_tom']} | "
            f"PALETTE ADJUSTMENT: {series['ajustes_paleta']}"
        ),
    }
    prompt = _replace_placeholders(template, values)
    details = [
        "\n\n--- DETALHAMENTO DE BULLETS "
        "(texto verbatim a aparecer na imagem) ---",
        f"\nBOX 1 bullets:{_bullets(content['box1_bullets'], 'box1_bullets')}",
        f"\nBOX 2 bullets:{_bullets(content['box2_bullets'], 'box2_bullets')}",
        f"\nBOX 3 bullets:{_bullets(content['box3_bullets'], 'box3_bullets')}",
        f"\nBOX 4 bullets:{_bullets(content['box4_bullets'], 'box4_bullets')}",
    ]
    if box5_type == "aula":
        details.append(
            f"\nBOX 5 bullets:{_bullets(content['box5_bullets'], 'box5_bullets')}"
        )
    return prompt + "\n".join(details)


def _scientific_cards(items: Any) -> str:
    cards = _list(items, "cards")
    if not cards:
        return (
            "(NO BOTTOM CALLOUT BAND — Zone 3 is collapsed; all the content "
            "lives in Zone 2 sections of the central composition)"
        )
    if not 3 <= len(cards) <= 6:
        raise ConfigError(f"cards exige 0 ou 3 a 6 itens; recebeu {len(cards)}.")
    rendered = []
    for index, item in enumerate(cards, start=1):
        card = _mapping(item, f"cards[{index}]")
        bullets = "\n      - ".join(
            str(value) for value in _list(card.get("bullets", []), "card.bullets")
        )
        inset = card.get("inset_descricao", "")
        inset_line = f"\n   INSET: {inset}" if inset else ""
        rendered.append(
            f"\nCARD {index:02d}:\n"
            f"   CATEGORY TAG: {card['categoria_tag']} "
            f"(tag pill color: {card['categoria_cor']})\n"
            f"   HEADER: {card['titulo']}\n"
            f"   ICON: {card['icone']}\n"
            f"   BULLETS:\n      - {bullets}"
            f"{inset_line}"
        )
    return "\n".join(rendered)


def _scientific_flows(items: Any) -> str:
    values = _list(items, "fluxos")
    if not values:
        return "(no extra arrows beyond default central→cards radial connectors)"
    return " · ".join(f'"{item}"' for item in values)


def _scientific_summary(items: Any) -> str:
    values = _list(items, "resumo_visual")
    if not 3 <= len(values) <= 5:
        raise ConfigError(f"resumo_visual exige 3 a 5 etapas; recebeu {len(values)}.")
    return " → ".join(
        f'{_mapping(item, "etapa do resumo")["icone"]} '
        f'"{_mapping(item, "etapa do resumo")["legenda"]}"'
        for item in values
    )


def _scientific_vocabulary(items: Any) -> str:
    values = _list(items, "vocab_chave")
    if not 2 <= len(values) <= 4:
        raise ConfigError(f"vocab_chave exige 2 a 4 termos; recebeu {len(values)}.")
    return "; ".join(
        f'{_mapping(item, "termo de vocabulário")["termo"]} = '
        f'{_mapping(item, "termo de vocabulário")["definicao"]}'
        for item in values
    )


def _render_scientific(
    content: Mapping[str, Any],
    discipline: Mapping[str, Any],
    series: Mapping[str, Any],
    template: str,
) -> str:
    allow_christian = bool(discipline.get("permitir_cristao", False))
    quote = str(content.get("citacao_fechamento", "")).strip()
    quote_author = str(content.get("citacao_fechamento_autor", "")).strip()
    if allow_christian and quote:
        footer_quote = (
            "\n   Below the summary footer, a thin separator and a small "
            "italic dark-teal CLOSING QUOTE in 1-2 lines, with a tiny mustard "
            f'cross pictogram beside the attribution: "{quote}" — {quote_author}'
        )
    else:
        footer_quote = ""
    credit = str(content.get("credito_curto", "")).strip()
    if credit:
        credit_block = (
            "   - Directly below: small COLORED CATEGORY TAG (rounded pill) "
            "in the chapter accent color, containing the discipline-rubric "
            f'text in white all-caps tracked-out sans-serif: "{credit}".'
        )
    else:
        credit_block = (
            "   - (NO CREDIT PILL — `credito_curto` is empty. Render NOTHING "
            "in this slot. Do NOT invent a substitute.)"
        )
    values = {
        "tema_principal": content["tema_principal"],
        "credito_curto": content.get("credito_curto", ""),
        "disciplina_legivel": discipline["disciplina_legivel"],
        "tom_disciplina": discipline["tom_disciplina"],
        "cor_destaque": discipline["cor_destaque"],
        "cor_secundaria_escura": discipline["cor_secundaria_escura"],
        "atmosfera_capitulo": content.get(
            "atmosfera_capitulo", "(no specific atmosphere provided)"
        ),
        "paleta_acessoria_capitulo": content.get(
            "paleta_acessoria_capitulo", "(use discipline canonical palette)"
        ),
        "iconografia_capitulo": content.get(
            "iconografia_capitulo", "(use discipline-default iconography)"
        ),
        "titulo_linha1": content.get("titulo_linha1", ""),
        "titulo_linha2": content.get("titulo_linha2", ""),
        "titulo_linha3": content.get("titulo_linha3", ""),
        "titulo_cor_protagonista": content.get(
            "titulo_cor_protagonista", discipline["cor_destaque"]
        ),
        "titulo_cor_letras_cream": content.get(
            "titulo_cor_letras_cream", "rich black #1A1A1A"
        ),
        "subtitulo_hook": content["subtitulo_hook"],
        "conceito_central_tipo": content["conceito_central_tipo"],
        "conceito_central_descricao": content["conceito_central_descricao"],
        "conceito_central_tratamento": content.get(
            "conceito_central_tratamento",
            discipline["hero_tratamento_default"],
        ),
        "conceito_central_estilo": content.get(
            "conceito_central_estilo",
            discipline["hero_estilo_renderizacao"],
        ),
        "cards_lista_detalhada": _scientific_cards(content["cards"]),
        "fluxos_conexoes": _scientific_flows(content.get("fluxos", [])),
        "resumo_visual_etapas": _scientific_summary(content["resumo_visual"]),
        "vocabulario_chave": _scientific_vocabulary(content["vocab_chave"]),
        "rodape_bible_block": footer_quote,
        "credit_pill_block": credit_block,
        "faixa_etaria": series["faixa_etaria"],
        "densidade_pedagogica": (
            f"{series['densidade_pedagogica']} | "
            f"TONE: {series['ajustes_tom']} | "
            f"PALETTE: {series['ajustes_paleta']}"
        ),
    }
    return _replace_placeholders(template, values)


def _colagem_lines(items: Any, label: str, indent: str = "") -> str:
    values = _list(items, label)
    if not values:
        raise ConfigError(f"{label} não pode ficar vazio.")
    return "\n".join(f'{indent}"{item}"' for item in values)


def _colagem_paineis(items: Any) -> str:
    values = _list(items, "paineis")
    if len(values) != 4:
        raise ConfigError(f"paineis exige exatamente 4 itens; recebeu {len(values)}.")
    posicoes = [
        "painel superior esquerdo",
        "painel superior direito",
        "painel inferior esquerdo",
        "painel inferior direito",
    ]
    return "\n".join(
        f"   - {pos}: {item}" for pos, item in zip(posicoes, values)
    )


def _colagem_cartelas(items: Any) -> str:
    values = _list(items, "cartelas")
    if len(values) != 3:
        raise ConfigError(f"cartelas exige exatamente 3 itens; recebeu {len(values)}.")
    cores = ["teal, com texto creme", "magenta, com texto creme", "mostarda, com texto preto"]
    blocos = []
    for index, (item, cor) in enumerate(zip(values, cores), start=1):
        card = _mapping(item, f"cartelas[{index}]")
        titulo = _colagem_lines(card["titulo"], f"cartelas[{index}].titulo")
        corpo = _colagem_lines(card["corpo"], f"cartelas[{index}].corpo")
        blocos.append(f"Cartela chapada em {cor}:\n{titulo}\n{corpo}")
    return "\n\n".join(blocos)


def _colagem_secoes_visual(items: Any) -> str:
    values = _list(items, "secoes")
    if len(values) != 4:
        raise ConfigError(f"secoes exige exatamente 4 itens; recebeu {len(values)}.")
    blocos = []
    for index, item in enumerate(values, start=1):
        sec = _mapping(item, f"secoes[{index}]")
        ancora = sec.get("ancoragem", "")
        extra = f"\n     ANCORAGEM: {ancora}" if ancora else ""
        blocos.append(
            f"   SEÇÃO {index} — ilustração: {sec['ilustracao']}{extra}"
        )
    return "\n\n".join(blocos)


def _colagem_secoes_texto(items: Any) -> str:
    values = _list(items, "secoes")
    blocos = []
    for index, item in enumerate(values, start=1):
        sec = _mapping(item, f"secoes[{index}]")
        itens = _colagem_lines(sec["itens"], f"secoes[{index}].itens")
        rotulos = _colagem_lines(sec["rotulos"], f"secoes[{index}].rotulos")
        blocos.append(
            f"SEÇÃO {index} — plaquinha com o número {index}, título e itens:\n"
            f'"{sec["titulo"]}"\n{itens}\n\n'
            f"Rótulos sobre a ilustração da seção {index}, e nenhum outro:\n{rotulos}"
        )
    return "\n\n".join(blocos)


def _colagem_bullets(items: Any, label: str) -> str:
    values = _list(items, label)
    if not values:
        raise ConfigError(f"{label} não pode ficar vazio.")
    return "\n".join(f"- {item}" for item in values)


def _render_colagem(
    content: Mapping[str, Any],
    discipline: Mapping[str, Any],
    series: Mapping[str, Any],
    template: str,
    pagina: str,
) -> str:
    values = {
        "disciplina_legivel": discipline["disciplina_legivel"],
        "tom_disciplina": discipline["tom_disciplina"],
        "paleta": discipline["paleta"],
        "cor_titulo": discipline["cor_titulo"],
        "faixa_etaria": series["faixa_etaria"],
        "registro_escrita": series["registro_escrita"],
        "titulo_linha1": content["titulo_linha1"],
        "titulo_linha2": content["titulo_linha2"],
        "rodape_cadeia": content["rodape_cadeia"],
        "atencao_ortografica": _colagem_bullets(
            content["atencao_ortografica"], "atencao_ortografica"
        ),
        "restricoes_visuais": _colagem_bullets(
            content["restricoes_visuais"], "restricoes_visuais"
        ),
    }
    if pagina == "capa":
        values.update(
            {
                "linha_temas": content["linha_temas"],
                "pergunta_bilhete": content["pergunta_bilhete"],
                "paineis_colagem": _colagem_paineis(content["paineis"]),
                "cartela_central": _colagem_lines(
                    content["cartela_central"], "cartela_central"
                ),
                "cartelas_lista": _colagem_cartelas(content["cartelas"]),
            }
        )
    else:
        values.update(
            {
                "titulo_pagina": content["titulo_pagina"],
                "secoes_lista": _colagem_secoes_visual(content["secoes"]),
                "secoes_texto": _colagem_secoes_texto(content["secoes"]),
                "vocabulario_lista": _colagem_lines(
                    content["vocabulario"], "vocabulario"
                ),
            }
        )
    return _replace_placeholders(template, values)


def render_prompt(
    root: Path,
    path: Path,
    renderer: str = "texto",
    prompt_text: str | None = None,
    resource_texts: Mapping[str, Mapping[str, str]] | None = None,
) -> str:
    if renderer not in RENDERERS:
        raise ConfigError(
            f"Renderizador desconhecido: {renderer}. "
            f"Opções: {', '.join(sorted(RENDERERS))}."
        )
    parsed = _frontmatter(path, prompt_text)
    if renderer == "texto" or parsed is None:
        return prompt_text if prompt_text is not None else load_prompt(path)
    content, _notes = parsed
    selected_renderer = renderer
    if content.get("formato") == "colagem-editorial":
        selected_renderer = "colagem-editorial"
    elif (
        renderer == "infografico-cientifico"
        and "conceito_central_tipo" not in content
        and "hero_descricao" in content
    ):
        selected_renderer = "infografico-editorial"
    format_root = root / "formatos" / selected_renderer
    selected_resources: Mapping[str, str] | None = None
    if resource_texts is not None:
        try:
            selected_resources = resource_texts[selected_renderer]
        except KeyError as exc:
            raise ConfigError(
                f"Snapshot ausente para o renderizador {selected_renderer}."
            ) from exc
    required_resource_names = {
        "adaptacoes-disciplina.yaml",
        "adaptacoes-serie.yaml",
        (
            COLAGEM_MASTERS.get(str(content.get("pagina", "")).strip(), "")
            if selected_renderer == "colagem-editorial"
            else "MASTER-PROMPT.md"
        ),
    }
    if selected_resources is not None:
        missing_resources = sorted(
            name
            for name in required_resource_names
            if name and name not in selected_resources
        )
        if missing_resources:
            raise ConfigError(
                "Snapshot de recursos incompleto: " + ", ".join(missing_resources)
            )
    discipline_key = str(content.get("disciplina", ""))
    series_key = str(content.get("serie", ""))
    disciplines = _load_yaml(
        format_root / "adaptacoes-disciplina.yaml",
        None
        if selected_resources is None
        else selected_resources["adaptacoes-disciplina.yaml"],
    )
    series_all = _load_yaml(
        format_root / "adaptacoes-serie.yaml",
        None
        if selected_resources is None
        else selected_resources["adaptacoes-serie.yaml"],
    )
    if discipline_key not in disciplines:
        raise ConfigError(
            f"Disciplina '{discipline_key}' não existe em {selected_renderer}."
        )
    if series_key not in series_all:
        raise ConfigError(
            f"Série '{series_key}' não existe em {selected_renderer}."
        )
    if selected_renderer == "colagem-editorial":
        pagina = str(content.get("pagina", "")).strip()
        if pagina not in COLAGEM_MASTERS:
            raise ConfigError(
                "colagem-editorial exige pagina=capa ou pagina=conteudo; "
                f"recebeu '{pagina}'."
            )
        master_name = COLAGEM_MASTERS[pagina]
        template = _master_template(
            format_root / master_name,
            None if selected_resources is None else selected_resources[master_name],
        )
        return _render_colagem(
            content,
            _mapping(disciplines[discipline_key], discipline_key),
            _mapping(series_all[series_key], series_key),
            template,
            pagina,
        )
    template = _master_template(
        format_root / "MASTER-PROMPT.md",
        None if selected_resources is None else selected_resources["MASTER-PROMPT.md"],
    )
    if selected_renderer == "infografico-editorial":
        return _render_editorial(
            content,
            _mapping(disciplines[discipline_key], discipline_key),
            _mapping(series_all[series_key], series_key),
            template,
        )
    discipline = _mapping(disciplines[discipline_key], discipline_key)
    series = _mapping(series_all[series_key], series_key)
    return _render_scientific(content, discipline, series, template)
