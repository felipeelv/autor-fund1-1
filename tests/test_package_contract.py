from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import yaml

from gerador_imagens.authors import listar_autores
from gerador_imagens.projects import load_project
from gerador_imagens.storage import StorageSettings


ROOT = Path(__file__).resolve().parents[1]
AUTHOR_IDS = ("ingles", "matematica", "natureza-e-sociedade")


class PackageContractTests(unittest.TestCase):
    def test_package_contains_the_expected_authors(self) -> None:
        authors = sorted(
            path.parent.name
            for path in (ROOT / "autores").glob("*/autor.yaml")
            if not path.parent.name.startswith("_")
        )
        self.assertEqual(authors, sorted(AUTHOR_IDS))

    def test_template_author_is_never_loadable(self) -> None:
        template = ROOT / "autores" / "_modelo" / "autor.yaml"
        self.assertTrue(template.is_file())
        profile = yaml.safe_load(template.read_text(encoding="utf-8"))["autor"]
        self.assertFalse(profile["ativo"])
        self.assertNotIn("_modelo", [author.id for author in listar_autores(ROOT)])

    def test_authors_and_format_are_bidirectionally_authorized(self) -> None:
        format_profile = yaml.safe_load(
            (ROOT / "formatos/apostila-fund1/formato.yaml").read_text(
                encoding="utf-8"
            )
        )["formato"]
        self.assertEqual(format_profile["autores"], list(AUTHOR_IDS))
        for author_id in AUTHOR_IDS:
            with self.subTest(author=author_id):
                author = yaml.safe_load(
                    (ROOT / "autores" / author_id / "autor.yaml").read_text(
                        encoding="utf-8"
                    )
                )["autor"]
                self.assertEqual(author["id"], author_id)
                self.assertEqual(author["formatos"], ["apostila-fund1"])

    def test_all_projects_resolve_without_api_calls(self) -> None:
        project_paths = sorted(
            path
            for author_id in AUTHOR_IDS
            for path in (ROOT / "autores" / author_id / "projetos").rglob("*.yaml")
        )
        self.assertTrue(project_paths)
        with tempfile.TemporaryDirectory() as directory:
            storage = StorageSettings(
                Path(directory).resolve(),
                {
                    "revisao": "_revisao",
                    "aprovadas": "aprovadas",
                    "historico": "historico-importado",
                },
            )
            for project_path in project_paths:
                with self.subTest(project=project_path.name):
                    plan = load_project(ROOT, project_path, storage)
                    self.assertTrue(plan.tasks)
                    self.assertTrue(all(task.prompt_path.is_file() for task in plan.tasks))
                    for task in plan.tasks:
                        if task.provider == "openai":
                            self.assertEqual(task.options.model, "gpt-image-2")
                        elif task.provider == "xai":
                            self.assertEqual(
                                task.options.model,
                                "grok-imagine-image-2.0",
                            )
                        else:
                            self.fail(f"Provider inesperado: {task.provider}")

    def test_initial_math_project_has_six_unique_pages(self) -> None:
        project_path = (
            ROOT
            / "autores"
            / "matematica"
            / "projetos"
            / "2026"
            / "3-bimestre"
            / "unidades-05-06-6paginas-v1.yaml"
        )
        source_path = (
            ROOT
            / "autores"
            / "matematica"
            / "anos"
            / "3ano"
            / "fontes"
            / "2026-2-semestre"
            / "3bim-divisao-resto-geometria-v1.md"
        )
        self.assertTrue(source_path.is_file())
        with tempfile.TemporaryDirectory() as directory:
            storage = StorageSettings(
                Path(directory).resolve(),
                {
                    "revisao": "_revisao",
                    "aprovadas": "aprovadas",
                    "historico": "historico-importado",
                },
            )
            plan = load_project(ROOT, project_path, storage)
        self.assertEqual(len(plan.tasks), 6)
        self.assertEqual(len({task.prompt_path for task in plan.tasks}), 6)
        self.assertEqual(len({task.output_path for task in plan.tasks}), 6)

    def test_repository_contains_no_production_binaries(self) -> None:
        prohibited = {
            ".avif",
            ".gif",
            ".jpeg",
            ".jpg",
            ".pdf",
            ".png",
            ".tif",
            ".tiff",
            ".webp",
        }
        binaries = sorted(
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("*")
            if path.is_file()
            and ".venv" not in path.relative_to(ROOT).parts
            and path.suffix.lower() in prohibited
        )
        self.assertEqual(binaries, [])


if __name__ == "__main__":
    unittest.main()
