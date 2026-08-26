# Registro de produção — Unidade 3 · Bloco 2 · Wild Animals · 2º ano · 4 páginas · Grok v1

Data: 25–26/08/2026
Estado: conferido e promovido para `aprovadas` em 26/08/2026, por Nicolas Basso.

## Pedido aprovado

Produzir o primeiro lote de imagens do autor `ingles` para o 2º ano —
nenhum bloco anterior existia para este ano. Fonte:
`fontes/2026-2-semestre/3bim-bloco2.md` (Wild Animals).

## Progressão pedagógica

1. nomear quatro animais selvagens (`lion, elephant, monkey, snake`);
2. perguntar e responder que animal é (`What animal is it? / It is a(n)...`),
   incluindo a regra do artigo `an` antes de vogal;
3. dizer preferência (`I like... / I don't like...`);
4. revisar vocabulário e as três estruturas do bloco.

`PETS` e `FARM ANIMALS`, citados só na revisão da fonte sem vocabulário ou
estrutura desenvolvidos neste bloco, ficaram fora do recorte — decisão
registrada na nota editorial da fonte.

## Execução

- projeto: `projetos/2026/3-bimestre/2ano-unidade-03-bloco-02-4paginas-grok-v1.yaml`;
- provider: OpenRouter, roteando para o modelo Grok da xAI, por decisão
  explícita do responsável editorial (sem `XAI_API_KEY` nativa neste
  ambiente);
- modelo: `x-ai/grok-imagine-image-2.0`;
- formato: JPEG, proporção 2:3, resolução 2k, qualidade medium;
- linguagem visual: colagem, sketchnote e ilustração semirrealista, com cena
  como apoio principal (ajuste do 2º ano: 3–4 núcleos por página);
- área: `_revisao` externa.
- a página 1 foi corrigida uma vez antes da aprovação: a v1 não trazia a
  abertura "Nesta unidade você vai aprender"; a v2 adicionou esse resumo
  sem reduzir a cena principal.

## Saídas

| Página | Caminho relativo externo | SHA-256 |
|---|---|---|
| Conheça os animais | `ingles/2ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/p01-conheca-os-animais-v2.jpg` | `945e35e9377dfcf2d95b4fe0c539d5e49107e5933c9a0fa4e00a2f86e77b80e1` |
| What animal is it? | `ingles/2ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/p02-what-animal-is-it-v1.jpg` | `75692b495ca07c743bee7260cece478156d4d15626899d1b0a37c274fd9d00b7` |
| I like / I don't like | `ingles/2ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/p03-i-like-i-dont-like-v1.jpg` | `50aa092459a08a6a979f0bf25c2d4801fc7aeff039b581176791b7fea16b7ef1` |
| Revisão do bloco | `ingles/2ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/p04-revisao-do-bloco-v1.jpg` | `74be25297d96a771c7426f08bf80624e5b2e135a06b23b219725ef83344ec3d6` |

## Verificação

- `dry-run` aprovado antes de cada geração;
- bytes, formato JPEG e proporção 2:3 validados nas quatro imagens;
- inspeção visual em resolução original: as quatro etiquetas de animal
  corretas em todas as páginas, regra do artigo `an` respeitada, crianças
  brasileiras diversas sem estereótipo nos diálogos, sem tradução inventada
  para `dog`/`spider`, sem tabela quebrada, sem título órfão, caixas
  fechadas.

## Conferência humana

Nicolas Basso conferiu as quatro páginas ao longo da sessão de produção,
incluindo a correção da página 1, e autorizou a promoção em 26 de agosto de
2026. A conferência cobriu nomes de animais, ortografia inglesa e ausência
de estereótipo. As quatro imagens foram promovidas com `aprovar.py`; os
registros de aprovação estão em
`registros/aprovacoes/ingles/2ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/`.

## Parecer visual

Primeiro lote do 2º ano: cena central mais realista que o 1º ano, coerente
com a regra de que a ilustração dá a pista e o texto conclui. Sequência
clara entre vocabulário, pergunta/resposta e preferência, terminando em
revisão sem vocabulário novo.
