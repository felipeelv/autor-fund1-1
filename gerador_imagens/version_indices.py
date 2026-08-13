from __future__ import annotations

import os
import re
import stat
import unicodedata
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

import yaml
from yaml.constructor import ConstructorError
from yaml.nodes import MappingNode


PORTABLE_ID_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*", re.ASCII)
SCHOOL_YEAR_PATTERN = re.compile(r"[1-9][0-9]*(?:ano|serie)", re.ASCII)
ACADEMIC_YEAR_PATTERN = re.compile(r"[0-9]{4}", re.ASCII)
INDEX_STATES = frozenset({"em-revisao", "aprovado"})
PREVIOUS_STATES = frozenset(
    {"substituido", "rejeitado", "historico", "experimento"}
)
DECISION_SOURCE_SUFFIXES = frozenset({".md", ".txt", ".json", ".yaml", ".yml"})
WINDOWS_FORBIDDEN = frozenset('<>:"|?*')
WINDOWS_DEVICES = frozenset(
    {"con", "prn", "aux", "nul"}
    | {f"com{number}" for number in range(1, 10)}
    | {f"lpt{number}" for number in range(1, 10)}
)
MAX_INDEX_BYTES = 1024 * 1024
MAX_MANIFEST_BYTES = 1024 * 1024
MAX_PROJECT_BYTES = 4 * 1024 * 1024
MAX_SOURCE_BYTES = 8 * 1024 * 1024
MAX_PROMPT_BYTES = 8 * 1024 * 1024
MAX_IMAGE_BYTES = 128 * 1024 * 1024
MAX_YAML_NODES = 20_000
MAX_YAML_DEPTH = 64
PROMPT_RENDERERS = frozenset(
    {
        "texto",
    }
)


@dataclass(frozen=True)
class VersionDecision:
    responsavel: str
    data: str
    fonte: str


@dataclass(frozen=True)
class PreviousVersion:
    arquivo: str
    situacao: str


@dataclass(frozen=True)
class VersionItem:
    id: str
    atual: str
    estado: str
    anteriores: tuple[PreviousVersion, ...]


@dataclass(frozen=True)
class VersionArchitecture:
    id: str
    projeto: str


@dataclass(frozen=True)
class VersionIndex:
    """Índice tecnicamente válido, metadata-only e serializável."""

    path: str
    autor: str
    ano: str
    ano_letivo: str
    periodo: str
    id: str
    estado: str
    decisao: VersionDecision
    itens: tuple[VersionItem, ...]
    arquitetura: VersionArchitecture | None


@dataclass(frozen=True)
class VersionIndexReport:
    path: str
    valid: bool
    error: str | None
    candidate: bool


@dataclass(frozen=True)
class PromptSnapshot:
    path: Path
    autor: str
    renderer: str
    text: str


@dataclass(frozen=True)
class PromptDiscoveryReport:
    path: str
    valid: bool
    error: str


@dataclass(frozen=True)
class PromptAreaContract:
    """Área declarada no manifesto e seus prompts materializados com segurança."""

    autor: str
    ano: str
    planejado: bool
    padrao: str
    arquivos: tuple[str, ...]


@dataclass(frozen=True)
class RenderResourceReport:
    path: str
    renderer: str
    valid: bool
    error: str | None


@dataclass(frozen=True)
class RenderResourceSnapshot:
    renderer: str
    texts: dict[str, str]


@dataclass(frozen=True)
class YamlSnapshot:
    path: Path
    text: str


@dataclass(frozen=True)
class YamlDiscoveryReport:
    path: str
    valid: bool
    error: str


@dataclass(frozen=True)
class ImageSnapshot:
    path: Path
    data: bytes


@dataclass(frozen=True)
class ImageDiscoveryReport:
    path: str
    valid: bool
    error: str


@dataclass(frozen=True)
class _FileSnapshot:
    path: Path
    relative: str
    identity: tuple[int, int]
    data: bytes


@dataclass(frozen=True)
class _IndexSnapshot:
    file: _FileSnapshot
    autor: str
    ano: str
    ano_letivo: str
    periodo: str


@dataclass(frozen=True)
class _LexicalIndex:
    id: str
    estado: str
    decisao: VersionDecision
    itens: tuple[VersionItem, ...]
    arquitetura: VersionArchitecture | None


@dataclass(frozen=True)
class _ManifestContract:
    projetos: tuple[str, ...]
    registros: tuple[str, ...]


@dataclass(frozen=True)
class _PromptManifestContract:
    areas: tuple["_PromptAreaDefinition", ...]

    @property
    def patterns(self) -> tuple[tuple[str, ...], ...]:
        return tuple(area.directory_pattern for area in self.areas)


@dataclass(frozen=True)
class _PromptAreaDefinition:
    autor: str
    ano: str
    planejado: bool
    directory_pattern: tuple[str, ...]
    source_pattern: tuple[str, ...]


@dataclass
class _Draft:
    snapshot: _IndexSnapshot
    lexical: _LexicalIndex
    claims: tuple[str, ...]
    errors: set[str] = field(default_factory=set)
    member_identities: tuple[tuple[int, int], ...] = ()
    contract: VersionIndex | None = None


@dataclass(frozen=True)
class _Entry:
    name: str
    mode: int

    @property
    def is_dir(self) -> bool:
        return stat.S_ISDIR(self.mode)

    @property
    def is_file(self) -> bool:
        return stat.S_ISREG(self.mode)

    @property
    def is_symlink(self) -> bool:
        return stat.S_ISLNK(self.mode)


class _IndexError(ValueError):
    pass


class _UniqueKeyLoader(yaml.SafeLoader):
    """SafeLoader com chaves únicas e limites explícitos de complexidade."""

    def __init__(self, stream: str) -> None:
        super().__init__(stream)
        self._node_count = 0
        self._compose_depth = 0

    def compose_node(self, parent: Any, index: Any) -> Any:
        self._node_count += 1
        if self._node_count > MAX_YAML_NODES:
            raise ConstructorError(
                None,
                None,
                "YAML excede o limite de nós",
                self.peek_event().start_mark,
            )
        self._compose_depth += 1
        if self._compose_depth > MAX_YAML_DEPTH:
            raise ConstructorError(
                None,
                None,
                "YAML excede o limite de profundidade",
                self.peek_event().start_mark,
            )
        try:
            return super().compose_node(parent, index)
        finally:
            self._compose_depth -= 1


