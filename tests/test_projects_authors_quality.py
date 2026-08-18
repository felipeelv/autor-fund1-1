from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from gerador_imagens.authors import aplicar_autor, load_author
from gerador_imagens.projects import load_project
from gerador_imagens.quality import (
    analyze_prompt,
    compare_ocr_text,
    extract_expected_text,
)
from gerador_imagens.storage import StorageSettings


class ProjectAuthorQualityTests(unittest.TestCase):
    def test_author_is_applied(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            folder = root / "autores" / "ciencias"
            folder.mkdir(parents=True)
            (folder / "autor.yaml").write_text(
                """
autor:
  id: ciencias
  nome: Autor de Ciências
  disciplina: Ciências
  prompt_prefixo: "PREFIXO"
  prompt_sufixo: "SUFIXO"
""",
                encoding="utf-8",
            )
            author = load_author(root, "ciencias")
            prompt, applied = aplicar_autor(root, "ciencias", "CONTEÚDO")
            self.assertEqual(author.name, "Autor de Ciências")
            self.assertIsNotNone(applied)
            self.assertEqual(prompt, "PREFIXO\n\nCONTEÚDO\n\nSUFIXO")

    def test_project_yaml_is_loaded(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root = base / "project"
            root.mkdir()
            (root / "prompts").mkdir()
            (root / "modelos").mkdir()
            (root / "prompts" / "page.md").write_text("Prompt", encoding="utf-8")
            project = root / "modelos" / "project.yaml"
            project.write_text(
                """
projeto:
  titulo: Teste
modelo:
  provider: openai
  id: gpt-image-2
parametros_api:
  tamanho: 1024x1024
imagens:
  - prompt: prompts/page.md
    saida: page.png
""",
                encoding="utf-8",
            )
            output_root = base / "outputs"
            output_root.mkdir()
            storage = StorageSettings(
                output_root,
                {
                    "revisao": "_revisao",
                    "aprovadas": "aprovadas",
                    "historico": "historico-importado",
                },
            )
            plan = load_project(root, project, storage)
            self.assertEqual(plan.title, "Teste")
            self.assertEqual(plan.tasks[0].provider, "openai")
            self.assertEqual(plan.tasks[0].options.size, "1024x1024")
            self.assertEqual(
                plan.tasks[0].output_path,
                (output_root / "_revisao" / "page.png").resolve(),
            )

    def test_xai_project_requires_explicit_image_parameters(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root = base / "project"
            root.mkdir()
            (root / "prompts").mkdir()
            (root / "modelos").mkdir()
            (root / "prompts" / "page.md").write_text(
                "Prompt",
                encoding="utf-8",
            )
            project = root / "modelos" / "project.yaml"
            project.write_text(
                """
projeto:
  titulo: Teste xAI
modelo:
  provider: xai
  id: grok-imagine-image-2.0
parametros_api:
  tamanho: auto
  qualidade: medium
  formato: jpeg
  proporcao: "2:3"
  resolucao: 2k
imagens:
  - prompt: prompts/page.md
    saida: page.jpg
""",
                encoding="utf-8",
            )
            output_root = base / "outputs"
            output_root.mkdir()
            storage = StorageSettings(
                output_root,
                {
                    "revisao": "_revisao",
                    "aprovadas": "aprovadas",
                    "historico": "historico-importado",
                },
            )
            plan = load_project(root, project, storage)
        task = plan.tasks[0]
        self.assertEqual(task.provider, "xai")
        self.assertEqual(task.options.aspect_ratio, "2:3")
        self.assertEqual(task.options.resolution, "2k")

    def test_prompt_analysis_and_ocr_comparison(self) -> None:
        findings = analyze_prompt(
            "Pesquisas mostram que 9 em cada 10 estudantes fazem algo."
        )
        codes = {finding.code for finding in findings}
        self.assertIn("statistic-ratio", codes)
        self.assertIn("unsourced-research", codes)
        expected = extract_expected_text(
            "Instruções\n\nTEXT TO RENDER VERBATIM\nTítulo correto\nFrase final"
        )
        comparison = compare_ocr_text("Título correto", expected)
        self.assertEqual(comparison["expected_count"], 2)
        self.assertEqual(comparison["missing"], ["Frase final"])
