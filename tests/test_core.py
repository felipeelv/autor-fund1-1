from __future__ import annotations

import base64
import tempfile
import unittest
from io import BytesIO
from pathlib import Path
from types import SimpleNamespace

from PIL import Image

from gerador_imagens.config import GenerationOptions
from gerador_imagens.core import (
    GenerationError,
    create_pdf,
    generate_image,
    save_image,
)


def png_base64(size: tuple[int, int] = (1024, 1024)) -> str:
    buffer = BytesIO()
    Image.new("RGB", size, "white").save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("ascii")


class FakeImages:
    def __init__(self, response: object) -> None:
        self.response = response
        self.kwargs: dict[str, object] | None = None

    def generate(self, **kwargs: object) -> object:
        self.kwargs = kwargs
        return self.response


class CoreTests(unittest.TestCase):
    def test_valid_image_is_saved(self) -> None:
        options = GenerationOptions(size="1024x1024")
        data = base64.b64decode(png_base64())
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "image.png"
            info = save_image(output, data, options, overwrite=False)
            self.assertTrue(output.exists())
            self.assertEqual((info["width"], info["height"]), (1024, 1024))

    def test_invalid_bytes_are_not_saved(self) -> None:
        options = GenerationOptions(size="1024x1024")
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "image.png"
            with self.assertRaises(GenerationError):
                save_image(output, b"not-an-image", options, overwrite=False)
            self.assertFalse(output.exists())

    def test_generation_writes_image_and_metadata(self) -> None:
        response = SimpleNamespace(
            data=[SimpleNamespace(b64_json=png_base64())],
            usage=SimpleNamespace(
                model_dump=lambda mode="json": {"total_tokens": 10}
            ),
            _request_id="req_test",
        )
        client = SimpleNamespace(images=FakeImages(response))
        options = GenerationOptions(size="1024x1024")
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "image.png"
            result = generate_image(
                client=client,
                prompt="Uma imagem branca para teste.",
                output=output,
                options=options,
            )
            self.assertEqual(result.output_paths, [output])
            self.assertTrue(output.exists())
            self.assertTrue((Path(directory) / "image.metadata.json").exists())
            self.assertEqual(result.request_id, "req_test")

    def test_existing_output_is_protected_before_api_call(self) -> None:
        response = SimpleNamespace(data=[])
        images = FakeImages(response)
        client = SimpleNamespace(images=images)
        options = GenerationOptions(size="1024x1024")
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "image.png"
            output.write_bytes(b"existing")
            with self.assertRaises(GenerationError):
                generate_image(
                    client=client,
                    prompt="Teste",
                    output=output,
                    options=options,
                )
            self.assertIsNone(images.kwargs)

    def test_streaming_saves_partial_and_final(self) -> None:
        events = [
            SimpleNamespace(
                type="image_generation.partial_image",
                partial_image_index=0,
                b64_json=png_base64(),
            ),
            SimpleNamespace(
                type="image_generation.completed",
                b64_json=png_base64(),
                usage=None,
                request_id="req_stream",
            ),
        ]
        client = SimpleNamespace(images=FakeImages(events))
        options = GenerationOptions(
            size="1024x1024",
            stream=True,
            partial_images=1,
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "image.png"
            result = generate_image(
                client=client,
                prompt="Teste de streaming.",
                output=output,
                options=options,
            )
            self.assertTrue(output.exists())
            self.assertEqual(len(result.partial_paths), 1)
            self.assertTrue(result.partial_paths[0].exists())
            self.assertEqual(result.request_id, "req_stream")

    def test_pdf_is_created(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pages: list[Path] = []
            for index in range(2):
                path = root / f"page-{index}.png"
                Image.new("RGB", (64, 96), "white").save(path, format="PNG")
                pages.append(path)
            pdf = root / "book.pdf"
            create_pdf(pages, pdf, overwrite=False, dpi=72)
            self.assertTrue(pdf.exists())
            self.assertGreater(pdf.stat().st_size, 0)
