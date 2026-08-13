from __future__ import annotations

import inspect
import unittest

from openai import OpenAI


class SdkContractTests(unittest.TestCase):
    def test_image_generation_parameters_exist_in_pinned_sdk(self) -> None:
        client = OpenAI(api_key="sk-test")
        parameters = set(inspect.signature(client.images.generate).parameters)
        expected = {
            "model",
            "prompt",
            "size",
            "quality",
            "output_format",
            "output_compression",
            "background",
            "moderation",
            "n",
            "stream",
            "partial_images",
        }
        self.assertFalse(expected - parameters)
