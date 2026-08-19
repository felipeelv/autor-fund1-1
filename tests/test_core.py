from __future__ import annotations

import base64
import json
import tempfile
import unittest
from io import BytesIO
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import httpx
from PIL import Image

from gerador_imagens.config import GenerationOptions
from gerador_imagens.core import (
    GenerationError,
    build_client,
    check_authentication,
    create_pdf,
    generate_image,
    load_api_key,
    save_image,
)


def png_base64(size: tuple[int, int] = (1024, 1024)) -> str:
    buffer = BytesIO()
    Image.new("RGB", size, "white").save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("ascii")


def jpeg_base64(size: tuple[int, int] = (1365, 2048)) -> str:
    buffer = BytesIO()
    Image.new("RGB", size, "white").save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode("ascii")


class FakeImages:
    def __init__(self, response: object) -> None:
        self.response = response
        self.kwargs: dict[str, object] | None = None

    def generate(self, **kwargs: object) -> object:
        self.kwargs = kwargs
        return self.response


class CoreTests(unittest.TestCase):
    def test_openai_key_is_loaded_from_provider_specific_env(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".env.openai.local").write_text(
                "OPENAI_API_KEY=sk-test-local\n",
                encoding="utf-8",
            )
            with patch.dict("os.environ", {}, clear=True):
                self.assertEqual(load_api_key(root), "sk-test-local")

    def test_missing_openai_key_names_provider_specific_env(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.dict("os.environ", {}, clear=True):
                with self.assertRaisesRegex(
                    GenerationError,
                    r"\.env\.openai\.local",
                ):
                    load_api_key(root)

    def test_xai_key_is_loaded_from_grok_env(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".env.grok.local").write_text(
                "XAI_API_KEY=xai-test-local\n",
                encoding="utf-8",
            )
            with patch.dict("os.environ", {}, clear=True):
                self.assertEqual(load_api_key(root, "xai"), "xai-test-local")

    def test_openrouter_key_is_loaded_from_openrouter_env(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".env.openrouter.local").write_text(
                "OPENROUTER_API_KEY=sk-or-v1-test-local\n",
                encoding="utf-8",
            )
            with patch.dict("os.environ", {}, clear=True):
                self.assertEqual(
                    load_api_key(root, "openrouter"), "sk-or-v1-test-local"
                )

    def test_openrouter_client_is_an_httpx_client_with_bearer_auth(self) -> None:
        options = GenerationOptions(timeout=42.0)
        client = build_client("sk-or-v1-test", options, "openrouter")
        try:
            self.assertIsInstance(client, httpx.Client)
            self.assertEqual(str(client.base_url), "https://openrouter.ai/api/v1/")
            self.assertEqual(
                client.headers.get("authorization"), "Bearer sk-or-v1-test"
            )
        finally:
            client.close()

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

    def test_xai_generation_uses_imagine_contract_and_provider_metadata(self) -> None:
        response = SimpleNamespace(
            data=[SimpleNamespace(b64_json=jpeg_base64())],
            usage=SimpleNamespace(
                model_dump=lambda mode="json": {"cost_in_usd_ticks": 1}
            ),
            _request_id="req_xai_test",
        )
        images = FakeImages(response)
        client = SimpleNamespace(images=images)
        options = GenerationOptions(
            model="grok-imagine-image-2.0",
            size="auto",
            quality="medium",
            output_format="jpeg",
            aspect_ratio="2:3",
            resolution="2k",
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "image.jpg"
            result = generate_image(
                client=client,
                prompt="Página pedagógica de teste.",
                output=output,
                options=options,
                provider="xai",
            )
            metadata = json.loads(
                (Path(directory) / "image.metadata.json").read_text(
                    encoding="utf-8"
                )
            )
        self.assertEqual(result.output_paths, [output])
        self.assertEqual(images.kwargs["response_format"], "b64_json")
        self.assertEqual(
            images.kwargs["extra_body"],
            {"aspect_ratio": "2:3", "resolution": "2k"},
        )
        self.assertNotIn("size", images.kwargs)
        self.assertEqual(metadata["provider"], "xai")
        self.assertEqual(metadata["model"], "grok-imagine-image-2.0")
        self.assertEqual(metadata["image"]["source_format"], "jpeg")
        self.assertFalse(metadata["image"]["transcoded"])

    def test_xai_png_response_is_transcoded_to_requested_jpeg(self) -> None:
        response = SimpleNamespace(
            data=[SimpleNamespace(b64_json=png_base64((1365, 2048)))],
            usage=None,
            _request_id="req_xai_png_test",
        )
        client = SimpleNamespace(images=FakeImages(response))
        options = GenerationOptions(
            model="grok-imagine-image-2.0",
            size="auto",
            quality="medium",
            output_format="jpeg",
            aspect_ratio="2:3",
            resolution="2k",
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "image.jpg"
            generate_image(
                client=client,
                prompt="Página pedagógica de teste.",
                output=output,
                options=options,
                provider="xai",
            )
            with Image.open(output) as generated:
                self.assertEqual(generated.format, "JPEG")
                self.assertEqual(generated.size, (1365, 2048))
                self.assertEqual(generated.mode, "RGB")
            metadata = json.loads(
                (Path(directory) / "image.metadata.json").read_text(
                    encoding="utf-8"
                )
            )
        self.assertEqual(metadata["image"]["source_format"], "png")
        self.assertTrue(metadata["image"]["transcoded"])

    def test_openrouter_generation_uses_images_endpoint_and_provider_metadata(
        self,
    ) -> None:
        captured: dict[str, object] = {}

        def handler(request: httpx.Request) -> httpx.Response:
            captured["method"] = request.method
            captured["path"] = request.url.path
            captured["body"] = json.loads(request.content)
            return httpx.Response(
                200,
                json={
                    "id": "gen_openrouter_test",
                    "data": [{"b64_json": jpeg_base64(), "media_type": "image/jpeg"}],
                    "usage": {"cost": 0.08},
                },
            )

        client = httpx.Client(
            base_url="https://openrouter.ai/api/v1",
            transport=httpx.MockTransport(handler),
        )
        options = GenerationOptions(
            model="x-ai/grok-imagine-image-2.0",
            size="auto",
            quality="medium",
            output_format="jpeg",
            aspect_ratio="2:3",
            resolution="2k",
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "image.jpg"
            result = generate_image(
                client=client,
                prompt="Página pedagógica de teste.",
                output=output,
                options=options,
                provider="openrouter",
            )
            metadata = json.loads(
                (Path(directory) / "image.metadata.json").read_text(
                    encoding="utf-8"
                )
            )
        client.close()
        self.assertEqual(result.output_paths, [output])
        self.assertEqual(captured["method"], "POST")
        self.assertEqual(captured["path"], "/api/v1/images")
        self.assertEqual(captured["body"]["model"], "x-ai/grok-imagine-image-2.0")
        self.assertEqual(captured["body"]["aspect_ratio"], "2:3")
        self.assertEqual(captured["body"]["resolution"], "2K")
        self.assertEqual(result.request_id, "gen_openrouter_test")
        self.assertEqual(metadata["provider"], "openrouter")
        self.assertEqual(metadata["model"], "x-ai/grok-imagine-image-2.0")
        self.assertFalse(metadata["image"]["transcoded"])

    def test_openrouter_png_response_is_transcoded_to_requested_jpeg(self) -> None:
        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(
                200,
                json={"data": [{"b64_json": png_base64((1365, 2048))}]},
            )

        client = httpx.Client(
            base_url="https://openrouter.ai/api/v1",
            transport=httpx.MockTransport(handler),
        )
        options = GenerationOptions(
            model="x-ai/grok-imagine-image-2.0",
            size="auto",
            quality="medium",
            output_format="jpeg",
            aspect_ratio="2:3",
            resolution="2k",
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "image.jpg"
            generate_image(
                client=client,
                prompt="Página pedagógica de teste.",
                output=output,
                options=options,
                provider="openrouter",
            )
            with Image.open(output) as generated:
                self.assertEqual(generated.format, "JPEG")
        client.close()

    def test_openrouter_error_response_is_reported_without_saving(self) -> None:
        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(
                402, json={"error": {"message": "Insufficient credits"}}
            )

        client = httpx.Client(
            base_url="https://openrouter.ai/api/v1",
            transport=httpx.MockTransport(handler),
        )
        options = GenerationOptions(
            model="x-ai/grok-imagine-image-2.0",
            size="auto",
            quality="medium",
            output_format="jpeg",
            aspect_ratio="2:3",
            resolution="2k",
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "image.jpg"
            with self.assertRaisesRegex(GenerationError, "Insufficient credits"):
                generate_image(
                    client=client,
                    prompt="Teste",
                    output=output,
                    options=options,
                    provider="openrouter",
                )
            self.assertFalse(output.exists())
        client.close()

    def test_openrouter_stream_is_rejected(self) -> None:
        client = httpx.Client(
            base_url="https://openrouter.ai/api/v1",
            transport=httpx.MockTransport(
                lambda request: httpx.Response(200, json={"data": []})
            ),
        )
        options = GenerationOptions(
            model="x-ai/grok-imagine-image-2.0",
            size="auto",
            quality="medium",
            output_format="jpeg",
            aspect_ratio="2:3",
            resolution="2k",
            stream=True,
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "image.jpg"
            with self.assertRaisesRegex(GenerationError, "streaming"):
                generate_image(
                    client=client,
                    prompt="Teste",
                    output=output,
                    options=options,
                    provider="openrouter",
                )
        client.close()

    def test_check_authentication_openrouter_validates_key_and_model(self) -> None:
        def handler(request: httpx.Request) -> httpx.Response:
            if request.url.path == "/api/v1/key":
                return httpx.Response(200, json={"data": {"label": "test"}})
            if request.url.path == "/api/v1/models":
                return httpx.Response(
                    200,
                    json={"data": [{"id": "x-ai/grok-imagine-image-2.0"}]},
                )
            return httpx.Response(404, json={"error": {"message": "not found"}})

        client = httpx.Client(
            base_url="https://openrouter.ai/api/v1",
            transport=httpx.MockTransport(handler),
        )
        try:
            model_id = check_authentication(
                client, "x-ai/grok-imagine-image-2.0", "openrouter"
            )
        finally:
            client.close()
        self.assertEqual(model_id, "x-ai/grok-imagine-image-2.0")

    def test_check_authentication_openrouter_rejects_invalid_key(self) -> None:
        client = httpx.Client(
            base_url="https://openrouter.ai/api/v1",
            transport=httpx.MockTransport(
                lambda request: httpx.Response(
                    401, json={"error": {"message": "Invalid API key"}}
                )
            ),
        )
        try:
            with self.assertRaisesRegex(GenerationError, "Invalid API key"):
                check_authentication(
                    client, "x-ai/grok-imagine-image-2.0", "openrouter"
                )
        finally:
            client.close()

    def test_openai_format_mismatch_remains_rejected(self) -> None:
        response = SimpleNamespace(
            data=[SimpleNamespace(b64_json=png_base64())],
            usage=None,
            _request_id="req_openai_mismatch_test",
        )
        client = SimpleNamespace(images=FakeImages(response))
        options = GenerationOptions(
            size="1024x1024",
            output_format="jpeg",
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "image.jpg"
            with self.assertRaisesRegex(
                GenerationError,
                "retornou png, mas foi solicitado jpeg",
            ):
                generate_image(
                    client=client,
                    prompt="Página pedagógica de teste.",
                    output=output,
                    options=options,
                    provider="openai",
                )
            self.assertFalse(output.exists())

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
