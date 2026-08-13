from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from gerador_imagens.config import ConfigError
from gerador_imagens.quality import validate_image_file
from gerador_imagens.storage import load_storage


ROOT = Path(__file__).resolve().parent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Promove imagens da revisão externa para a área de aprovadas."
    )
    parser.add_argument("imagens", nargs="+", help="Caminhos na área _revisao.")
    parser.add_argument("--saida-root", help="Sobrescreve a raiz externa configurada.")
    parser.add_argument("--revisor", help="Nome de quem fez a aprovação.")
    parser.add_argument("--forcar", action="store_true", help="Substitui a versão aprovada.")
    return parser


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_copy(source: Path, destination: Path, overwrite: bool) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and not overwrite:
        raise ConfigError(
            f"A versão aprovada já existe: {destination}. Use --forcar."
        )
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            dir=destination.parent,
            prefix=f".{destination.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary = Path(handle.name)
        shutil.copy2(source, temporary)
        os.replace(temporary, destination)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()


def write_approval(
    source: Path,
    destination: Path,
    review_root: Path,
    approved_root: Path,
    record_path: Path,
    reviewer: str | None,
    overwrite: bool,
) -> Path:
    record = {
        "schema_version": 2,
        "approved_at": datetime.now(timezone.utc).isoformat(),
        "reviewer": reviewer,
        "source_relative": source.relative_to(review_root).as_posix(),
        "approved_relative": destination.relative_to(approved_root).as_posix(),
        "image_sha256": sha256(destination),
        "image_bytes": destination.stat().st_size,
    }
    if record_path.exists() and not overwrite:
        raise ConfigError(
            f"O registro de aprovação já existe: {record_path}. Use --forcar."
        )
    record_path.parent.mkdir(parents=True, exist_ok=True)
    payload = (
        json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            dir=record_path.parent,
            prefix=f".{record_path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary = Path(handle.name)
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, record_path)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()
    return record_path


def resolve_source(value: str, review_root: Path) -> Path:
    raw = Path(value).expanduser()
    source = raw.resolve() if raw.is_absolute() else (review_root / raw).resolve()
    if not source.is_relative_to(review_root):
        raise ConfigError(f"A imagem não está na área de revisão: {source}")
    if not source.is_file():
        raise ConfigError(f"Imagem de revisão não encontrada: {source}")
    result = validate_image_file(source)
    if not result["valid"]:
        raise ConfigError(f"Imagem inválida: {source}: {result.get('error')}")
    return source


def run(args: argparse.Namespace) -> int:
    storage = load_storage(ROOT, args.saida_root)
    review_root = storage.area_root("revisao")
    approved_root = storage.area_root("aprovadas")
    records_root = ROOT / "registros" / "aprovacoes"
    for value in args.imagens:
        source = resolve_source(value, review_root)
        relative = source.relative_to(review_root)
        destination = approved_root / relative
        metadata_source = source.with_name(f"{source.stem}.metadata.json")
        metadata_destination = (records_root / relative).with_name(
            f"{destination.stem}.metadata.json"
        )
        record_path = (records_root / relative).with_name(
            f"{destination.stem}.approval.json"
        )
        planned = [destination, record_path]
        if metadata_source.exists():
            planned.append(metadata_destination)
        occupied = [path for path in planned if path.exists()]
        if occupied and not args.forcar:
            raise ConfigError(
                "Destino(s) já existente(s): "
                + ", ".join(str(path) for path in occupied)
                + ". Use --forcar."
            )
        atomic_copy(source, destination, args.forcar)
        if metadata_source.exists():
            atomic_copy(metadata_source, metadata_destination, args.forcar)
        record = write_approval(
            source,
            destination,
            review_root,
            approved_root,
            record_path,
            args.revisor,
            args.forcar,
        )
        print(f"Aprovada: {destination}")
        if metadata_source.exists():
            print(f"Metadados: {metadata_destination}")
        print(f"Registro: {record}")
    return 0


def main() -> int:
    try:
        return run(build_parser().parse_args())
    except ConfigError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("Operação interrompida.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
