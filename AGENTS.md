# AGENTS.md — Autores · Fundamental I

## Escopo

Este é o repositório autônomo de autores definitivos do Fundamental I, com dois
perfis autorais:

- `autor-fund1`: imagens pedagógicas de Inglês do Fundamental I;
- `autor-mat3`: imagens pedagógicas de Matemática do 3º ano do Fundamental I.

Provedores de imagem autorizados:

- OpenAI Images API com `gpt-image-2`;
- xAI Images API com `grok-imagine-image-2.0`.

Não introduza outros autores, disciplinas, modelos ou provedores sem
autorização explícita. Cada projeto precisa declarar o provedor e o modelo;
nunca troque um pelo outro silenciosamente.

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
- Preserve os autores `autor-fund1` e `autor-mat3`.
- Preserve o formato `apostila-fund1`.
- Preserve a linguagem visual de colagem, sketchnote e visual note-taking.
- Não misture conteúdos, fontes, prompts ou saídas entre os autores.
- Não altere prompts aprovados durante mudanças puramente técnicas.
- Não invente estatísticas, fontes, traduções, definições, propriedades ou fatos.
- Inglês exige conferência literal de palavras, frases e traduções.
- Matemática exige conferência de números, sinais, cálculos e classificações.
- Dados factuais e citações exigem revisão humana.

## Fluxo

1. selecionar autor, fonte, conteúdo e prompt versionado;
2. declarar ou revisar o projeto YAML do autor correto;
3. executar `--dry-run`;
4. gerar na área externa `_revisao` do respectivo autor;
5. conferir imagem, metadados, conteúdo, cálculos e OCR;
6. promover com `aprovar.py` somente após revisão humana;
7. manter versões anteriores; sobrescrever apenas com autorização e `--forcar`.

## Código e segurança

- Python mínimo: 3.10.
- Dependências diretas ficam fixadas em `pyproject.toml` e `uv.lock`.
- Nunca exponha ou registre `OPENAI_API_KEY` ou `XAI_API_KEY`.
- Credenciais locais ficam separadas em `.env.openai.local` e `.env.grok.local`.
- O adaptador xAI só pode usar projetos com `provider: xai`, formato JPEG,
  proporção e resolução explícitas.
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
  --projeto autores/autor-fund1/projetos/2026/3-bimestre/unidade-03-bloco-01-autonomia-guiada-4paginas-v5.yaml \
  --dry-run
uv run gerar.py \
  --projeto autores/autor-mat3/projetos/2026/3-bimestre/unidades-05-06-6paginas-v1.yaml \
  --dry-run
uv run validar.py --acervo
```

`--check-auth` acessa a API, mas não gera imagens. Use-o somente quando houver
necessidade explícita de verificar a credencial e o acesso ao modelo.
