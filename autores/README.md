# Autores por disciplina

Cada pasta representa uma direção editorial especializada dos anos iniciais e
contém:

```text
autores/<id>/
├── README.md
├── autor.yaml        # perfil executável: nome, disciplina, formatos, parâmetros
├── manifesto.yaml    # mapa e estado do autor
├── adaptacoes.yaml   # vínculo com o formato, por ano
├── direcao/          # regras estáveis da disciplina
├── anos/             # fontes, conteúdos e prompts que variam por ano
├── projetos/         # área lógica, materializada com o primeiro lote real
└── registros/        # área lógica, materializada com o primeiro registro real
```

`projetos/` e `registros/` são **áreas lógicas**: ficam declaradas em
`manifesto.yaml`, sob `producao`, e não precisam de diretório vazio nem de
`.gitkeep`. Crie a pasta somente quando ela receber o primeiro arquivo real.

## Autores ativos

| ID | Disciplina | Anos atendidos |
|---|---|---|
| `ingles` | Inglês | 1º e 3º ano |
| `matematica` | Matemática | 3º ano |
| `natureza-e-sociedade` | Natureza e Sociedade | 3º ano |

Todos usam o formato `apostila-fund1`, autorizado nos dois sentidos: o autor
declara o formato em `autor.yaml` e o formato declara o autor em
`formatos/apostila-fund1/formato.yaml`. As duas listas precisam concordar.

## Criar um autor novo

1. copie `_modelo/autor.yaml` para `autores/<id>/autor.yaml` e preencha;
2. escreva `manifesto.yaml`, `adaptacoes.yaml` e `README.md`;
3. escreva `direcao/AUTOR.md`, `direcao/MEMORIA.md` e o padrão visual do ano;
4. declare o ID em `formatos/apostila-fund1/formato.yaml`;
5. acrescente o ID a `AUTHOR_IDS` em `tests/test_package_contract.py`;
6. registre a disciplina em `CLAUDE.md`.

O ID é o nome da pasta, em minúsculas, com hífen, e precisa ser idêntico ao
campo `autor.id` do `autor.yaml`. Ele também nomeia a pasta de saída na raiz
externa, então precisa ser estável e não ambíguo.

Não copie código, `.env`, ambiente virtual, imagem ou master compartilhado para
dentro de um autor. Não misture conteúdos, fontes, prompts ou saídas entre
autores.

## Comandos

```bash
uv run gerar.py --listar-autores
uv run gerar.py \
  --autor <id> \
  --prompt autores/<id>/anos/<ano>/prompts/<ano-letivo>/<bimestre>/<arquivo>.md \
  --saida <id>/<ano>/<bimestre>/<arquivo> \
  --dry-run
```
