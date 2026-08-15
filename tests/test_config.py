from __future__ import annotations

import unittest
from pathlib import Path

from gerador_imagens.config import (
    ConfigError,
    GenerationOptions,
    normalize_output_path,
    options_from_mapping,
    output_paths,
    validate_size,
)


class ConfigTests(unittest.TestCase):
    def test_known_sizes_are_valid(self) -> None:
        self.assertEqual(validate_size("1024x1536"), (1024, 1536))
        self.assertEqual(validate_size("2160x3056"), (2160, 3056))
        self.assertIsNone(validate_size("auto"))

    def test_invalid_size_is_rejected(self) -> None:
        with self.assertRaises(ConfigError):
            validate_size("1000x1500")
        with self.assertRaises(ConfigError):
            validate_size("4096x4096")

    def test_portuguese_aliases(self) -> None:
        options = options_from_mapping(
            {"tamanho": "1024x1024", "qualidade": "low", "formato": "jpg"}
        )
        self.assertEqual(options.size, "1024x1024")
        self.assertEqual(options.quality, "low")
        self.assertEqual(options.output_format, "jpeg")

    def test_compression_requires_jpeg_or_webp(self) -> None:
        with self.assertRaises(ConfigError):
            options_from_mapping({"formato": "png", "compressao": 50})

    def test_streaming_requires_single_image(self) -> None:
        with self.assertRaises(ConfigError):
            GenerationOptions(stream=True, n=2).validated()

    def test_xai_aspect_ratio_and_resolution_aliases(self) -> None:
        options = options_from_mapping(
            {
                "tamanho": "auto",
                "formato": "jpeg",
                "proporcao": "2:3",
                "resolucao": "2k",
            }
        )
        self.assertEqual(options.aspect_ratio, "2:3")
        self.assertEqual(options.resolution, "2k")

    def test_resolution_accepts_uppercase_openrouter_form(self) -> None:
        options = options_from_mapping({"resolucao": "2K"})
        self.assertEqual(options.resolution, "2k")

    def test_output_extension_and_numbering(self) -> None:
        path = normalize_output_path(Path("imagem"), "png")
        self.assertEqual(path, Path("imagem.png"))
        self.assertEqual(
            output_paths(path, 2, "png"),
            [Path("imagem-01.png"), Path("imagem-02.png")],
        )
