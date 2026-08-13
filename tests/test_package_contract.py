from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import yaml

from gerador_imagens.projects import load_project
from gerador_imagens.storage import StorageSettings


ROOT = Path(__file__).resolve().parents[1]
AUTHOR_ID = "autor-teste-fund1"


class IndependentPackageContractTests(unittest.TestCase):
    def test_package_contains_only_the_expected_author(self) -> None:
        authors = sorted(
            path.parent.name
            for path in (ROOT / "autores").glob("*/autor.yaml")
        )
        self.assertEqual(authors, [AUTHOR_ID])

    def test_author_and_format_are_bidirectionally_authorized(self) -> None:
        author = yaml.safe_load(
            (ROOT / "autores" / AUTHOR_ID / "autor.yaml").read_text(
                encoding="utf-8"
            )
        )["autor"]
        format_profile = yaml.safe_load(
            (ROOT / "formatos/apostila-fund1/formato.yaml").read_text(
                encoding="utf-8"
            )
        )["formato"]
        self.assertEqual(author["id"], AUTHOR_ID)
        self.assertEqual(author["formatos"], ["apostila-fund1"])
        self.assertEqual(format_profile["autores"], [AUTHOR_ID])

    def test_all_projects_resolve_without_api_calls(self) -> None:
        project_paths = sorted(
            (ROOT / "autores" / AUTHOR_ID / "projetos").rglob("*.yaml")
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
                    self.assertTrue(
                        all(task.options.model == "gpt-image-2" for task in plan.tasks)
                    )

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
