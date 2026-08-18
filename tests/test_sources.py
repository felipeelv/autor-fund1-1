"""Testes do leitor de fonte bruta e do rascunho de prompt.

Nenhum teste aqui chama a API nem consome crédito.
"""

from __future__ import annotations

import unittest

from gerador_imagens.sources import (
    Section,
    build_prompt_draft,
    clean_export_escapes,
    parse_source,
    section_literals,
)

FONTE = """# **MATEMÁTICA \\- 2º ANO**

## 3º Bimestre: Multiplicação

# **UNIDADE 5**

# **Capítulo 1**

## Grupos Iguais

### **O que são grupos iguais**

Quando juntamos quantidades iguais, temos grupos iguais\\!

*\\[Ilustração: Três cestas com 4 maçãs cada\\]*

| Sólido | Objeto |
| :---- | :---- |
| Cubo | Dado, gelo |

- Somar parcelas iguais é multiplicar
- O sinal de vezes é ×

### **O sinal de vezes**

O sinal × significa "vezes".
"""


class CleanEscapesTests(unittest.TestCase):
    def test_remove_escapes_do_google_docs(self) -> None:
        self.assertEqual(clean_export_escapes(r"MATEMÁTICA \- 2º ANO"), "MATEMÁTICA - 2º ANO")
        self.assertEqual(clean_export_escapes(r"iguais\!"), "iguais!")
        self.assertEqual(clean_export_escapes(r"14 \= 4 × 3 \+ 2"), "14 = 4 × 3 + 2")

    def test_preserva_barra_que_nao_e_escape(self) -> None:
        self.assertEqual(clean_export_escapes(r"caminho\\arquivo"), r"caminho\\arquivo")


class ParseSourceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sections = parse_source(FONTE)

    def test_ignora_cabecalho_vazio(self) -> None:
        self.assertTrue(all(section.title for section in self.sections))

    def test_remove_negrito_e_escape_do_titulo(self) -> None:
        titles = [section.title for section in self.sections]
        self.assertIn("MATEMÁTICA - 2º ANO", titles)
        self.assertIn("Capítulo 1", titles)

    def test_registra_nivel_e_indice_estavel(self) -> None:
        by_title = {section.title: section for section in self.sections}
        self.assertEqual(by_title["MATEMÁTICA - 2º ANO"].level, 1)
        self.assertEqual(by_title["3º Bimestre: Multiplicação"].level, 2)
        self.assertEqual(by_title["O que são grupos iguais"].level, 3)
        indices = [section.index for section in self.sections]
        self.assertEqual(indices, list(range(1, len(self.sections) + 1)))

    def test_corpo_vai_ate_o_proximo_cabecalho(self) -> None:
        by_title = {section.title: section for section in self.sections}
        corpo = by_title["O que são grupos iguais"].body
        self.assertIn("grupos iguais!", corpo)
        self.assertNotIn('O sinal × significa "vezes".', corpo)

    def test_conta_ilustracoes_e_tabelas(self) -> None:
        by_title = {section.title: section for section in self.sections}
        section = by_title["O que são grupos iguais"]
        self.assertEqual(section.illustrations, 1)
        self.assertTrue(section.has_table)


class SectionLiteralsTests(unittest.TestCase):
    def setUp(self) -> None:
        by_title = {section.title: section for section in parse_source(FONTE)}
        self.literals = section_literals(by_title["O que são grupos iguais"])

    def test_extrai_itens_de_lista_e_celulas_de_tabela(self) -> None:
        self.assertIn("Somar parcelas iguais é multiplicar", self.literals)
        self.assertIn("Cubo", self.literals)
        self.assertIn("Dado, gelo", self.literals)

    def test_descarta_marcacao_de_ilustracao(self) -> None:
        for literal in self.literals:
            self.assertNotIn("Ilustração", literal)

    def test_descarta_separador_de_tabela(self) -> None:
        self.assertNotIn(":----", " ".join(self.literals))

    def test_nao_repete_literal(self) -> None:
        self.assertEqual(len(self.literals), len(set(self.literals)))


class BuildPromptDraftTests(unittest.TestCase):
    def setUp(self) -> None:
        sections = parse_source(FONTE)
        self.draft = build_prompt_draft(
            author="matematica",
            discipline="Matemática",
            school_year="2ano",
            year_label="2º ano",
            unit="Unidade 5",
            page_number=1,
            page_title="GRUPOS IGUAIS",
            sections=[sections[5]],
            source_path="autores/matematica/anos/2ano/fontes/2026-2-semestre/x.md",
            visual_system="Fundo branco puro. Colagem tátil.",
            locks="Não inventar número.",
        )

    def test_mantem_as_cinco_secoes_canonicas(self) -> None:
        for header in (
            "## PEDIDO",
            "## SISTEMA VISUAL",
            "## COMPOSIÇÃO E TÍTULO",
            "## TEXTOS EXATOS",
            "## TRAVAS",
        ):
            self.assertIn(header, self.draft)

    def test_cabecalho_declara_use_case_e_asset_type(self) -> None:
        self.assertTrue(self.draft.startswith("Use case: scientific-educational"))
        self.assertIn("Asset type: página 1", self.draft)
        self.assertIn("Matemática do 2º ano", self.draft)

    def test_transporta_literais_da_fonte(self) -> None:
        self.assertIn("Somar parcelas iguais é multiplicar", self.draft)

    def test_marca_o_que_exige_decisao_editorial(self) -> None:
        self.assertIn("DECISÃO EDITORIAL", self.draft)
        self.assertEqual(self.draft.count("<<DECISÃO EDITORIAL"), 2)

    def test_declara_rascunho_e_rastreia_a_fonte(self) -> None:
        self.assertIn("RASCUNHO", self.draft)
        self.assertIn("autores/matematica/anos/2ano/fontes/2026-2-semestre/x.md", self.draft)

    def test_injeta_sistema_visual_e_travas_do_autor(self) -> None:
        self.assertIn("Fundo branco puro. Colagem tátil.", self.draft)
        self.assertIn("Não inventar número.", self.draft)


class SectionDataclassTests(unittest.TestCase):
    def test_section_expoe_intervalo_de_linhas(self) -> None:
        section = Section(
            index=1, level=2, title="T", body="x", start_line=10, end_line=20
        )
        self.assertEqual(section.line_range, "10-20")


if __name__ == "__main__":
    unittest.main()
