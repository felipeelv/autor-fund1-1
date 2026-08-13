from __future__ import annotations

import re
import shutil
import subprocess
import unicodedata
from io import BytesIO
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from PIL import Image, UnidentifiedImageError


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str


def analyze_prompt(prompt: str) -> list[Finding]:
    findings: list[Finding] = []
    words = prompt.split()
    if not prompt.strip():
        return [Finding("error", "empty", "O prompt está vazio.")]
    if len(prompt) > 12_000:
        findings.append(
            Finding(
                "warning",
                "long-characters",
                f"Prompt muito extenso: {len(prompt):,} caracteres.",
            )
        )
    if len(words) > 2_000:
        findings.append(
            Finding(
                "warning",
                "long-words",
                f"Prompt muito extenso: {len(words):,} palavras.",
            )
        )
    if re.search(r"\b\d+(?:[.,]\d+)?\s*%", prompt):
        findings.append(
            Finding(
                "review",
                "statistic-percent",
                "Há percentuais no conteúdo; confirme a fonte antes da publicação.",
            )
        )
    if re.search(r"\b\d+\s+em\s+cada\s+\d+\b", prompt, re.IGNORECASE):
        findings.append(
            Finding(
                "review",
                "statistic-ratio",
                "Há uma estatística do tipo 'N em cada N'; confirme a fonte.",
            )
        )
    if re.search(
        r"\b(?:pesquisas?|estudos?)\s+(?:mostram|indicam|comprovam)\b",
        prompt,
        re.IGNORECASE,
    ):
        findings.append(
            Finding(
                "review",
                "unsourced-research",
                "O prompt atribui uma afirmação a pesquisas/estudos; registre a fonte.",
            )
        )
    if re.search(r"\b(?:19|20)\d{2}\b", prompt):
        findings.append(
            Finding(
                "review",
                "date",
                "Há datas no conteúdo; confirme o contexto histórico.",
            )
        )
    return findings


def validate_image_file(
    path: Path,
    image_bytes: bytes | None = None,
) -> dict[str, Any]:
    try:
        source = BytesIO(image_bytes) if image_bytes is not None else path
        with Image.open(source) as image:
            width, height = image.size
            image_format = (image.format or "").lower()
            image.verify()
    except (UnidentifiedImageError, OSError, SyntaxError) as exc:
        return {
            "path": str(path),
            "valid": False,
            "error": str(exc),
        }
    return {
        "path": str(path),
        "valid": True,
        "width": width,
        "height": height,
        "format": image_format,
        "bytes": len(image_bytes) if image_bytes is not None else path.stat().st_size,
    }


def validate_yaml_file(
    path: Path,
    yaml_text: str | None = None,
) -> dict[str, Any]:
    try:
        text = yaml_text if yaml_text is not None else path.read_text(encoding="utf-8")
        value = yaml.safe_load(text)
    except (OSError, UnicodeError, yaml.YAMLError, ValueError) as exc:
        return {"path": str(path), "valid": False, "error": str(exc)}
    return {
        "path": str(path),
        "valid": isinstance(value, dict),
        "error": None if isinstance(value, dict) else "A raiz do YAML não é um objeto.",
    }


def extract_expected_text(prompt: str) -> list[str]:
    markers = (
        "TEXT TO RENDER VERBATIM",
        "TEXTO A RENDERIZAR",
        "TEXTO PARA RENDERIZAR",
        "TEXTOS OBRIGATÓRIOS",
        "TEXTOS OBRIGATORIOS",
    )
    upper = prompt.upper()
    positions = [upper.rfind(marker) for marker in markers]
    start = max(positions)
    if start < 0:
        return []
    block = prompt[start:].splitlines()[1:]
    expected: list[str] = []
    for raw_line in block:
        line = raw_line.strip()
        if not line or line.startswith("```"):
            continue
        if line.startswith("#"):
            break
        line = re.sub(r"^[-*•]\s*", "", line)
        line = line.strip("\"'“”")
        if line and not set(line) <= {"-", "=", "═", "_"}:
            expected.append(line)
    return expected


def _normalize_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    value = re.sub(r"[^\w\s]", " ", value, flags=re.UNICODE)
    return re.sub(r"\s+", " ", value).strip()


def compare_ocr_text(ocr_text: str, expected_lines: list[str]) -> dict[str, Any]:
    normalized_ocr = _normalize_text(ocr_text)
    checked: list[dict[str, Any]] = []
    for line in expected_lines:
        normalized_line = _normalize_text(line)
        present = bool(normalized_line and normalized_line in normalized_ocr)
        checked.append({"text": line, "present": present})
    missing = [item["text"] for item in checked if not item["present"]]
    return {
        "expected_count": len(checked),
        "present_count": len(checked) - len(missing),
        "missing_count": len(missing),
        "missing": missing,
        "items": checked,
    }


def run_tesseract(path: Path, language: str = "por") -> str:
    executable = shutil.which("tesseract")
    if not executable:
        raise RuntimeError(
            "Tesseract não encontrado. Instale-o para habilitar OCR automático."
        )
    process = subprocess.run(
        [executable, str(path), "stdout", "-l", language],
        check=False,
        capture_output=True,
        text=True,
        timeout=180,
    )
    if process.returncode:
        message = process.stderr.strip() or "falha desconhecida do Tesseract"
        raise RuntimeError(f"OCR falhou: {message}")
    return process.stdout
