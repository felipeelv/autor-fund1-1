# Registro — Povos Indígenas (3º ano) · seis páginas · v4

**Data:** 22/08/2026. **Pedido:** Nicolas Basso — "refazer a Unidade 2 a
partir do material bruto, em seis páginas", com atenção a ritmo, respiro,
tipografia, hierarquia, aparência impressa, grade/estilo/cores/espaçamento/
composição consistentes, e sem títulos órfãos, tabelas partidas ou caixas
quebradas.

## Por que um quarto lote

Os três lotes anteriores (`v1`, `v2`, `v3` — aprovado em 15/08/2026) usaram
uma fonte mais curta. Em 19/08/2026 chegou uma fonte combinada mais rica
(`3bim-solo-e-povos-indigenas-u1-u2-v1.md`) com duas seções inteiramente
novas — organização social e arte e cultura — sem equivalente no material
usado pelo v3. Detalhe completo em
`anos/3ano/conteudos/2026/3-bimestre/unidade-povos-indigenas-6paginas-v4/COBERTURA-DA-FONTE.md`.

## Estado

Seis páginas geradas em `_revisao`, todas corretas. Nenhuma promovida para
`aprovadas`. A página 2 precisou de uma segunda rodada (roupa moderna na
cena histórica, corrigida especificando as peças proibidas no corpo do
prompt, além do que o `prompt_prefixo` já cobre).

| Página | Título | Versão | Estado |
|---|---|---|---|
| 1 | O Brasil não começou em 1500 (capa) | v1 | correta |
| 2 | Aqui moravam os Caiapós | v2 | correta (v1 tinha roupa moderna) |
| 3 | A floresta era a escola | v1 | correta |
| 4 | Sabiam tudo — e mesmo assim não destruíram | v1 | correta |
| 5 | Como a aldeia se organizava | v1 | correta, com pendência registrada |
| 6 | O que aconteceu — e o que fazemos agora | v1 | correta |

## Três decisões que precisam de confirmação humana antes da aprovação

1. **versículo bíblico**: Romanos 12:4 no lugar do Atos 17:26 do v3 — a
   fonte nova não contém Atos 17:26; Romanos 12:4 é o que ela liga à
   diversidade, tema desde a página 1;
2. **tabela de povos (página 1)**: a fonte nova lista Quéchuas (Peru,
   Bolívia) como exemplo de povo indígena *brasileiro* — substituído por
   Xavantes, o sexto povo já usado na tabela aprovada do v3;
3. **"terra vazia" (página 2)**: a fonte nova reintroduz essa tese, que o
   v3 já havia revertido com revisão humana registrada em `MEMORIA.md`.
   Este lote carrega a formulação do v3.

Carregadas sem reabrir, porque já têm decisão humana aprovada em
15/08/2026: o corte da estatística "10%/80% da biodiversidade" (sem base
científica) e a substituição dos números de população pelo Censo IBGE 2022
(1,7 milhão, 391 povos, 295 línguas).

## Pendência que se agrava

A página 5 (organização social + arte e cultura, conteúdo novo deste lote)
é construída sobre generalizações da própria fonte sobre povos indígenas em
bloco. `MEMORIA.md` já registrou isso como pendência a partir da página 4
do v3; agora é uma página inteira desse tipo. Onde a fonte permitia, o texto
usa "em muitos povos" em vez de afirmação fechada.

## O que este lote confirmou sobre o autor

- o `prompt_prefixo`/`prompt_sufixo` do autor já cobrem paleta, camadas,
  cinco naturezas de imagem e representação responsável — prompts
  delta-only (só a composição e o texto específico de cada página) coube
  com folga de ~2.700 a 3.300 bytes por página, contra os ~4.721 B de
  orçamento;
- a trava de "sem roupa moderna em cena anterior a 1500" do prefixo não é
  suficiente por si só — precisou da lista explícita de peças proibidas no
  corpo do prompt da página para funcionar, mesma lição que
  `PADRAO-VISUAL-3ANO.md` já registrava de forma mais genérica;
- a nota de orçamento de bytes do `PADRAO-VISUAL-3ANO.md` estava
  desatualizada (não contava o sufixo) — corrigida neste lote.

## Pendência obrigatória

Antes de `aprovar.py`, uma pessoa deve confirmar as três decisões acima e a
pendência de generalização da página 5, e decidir se este lote substitui o
v3 como referência visual canônica do autor.