def _construct_unique_mapping(
    loader: _UniqueKeyLoader,
    node: MappingNode,
    deep: bool = False,
) -> dict[Any, Any]:
    if not isinstance(node, MappingNode):
        raise ConstructorError(None, None, "era esperado um objeto YAML", node.start_mark)
    mapping: dict[Any, Any] = {}
    portable_keys: dict[str, str] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            repeated = key in mapping
        except TypeError as exc:
            raise ConstructorError(
                "ao construir um objeto YAML",
                node.start_mark,
                "a chave YAML não é escalar",
                key_node.start_mark,
            ) from exc
        if repeated:
            raise ConstructorError(
                "ao construir um objeto YAML",
                node.start_mark,
                f"chave duplicada: {key!r}",
                key_node.start_mark,
            )
        if isinstance(key, str):
            portable = _portable_key(key)
            if portable in portable_keys:
                raise ConstructorError(
                    "ao construir um objeto YAML",
                    node.start_mark,
                    "chaves aliases por Unicode NFKC + casefold: "
                    f"{portable_keys[portable]!r} e {key!r}",
                    key_node.start_mark,
                )
            portable_keys[portable] = key
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def _absolute_lexical(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def _portable_key(value: str) -> str:
    return unicodedata.normalize(
        "NFKC",
        unicodedata.normalize("NFKC", value).casefold(),
    )


def _portable_component_error(value: str) -> str | None:
    if not value or value != unicodedata.normalize("NFKC", value):
        return "deve usar Unicode NFKC canônico"
    if value != value.strip() or value.endswith((".", " ")):
        return "não pode ter ponto ou espaço final/externo"
    if any(character in WINDOWS_FORBIDDEN for character in value):
        return "contém caractere incompatível com Windows"
    if any(unicodedata.category(character).startswith("C") for character in value):
        return "contém caractere de controle"
    device_stem = value.split(".", 1)[0].casefold()
    if device_stem in WINDOWS_DEVICES:
        return "usa nome de dispositivo reservado no Windows"
    return None


def _valid_id(value: object) -> bool:
    return (
        isinstance(value, str)
        and _portable_component_error(value) is None
        and bool(PORTABLE_ID_PATTERN.fullmatch(value))
    )


def _valid_school_year(value: object) -> bool:
    return (
        isinstance(value, str)
        and _portable_component_error(value) is None
        and bool(SCHOOL_YEAR_PATTERN.fullmatch(value))
    )


def _relative_parts(
    value: object,
    *,
    label: str,
    basename_only: bool = False,
    suffix: str | None = None,
) -> tuple[str, ...]:
    if not isinstance(value, str) or not value:
        raise _IndexError(f"{label} deve ser um caminho relativo não vazio.")
    normalized = unicodedata.normalize("NFKC", value)
    if value != normalized:
        raise _IndexError(f"{label} deve usar Unicode NFKC canônico, sem aliases.")
    if (
        value.startswith(("~", "/"))
        or "\\" in value
        or "\x00" in value
        or re.match(r"^[A-Za-z]:", value)
        or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", value)
    ):
        raise _IndexError(f"{label} deve ser relativo e interno ao repositório.")
    parts = tuple(value.split("/"))
    if any(part in {"", ".", ".."} for part in parts):
        raise _IndexError(f"{label} contém segmento reservado ou vazio.")
    for part in parts:
        reason = _portable_component_error(part)
        if reason:
            raise _IndexError(f"{label}: o segmento {part!r} {reason}.")
    if basename_only and len(parts) != 1:
        raise _IndexError(f"{label} deve ser somente um nome de arquivo.")
    if suffix is not None and not value.endswith(suffix):
        raise _IndexError(f"{label} deve terminar em {suffix}.")
    return parts


def _exact_mapping(
    value: object,
    expected: frozenset[str],
    label: str,
) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise _IndexError(f"{label} deve ser um objeto YAML.")
    keys = set(value)
    if any(not isinstance(key, str) for key in keys):
        raise _IndexError(f"{label} aceita somente chaves textuais.")
    portable = [_portable_key(key) for key in keys]
    if len(portable) != len(set(portable)):
        raise _IndexError(f"{label} contém chaves aliases por NFKC + casefold.")
    missing = expected - keys
    unknown = keys - expected
    if missing or unknown:
        details: list[str] = []
        if missing:
            details.append(f"faltam {', '.join(sorted(missing))}")
        if unknown:
            details.append(f"chaves desconhecidas: {', '.join(sorted(unknown))}")
        raise _IndexError(f"{label} tem chaves inválidas ({'; '.join(details)}).")
    return value


def _nonempty_text(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise _IndexError(f"{label} deve ser texto não vazio, sem espaços externos.")
    if value != unicodedata.normalize("NFKC", value):
        raise _IndexError(f"{label} deve usar Unicode NFKC canônico.")
    if any(unicodedata.category(char).startswith("C") for char in value):
        raise _IndexError(f"{label} contém caractere de controle.")
    return value


def _yaml_from_bytes(data: bytes, label: str) -> object:
    try:
        content = data.decode("utf-8")
        return yaml.load(content, Loader=_UniqueKeyLoader)
    except (
        UnicodeError,
        yaml.YAMLError,
        RecursionError,
        ValueError,
        TypeError,
    ) as exc:
        raise _IndexError(f"{label} inválido: {exc}") from exc


def _stable_stat_key(value: os.stat_result) -> tuple[int, ...]:
    return (
        value.st_dev,
        value.st_ino,
        value.st_mode,
        value.st_nlink,
        value.st_size,
        value.st_mtime_ns,
        value.st_ctime_ns,
    )


class SecureRepository:
    """Leitura interna por descritores; sem suporte seguro, falha fechado."""

    def __init__(self, root: Path) -> None:
        self.root = _absolute_lexical(root)
        self._root_fd: int | None = None

    def __enter__(self) -> SecureRepository:
        required = (
            getattr(os, "O_NOFOLLOW", 0),
            getattr(os, "O_DIRECTORY", 0),
        )
        if (
            not all(required)
            or os.open not in os.supports_dir_fd
            or os.stat not in os.supports_dir_fd
            or os.stat not in os.supports_follow_symlinks
            or os.listdir not in os.supports_fd
        ):
            raise _IndexError(
                "a plataforma não oferece openat/O_NOFOLLOW seguros; "
                "a validação falhou de forma fechada"
            )
        try:
            before = os.lstat(self.root)
            if stat.S_ISLNK(before.st_mode):
                raise _IndexError("a raiz do projeto não pode ser link simbólico.")
            flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
            flags |= getattr(os, "O_CLOEXEC", 0)
            descriptor = os.open(self.root, flags)
            after = os.fstat(descriptor)
        except _IndexError:
            raise
        except OSError as exc:
            raise _IndexError(f"a raiz do projeto não pôde ser aberta: {exc}") from exc
        if not stat.S_ISDIR(after.st_mode) or (
            before.st_dev,
            before.st_ino,
        ) != (after.st_dev, after.st_ino):
            os.close(descriptor)
            raise _IndexError("a identidade da raiz mudou durante a abertura.")
        self._root_fd = descriptor
        return self

    def __exit__(self, *_args: object) -> None:
        if self._root_fd is not None:
            os.close(self._root_fd)
            self._root_fd = None

    def _root_dup(self) -> int:
        if self._root_fd is None:
            raise _IndexError("o repositório seguro não está aberto.")
        try:
            return os.dup(self._root_fd)
        except OSError as exc:
            raise _IndexError(f"a raiz não pôde ser duplicada: {exc}") from exc

    def _names(self, descriptor: int, label: str) -> list[str]:
        try:
            return sorted(os.listdir(descriptor))
        except OSError as exc:
            raise _IndexError(f"{label} não pôde ser listado: {exc}") from exc

    def _select_exact(
        self,
        descriptor: int,
        expected: str,
        label: str,
        *,
        optional: bool = False,
    ) -> str | None:
        portable = _portable_key(expected)
        matches = [
            name for name in self._names(descriptor, label) if _portable_key(name) == portable
        ]
        if not matches and optional:
            return None
        if len(matches) != 1:
            raise _IndexError(
                f"{label} é ausente ou ambíguo segundo Unicode NFKC + casefold."
            )
        if matches[0] != expected:
            raise _IndexError(f"{label} existe apenas com grafia não canônica.")
        return expected

    def _open_component(
        self,
        parent_fd: int,
        name: str,
        label: str,
        *,
        directory: bool,
        optional: bool = False,
    ) -> int | None:
        selected = self._select_exact(parent_fd, name, label, optional=optional)
        if selected is None:
            return None
        try:
            before = os.stat(selected, dir_fd=parent_fd, follow_symlinks=False)
            if stat.S_ISLNK(before.st_mode):
                raise _IndexError(f"{label} não pode ser link simbólico.")
            flags = os.O_RDONLY | os.O_NOFOLLOW | getattr(os, "O_CLOEXEC", 0)
            if directory:
                flags |= os.O_DIRECTORY
            else:
                flags |= getattr(os, "O_NONBLOCK", 0)
            descriptor = os.open(selected, flags, dir_fd=parent_fd)
            after = os.fstat(descriptor)
        except _IndexError:
            raise
        except OSError as exc:
            raise _IndexError(f"{label} não pôde ser aberto com segurança: {exc}") from exc
        expected_kind = stat.S_ISDIR if directory else stat.S_ISREG
        if not expected_kind(after.st_mode) or _stable_stat_key(before) != _stable_stat_key(after):
            os.close(descriptor)
            raise _IndexError(f"{label} mudou durante a abertura segura.")
        return descriptor

    def _open_directory(
        self,
        parts: tuple[str, ...],
        label: str,
        *,
        optional_last: bool = False,
        optional_suffix: bool = False,
    ) -> int | None:
        descriptor = self._root_dup()
        try:
            for index, part in enumerate(parts):
                child = self._open_component(
                    descriptor,
                    part,
                    label,
                    directory=True,
                    optional=(
                        optional_suffix
                        or (optional_last and index == len(parts) - 1)
                    ),
                )
                if child is None:
                    os.close(descriptor)
                    return None
                os.close(descriptor)
                descriptor = child
            return descriptor
        except Exception:
            os.close(descriptor)
            raise

    def entries(
        self,
        parts: tuple[str, ...],
        label: str,
        *,
        optional: bool = False,
    ) -> list[_Entry] | None:
        descriptor = self._open_directory(parts, label, optional_last=optional)
        if descriptor is None:
            return None
        try:
            entries: list[_Entry] = []
            for name in self._names(descriptor, label):
                try:
                    metadata = os.stat(name, dir_fd=descriptor, follow_symlinks=False)
                except OSError as exc:
                    raise _IndexError(f"{label}/{name} não pôde ser inspecionado: {exc}") from exc
                entries.append(_Entry(name, metadata.st_mode))
            return entries
        finally:
            os.close(descriptor)

    def directory_identity(
        self,
        parts: tuple[str, ...],
        label: str,
        *,
        optional: bool = False,
    ) -> tuple[int, int] | None:
        descriptor = self._open_directory(parts, label, optional_suffix=optional)
        if descriptor is None:
            return None
        try:
            metadata = os.fstat(descriptor)
            return metadata.st_dev, metadata.st_ino
        except OSError as exc:
            raise _IndexError(f"{label} não pôde ser confirmado: {exc}") from exc
        finally:
            os.close(descriptor)

    def read_file(
        self,
        parts: tuple[str, ...],
        label: str,
        *,
        max_bytes: int,
        require_single_link: bool = True,
    ) -> _FileSnapshot:
        if not parts:
            raise _IndexError(f"{label} não identifica arquivo.")
        parent_fd = self._open_directory(parts[:-1], label)
        if parent_fd is None:
            raise _IndexError(f"{label} não existe.")
        descriptor: int | None = None
        try:
            descriptor = self._open_component(
                parent_fd,
                parts[-1],
                label,
                directory=False,
            )
            if descriptor is None:
                raise _IndexError(f"{label} não existe.")
            before = os.fstat(descriptor)
            if require_single_link and before.st_nlink != 1:
                raise _IndexError(f"{label} não pode possuir hardlinks.")
            if before.st_size > max_bytes:
                raise _IndexError(f"{label} excede o limite de tamanho.")
            chunks: list[bytes] = []
            total = 0
            while True:
                chunk = os.read(descriptor, min(65536, max_bytes + 1 - total))
                if not chunk:
                    break
                chunks.append(chunk)
                total += len(chunk)
                if total > max_bytes:
                    raise _IndexError(f"{label} excede o limite de tamanho.")
            after = os.fstat(descriptor)
            if _stable_stat_key(before) != _stable_stat_key(after):
                raise _IndexError(f"{label} mudou durante a leitura segura.")
            relative = "/".join(parts)
            return _FileSnapshot(
                path=self.root.joinpath(*parts),
                relative=relative,
                identity=(after.st_dev, after.st_ino),
                data=b"".join(chunks),
            )
        except _IndexError:
            raise
        except OSError as exc:
            raise _IndexError(f"{label} falhou durante a leitura segura: {exc}") from exc
        finally:
            if descriptor is not None:
                os.close(descriptor)
            os.close(parent_fd)


def _parse_lexical_index(snapshot: _IndexSnapshot, raw: object) -> _LexicalIndex:
    allowed = frozenset({"schema", "id", "estado", "decisao", "itens"})
    if isinstance(raw, dict) and "arquitetura" in raw:
        allowed |= {"arquitetura"}
    data = _exact_mapping(raw, allowed, "índice")
    if type(data["schema"]) is not int or data["schema"] != 1:
        raise _IndexError("schema deve ser exatamente o inteiro 1.")
    index_id = data["id"]
    if not _valid_id(index_id) or index_id != Path(snapshot.file.relative).stem:
        raise _IndexError("id deve ser portátil e igual ao nome do arquivo YAML.")
    state = data["estado"]
    if not isinstance(state, str) or state not in INDEX_STATES:
        raise _IndexError("estado deve ser em-revisao ou aprovado.")

    decision_data = _exact_mapping(
        data["decisao"],
        frozenset({"responsavel", "data", "fonte"}),
        "decisao",
    )
    responsible = _nonempty_text(decision_data["responsavel"], "decisao.responsavel")
    decision_date = decision_data["data"]
    if not isinstance(decision_date, str) or not re.fullmatch(
        r"[0-9]{4}-[0-9]{2}-[0-9]{2}", decision_date
    ):
        raise _IndexError("decisao.data deve ser string ISO AAAA-MM-DD entre aspas.")
    try:
        date.fromisoformat(decision_date)
    except ValueError as exc:
        raise _IndexError("decisao.data não é data de calendário válida.") from exc
    source = decision_data["fonte"]
    source_parts = _relative_parts(source, label="decisao.fonte")
    if Path(source).suffix not in DECISION_SOURCE_SUFFIXES:
        raise _IndexError("decisao.fonte deve usar .md, .txt, .json, .yaml ou .yml.")
    if _portable_key("/".join(source_parts)) == _portable_key(snapshot.file.relative):
        raise _IndexError("decisao.fonte não pode ser o próprio índice.")
    if source_parts[0] != "registros" and source_parts[:2] != (
        "autores",
        snapshot.autor,
    ):
        raise _IndexError(
            "decisao.fonte deve apontar lexicalmente para registros globais "
            "ou para o mesmo autor."
        )
    decision = VersionDecision(responsible, decision_date, source)

    items_data = data["itens"]
    if not isinstance(items_data, dict) or not items_data:
        raise _IndexError("itens deve ser mapa não vazio.")
    item_keys = [_portable_key(str(key)) for key in items_data]
    if len(item_keys) != len(set(item_keys)):
        raise _IndexError("itens contém IDs aliases por NFKC + casefold.")
    items: list[VersionItem] = []
    members: dict[str, str] = {}
    for item_id, item_value in items_data.items():
        if not _valid_id(item_id):
            raise _IndexError("cada chave de itens deve ser um ID portátil.")
        item_data = _exact_mapping(
            item_value,
            frozenset({"atual", "estado", "anteriores"}),
            f"itens.{item_id}",
        )
        current = item_data["atual"]
        _relative_parts(
            current,
            label=f"itens.{item_id}.atual",
            basename_only=True,
            suffix=".md",
        )
        item_state = item_data["estado"]
        if not isinstance(item_state, str) or item_state not in INDEX_STATES:
            raise _IndexError(f"itens.{item_id}.estado é inválido.")
        previous_data = item_data["anteriores"]
        if not isinstance(previous_data, list):
            raise _IndexError(f"itens.{item_id}.anteriores deve ser lista.")
        previous: list[PreviousVersion] = []
        filenames = [current]
        for position, value in enumerate(previous_data):
            previous_map = _exact_mapping(
                value,
                frozenset({"arquivo", "situacao"}),
                f"itens.{item_id}.anteriores[{position}]",
            )
            filename = previous_map["arquivo"]
            _relative_parts(
                filename,
                label=f"itens.{item_id}.anteriores[{position}].arquivo",
                basename_only=True,
                suffix=".md",
            )
            situation = previous_map["situacao"]
            if not isinstance(situation, str) or situation not in PREVIOUS_STATES:
                raise _IndexError(
                    f"itens.{item_id}.anteriores[{position}].situacao é inválida."
                )
            previous.append(PreviousVersion(filename, situation))
            filenames.append(filename)
        for filename in filenames:
            key = _portable_key(filename)
            if key in members:
                raise _IndexError(
                    f"{filename!r} repete ou é alias de {members[key]!r} no índice."
                )
            members[key] = filename
        items.append(VersionItem(item_id, current, item_state, tuple(previous)))
    if state == "aprovado" and any(item.estado != "aprovado" for item in items):
        raise _IndexError("índice aprovado exige todos os itens aprovados.")

    architecture: VersionArchitecture | None = None
    if "arquitetura" in data:
        architecture_data = _exact_mapping(
            data["arquitetura"],
            frozenset({"id", "projeto"}),
            "arquitetura",
        )
        architecture_id = architecture_data["id"]
        if not _valid_id(architecture_id):
            raise _IndexError("arquitetura.id deve ser ID portátil.")
        project = architecture_data["projeto"]
        project_parts = _relative_parts(
            project,
            label="arquitetura.projeto",
            suffix=".yaml",
        )
        if _portable_key("/".join(project_parts)) == _portable_key(snapshot.file.relative):
            raise _IndexError("arquitetura.projeto não pode ser o próprio índice.")
        if project_parts[:2] != ("autores", snapshot.autor):
            raise _IndexError(
                "arquitetura.projeto deve apontar lexicalmente para o mesmo autor."
            )
        architecture = VersionArchitecture(architecture_id, project)
    return _LexicalIndex(index_id, state, decision, tuple(items), architecture)


def _tuple_key(parts: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(_portable_key(part) for part in parts)


def _contains(parent: tuple[str, ...], child: tuple[str, ...]) -> bool:
    return len(parent) <= len(child) and child[: len(parent)] == parent


def _manifest_contract(
    repo: SecureRepository,
    author: str,
    school_year: str,
) -> _ManifestContract:
    parts = ("autores", author, "manifesto.yaml")
    snapshot = repo.read_file(
        parts,
        "manifesto.yaml",
        max_bytes=MAX_MANIFEST_BYTES,
    )
    data = _yaml_from_bytes(snapshot.data, "manifesto.yaml")
    if not isinstance(data, dict):
        raise _IndexError("manifesto.yaml deve conter objeto YAML.")
    if type(data.get("schema")) is not int or data.get("schema") != 1:
        raise _IndexError("manifesto.yaml deve declarar schema inteiro 1.")
    discipline = data.get("disciplina")
    if not isinstance(discipline, dict) or discipline.get("id") != author:
        raise _IndexError("manifesto.yaml deve declarar disciplina.id igual ao autor.")
    if "anos" not in data or "anos_planejados" not in data:
        raise _IndexError("manifesto.yaml exige anos e anos_planejados.")
    years = data["anos"]
    planned = data["anos_planejados"]
    if not isinstance(years, list) or not isinstance(planned, list):
        raise _IndexError("anos e anos_planejados devem ser listas.")
    if any(not _valid_school_year(value) for value in years + planned):
        raise _IndexError("anos e anos_planejados aceitam somente IDs canônicos.")
    year_keys = [_portable_key(value) for value in years]
    planned_keys = [_portable_key(value) for value in planned]
    if len(year_keys) != len(set(year_keys)) or len(planned_keys) != len(set(planned_keys)):
        raise _IndexError("anos e anos_planejados não aceitam duplicatas/aliases.")
    if not set(planned_keys).issubset(set(year_keys)):
        raise _IndexError("anos_planejados deve ser subconjunto portátil de anos.")
    school_key = _portable_key(school_year)
    if school_year not in years:
        raise _IndexError("o ano do índice deve constar exatamente em anos.")
    if school_key in set(planned_keys):
        raise _IndexError("ano ainda planejado não pode possuir índice real.")

    production = data.get("producao")
    if not isinstance(production, dict):
        raise _IndexError("manifesto.yaml exige mapa producao.")
    projects = _relative_parts(production.get("projetos"), label="producao.projetos")
    records = _relative_parts(production.get("registros"), label="producao.registros")
    project_key = _tuple_key(projects)
    record_key = _tuple_key(records)
    if (
        _contains(project_key, record_key)
        or _contains(record_key, project_key)
    ):
        raise _IndexError("producao.projetos e producao.registros devem ser disjuntos.")
    reserved_key = ("anos",)
    for area_name, area in (("projetos", project_key), ("registros", record_key)):
        if _contains(area, reserved_key) or _contains(reserved_key, area):
            raise _IndexError(
                f"producao.{area_name} sobrepõe a árvore reservada anos/**."
            )
    project_identity = repo.directory_identity(
        ("autores", author, *projects),
        "producao.projetos",
        optional=True,
    )
    record_identity = repo.directory_identity(
        ("autores", author, *records),
        "producao.registros",
        optional=True,
    )
    if (
        project_identity is not None
        and record_identity is not None
        and project_identity == record_identity
    ):
        raise _IndexError("áreas de produção apontam para o mesmo diretório físico.")
    production_identities = {
        identity
        for identity in (project_identity, record_identity)
        if identity is not None
    }
    years_identity = repo.directory_identity(
        ("autores", author, "anos"),
        "árvore reservada anos/**",
        optional=True,
    )
    if years_identity is not None and years_identity in production_identities:
        raise _IndexError("uma área de produção aponta para a árvore reservada anos/**.")
    return _ManifestContract(projects, records)


def _group_entries(entries: list[_Entry]) -> list[list[_Entry]]:
    grouped: dict[str, list[_Entry]] = {}
    for entry in entries:
        if entry.name in {".DS_Store", ".gitkeep"}:
            continue
        grouped.setdefault(_portable_key(entry.name), []).append(entry)
    return [grouped[key] for key in sorted(grouped)]


def _invalid(
    path: Path,
    message: str,
    *,
    candidate: bool = False,
) -> VersionIndexReport:
    return VersionIndexReport(str(path), False, message, candidate)


def _fixed_directory_exists(
    repo: SecureRepository,
    parent: tuple[str, ...],
    name: str,
    label: str,
    *,
    optional: bool,
) -> bool:
    entries = repo.entries(parent, label)
    if entries is None:
        return False
    matches = [entry for entry in entries if _portable_key(entry.name) == _portable_key(name)]
    if not matches and optional:
        return False
    if len(matches) != 1 or matches[0].name != name:
        raise _IndexError(f"{label} é ausente ou possui alias NFKC + casefold.")
    if not matches[0].is_dir:
        raise _IndexError(f"{label} não é diretório real.")
    repo.directory_identity((*parent, name), label)
    return True


def _discover_index_snapshots(
    repo: SecureRepository,
) -> tuple[list[_IndexSnapshot], list[VersionIndexReport]]:
    reports: list[VersionIndexReport] = []
    snapshots: list[_IndexSnapshot] = []
    try:
        if not _fixed_directory_exists(repo, (), "autores", "autores/", optional=False):
            return [], reports
        author_entries = repo.entries(("autores",), "autores/") or []
    except _IndexError as exc:
        return [], [_invalid(repo.root / "autores", str(exc))]
    for author_group in _group_entries(author_entries):
        paths = [repo.root / "autores" / item.name for item in author_group]
        if len(author_group) != 1:
            for path in paths:
                reports.append(_invalid(path, "alias de autor por NFKC + casefold."))
            continue
        author_entry = author_group[0]
        author = author_entry.name
        if author.startswith("_") or author_entry.is_file:
            continue
        if not _valid_id(author) or not author_entry.is_dir:
            reports.append(_invalid(paths[0], "pasta de autor inválida ou não portátil."))
            continue
        try:
            if not _fixed_directory_exists(
                repo,
                ("autores", author),
                "anos",
                f"autores/{author}/anos",
                optional=True,
            ):
                continue
            school_entries = repo.entries(
                ("autores", author, "anos"),
                f"autores/{author}/anos",
            ) or []
        except _IndexError as exc:
            reports.append(_invalid(paths[0] / "anos", str(exc)))
            continue
        for school_group in _group_entries(school_entries):
            school_paths = [paths[0] / "anos" / item.name for item in school_group]
            if len(school_group) != 1:
                for path in school_paths:
                    reports.append(_invalid(path, "alias de ano por NFKC + casefold."))
                continue
            school_entry = school_group[0]
            school_year = school_entry.name
            if not _valid_school_year(school_year) or not school_entry.is_dir:
                reports.append(_invalid(school_paths[0], "ano escolar inválido."))
                continue
            school_parts = ("autores", author, "anos", school_year)
            try:
                if not _fixed_directory_exists(
                    repo,
                    school_parts,
                    "indices",
                    f"{'/'.join(school_parts)}/indices",
                    optional=True,
                ):
                    continue
                academic_entries = repo.entries(
                    (*school_parts, "indices"),
                    f"{'/'.join(school_parts)}/indices",
                ) or []
            except _IndexError as exc:
                reports.append(_invalid(school_paths[0] / "indices", str(exc)))
                continue
            for academic_group in _group_entries(academic_entries):
                academic_paths = [
                    school_paths[0] / "indices" / item.name for item in academic_group
                ]
                if len(academic_group) != 1:
                    for path in academic_paths:
                        reports.append(_invalid(path, "alias de ano letivo por NFKC + casefold."))
                    continue
                academic_entry = academic_group[0]
                academic_year = academic_entry.name
                if (
                    _portable_component_error(academic_year)
                    or not ACADEMIC_YEAR_PATTERN.fullmatch(academic_year)
                    or not academic_entry.is_dir
                ):
                    reports.append(_invalid(academic_paths[0], "ano letivo inválido."))
                    continue
                academic_parts = (*school_parts, "indices", academic_year)
                try:
                    period_entries = repo.entries(
                        academic_parts,
                        "/".join(academic_parts),
                    ) or []
                except _IndexError as exc:
                    reports.append(_invalid(academic_paths[0], str(exc)))
                    continue
                for period_group in _group_entries(period_entries):
                    period_paths = [academic_paths[0] / item.name for item in period_group]
                    if len(period_group) != 1:
                        for path in period_paths:
                            reports.append(_invalid(path, "alias de período por NFKC + casefold."))
                        continue
                    period_entry = period_group[0]
                    period = period_entry.name
                    if not _valid_id(period) or not period_entry.is_dir:
                        reports.append(_invalid(period_paths[0], "período inválido."))
                        continue
                    period_parts = (*academic_parts, period)
                    try:
                        file_entries = repo.entries(period_parts, "/".join(period_parts)) or []
                    except _IndexError as exc:
                        reports.append(_invalid(period_paths[0], str(exc)))
                        continue
                    for file_group in _group_entries(file_entries):
                        file_paths = [period_paths[0] / item.name for item in file_group]
                        portable_yaml = _portable_key(file_group[0].name).endswith(".yaml")
                        if len(file_group) != 1:
                            for path in file_paths:
                                reports.append(
                                    _invalid(
                                        path,
                                        "alias de índice por NFKC + casefold.",
                                        candidate=portable_yaml,
                                    )
                                )
                            continue
                        entry = file_group[0]
                        if entry.name.startswith("."):
                            reports.append(
                                _invalid(
                                    file_paths[0],
                                    "conteúdo oculto não permitido em índices.",
                                    candidate=portable_yaml,
                                )
                            )
                            continue
                        if not portable_yaml:
                            reports.append(_invalid(file_paths[0], "índice deve usar .yaml."))
                            continue
                        if (
                            _portable_component_error(entry.name)
                            or not entry.name.endswith(".yaml")
                        ):
                            reports.append(
                                _invalid(
                                    file_paths[0],
                                    "nome de índice deve ser canônico e usar sufixo literal .yaml.",
                                    candidate=True,
                                )
                            )
                            continue
                        if entry.is_symlink:
                            reports.append(
                                _invalid(
                                    file_paths[0],
                                    "índice não pode ser link simbólico.",
                                    candidate=portable_yaml,
                                )
                            )
                            continue
                        if not entry.is_file or not _valid_id(Path(entry.name).stem):
                            reports.append(
                                _invalid(
                                    file_paths[0],
                                    "arquivo de índice inválido ou não portátil.",
                                    candidate=True,
                                )
                            )
                            continue
                        relative = (*period_parts, entry.name)
                        try:
                            file_snapshot = repo.read_file(
                                relative,
                                "índice de versão",
                                max_bytes=MAX_INDEX_BYTES,
                            )
                        except _IndexError as exc:
                            reports.append(_invalid(file_paths[0], str(exc), candidate=True))
                            continue
                        snapshots.append(
                            _IndexSnapshot(
                                file_snapshot,
                                author,
                                school_year,
                                academic_year,
                                period,
                            )
                        )
    return snapshots, reports


def _claims(snapshot: _IndexSnapshot, lexical: _LexicalIndex) -> tuple[str, ...]:
    prefix = (
        "autores",
        snapshot.autor,
        "anos",
        snapshot.ano,
        "prompts",
        snapshot.ano_letivo,
        snapshot.periodo,
    )
    return tuple(
        "/".join((*prefix, filename))
        for item in lexical.itens
        for filename in (
            item.atual,
            *(previous.arquivo for previous in item.anteriores),
        )
    )


def _source_allowed(
    source: tuple[str, ...],
    author: str,
    manifest: _ManifestContract,
) -> bool:
    transversal = len(source) > 1 and source[0] == "registros"
    author_prefix = ("autores", author, *manifest.registros)
    author_record = len(source) > len(author_prefix) and source[: len(author_prefix)] == author_prefix
    return transversal or author_record


def _validate_draft(
    repo: SecureRepository,
    draft: _Draft,
    manifest: _ManifestContract,
) -> None:
    snapshot = draft.snapshot
    lexical = draft.lexical
    source_parts = _relative_parts(lexical.decisao.fonte, label="decisao.fonte")
    if not _source_allowed(source_parts, snapshot.autor, manifest):
        raise _IndexError("decisao.fonte deve ficar em área interna de registros.")
    project_parts: tuple[str, ...] | None = None
    if lexical.arquitetura is not None:
        project_parts = _relative_parts(
            lexical.arquitetura.projeto,
            label="arquitetura.projeto",
            suffix=".yaml",
        )
        expected = ("autores", snapshot.autor, *manifest.projetos)
        if len(project_parts) <= len(expected) or project_parts[: len(expected)] != expected:
            raise _IndexError("arquitetura.projeto deve ficar na área producao.projetos.")

    # Somente após toda a fase contextual lexical estar concluída são abertos
    # fonte, projeto e prompts. Assim um caminho rejeitável não causa inspeção
    # parcial de qualquer alvo declarado.
    source = repo.read_file(
        source_parts,
        "decisao.fonte",
        max_bytes=MAX_SOURCE_BYTES,
    )
    if source.identity == snapshot.file.identity:
        raise _IndexError("decisao.fonte não pode ser o próprio índice físico.")
    try:
        source.data.decode("utf-8")
    except UnicodeError as exc:
        raise _IndexError("decisao.fonte deve ser UTF-8 integralmente legível.") from exc

    if project_parts is not None:
        project = repo.read_file(
            project_parts,
            "arquitetura.projeto",
            max_bytes=MAX_PROJECT_BYTES,
        )
        if project.identity == snapshot.file.identity:
            raise _IndexError("arquitetura.projeto não pode ser o próprio índice físico.")
        project_data = _yaml_from_bytes(project.data, "arquitetura.projeto")
        project_info = project_data.get("projeto") if isinstance(project_data, dict) else None
        if not isinstance(project_info, dict) or project_info.get("autor") != snapshot.autor:
            raise _IndexError("arquitetura.projeto deve declarar projeto.autor igual ao índice.")

    identities: list[tuple[int, int]] = []
    for claim in draft.claims:
        prompt = repo.read_file(
            tuple(claim.split("/")),
            f"prompt {Path(claim).name!r}",
            max_bytes=MAX_PROMPT_BYTES,
        )
        if prompt.identity in identities:
            raise _IndexError("dois membros apontam para o mesmo prompt físico.")
        identities.append(prompt.identity)
    draft.member_identities = tuple(identities)
    draft.contract = VersionIndex(
        path=str(snapshot.file.path),
        autor=snapshot.autor,
        ano=snapshot.ano,
        ano_letivo=snapshot.ano_letivo,
        periodo=snapshot.periodo,
        id=lexical.id,
        estado=lexical.estado,
        decisao=lexical.decisao,
        itens=lexical.itens,
        arquitetura=lexical.arquitetura,
    )


def _apply_global_ownership(drafts: list[_Draft]) -> None:
    lexical_claims: dict[str, list[_Draft]] = {}
    physical_claims: dict[tuple[int, int], list[_Draft]] = {}
    for draft in drafts:
        for claim in draft.claims:
            lexical_claims.setdefault(_portable_key(claim), []).append(draft)
        for identity in draft.member_identities:
            physical_claims.setdefault(identity, []).append(draft)
    for groups, label in (
        (lexical_claims.values(), "caminho portátil"),
        (physical_claims.values(), "identidade física"),
    ):
        for group in groups:
            unique = {id(draft): draft for draft in group}
            if len(unique) <= 1:
                continue
            for draft in unique.values():
                draft.errors.add(
                    f"prompt reivindicado por mais de um índice ({label})."
                )


def discover_version_indices(
    root: Path,
) -> tuple[list[VersionIndex], list[VersionIndexReport]]:
    """Descobre contratos tecnicamente válidos, sem efeito na geração."""

    try:
        with SecureRepository(root) as repo:
            snapshots, structural_reports = _discover_index_snapshots(repo)
            drafts: list[_Draft] = []
            reports = list(structural_reports)
            for snapshot in snapshots:
                try:
                    raw = _yaml_from_bytes(snapshot.file.data, "índice YAML")
                    lexical = _parse_lexical_index(snapshot, raw)
                except _IndexError as exc:
                    reports.append(_invalid(snapshot.file.path, str(exc), candidate=True))
                    continue
                draft = _Draft(snapshot, lexical, _claims(snapshot, lexical))
                drafts.append(draft)
                try:
                    manifest = _manifest_contract(repo, snapshot.autor, snapshot.ano)
                    _validate_draft(repo, draft, manifest)
                except _IndexError as exc:
                    draft.errors.add(str(exc))
            _apply_global_ownership(drafts)
            contracts: list[VersionIndex] = []
            for draft in drafts:
                if draft.errors or draft.contract is None:
                    reports.append(
                        _invalid(
                            draft.snapshot.file.path,
                            "; ".join(sorted(draft.errors)) or "índice inválido",
                            candidate=True,
                        )
                    )
                else:
                    contracts.append(draft.contract)
                    reports.append(
                        VersionIndexReport(
                            str(draft.snapshot.file.path),
                            True,
                            None,
                            True,
                        )
                    )
            return (
                sorted(contracts, key=lambda item: item.path),
                sorted(reports, key=lambda item: (item.path, item.valid)),
            )
    except _IndexError as exc:
        path = _absolute_lexical(root)
        return [], [_invalid(path, str(exc))]


def _walk_prompt_tree(
    repo: SecureRepository,
    parts: tuple[str, ...],
    author: str,
    renderer: str,
    inside_prompts: bool,
    snapshots: list[PromptSnapshot],
    reports: list[PromptDiscoveryReport],
) -> None:
    try:
        entries = repo.entries(parts, "/".join(parts)) or []
    except _IndexError as exc:
        reports.append(PromptDiscoveryReport(str(repo.root.joinpath(*parts)), False, str(exc)))
        return
    for group in _group_entries(entries):
        paths = [repo.root.joinpath(*parts, entry.name) for entry in group]
        if len(group) != 1:
            for path in paths:
                reports.append(
                    PromptDiscoveryReport(str(path), False, "alias NFKC + casefold no acervo")
                )
            continue
        entry = group[0]
        path = paths[0]
        prompts_alias = _portable_key(entry.name) == _portable_key("prompts")
        if prompts_alias and entry.name != "prompts":
            reports.append(
                PromptDiscoveryReport(
                    str(path),
                    False,
                    "a área prompts existe apenas com grafia não canônica",
                )
            )
            continue
        if entry.name.startswith("."):
            reports.append(
                PromptDiscoveryReport(str(path), False, "conteúdo oculto não permitido")
            )
            continue
        reason = _portable_component_error(entry.name)
        if reason:
            reports.append(PromptDiscoveryReport(str(path), False, reason))
            continue
        if entry.is_symlink:
            reports.append(PromptDiscoveryReport(str(path), False, "link simbólico proibido"))
            continue
        child_parts = (*parts, entry.name)
        child_inside = inside_prompts or entry.name == "prompts"
        if entry.is_dir:
            _walk_prompt_tree(
                repo,
                child_parts,
                author,
                renderer,
                child_inside,
                snapshots,
                reports,
            )
        elif child_inside and Path(entry.name).suffix == ".md":
            if not _prompt_file_matches(entry.name):
                reports.append(
                    PromptDiscoveryReport(
                        str(path),
                        False,
                        "<arquivo>.md exige nome-base como ID portátil",
                    )
                )
            else:
                _append_prompt_snapshot(
                    repo,
                    child_parts,
                    author,
                    renderer,
                    snapshots,
                    reports,
                )
        elif child_inside and Path(entry.name).suffix.lower() in {".md", ".txt"}:
            reports.append(
                PromptDiscoveryReport(
                    str(path),
                    False,
                    "arquivo não satisfaz o sufixo .md declarado no manifesto",
                )
            )


def _append_prompt_snapshot(
    repo: SecureRepository,
    parts: tuple[str, ...],
    author: str,
    renderer: str,
    snapshots: list[PromptSnapshot],
    reports: list[PromptDiscoveryReport],
) -> None:
    """Materializa um prompt por um único descritor e nunca reabre seu caminho."""

    path = repo.root.joinpath(*parts)
    name = parts[-1]
    try:
        file = repo.read_file(
            parts,
            f"prompt {name!r}",
            max_bytes=MAX_PROMPT_BYTES,
        )
        text = file.data.decode("utf-8").strip()
        if not text:
            raise _IndexError("o prompt está vazio")
    except (UnicodeError, _IndexError) as exc:
        reports.append(PromptDiscoveryReport(str(path), False, str(exc)))
        return
    selected_renderer = renderer
    if text.startswith("---"):
        match = re.match(
            r"\A---[ \t]*\n(.*?)\n---[ \t]*(?:\n|\Z)(.*)\Z",
            text,
            re.DOTALL,
        )
        if match:
            try:
                frontmatter = _yaml_from_bytes(
                    match.group(1).encode("utf-8"),
                    f"frontmatter de {name}",
                )
            except _IndexError:
                frontmatter = None
            if isinstance(frontmatter, dict):
                if frontmatter.get("formato") == "colagem-editorial":
                    selected_renderer = "colagem-editorial"
                elif (
                    renderer == "infografico-cientifico"
                    and "conceito_central_tipo" not in frontmatter
                    and "hero_descricao" in frontmatter
                ):
                    selected_renderer = "infografico-editorial"
    snapshots.append(PromptSnapshot(path, author, selected_renderer, text))


def _prompt_renderer(repo: SecureRepository, author: str) -> str:
    profile = repo.read_file(
        ("autores", author, "autor.yaml"),
        f"autores/{author}/autor.yaml",
        max_bytes=MAX_MANIFEST_BYTES,
    )
    raw = _yaml_from_bytes(profile.data, f"autores/{author}/autor.yaml")
    if not isinstance(raw, dict):
        raise _IndexError("autor.yaml deve conter objeto YAML.")
    data = raw.get("autor")
    if not isinstance(data, dict):
        raise _IndexError("autor.yaml deve conter o mapa autor.")
    if data.get("id") != author:
        raise _IndexError("autor.yaml deve declarar autor.id igual à pasta.")
    if type(data.get("ativo")) is not bool or not data["ativo"]:
        raise _IndexError("autor.yaml deve declarar ativo: true.")
    renderer = data.get("renderizador_padrao")
    if not isinstance(renderer, str) or renderer not in PROMPT_RENDERERS:
        raise _IndexError("autor.yaml declara renderizador_padrao inválido.")
    return renderer


def _prompt_manifest_contract(
    repo: SecureRepository,
    author: str,
) -> _PromptManifestContract:
    snapshot = repo.read_file(
        ("autores", author, "manifesto.yaml"),
        f"autores/{author}/manifesto.yaml",
        max_bytes=MAX_MANIFEST_BYTES,
    )
    raw = _yaml_from_bytes(snapshot.data, f"autores/{author}/manifesto.yaml")
    if not isinstance(raw, dict):
        raise _IndexError("manifesto.yaml deve conter objeto YAML.")
    if type(raw.get("schema")) is not int or raw.get("schema") != 1:
        raise _IndexError("manifesto.yaml deve declarar schema inteiro 1.")
    discipline = raw.get("disciplina")
    if not isinstance(discipline, dict) or discipline.get("id") != author:
        raise _IndexError("manifesto.yaml deve declarar disciplina.id igual ao autor.")
    if "anos" not in raw or "anos_planejados" not in raw:
        raise _IndexError("manifesto.yaml exige anos e anos_planejados.")
    years = raw["anos"]
    planned = raw["anos_planejados"]
    if not isinstance(years, list) or not isinstance(planned, list):
        raise _IndexError("anos e anos_planejados devem ser listas.")
    if any(not _valid_school_year(value) for value in [*years, *planned]):
        raise _IndexError("anos e anos_planejados aceitam somente IDs canônicos.")
    year_keys = [_portable_key(value) for value in years]
    planned_keys = [_portable_key(value) for value in planned]
    if len(year_keys) != len(set(year_keys)) or len(planned_keys) != len(
        set(planned_keys)
    ):
        raise _IndexError("anos e anos_planejados não aceitam duplicatas/aliases.")
    if not set(planned_keys).issubset(set(year_keys)):
        raise _IndexError("anos_planejados deve ser subconjunto portátil de anos.")
    structure = raw.get("estrutura_por_ano")
    template = structure.get("prompts") if isinstance(structure, dict) else None
    template_parts = _prompt_template_parts(
        template,
        "estrutura_por_ano.prompts",
    )
    if template_parts[:3] != ("anos", "<ano>", "prompts"):
        raise _IndexError(
            "estrutura_por_ano.prompts deve começar por anos/<ano>/prompts."
        )
    if template_parts.count("<ano>") != 1:
        raise _IndexError("estrutura_por_ano.prompts deve usar <ano> uma única vez.")
    operational = raw.get("fonte_operacional")
    source_template = (
        operational.get("caminho") if isinstance(operational, dict) else None
    )
    source_parts = _prompt_template_parts(
        source_template,
        "fonte_operacional.caminho",
        file_template=True,
    )
    if source_parts[-1] != "<arquivo>.md":
        raise _IndexError(
            "fonte_operacional.caminho deve terminar exatamente em <arquivo>.md."
        )
    if source_parts[: len(template_parts)] != template_parts:
        raise _IndexError(
            "fonte_operacional.caminho deve começar pelo template de "
            "estrutura_por_ano.prompts."
        )
    if len(source_parts) <= len(template_parts):
        raise _IndexError(
            "fonte_operacional.caminho deve declarar o arquivo abaixo da área de prompts."
        )
    if source_parts.count("<ano>") != 1:
        raise _IndexError("fonte_operacional.caminho deve usar <ano> uma única vez.")

    # O padrão operacional define os segmentos obrigatórios antes da folha.
    # Abaixo da folha materializada, subpastas editoriais continuam permitidas.
    directory_pattern = source_parts[:-1]
    planned_key_set = set(planned_keys)
    areas: list[_PromptAreaDefinition] = []
    for year in years:
        rendered_directory = tuple(
            ("autores", author)
            + tuple(year if part == "<ano>" else part for part in directory_pattern)
        )
        rendered_source = tuple(
            ("autores", author)
            + tuple(year if part == "<ano>" else part for part in source_parts)
        )
        areas.append(
            _PromptAreaDefinition(
                author,
                year,
                _portable_key(year) in planned_key_set,
                rendered_directory,
                rendered_source,
            )
        )
    return _PromptManifestContract(tuple(areas))


def _prompt_template_parts(
    value: object,
    label: str,
    *,
    file_template: bool = False,
) -> tuple[str, ...]:
    if not isinstance(value, str) or value != unicodedata.normalize("NFKC", value):
        raise _IndexError(f"{label} deve ser template canônico.")
    if (
        not value
        or value.startswith(("/", "~"))
        or "\\" in value
        or "\x00" in value
        or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", value)
    ):
        raise _IndexError(f"{label} deve ser caminho relativo portátil.")
    parts = tuple(value.split("/"))
    if any(part in {"", ".", ".."} for part in parts):
        raise _IndexError(f"{label} contém segmento inválido.")
    for position, part in enumerate(parts):
        if file_template and position == len(parts) - 1 and part == "<arquivo>.md":
            continue
        if re.fullmatch(r"<[a-z0-9]+(?:-[a-z0-9]+)*>", part):
            if part == "<arquivo>":
                raise _IndexError(f"{label} usa <arquivo> fora do nome final.")
            continue
        if not _valid_id(part):
            raise _IndexError(f"{label} contém segmento de template inválido.")
    return parts


def _is_placeholder(value: str) -> bool:
    return bool(re.fullmatch(r"<[a-z0-9]+(?:-[a-z0-9]+)*>", value))


def _prompt_placeholder_matches(placeholder: str, value: str) -> bool:
    if placeholder == "<ano-letivo>":
        return (
            _portable_component_error(value) is None
            and bool(ACADEMIC_YEAR_PATTERN.fullmatch(value))
        )
    return _valid_id(value)


def _prompt_file_matches(value: str) -> bool:
    return (
        Path(value).suffix == ".md"
        and _portable_component_error(value) is None
        and _valid_id(Path(value).stem)
    )


def _prompt_pattern_matches(
    pattern: tuple[str, ...],
    candidate: tuple[str, ...],
) -> bool:
    if len(candidate) <= len(pattern):
        return False
    for expected, actual in zip(pattern, candidate):
        if _is_placeholder(expected):
            if not _prompt_placeholder_matches(expected, actual):
                return False
        elif expected != actual:
            return False
    return _prompt_file_matches(candidate[-1])


def _walk_prompt_pattern(
    repo: SecureRepository,
    pattern: tuple[str, ...],
    author: str,
    renderer: str,
    snapshots: list[PromptSnapshot],
    reports: list[PromptDiscoveryReport],
) -> None:
    """Expande placeholders, exigindo cada segmento antes da travessia livre."""

    def expand(parts: tuple[str, ...], position: int) -> None:
        if position == len(pattern):
            _walk_prompt_tree(
                repo,
                parts,
                author,
                renderer,
                True,
                snapshots,
                reports,
            )
            return
        expected = pattern[position]
        if not _is_placeholder(expected):
            try:
                identity = repo.directory_identity(
                    (*parts, expected),
                    "/".join((*parts, expected)),
                    optional=True,
                )
            except _IndexError as exc:
                reports.append(
                    PromptDiscoveryReport(
                        str(repo.root.joinpath(*parts, expected)),
                        False,
                        str(exc),
                    )
                )
                return
            if identity is not None:
                expand((*parts, expected), position + 1)
            return
        try:
            entries = repo.entries(parts, "/".join(parts)) or []
        except _IndexError as exc:
            reports.append(
                PromptDiscoveryReport(str(repo.root.joinpath(*parts)), False, str(exc))
            )
            return
        for group in _group_entries(entries):
            paths = [repo.root.joinpath(*parts, item.name) for item in group]
            if len(group) != 1:
                for path in paths:
                    reports.append(
                        PromptDiscoveryReport(
                            str(path),
                            False,
                            "alias NFKC + casefold em placeholder de prompts",
                        )
                    )
                continue
            entry = group[0]
            if entry.is_symlink:
                reports.append(
                    PromptDiscoveryReport(
                        str(paths[0]), False, "link simbólico proibido em prompts"
                    )
                )
                continue
            if entry.is_dir and _prompt_placeholder_matches(expected, entry.name):
                expand((*parts, entry.name), position + 1)
            elif entry.is_dir or Path(entry.name).suffix.lower() in {".md", ".txt"}:
                reports.append(
                    PromptDiscoveryReport(
                        str(paths[0]),
                        False,
                        "entrada não satisfaz placeholder obrigatório do manifesto",
                    )
                )

    fixed_prefix: list[str] = []
    for part in pattern:
        if _is_placeholder(part):
            break
        fixed_prefix.append(part)
    try:
        fixed_identity = repo.directory_identity(
            tuple(fixed_prefix),
            "/".join(fixed_prefix),
            optional=True,
        )
    except _IndexError as exc:
        reports.append(
            PromptDiscoveryReport(
                str(repo.root.joinpath(*fixed_prefix)),
                False,
                str(exc),
            )
        )
        return
    if fixed_identity is None:
        return
    expand(tuple(fixed_prefix), len(fixed_prefix))


def _scan_prompt_decoys(
    repo: SecureRepository,
    parts: tuple[str, ...],
    allowed_patterns: tuple[tuple[str, ...], ...],
    reports: list[PromptDiscoveryReport],
    *,
    under_prompt_component: bool = False,
) -> None:
    """Inspeciona somente metadados e denuncia áreas de prompts não declaradas."""

    if any(
        not any(_is_placeholder(part) for part in pattern)
        and _contains(pattern, parts)
        for pattern in allowed_patterns
    ):
        # A travessia segura que materializa snapshots valida integralmente a
        # árvore autorizada; este scanner cuida apenas de árvores concorrentes.
        return

    try:
        entries = repo.entries(parts, "/".join(parts)) or []
    except _IndexError as exc:
        reports.append(
            PromptDiscoveryReport(str(repo.root.joinpath(*parts)), False, str(exc))
        )
        return
    for group in _group_entries(entries):
        paths = [repo.root.joinpath(*parts, entry.name) for entry in group]
        prompt_named = any(
            _portable_key(entry.name) == _portable_key("prompts") for entry in group
        )
        if len(group) != 1:
            for path in paths:
                reports.append(
                    PromptDiscoveryReport(
                        str(path),
                        False,
                        "alias NFKC + casefold na travessia do autor",
                    )
                )
            continue
        entry = group[0]
        child = (*parts, entry.name)
        child_under = under_prompt_component or prompt_named
        if entry.is_symlink:
            if child_under:
                reports.append(
                    PromptDiscoveryReport(
                        str(paths[0]),
                        False,
                        "link simbólico proibido em árvore de prompts",
                    )
                )
            continue
        if entry.is_dir:
            _scan_prompt_decoys(
                repo,
                child,
                allowed_patterns,
                reports,
                under_prompt_component=child_under,
            )
            continue
        if not child_under or Path(entry.name).suffix.lower() not in {".md", ".txt"}:
            continue
        if not any(_prompt_pattern_matches(pattern, child) for pattern in allowed_patterns):
            reports.append(
                PromptDiscoveryReport(
                    str(paths[0]),
                    False,
                    "prompt fora de raiz declarada pelo manifesto",
                )
            )


def discover_prompt_inventory(
    root: Path,
    *,
    require_author_profile: bool = True,
) -> tuple[
    list[PromptAreaContract],
    list[PromptSnapshot],
    list[PromptDiscoveryReport],
]:
    """Descobre áreas declaradas e lê prompts uma vez por descritor seguro."""

    snapshots: list[PromptSnapshot] = []
    reports: list[PromptDiscoveryReport] = []
    definitions: list[_PromptAreaDefinition] = []
    try:
        with SecureRepository(root) as repo:
            if not _fixed_directory_exists(repo, (), "autores", "autores/", optional=False):
                return [], [], reports
            authors = repo.entries(("autores",), "autores/") or []
            for group in _group_entries(authors):
                paths = [repo.root / "autores" / entry.name for entry in group]
                if len(group) != 1:
                    for path in paths:
                        reports.append(
                            PromptDiscoveryReport(str(path), False, "alias de autor")
                        )
                    continue
                entry = group[0]
                if entry.name.startswith("_") or entry.is_file:
                    continue
                if not _valid_id(entry.name) or not entry.is_dir:
                    reports.append(
                        PromptDiscoveryReport(str(paths[0]), False, "autor inválido")
                    )
                    continue
                try:
                    manifest = _prompt_manifest_contract(repo, entry.name)
                except _IndexError as exc:
                    reports.append(
                        PromptDiscoveryReport(
                            str(paths[0] / "manifesto.yaml"),
                            False,
                            str(exc),
                        )
                    )
                    continue
                patterns = manifest.patterns
                definitions.extend(manifest.areas)
                renderer = "texto"
                if require_author_profile:
                    try:
                        renderer = _prompt_renderer(repo, entry.name)
                    except _IndexError as exc:
                        reports.append(
                            PromptDiscoveryReport(
                                str(paths[0] / "autor.yaml"),
                                False,
                                str(exc),
                            )
                        )
                        continue
                _scan_prompt_decoys(
                    repo,
                    ("autores", entry.name),
                    patterns,
                    reports,
                )
                for pattern in patterns:
                    _walk_prompt_pattern(
                        repo,
                        pattern,
                        entry.name,
                        renderer,
                        snapshots,
                        reports,
                    )
    except _IndexError as exc:
        reports.append(PromptDiscoveryReport(str(_absolute_lexical(root)), False, str(exc)))

    sorted_snapshots = sorted(snapshots, key=lambda item: str(item.path))
    root_path = _absolute_lexical(root)
    areas: list[PromptAreaContract] = []
    for definition in definitions:
        members: list[str] = []
        for snapshot in sorted_snapshots:
            try:
                candidate = snapshot.path.relative_to(root_path).parts
            except ValueError:
                continue
            if _prompt_pattern_matches(definition.directory_pattern, candidate):
                members.append("/".join(candidate))
        areas.append(
            PromptAreaContract(
                definition.autor,
                definition.ano,
                definition.planejado,
                "/".join(definition.source_pattern),
                tuple(members),
            )
        )
    unique_reports = {
        (report.path, report.error): report
        for report in reports
    }
    return (
        sorted(areas, key=lambda item: (item.autor, item.ano)),
        sorted_snapshots,
        sorted(unique_reports.values(), key=lambda item: (item.path, item.error)),
    )


def discover_prompt_snapshots(
    root: Path,
    *,
    require_author_profile: bool = True,
) -> tuple[list[PromptSnapshot], list[PromptDiscoveryReport]]:
    """API compatível: retorna snapshots e relatórios do inventário canônico."""

    _areas, snapshots, reports = discover_prompt_inventory(
        root,
        require_author_profile=require_author_profile,
    )
    return snapshots, reports


def discover_render_resources(
    root: Path,
    renderers: set[str] | frozenset[str],
) -> tuple[dict[str, dict[str, str]], list[RenderResourceReport]]:
    """Obtém snapshots seguros dos recursos usados pelos renderizadores.

    As chaves do mapa interno são caminhos relativos a ``formatos/<renderer>``.
    Um renderizador só é publicado quando todo o seu conjunto obrigatório foi
    lido no mesmo contexto seguro.
    """

    resources: dict[str, dict[str, str]] = {}
    reports: list[RenderResourceReport] = []
    requested = sorted(set(renderers) - {"texto"})
    if any(renderer not in PROMPT_RENDERERS for renderer in requested):
        invalid = sorted(set(requested) - PROMPT_RENDERERS)
        return {}, [
            RenderResourceReport(
                str(_absolute_lexical(root) / "formatos" / renderer),
                renderer,
                False,
                "renderizador desconhecido",
            )
            for renderer in invalid
        ]
    if not requested:
        return {}, []
    try:
        with SecureRepository(root) as repo:
            if not _fixed_directory_exists(
                repo,
                (),
                "formatos",
                "formatos/",
                optional=False,
            ):
                return {}, []
            format_entries = repo.entries(("formatos",), "formatos/") or []
            for renderer in requested:
                matches = [
                    entry
                    for entry in format_entries
                    if _portable_key(entry.name) == _portable_key(renderer)
                ]
                base = repo.root / "formatos" / renderer
                if len(matches) != 1 or matches[0].name != renderer:
                    reports.append(
                        RenderResourceReport(
                            str(base),
                            renderer,
                            False,
                            "pasta do renderizador ausente ou ambígua por NFKC + casefold",
                        )
                    )
                    continue
                if matches[0].is_symlink or not matches[0].is_dir:
                    reports.append(
                        RenderResourceReport(
                            str(base),
                            renderer,
                            False,
                            "pasta do renderizador deve ser diretório real sem link simbólico",
                        )
                    )
                    continue
                required = [
                    "adaptacoes-disciplina.yaml",
                    "adaptacoes-serie.yaml",
                ]
                if renderer == "colagem-editorial":
                    required.extend(("MASTER-CAPA.md", "MASTER-CONTEUDO.md"))
                else:
                    required.append("MASTER-PROMPT.md")
                renderer_texts: dict[str, str] = {}
                renderer_errors: list[RenderResourceReport] = []
                try:
                    entries = repo.entries(
                        ("formatos", renderer),
                        f"formatos/{renderer}",
                    ) or []
                    for name in required:
                        aliases = [
                            entry
                            for entry in entries
                            if _portable_key(entry.name) == _portable_key(name)
                        ]
                        path = base / name
                        if len(aliases) != 1 or aliases[0].name != name:
                            raise _IndexError(
                                f"{name} ausente ou ambíguo por NFKC + casefold"
                            )
                        if aliases[0].is_symlink or not aliases[0].is_file:
                            raise _IndexError(f"{name} não pode ser link simbólico")
                        snapshot = repo.read_file(
                            ("formatos", renderer, name),
                            f"recurso de renderização {renderer}/{name}",
                            max_bytes=MAX_PROJECT_BYTES,
                        )
                        text = snapshot.data.decode("utf-8")
                        if name.endswith(".yaml"):
                            value = _yaml_from_bytes(
                                snapshot.data,
                                f"recurso de renderização {renderer}/{name}",
                            )
                            if not isinstance(value, dict):
                                raise _IndexError(f"{name} deve conter objeto YAML")
                        renderer_texts[name] = text
                except (UnicodeError, _IndexError) as exc:
                    renderer_errors.append(
                        RenderResourceReport(
                            str(base),
                            renderer,
                            False,
                            str(exc),
                        )
                    )
                if renderer_errors:
                    reports.extend(renderer_errors)
                else:
                    resources[renderer] = renderer_texts
    except _IndexError as exc:
        reports.append(
            RenderResourceReport(
                str(_absolute_lexical(root) / "formatos"),
                "*",
                False,
                str(exc),
            )
        )
    return resources, sorted(reports, key=lambda item: (item.renderer, item.path))


def discover_operational_yaml_snapshots(
    root: Path,
    additional_paths: list[Path] | tuple[Path, ...] = (),
) -> tuple[list[YamlSnapshot], list[YamlDiscoveryReport]]:
    """Descobre e lê YAMLs operacionais por descritor, sem reabrir ``Path``."""

    snapshots: dict[str, YamlSnapshot] = {}
    reports: list[YamlDiscoveryReport] = []

    def report(path: Path, error: str) -> None:
        reports.append(YamlDiscoveryReport(str(path), False, error))

    def read(repo: SecureRepository, parts: tuple[str, ...], label: str) -> None:
        key = "/".join(parts)
        if key in snapshots:
            return
        try:
            file = repo.read_file(parts, label, max_bytes=MAX_PROJECT_BYTES)
            text = file.data.decode("utf-8")
        except (UnicodeError, _IndexError) as exc:
            report(repo.root.joinpath(*parts), str(exc))
            return
        snapshots[key] = YamlSnapshot(file.path, text)

    def direct_yaml_files(
        repo: SecureRepository,
        parent: tuple[str, ...],
        label: str,
        *,
        matcher: Any,
        canonical: Any,
    ) -> None:
        try:
            entries = repo.entries(parent, label) or []
        except _IndexError as exc:
            report(repo.root.joinpath(*parent), str(exc))
            return
        for group in _group_entries(entries):
            paths = [repo.root.joinpath(*parent, item.name) for item in group]
            selected = [item for item in group if matcher(item.name)]
            if not selected:
                continue
            if len(group) != 1:
                for path in paths:
                    report(path, "alias NFKC + casefold em YAML operacional")
                continue
            entry = group[0]
            if not canonical(entry.name):
                report(paths[0], "nome de YAML operacional não canônico")
                continue
            if entry.is_symlink:
                report(paths[0], "YAML operacional não pode ser link simbólico")
                continue
            if not entry.is_file:
                report(paths[0], "YAML operacional deve ser arquivo regular")
                continue
            read(repo, (*parent, entry.name), label)

    def child_directories(
        repo: SecureRepository,
        collection: str,
    ) -> list[str]:
        try:
            if not _fixed_directory_exists(
                repo,
                (),
                collection,
                f"{collection}/",
                optional=True,
            ):
                return []
            entries = repo.entries((collection,), f"{collection}/") or []
        except _IndexError as exc:
            report(repo.root / collection, str(exc))
            return []
        children: list[str] = []
        for group in _group_entries(entries):
            directory_items = [item for item in group if item.is_dir or item.is_symlink]
            if not directory_items:
                continue
            paths = [repo.root / collection / item.name for item in group]
            if len(group) != 1:
                for path in paths:
                    report(path, f"alias NFKC + casefold em {collection}/")
                continue
            entry = group[0]
            if entry.is_symlink:
                report(paths[0], f"pasta em {collection}/ não pode ser link simbólico")
                continue
            if entry.is_dir:
                if entry.name != "_modelo" and not _valid_id(entry.name):
                    report(paths[0], f"identificador inválido em {collection}/")
                    continue
                children.append(entry.name)
        return children

    try:
        with SecureRepository(root) as repo:
            for collection in ("modelos", "compartilhado"):
                try:
                    if not _fixed_directory_exists(
                        repo,
                        (),
                        collection,
                        f"{collection}/",
                        optional=True,
                    ):
                        continue
                except _IndexError as exc:
                    report(repo.root / collection, str(exc))
                    continue
                direct_yaml_files(
                    repo,
                    (collection,),
                    f"YAML em {collection}/",
                    matcher=lambda name: _portable_key(name).endswith(".yaml"),
                    canonical=lambda name: name.endswith(".yaml")
                    and _portable_component_error(name) is None,
                )

            for author in child_directories(repo, "autores"):
                direct_yaml_files(
                    repo,
                    ("autores", author),
                    f"YAML do autor {author}",
                    matcher=lambda name: _portable_key(name)
                    in {"autor.yaml", "adaptacoes.yaml", "manifesto.yaml"},
                    canonical=lambda name: name
                    in {"autor.yaml", "adaptacoes.yaml", "manifesto.yaml"},
                )

            for renderer in child_directories(repo, "formatos"):
                direct_yaml_files(
                    repo,
                    ("formatos", renderer),
                    f"YAML do formato {renderer}",
                    matcher=lambda name: _portable_key(name) == "formato.yaml"
                    or (
                        _portable_key(name).startswith("adaptacoes-")
                        and _portable_key(name).endswith(".yaml")
                    ),
                    canonical=lambda name: name == "formato.yaml"
                    or (
                        name.startswith("adaptacoes-")
                        and name.endswith(".yaml")
                        and _portable_component_error(name) is None
                    ),
                )

            for path in additional_paths:
                lexical = _absolute_lexical(path)
                try:
                    relative = lexical.relative_to(repo.root)
                    parts = _relative_parts(
                        relative.as_posix(),
                        label="YAML operacional adicional",
                    )
                except (ValueError, _IndexError) as exc:
                    report(lexical, f"YAML operacional adicional externo/inválido: {exc}")
                    continue
                if Path(parts[-1]).suffix.lower() not in {".yaml", ".yml"}:
                    report(lexical, "YAML operacional adicional deve usar .yaml ou .yml")
                    continue
                read(repo, parts, "YAML operacional adicional")
    except _IndexError as exc:
        report(_absolute_lexical(root), str(exc))
    return (
        sorted(snapshots.values(), key=lambda item: str(item.path)),
        sorted(reports, key=lambda item: item.path),
    )


IMAGE_SUFFIXES = frozenset(
    {".avif", ".gif", ".jpeg", ".jpg", ".png", ".tif", ".tiff", ".webp"}
)


def discover_image_snapshots(
    root: Path,
    *,
    ignored_top_level: frozenset[str] = frozenset(),
) -> tuple[list[ImageSnapshot], list[ImageDiscoveryReport]]:
    """Descobre imagens sem seguir links e conserva os bytes validados."""

    snapshots: list[ImageSnapshot] = []
    reports: list[ImageDiscoveryReport] = []

    def walk(repo: SecureRepository, parts: tuple[str, ...]) -> None:
        try:
            entries = repo.entries(parts, "/".join(parts) or ".") or []
        except _IndexError as exc:
            reports.append(
                ImageDiscoveryReport(str(repo.root.joinpath(*parts)), False, str(exc))
            )
            return
        for group in _group_entries(entries):
            if (
                not parts
                and len(group) == 1
                and group[0].name in ignored_top_level
            ):
                continue
            relevant = [
                item
                for item in group
                if item.is_dir
                or item.is_symlink
                or Path(item.name).suffix.lower() in IMAGE_SUFFIXES
            ]
            if not relevant:
                continue
            paths = [repo.root.joinpath(*parts, item.name) for item in group]
            if len(group) != 1:
                for path in paths:
                    reports.append(
                        ImageDiscoveryReport(
                            str(path),
                            False,
                            "alias NFKC + casefold na descoberta de imagens",
                        )
                    )
                continue
            entry = group[0]
            path = paths[0]
            if entry.is_symlink:
                reports.append(
                    ImageDiscoveryReport(str(path), False, "link simbólico proibido")
                )
                continue
            child = (*parts, entry.name)
            if entry.is_dir:
                walk(repo, child)
                continue
            if Path(entry.name).suffix.lower() not in IMAGE_SUFFIXES:
                continue
            try:
                file = repo.read_file(
                    child,
                    f"imagem {entry.name!r}",
                    max_bytes=MAX_IMAGE_BYTES,
                )
            except _IndexError as exc:
                reports.append(ImageDiscoveryReport(str(path), False, str(exc)))
                continue
            snapshots.append(ImageSnapshot(path, file.data))

    try:
        with SecureRepository(root) as repo:
            walk(repo, ())
    except _IndexError as exc:
        reports.append(
            ImageDiscoveryReport(str(_absolute_lexical(root)), False, str(exc))
        )
    return (
        sorted(snapshots, key=lambda item: str(item.path)),
        sorted(reports, key=lambda item: item.path),
    )
