from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path
from typing import Any

import openai

from gerador_imagens.authors import aplicar_autor, listar_autores, load_author
from gerador_imagens.config import (
    PRESETS,
    ConfigError,
    GenerationOptions,
    normalize_output_path,
    options_from_mapping,
)
from gerador_imagens.core import (
    GenerationError,
    build_client,
    check_authentication,
    create_pdf,
    generate_image,
    load_api_key,
    load_prompt,
)
from gerador_imagens.projects import ProjectPlan, load_project
from gerador_imagens.quality import analyze_prompt
from gerador_imagens.renderers import RENDERERS, render_prompt
from gerador_imagens.storage import load_storage, resolve_external_output


ROOT = Path(__file__).resolve().parent
DEFAULT_PROMPT = ROOT / "modelos" / "prompt.txt"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Gerador autônomo de imagens pedagógicas com GPT Image 2.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "texto",
        nargs="?",
        default=None,
        help="Prompt inline. Se omitido, usa --prompt ou modelos/prompt.txt.",
    )
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--prompt", help="Arquivo de prompt em UTF-8.")
    source.add_argument("--projeto", help="Projeto YAML com uma ou mais imagens.")

    parser.add_argument("--saida", help="Arquivo de saída para geração direta.")
    parser.add_argument(
        "--saida-root",
        help="Sobrescreve a raiz externa configurada para esta execução.",
    )
    parser.add_argument(
        "--area",
        choices=("revisao", "aprovadas", "historico"),
        default="revisao",
        help="Área externa usada para caminhos de saída relativos.",
    )
    parser.add_argument("--autor", help="ID de um perfil em autores/<id>/autor.yaml.")
    parser.add_argument(
        "--provider",
        choices=("openai", "xai"),
        default="openai",
        help="Provedor da Images API para geração direta ou check-auth.",
    )
    parser.add_argument(
        "--renderizador",
        choices=sorted(RENDERERS),
        help="Converte frontmatter estruturado usando um formato compartilhado.",
    )
    parser.add_argument("--modelo", help="Modelo da Images API.")
    parser.add_argument("--preset", choices=sorted(PRESETS), help="Preset de dimensões.")
    parser.add_argument("--tamanho", help="Dimensões WIDTHxHEIGHT ou auto.")
    parser.add_argument(
        "--qualidade",
        choices=("auto", "low", "medium", "high"),
        help="Qualidade de renderização.",
    )
    parser.add_argument(
        "--formato",
        choices=("png", "jpeg", "jpg", "webp"),
        help="Formato do arquivo devolvido pela API.",
    )
    parser.add_argument(
        "--compressao",
        type=int,
        help="Compressão de 0 a 100; válida apenas para JPEG e WebP.",
    )
    parser.add_argument(
        "--fundo",
        choices=("auto", "opaque"),
        help="Fundo automático ou opaco. GPT Image 2 não aceita transparente.",
    )
    parser.add_argument(
        "--moderacao",
        choices=("auto", "low"),
        help="Nível de moderação da Images API.",
    )
    parser.add_argument(
        "--quantidade",
        type=int,
        help="Quantidade de imagens na mesma requisição (1 a 10).",
    )
    parser.add_argument(
        "--stream",
        action="store_true",
        help="Recebe e salva imagens parciais durante a geração.",
    )
    parser.add_argument(
        "--parciais",
        type=int,
        help="Número de imagens parciais no streaming (0 a 3).",
    )
    parser.add_argument("--timeout", type=float, help="Timeout total da requisição, em segundos.")
    parser.add_argument(
        "--retries",
        type=int,
        help="Retries do SDK para falhas transitórias, como 429 e 5xx.",
    )
    parser.add_argument(
        "--forcar",
        action="store_true",
        help="Permite substituir arquivos existentes.",
    )
    parser.add_argument(
        "--sem-metadados",
        action="store_true",
        help="Não cria o arquivo .metadata.json ao lado da imagem.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Valida e mostra o plano sem chamar a API.",
    )
    parser.add_argument(
        "--somente-pdf",
        action="store_true",
        help="Em um projeto YAML, monta o PDF usando imagens já existentes.",
    )
    parser.add_argument(
        "--check-auth",
        action="store_true",
        help="Valida a chave e o acesso ao modelo sem gerar imagem.",
    )
    parser.add_argument(
        "--listar-autores",
        action="store_true",
        help="Lista os perfis de autores disponíveis.",
    )
    return parser


