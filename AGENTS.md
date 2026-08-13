# AGENTS.md — Autor-teste de Inglês · Fundamental I

## Escopo

Este é um repositório autônomo e exclusivo do autor `autor-teste-fund1`, para
imagens pedagógicas de Inglês do Fundamental I. Use somente a OpenAI Images API
com `gpt-image-2`. Não introduza outros autores, disciplinas ou provedores.

Não dependa de código, prompts, configurações ou credenciais fora desta pasta.

## Armazenamento

O repositório não pode conter imagens geradas, imagens de referência, PDFs de
produção ou prévias.

- Código, fontes, conteúdos, prompts, formatos, projetos e registros textuais
  ficam no repositório.
- Toda saída vai para a raiz externa configurada.
- Caminhos relativos geram primeiro em `_revisao`.
- Promoção para `aprovadas` exige revisão humana.
- Nunca crie uma saída local de contingência.

## Conteúdo e identidade

- Responda e documente em português brasileiro.
- Preserve o autor `autor-teste-fund1` e o formato `apostila-fund1`.
- Preserve a linguagem visual de colagem, sketchnote e visual note-taking.
- Não altere prompts aprovados durante mudanças puramente técnicas.
- Não invente estatísticas, fontes, traduções ou fatos.
- Dados factuais e citações exigem revisão humana.

## Fluxo

1. selecionar fonte, conteúdo e prompt versionado;
2. declarar ou revisar o projeto YAML;
3. executar `--dry-run`;
4. gerar na área externa `_revisao`;
5. conferir imagem, metadados, conteúdo e OCR;
6. promover com `aprovar.py` somente após revisão humana;
7. manter versões anteriores; sobrescrever apenas com autorização e `--forcar`.

## Código e segurança

- Python mínimo: 3.10.
- Dependências diretas ficam fixadas em `pyproject.toml` e `uv.lock`.
- Nunca exponha ou registre `OPENAI_API_KEY`.
- Testes e dry-runs não podem chamar a API nem consumir créditos.
- Valide bytes, formato e dimensões antes de salvar.
- Preserve gravação atômica e proteção contra sobrescrita.
- Novas funcionalidades exigem testes sem chamadas reais à API.

## Verificação

```bash
uv sync --locked
uv run python -m unittest discover -s tests -v
uv run gerar.py --help
uv run gerar.py --listar-autores
uv run gerar.py \
  --projeto autores/autor-teste-fund1/projetos/2026/3-bimestre/unidade-03-bloco-01-autonomia-guiada-4paginas-v5.yaml \
  --dry-run
uv run validar.py --acervo
```

`--check-auth` acessa a API, mas não gera imagens. Use-o somente quando houver
necessidade explícita de verificar a credencial e o acesso ao modelo.
