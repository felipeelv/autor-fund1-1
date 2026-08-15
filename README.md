# Autores — Fundamental I

Repositório autônomo que reúne autores pedagógicos definitivos do Fundamental I
com OpenAI Images API (`gpt-image-2`), xAI Images API
(`grok-imagine-image-2.0`), OpenRouter Image API (`qwen/qwen-image-3-pro`) e
o formato visual `apostila-fund1`.

Autores disponíveis:

- `autor-fund1`: Inglês do Fundamental I;
- `autor-mat3`: Matemática do 3º ano do Fundamental I;
- `autor-nat3`: Natureza e Sociedade do 3º ano do Fundamental I.

Cada autor mantém fontes, direção, conteúdos, prompts, projetos e registros em
sua própria pasta. O núcleo Python, o formato e as regras comuns são
compartilhados. Imagens, PDFs, prévias, credenciais e ambientes virtuais não
fazem parte do acervo versionado.

## Estrutura

```text
autor-fund1-1/
├── autores/
│   ├── autor-fund1/      # Inglês · Fundamental I
│   ├── autor-mat3/       # Matemática · 3º ano
│   └── autor-nat3/       # Natureza e Sociedade · 3º ano
├── compartilhado/              # regras editoriais e parâmetros comuns
├── formatos/apostila-fund1/    # formato autorizado pelos três autores
├── gerador_imagens/             # núcleo Python
├── modelos/                     # modelos de prompt e projeto
├── tests/                       # testes sem chamadas à API
├── gerar.py                     # geração e dry-run
├── validar.py                   # auditoria local
└── aprovar.py                   # promoção para aprovadas
```

## Requisitos e configuração

- Python 3.10 ou superior;
- `uv`;
- chave do provedor que será usado: OpenAI com acesso a `gpt-image-2`, xAI
  com acesso a `grok-imagine-image-2.0` e/ou OpenRouter com acesso a
  `qwen/qwen-image-3-pro`;
- pasta de saída fora deste repositório.

```bash
cd /Users/feliperosa/Documents/Codex/autor-fund1-1
uv sync --locked
cp .env.example .env
cp config.example.yaml config.local.yaml
```

Informe as chaves em um único `.env` e configure uma raiz externa em
`config.local.yaml`. Os dois arquivos são ignorados pelo Git.

Projetos OpenAI usam `OPENAI_API_KEY`. Projetos xAI usam `XAI_API_KEY`.
Projetos OpenRouter usam `OPENROUTER_API_KEY`. O provedor é declarado em
cada projeto e nenhuma credencial altera silenciosamente o modelo
selecionado. Arquivos separados (`.env.openai.local` e `.env.grok.local`)
ainda são lidos se existirem.

## Verificação sem consumo de créditos

```bash
uv run python -m unittest discover -s tests -v
uv run gerar.py --help
uv run gerar.py --listar-autores
uv run validar.py --acervo
```

Dry-run de Inglês:

```bash
uv run gerar.py \
  --projeto autores/autor-fund1/projetos/2026/3-bimestre/unidade-03-bloco-01-autonomia-guiada-4paginas-v5.yaml \
  --dry-run
```

Dry-run de Matemática:

```bash
uv run gerar.py \
  --projeto autores/autor-mat3/projetos/2026/3-bimestre/unidades-05-06-6paginas-v1.yaml \
  --dry-run
```

Dry-run de Natureza e Sociedade:

```bash
uv run gerar.py \
  --projeto autores/autor-nat3/projetos/2026/3-bimestre/povos-indigenas-6paginas-v1.yaml \
  --dry-run
```

Dry-run da amostra de Matemática com Grok Imagine 2:

```bash
uv run gerar.py \
  --projeto autores/autor-mat3/projetos/2026/3-bimestre/unidades-05-06-p01-amostra-grok-v1.yaml \
  --dry-run
```

## Lote de Matemática com seis páginas

O lote inicial de Matemática usa a fonte interna integral do 3º bimestre e
cria seis páginas sobre:

1. divisão com resto;
2. verificação e interpretação do resto;
3. quatro operações;
4. sólidos geométricos;
5. planificação 3D e 2D;
6. polígonos e quadriláteros.

Projeto:
`autores/autor-mat3/projetos/2026/3-bimestre/unidades-05-06-6paginas-v1.yaml`.

## Lote de Natureza e Sociedade com seis páginas

O lote inicial trabalha povos indígenas no passado e no presente: anterioridade
histórica, registros do interior paulista, modos de aprender, cuidado com os
territórios, diversidade e direitos. Dados e afirmações históricas permanecem
condicionados à revisão humana.

Projeto:
`autores/autor-nat3/projetos/2026/3-bimestre/povos-indigenas-6paginas-v1.yaml`.

## Fluxo editorial

1. selecionar o autor correto;
2. revisar fonte, conteúdo e prompt versionado;
3. declarar o lote em um projeto YAML;
4. executar `--dry-run`;
5. gerar na área externa `_revisao/<autor>/...`;
6. conferir texto, símbolos, correspondências visuais, metadados e OCR;
7. promover somente após revisão humana.

O gerador protege arquivos existentes. `--forcar` só deve ser usado com
autorização explícita e depois de confirmar o destino exato.
