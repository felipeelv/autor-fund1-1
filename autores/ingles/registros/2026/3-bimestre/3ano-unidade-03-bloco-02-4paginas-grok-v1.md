# Registro de produção — Unidade 3 · Bloco 2 · Clothes & Seasons · 3º ano · 4 páginas · Grok v1

Data: 26/08/2026
Estado: conferido e promovido para `aprovadas` em 26/08/2026, por Nicolas Basso.

## Pedido aprovado

Produzir o primeiro lote de imagens do autor `ingles` para o 3º ano —
nenhum bloco anterior existia para este ano. Fonte:
`fontes/2026-2-semestre/3bim-bloco2.md` (Clothes & Seasons).

## Progressão pedagógica

1. nomear seis roupas e usar `I wear...`;
2. nomear as quatro estações e combinar com roupa (`In + estação, I wear...`);
3. ler o gênero textual "calendário de estações" num exemplo pronto;
4. revisar vocabulário e as três estruturas do bloco.

O molde em branco `CREATE YOUR CALENDAR` da fonte não virou página de
preenchimento — `ingles` é autor de conteúdo, não de atividades — e entrou
só como tarefa curta de "AGORA É COM VOCÊ" na página 3, decisão registrada
na nota editorial da fonte.

## Execução

- projeto: `projetos/2026/3-bimestre/3ano-unidade-03-bloco-02-4paginas-grok-v1.yaml`;
- provider: OpenRouter, roteando para o modelo Grok da xAI, por decisão
  explícita do responsável editorial (sem `XAI_API_KEY` nativa neste
  ambiente);
- modelo: `x-ai/grok-imagine-image-2.0`;
- formato: JPEG, proporção 2:3, resolução 2k, qualidade medium;
- linguagem visual: colagem e sketchnote, com mais texto e registro que
  imagem (ajuste do 3º ano: 4–6 núcleos por página, ilustração como suporte);
- área: `_revisao` externa.
- a página 2 foi corrigida uma vez antes da aprovação: a v1 tinha quatro
  frases de exemplo com linhas convergindo para só dois ícones
  compartilhados (a frase da camiseta apontava para uma nuvem); a v2 deu a
  cada frase seu próprio ícone individual.

## Saídas

| Página | Caminho relativo externo | SHA-256 |
|---|---|---|
| Conheça as roupas | `ingles/3ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/p01-conheca-as-roupas-v1.jpg` | `b0757a23dbda89fb3c88c43ad99b8e0b129cb2201530ec7f8b5daef39fef0f74` |
| As estações e o que vestir | `ingles/3ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/p02-as-estacoes-e-o-que-vestir-v2.jpg` | `b1c9860fe798f89c591efc94464b825dbfbca12864e405c52889b2267f374726` |
| Seasons calendar | `ingles/3ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/p03-calendario-de-estacoes-v1.jpg` | `1d183e69bcd52c909d716afe483a4debaade750015f23a34ff1a0596ce1334dd` |
| Revisão do bloco | `ingles/3ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/p04-revisao-do-bloco-v1.jpg` | `b2d10c8c7972e1641118ee6f861198e61627f421c4025273e40195c72feff270` |

## Verificação

- `dry-run` aprovado antes de cada geração;
- bytes, formato JPEG e proporção 2:3 validados nas quatro imagens;
- inspeção visual em resolução original: vocabulário e correspondências
  corretas em todas as páginas, calendário de estações sem nenhuma lacuna em
  branco, sem tabela com bordas fechadas, sem título órfão, caixas fechadas;
- a v1 da página 2 foi rejeitada nesta inspeção por correspondência visual
  incorreta entre frase e ícone; a v2 corrigiu e foi confirmada uma a uma.

## Conferência humana

Nicolas Basso conferiu as quatro páginas ao longo da sessão de produção,
incluindo a correção da página 2, e autorizou a promoção em 26 de agosto de
2026. A conferência cobriu nomes de roupas e estações, ortografia inglesa e
ausência de conteúdo fora da fonte. As quatro imagens foram promovidas com
`aprovar.py`; os registros de aprovação estão em
`registros/aprovacoes/ingles/3ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/`.

## Parecer visual

Primeiro lote do 3º ano: mais texto e registro escrito que imagem, coerente
com a leitura autônoma esperada nessa idade. Sequência clara entre
vocabulário, estrutura combinada, gênero textual e revisão.