def cli_overrides(args: argparse.Namespace) -> dict[str, Any]:
    if args.preset and args.tamanho:
        raise ConfigError("Use apenas --preset ou --tamanho, não os dois.")
    size = PRESETS[args.preset] if args.preset else args.tamanho
    values: dict[str, Any] = {
        "model": args.modelo,
        "size": size,
        "quality": args.qualidade,
        "output_format": args.formato,
        "output_compression": args.compressao,
        "background": args.fundo,
        "moderation": args.moderacao,
        "n": args.quantidade,
        "partial_images": args.parciais,
        "timeout": args.timeout,
        "max_retries": args.retries,
    }
    if args.stream:
        values["stream"] = True
    if args.sem_metadados:
        values["write_metadata"] = False
    return {key: value for key, value in values.items() if value is not None}


def print_prompt_findings(prompt: str, label: str) -> None:
    findings = analyze_prompt(prompt)
    for finding in findings:
        if finding.severity in {"warning", "error"}:
            print(
                f"[{finding.severity.upper()}] {label}: {finding.message}",
                file=sys.stderr,
            )


def describe_task(
    prompt: str,
    output: Path,
    options: GenerationOptions,
    author_id: str | None,
    provider: str = "openai",
) -> None:
    digest = hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:12]
    print(
        "Plano:",
        f"provider={provider}",
        f"modelo={options.model}",
        f"tamanho={options.size}",
        f"qualidade={options.quality}",
        f"formato={options.output_format}",
        f"quantidade={options.n}",
        f"stream={options.stream}",
        f"autor={author_id or '-'}",
        f"prompt_sha256={digest}",
        f"saída={output}",
        sep="\n  ",
    )


def direct_options(args: argparse.Namespace) -> GenerationOptions:
    return options_from_mapping(cli_overrides(args))


def load_direct_prompt(args: argparse.Namespace) -> tuple[str, Path | None]:
    if args.texto is not None:
        prompt = args.texto.strip()
        if not prompt:
            raise ConfigError("O prompt inline está vazio.")
        return prompt, None
    prompt_path = Path(args.prompt).expanduser() if args.prompt else DEFAULT_PROMPT
    if not prompt_path.is_absolute():
        prompt_path = ROOT / prompt_path
    return load_prompt(prompt_path), prompt_path.resolve()


def generate_direct(args: argparse.Namespace) -> int:
    prompt, prompt_source = load_direct_prompt(args)
    profile = load_author(ROOT, args.autor) if args.autor else None
    renderer = args.renderizador or (
        profile.default_renderer if profile and prompt_source else "texto"
    )
    if prompt_source:
        prompt = render_prompt(ROOT, prompt_source, renderer)
    elif renderer != "texto":
        raise ConfigError(
            "Renderizadores estruturados exigem um arquivo informado por --prompt."
        )
    prompt, author = aplicar_autor(ROOT, args.autor, prompt)
    base_options = (
        options_from_mapping(author.parameters)
        if author and author.parameters
        else GenerationOptions()
    )
    options = options_from_mapping(cli_overrides(args), base_options)
    storage = load_storage(ROOT, args.saida_root)
    output = resolve_external_output(
        storage,
        args.saida or "imagem",
        args.area,
    )
    output = normalize_output_path(output, options.output_format)

    print_prompt_findings(prompt, str(prompt_source or "prompt inline"))
    if args.dry_run:
        describe_task(
            prompt,
            output,
            options,
            author.id if author else None,
            args.provider,
        )
        return 0

    api_key = load_api_key(ROOT, args.provider)
    client = build_client(api_key, options, args.provider)
    result = generate_image(
        client=client,
        prompt=prompt,
        output=output,
        options=options,
        overwrite=args.forcar,
        prompt_source=prompt_source,
        author_id=author.id if author else None,
        provider=args.provider,
    )
    for path in result.output_paths:
        print(f"Imagem salva em: {path}")
    for path in result.partial_paths:
        print(f"Prévia parcial salva em: {path}")
    if result.request_id:
        print(f"Request ID: {result.request_id}")
    return 0


def existing_project_images(plan: ProjectPlan) -> list[Path]:
    paths: list[Path] = []
    for task in plan.tasks:
        path = normalize_output_path(task.output_path, task.options.output_format)
        if task.options.n == 1:
            candidates = [path]
        else:
            candidates = [
                path.with_name(f"{path.stem}-{index:02d}{path.suffix}")
                for index in range(1, task.options.n + 1)
            ]
        missing = [candidate for candidate in candidates if not candidate.exists()]
        if missing:
            raise ConfigError(
                "Não foi possível montar o PDF; arquivos ausentes: "
                + ", ".join(str(item) for item in missing)
            )
        paths.extend(candidates)
    return paths


