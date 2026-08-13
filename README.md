# Autor-teste de Inglês — Fundamental I

Repositório autônomo para gerar as páginas pedagógicas do autor
`autor-teste-fund1` com a OpenAI Images API e o modelo `gpt-image-2`.

Este pacote não depende do repositório maior. Ele contém o núcleo Python, as
configurações compartilhadas necessárias, o formato `apostila-fund1`, as
fontes, os conteúdos editoriais, os prompts, os projetos YAML, os registros e
testes locais.

Imagens, PDFs, prévias, credenciais e ambientes virtuais não fazem parte do
repositório. Toda saída é gravada em uma raiz externa configurada.

## Estrutura

```text
autor-teste-fund1-independente/
├── autores/autor-teste-fund1/  # direção, conteúdo, prompts e projetos
├── compartilhado/              # regras editoriais e parâmetros comuns
├── formatos/apostila-fund1/    # formato visual autorizado
├── gerador_imagens/             # núcleo Python
├── modelos/                     # modelos de prompt e projeto
├── tests/                       # testes sem chamadas à API
├── gerar.py                     # geração e dry-run
├── validar.py                   # auditoria de prompts, projetos e imagens
└── aprovar.py                   # promoção de revisão para aprovadas
```

## Requisitos

- Python 3.10 ou superior;
- [uv](https://docs.astral.sh/uv/);
- uma chave da OpenAI com acesso a `gpt-image-2`;
- uma pasta de saída fora deste repositório.

## Instalação

```bash
cd /caminho/para/autor-teste-fund1-independente
uv sync --locked
cp .env.example .env
cp config.example.yaml config.local.yaml
```

Edite `.env` e informe somente a sua chave:

```dotenv
OPENAI_API_KEY=cole_sua_chave_aqui
```

Edite `config.local.yaml` e indique uma pasta externa existente:

```yaml
armazenamento:
  raiz: "/caminho/externo/Imagens"
  areas:
    revisao: "_revisao"
    aprovadas: "aprovadas"
    historico: "historico-importado"
```

`.env` e `config.local.yaml` são ignorados pelo Git. A configuração do destino
também pode ser feita pela variável `GERADOR_IMAGENS_SAIDA`.

## Verificação inicial

Os comandos abaixo não geram imagens nem consomem créditos:

```bash
uv run python -m unittest discover -s tests -v
uv run gerar.py --help
uv run gerar.py --listar-autores
uv run validar.py --acervo
uv run gerar.py \
  --projeto autores/autor-teste-fund1/projetos/2026/3-bimestre/unidade-03-bloco-01-autonomia-guiada-4paginas-v5.yaml \
  --dry-run
```

## Gerar as quatro páginas aprovadas

Depois do `dry-run`, execute:

```bash
uv run gerar.py \
  --projeto autores/autor-teste-fund1/projetos/2026/3-bimestre/unidade-03-bloco-01-autonomia-guiada-4paginas-v5.yaml
```

As imagens serão salvas em:

```text
<raiz externa>/_revisao/autor-teste-fund1/1ano/3-bimestre/
└── unidade-03-bloco-01-autonomia-guiada-v5/
```

O gerador não sobrescreve arquivos existentes. `--forcar` só deve ser usado
com autorização explícita e depois de confirmar o destino exato.

## Fluxo editorial

1. manter a fonte e o conteúdo pedagógico dentro do autor;
2. criar um prompt versionado para cada página;
3. declarar o lote em um projeto YAML;
4. executar `--dry-run`;
5. gerar na área externa `_revisao`;
6. conferir texto, correspondências visuais, metadados e OCR;
7. promover somente após revisão humana.

Exemplo de promoção:

```bash
uv run aprovar.py \
  autor-teste-fund1/1ano/3-bimestre/unidade-03-bloco-01-autonomia-guiada-v5/p01-cores-ao-nosso-redor-v5.png \
  --revisor "Nome do revisor"
```

A aprovação copia a imagem para a área externa `aprovadas` e cria registros
textuais de rastreabilidade em `registros/aprovacoes/`.

## Preparar o novo repositório Git

Depois de mover ou renomear esta pasta, ela pode receber seu próprio Git:

```bash
git init
git add .
git status
```

Confira o `git status` antes do primeiro commit. Nenhuma imagem, `.env`,
`config.local.yaml` ou `.venv` deve aparecer na lista de arquivos versionados.
