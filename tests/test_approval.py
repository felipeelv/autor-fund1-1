from __future__ import annotations

import tempfile
import unittest
from argparse import Namespace
from pathlib import Path
from unittest.mock import patch

from PIL import Image

import aprovar


class ApprovalTests(unittest.TestCase):
    def test_external_review_image_is_promoted_with_record(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            project_root = base / "project"
            project_root.mkdir()
            output_root = base / "output"
            output_root.mkdir()
            source = output_root / "_revisao" / "ciencias" / "teste.png"
            source.parent.mkdir(parents=True)
            Image.new("RGB", (64, 96), "white").save(source, format="PNG")
            with patch.object(aprovar, "ROOT", project_root):
                exit_code = aprovar.run(
                    Namespace(
                        imagens=["ciencias/teste.png"],
                        saida_root=str(output_root),
                        revisor="Teste automatizado",
                        forcar=False,
                    )
                )
            destination = output_root / "aprovadas" / "ciencias" / "teste.png"
            record = (
                project_root
                / "registros"
                / "aprovacoes"
                / "ciencias"
                / "teste.approval.json"
            )
            self.assertEqual(exit_code, 0)
            self.assertTrue(destination.exists())
            self.assertTrue(record.exists())
            self.assertFalse(
                destination.with_name("teste.approval.json").exists()
            )
            self.assertEqual(
                sorted(path.name for path in destination.parent.iterdir()),
                ["teste.png"],
            )
