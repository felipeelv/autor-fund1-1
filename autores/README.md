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

Cada disciplina tem um par: um autor de **conteúdo**, que apresenta e explica, e
um autor de **atividades**, que entrega enunciado e espaço de resposta. A
separação é de função, não de assunto — os dois cobrem o mesmo currículo e usam
a mesma linguagem visual.

| Conteúdo | Atividades | Disciplina | Anos com material |
|---|---|---|---|
| `ingles` | | Inglês | 1º ano |
| | `ingles-atividades` | Inglês | 3º ano |
| `matematica` | | Matemática | 3º ano |
| | `matematica-atividades` | Matemática | — |
| `natureza-e-sociedade` | | Natureza e Sociedade | 3º ano |
| | `natureza-e-sociedade-atividades` | Natureza e Sociedade | — |
| `portugues` | | Português | — |
| | `portugues-atividades` | Português | — |

Todos declaram como escopo o 1º, o 2º e o 3º ano; `manifesto.anos` lista os anos
que já têm material e `manifesto.anos_planejados`, os demais.

Os autores sem material têm direção editorial **provisória**, marcada como tal
no topo de `direcao/AUTOR.md` e no `estado` do `manifesto.yaml`. Eles ficam
`ativo: true` porque o acervo não admite autor inativo, mas não produzem nada
sem fonte e sem projeto: esperam a primeira fonte e o ajuste humano da direção
antes do primeiro lote.

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
