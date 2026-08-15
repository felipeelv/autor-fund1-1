# Gerador de imagens — anos iniciais

Repositório autônomo de imagens pedagógicas dos anos iniciais do Colégio Eleve,
da Educação Infantil 4 e 5 ao 3º ano do Ensino Fundamental.

Modelo padrão: xAI Images API com `grok-imagine-image-2.0`. OpenAI Images API
com `gpt-image-2` continua autorizada e é declarada projeto a projeto. Formato
visual: `apostila-fund1`.

Autores ativos:

| ID | Disciplina | Anos | Estado |
|---|---|---|---|
| `ingles` | Inglês | 1º e 3º ano | em produção |
| `matematica` | Matemática | 3º ano | em produção |
| `natureza-e-sociedade` | Natureza e Sociedade | 3º ano | estrutura pronta, aguardando fonte |

Cada autor mantém fontes, direção, conteúdos, prompts, projetos e registros na
própria pasta. O núcleo Python, o formato e as regras comuns são compartilhados.
Imagem, PDF, prévia, credencial e ambiente virtual não fazem parte do acervo
versionado.

As regras completas estão em [CLAUDE.md](CLAUDE.md) — fonte única, sem
`AGENTS.md`.

## Estrutura

```text
.
├── CLAUDE.md                   # regras do repositório (fonte única)
├── autores/
│   ├── _modelo/                # template para autor novo
│   ├── ingles/                 # Inglês · 1º e 3º ano
│   ├── matematica/             # Matemática · 3º ano
│   └── natureza-e-sociedade/   # Natureza e Sociedade · 3º ano
├── compartilhado/              # regras editoriais e parâmetros comuns
├── formatos/apostila-fund1/    # formato autorizado pelos três autores
├── gerador_imagens/            # núcleo Python
├── modelos/                    # modelos de prompt e projeto
├── tests/                      # testes sem chamadas à API
├── gerar.py                    # geração e dry-run
├── validar.py                  # auditoria local
└── aprovar.py                  # promoção para aprovadas
```

Dentro de cada autor:

```text
autores/<id>/
├── autor.yaml · manifesto.yaml · adaptacoes.yaml · README.md
├── direcao/       # regras estáveis da disciplina
├── anos/<ano>/    # fontes, conteudos e prompts
├── projetos/      # área lógica, criada com o primeiro lote real
└── registros/     # área lógica, criada com o primeiro registro real
```

## Requisitos e configuração

- Python 3.10 ou superior;
- `uv`;
- chave do provedor que será usado: xAI com acesso a `grok-imagine-image-2.0`
  e/ou OpenAI com acesso a `gpt-image-2`;
- pasta de saída fora deste repositório.

```bash
uv sync --locked
cp .env.grok.example .env.grok.local
cp .env.openai.example .env.openai.local
cp config.example.yaml config.local.yaml
```

Informe cada chave somente no arquivo local correspondente e configure uma raiz
externa em `config.local.yaml`. Os três arquivos `.local` são ignorados pelo
Git.

Projetos xAI usam `XAI_API_KEY` de `.env.grok.local`. Projetos OpenAI usam
`OPENAI_API_KEY` de `.env.openai.local`. O provedor é declarado em cada projeto
e nenhuma credencial altera silenciosamente o modelo selecionado.

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
  --projeto autores/ingles/projetos/2026/3-bimestre/unidade-03-bloco-01-autonomia-guiada-4paginas-v5.yaml \
  --dry-run
```

Dry-run de Matemática com Grok Imagine 2:

```bash
uv run gerar.py \
  --projeto autores/matematica/projetos/2026/3-bimestre/unidades-05-06-6paginas-grok-v14-branco-colagem-variada.yaml \
  --dry-run
```

## Fluxo editorial

1. selecionar o autor correto;
2. revisar fonte, conteúdo e prompt versionado;
3. declarar o lote em um projeto YAML, com provedor e modelo explícitos;
4. executar `--dry-run`;
5. gerar na área externa `_revisao/<autor>/...`;
6. conferir texto, símbolos, correspondências visuais, metadados e OCR;
7. promover somente após revisão humana.

O gerador protege arquivos existentes. `--forcar` só deve ser usado com
autorização explícita e depois de confirmar o destino exato.

## Criar um autor novo

O procedimento está em [autores/README.md](autores/README.md). Comece copiando
`autores/_modelo/autor.yaml`.
