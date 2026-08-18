"""Gate de aprovação do prompt.

Rascunho não gera imagem. Nenhum teste aqui chama a API.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from gerador_imagens.core import GenerationError, load_prompt
from gerador_imagens.sources import (
    approve_draft,
    prompt_state,
    split_front_matter,
)

CORPO = "Use case: scientific-educational\n\n## PEDIDO\n\nUma página.\n"


class SplitFrontMatterTests(unittest.TestCase):
    def test_sem_front_matter_devolve_texto_intacto(self) -> None:
        meta, body = split_front_matter(CORPO)
        self.assertEqual(meta, {})
        self.assertEqual(body, CORPO)

    def test_separa_front_matter_do_corpo(self) -> None:
        meta, body = split_front_matter(
            f"---\nestado: aprovado\nrevisor: Felipe Rosa\n---\n{CORPO}"
        )
        self.assertEqual(meta["estado"], "aprovado")
        self.assertEqual(meta["revisor"], "Felipe Rosa")
        self.assertEqual(body, CORPO)

    def test_front_matter_invalido_e_erro_claro(self) -> None:
        with self.assertRaises(ValueError):
            split_front_matter("---\nestado: [\n---\ncorpo\n")


class PromptStateTests(unittest.TestCase):
    def test_legado_sem_marcacao_conta_como_aprovado(self) -> None:
        self.assertEqual(prompt_state(Path("p01-tema-v1.md"), {}), "aprovado")

    def test_sufixo_rascunho_no_nome_marca_rascunho(self) -> None:
        self.assertEqual(prompt_state(Path("p01-tema-rascunho.md"), {}), "rascunho")

    def test_front_matter_marca_rascunho(self) -> None:
        self.assertEqual(
            prompt_state(Path("p01-tema-v1.md"), {"estado": "rascunho"}), "rascunho"
        )

    def test_front_matter_nao_promove_arquivo_de_rascunho(self) -> None:
        self.assertEqual(
            prompt_state(Path("p01-tema-rascunho.md"), {"estado": "aprovado"}),
            "rascunho",
        )


class LoadPromptGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _write(self, name: str, text: str) -> Path:
        path = self.dir / name
        path.write_text(text, encoding="utf-8")
        return path

    def test_prompt_aprovado_carrega_normalmente(self) -> None:
        path = self._write("p01-tema-v1.md", CORPO)
        self.assertIn("## PEDIDO", load_prompt(path))

    def test_recusa_arquivo_de_rascunho(self) -> None:
        path = self._write("p01-tema-rascunho.md", CORPO)
        with self.assertRaises(GenerationError) as erro:
            load_prompt(path)
        self.assertIn("rascunho", str(erro.exception).lower())

    def test_recusa_estado_rascunho_no_front_matter(self) -> None:
        path = self._write("p01-tema-v1.md", f"---\nestado: rascunho\n---\n{CORPO}")
        with self.assertRaises(GenerationError):
            load_prompt(path)

    def test_front_matter_nao_vai_para_a_api(self) -> None:
        path = self._write(
            "p01-tema-v1.md", f"---\nestado: aprovado\nrevisor: Felipe\n---\n{CORPO}"
        )
        prompt = load_prompt(path)
        self.assertNotIn("estado:", prompt)
        self.assertNotIn("revisor:", prompt)
        self.assertTrue(prompt.startswith("Use case:"))

    def test_recusa_prompt_com_decisao_editorial_pendente(self) -> None:
        path = self._write("p01-tema-v1.md", CORPO + "\n<<DECISÃO EDITORIAL: definir>>\n")
        with self.assertRaises(GenerationError) as erro:
            load_prompt(path)
        self.assertIn("decisão editorial", str(erro.exception).lower())


class ApproveDraftTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_recusa_aprovar_com_decisao_pendente(self) -> None:
        draft = self.dir / "unidade-p01-tema-rascunho.md"
        draft.write_text(CORPO + "\n<<DECISÃO EDITORIAL: definir>>\n", encoding="utf-8")
        with self.assertRaises(ValueError) as erro:
            approve_draft(draft, reviewer="Felipe Rosa", approved_at="2026-08-18")
        self.assertIn("decisão editorial", str(erro.exception).lower())

    def test_aprova_gerando_v1_com_front_matter(self) -> None:
        draft = self.dir / "unidade-p01-tema-rascunho.md"
        draft.write_text(
            "> **RASCUNHO gerado por `preparar.py`.** Não é prompt aprovado.\n\n" + CORPO,
            encoding="utf-8",
        )
        destino = approve_draft(draft, reviewer="Felipe Rosa", approved_at="2026-08-18")
        self.assertEqual(destino.name, "unidade-p01-tema-v1.md")
        texto = destino.read_text(encoding="utf-8")
        self.assertTrue(texto.startswith("---\n"))
        self.assertIn("estado: aprovado", texto)
        self.assertIn("revisor: Felipe Rosa", texto)
        self.assertNotIn("RASCUNHO gerado", texto)
        self.assertTrue(draft.exists(), "o rascunho é preservado")

    def test_nao_sobrescreve_versao_existente(self) -> None:
        draft = self.dir / "unidade-p01-tema-rascunho.md"
        draft.write_text(CORPO, encoding="utf-8")
        approve_draft(draft, reviewer="Felipe", approved_at="2026-08-18")
        with self.assertRaises(ValueError):
            approve_draft(draft, reviewer="Felipe", approved_at="2026-08-18")


if __name__ == "__main__":
    unittest.main()