def generate_project(args: argparse.Namespace) -> int:
    project_path = Path(args.projeto).expanduser()
    if not project_path.is_absolute():
        project_path = ROOT / project_path
    storage = load_storage(ROOT, args.saida_root)
    plan = load_project(
        ROOT,
        project_path,
        storage,
        cli_overrides(args),
        args.autor,
    )

    if args.somente_pdf:
        if not plan.pdf_path:
            raise ConfigError("O projeto não está configurado para gerar PDF.")
        images = existing_project_images(plan)
        create_pdf(images, plan.pdf_path, overwrite=args.forcar, dpi=plan.pdf_dpi)
        print(f"PDF salvo em: {plan.pdf_path}")
        return 0

    prepared: list[tuple[Any, str, Any]] = []
    for task in plan.tasks:
        profile = load_author(ROOT, task.author_id) if task.author_id else None
        renderer = args.renderizador or (
            profile.default_renderer if profile else "texto"
        )
        prompt = render_prompt(ROOT, task.prompt_path, renderer)
        prompt, author = aplicar_autor(ROOT, task.author_id, prompt)
        print_prompt_findings(prompt, str(task.prompt_path))
        prepared.append((task, prompt, author))

    if args.dry_run:
        print(f"Projeto: {plan.title} ({len(prepared)} tarefa(s))")
        for task, prompt, author in prepared:
            describe_task(
                prompt,
                task.output_path,
                task.options,
                author.id if author else None,
                task.provider,
            )
        if plan.pdf_path:
            print(f"PDF planejado: {plan.pdf_path}")
        return 0

    all_outputs: list[Path] = []
    clients: dict[tuple[str, float, int], Any] = {}
    for task, prompt, author in prepared:
        key = (task.provider, task.options.timeout, task.options.max_retries)
        client = clients.get(key)
        if client is None:
            api_key = load_api_key(ROOT, task.provider)
            client = build_client(api_key, task.options, task.provider)
            clients[key] = client
        result = generate_image(
            client=client,
            prompt=prompt,
            output=task.output_path,
            options=task.options,
            overwrite=args.forcar,
            prompt_source=task.prompt_path,
            author_id=author.id if author else None,
            project_source=plan.source,
            provider=task.provider,
        )
        all_outputs.extend(result.output_paths)
        for path in result.output_paths:
            print(f"Imagem salva em: {path}")
        for path in result.partial_paths:
            print(f"Prévia parcial salva em: {path}")

    if plan.pdf_path:
        create_pdf(all_outputs, plan.pdf_path, overwrite=args.forcar, dpi=plan.pdf_dpi)
        print(f"PDF salvo em: {plan.pdf_path}")
    return 0


def run(args: argparse.Namespace) -> int:
    if args.texto is not None and (args.prompt or args.projeto):
        raise ConfigError(
            "Não combine prompt inline com --prompt ou --projeto."
        )
    if args.listar_autores:
        authors = listar_autores(ROOT)
        if not authors:
            print("Nenhum autor ativo cadastrado.")
        for author in authors:
            print(f"{author.id}: {author.name} ({author.discipline or 'geral'})")
        return 0

    if args.check_auth:
        options = direct_options(args)
        api_key = load_api_key(ROOT, args.provider)
        client = build_client(api_key, options, args.provider)
        model_id = check_authentication(client, options.model)
        print(f"Autenticação e modelo: OK ({model_id})")
        return 0

    if args.projeto:
        return generate_project(args)
    if args.somente_pdf:
        raise ConfigError("--somente-pdf exige --projeto.")
    return generate_direct(args)


def print_api_error(exc: openai.OpenAIError) -> None:
    status = getattr(exc, "status_code", None)
    code = getattr(exc, "code", None)
    request_id = getattr(exc, "request_id", None)
    body = getattr(exc, "body", None)
    details = body.get("moderation_details") if isinstance(body, dict) else None
    parts = [f"Erro da API de imagens: {type(exc).__name__}"]
    if status is not None:
        parts.append(f"status={status}")
    if code:
        parts.append(f"código={code}")
    if request_id:
        parts.append(f"request_id={request_id}")
    print("; ".join(parts), file=sys.stderr)
    if code == "moderation_blocked":
        print(
            "A solicitação foi bloqueada pela moderação. Revise o prompt ou as imagens de entrada.",
            file=sys.stderr,
        )
        if details:
            print(f"Detalhes de moderação: {details}", file=sys.stderr)


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return run(args)
    except (ConfigError, GenerationError) as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 2
    except openai.OpenAIError as exc:
        print_api_error(exc)
        return 1
    except KeyboardInterrupt:
        print("Operação interrompida.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
