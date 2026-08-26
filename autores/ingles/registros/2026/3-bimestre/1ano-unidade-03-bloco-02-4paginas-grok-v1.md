# Registro de produção — Unidade 3 · Bloco 2 · Shapes & Numbers · 1º ano · 4 páginas · Grok v1

Data: 26/08/2026
Estado: conferido e promovido para `aprovadas` em 26/08/2026, por Nicolas Basso.

## Pedido aprovado

Converter em quatro páginas ilustradas a fonte do bloco 2 da Unidade 3
(`fontes/2026-2-semestre/3bim-bloco2.md`), que preenche a lacuna de números
deixada em aberto pelo bloco 1 e introduz `SHAPES` combinado com cores já
ensinadas.

## Progressão pedagógica

1. nomear quatro formas e combiná-las com cor (`It is a + cor + forma`);
2. contar formas com número, cor e forma (`Three red circles`);
3. perguntar o que é algo (`What is this?`) e dizer preferência (`I like...`);
4. revisar as quatro estruturas do bloco.

## Execução

- projeto: `projetos/2026/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1.yaml`;
- provider: OpenRouter, roteando para o modelo Grok da xAI (autorização de
  19/08/2026 em `CLAUDE.md`, usada aqui por decisão explícita do responsável
  editorial, já que não há `XAI_API_KEY` nativa configurada neste ambiente);
- modelo: `x-ai/grok-imagine-image-2.0`;
- formato: JPEG, proporção 2:3, resolução 2k, qualidade medium;
- linguagem visual: colagem, sketchnote e visual note-taking;
- área: `_revisao` externa.
- páginas 1 e 2 foram corrigidas uma vez cada antes da aprovação: a página 1
  trocou "UNIDADE 3" por "UNIT 3" no título e reposicionou a fórmula
  cor+forma junto da demonstração (v1 → v2); a página 2 corrigiu a contagem
  de "Five green rectangles", que a v1 desenhou com seis retângulos (v1 → v2).

## Saídas

| Página | Caminho relativo externo | SHA-256 |
|---|---|---|
| Formas e cores juntas | `ingles/1ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/p01-formas-e-cores-juntas-v2.jpg` | `27c69ef725da3b4ef171c19c62640c9835b1c527ebbaccfb7e708284eb998c3e` |
| Contando formas | `ingles/1ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/p02-contando-formas-v2.jpg` | `7dd696107d9e3ab83f067c5c7bb9c2793e7f9e6772b9c45331e0adade3abad1b` |
| What is this + I like | `ingles/1ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/p03-o-que-e-isto-e-eu-gosto-v1.jpg` | `4176b81ed821fef1364923ce915f9ba295841146264a2d73464ed365a608ad65` |
| Revisão do bloco | `ingles/1ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/p04-revisao-do-bloco-v1.jpg` | `9820318c7802fa206d06974effa9cb2aca697efc0d995d45dea052dcd89b25dc` |

## Verificação

- `dry-run` aprovado antes de cada geração;
- bytes, formato JPEG e proporção 2:3 validados nas quatro imagens;
- inspeção visual em resolução original: texto obrigatório completo em
  todas as páginas, sem forma associada a objeto real fora da fonte, sem
  mascote, logotipo ou número de página, caixas fechadas, sem título órfão
  nem tabela quebrada;
- a v1 da página 2 foi rejeitada nesta inspeção por contagem incorreta
  (5 anunciados, 6 desenhados); a v2 corrigiu e foi confirmada uma a uma.

## Conferência humana

Nicolas Basso conferiu as quatro páginas ao longo da sessão de produção e
autorizou a promoção em 26 de agosto de 2026. A conferência cobriu nomes de
formas e números, ortografia inglesa e ausência de conteúdo fora da fonte.
As quatro imagens foram promovidas com `aprovar.py`; os registros de
aprovação estão em
`registros/aprovacoes/ingles/1ano/3-bimestre/unidade-03-bloco-02-4paginas-grok-v1/`.

## Parecer visual

As quatro páginas mantêm a linguagem visual do bloco 1 (colagem, sketchnote,
visual note-taking, seis cores didáticas) e apresentam uma sequência clara:
vocabulário de formas, contagem, pergunta/resposta e revisão. Compatíveis
com o nível esperado do 1º ano.
