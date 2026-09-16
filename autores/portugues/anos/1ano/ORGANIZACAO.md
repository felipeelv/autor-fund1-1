# Organização — Português · 1º ano

## Estado

**Primeiro lote aprovado em 20/08/2026** (revisor: Nicolas Basso).

| Fonte | Unidades |
|---|---|
| `3bim-mundo-das-historias-e-somos-escritores-v1.md` | UNIDADE 5 — O MUNDO DAS HISTÓRIAS; UNIDADE 8 — SOMOS ESCRITORES (ocupa a posição da Unidade 6 do 3º bimestre — rótulo da fonte, não corrigido) |
| `4bim-cantigas-e-poesia-v1.md` | UNIDADE 7 — O MUNDO DAS CANTIGAS; UNIDADE 8 — BRINCANDO DE POETA |

Este ano saiu de `manifesto.anos_planejados` com esta aprovação.

## Português — 1º ano — 3º bimestre — Unidade 6 ("Somos escritores")

**Status: completo e aprovado em 20/08/2026** (revisor: Nicolas Basso). 4
páginas, revisão visual de conteúdo feita letra a letra contra os TEXTOS
EXATOS antes da aprovação.

**Reorganização de 6 para 4 páginas** (pedido de Nicolas Basso, 20/08/2026):
o recorte original (`unidade-06-6paginas-v1/`) separava cada sub-tema em uma
página; foi substituído por `unidade-06-4paginas-v1/`, que junta pares de
sub-temas que a própria fonte já encadeia. O recorte de 6 páginas e seus
prompts continuam no repositório como histórico, sem uso ativo.

| Página | Título | Recorte da fonte | Versão final |
|---|---|---|---|
| 1 | Vamos criar nossa própria história! (+ índice da unidade + regra S/Z) | Cap. 1, abertura | `v2-correcao-mesa` (v1 teve defeito: cartão MESA saiu como livro) |
| 2 | O roteiro da história (+ início, meio e fim) | Cap. 1, planejamento | `v1` |
| 3 | C e Ç: quando usar? | Cap. 2, abertura | `v1` |
| 4 | Nunca existe ÇE nem ÇI! (+ quadro COMPARE + palavras do livro) | Cap. 2, fecho | `v1` |

Cada página junta dois sub-temas que a fonte encadeia diretamente (ver
`recorte.yaml` para o detalhe da divisão) — por isso o número de núcleos por
página passou de 2-3 para até 4-5, mais do que o padrão geral do ano prevê.
Ajuste de densidade de conteúdo (reincluir texto literal cortado no primeiro
recorte — índice da unidade, subperguntas do roteiro, quadros COMPARE — não
inventar) registrado em `PADRAO-VISUAL-1ANO.md`, seção "Densidade e
conteúdo".

Caminhos: recorte em
`conteudos/2026/3-bimestre/unidade-06-4paginas-v1/recorte.yaml`; prompts em
`prompts/2026/3-bimestre/unidade-06-p01..p04-*-v1.md` (p01 final é
`v2-correcao-mesa`); projetos com prefixo `1ano-4paginas-` em
`../../projetos/2026/3-bimestre/`; imagens aprovadas em
`aprovadas/portugues/1ano/3-bimestre/unidade-06-4paginas/`; registros de
aprovação em
`registros/aprovacoes/portugues/1ano/3-bimestre/unidade-06-4paginas/`.

Pendente: Unidade 5 ("O mundo das histórias") do mesmo bimestre e fonte,
ainda sem recorte.

## Português — 1º ano — 4º bimestre — Unidades 7 e 8

**Conteúdo organizado em 26/08/2026** (recorte e rascunhos de prompt);
nenhuma página gerada ou aprovada ainda. Divisão combinada com Nicolas Basso:
4 páginas por unidade (2 por capítulo, abertura + fecho), o mesmo padrão da
Unidade 6.

| Unidade | Página | Título | Seções da fonte |
|---|---|---|---|
| 7 — O Mundo das Cantigas | 1 | Versos que encantam: cantiga e parlenda | 4, 6, 7, 8, 9 |
| 7 | 2 | Encontrando rimas, sinônimos e antônimos | 10, 11 |
| 7 | 3 | Letras que mudam o som: o R | 13, 14, 15 |
| 7 | 4 | Quando usar RR? | 16 |
| 8 — Brincando de Poeta | 1 | Letras que assoviam: o som do S | 18, 20, 21, 22 |
| 8 | 2 | Quando usar SS? | 23 |
| 8 | 3 | Lendo com entonação: as três regras | 25 (só regras) |
| 8 | 4 | Página do recital | 25 (só a parlenda de prática) |

A Unidade 8, Cap. 2 ("Lendo com entonação") vem de uma única seção da fonte
(25) que mistura regra e prática; o recorte separa manualmente as três
regras de pontuação (p3) da parlenda de prática (p4), que vira página de
recital — fecha o objetivo "fazer um recital para a turma" da própria
unidade.

Caminhos: recortes em
`conteudos/2026/4-bimestre/unidade-0{7,8}-4paginas-v1/recorte.yaml`;
rascunhos em
`prompts/2026/4-bimestre/unidade-0{7,8}-p01..p04-*-rascunho.md`.

Pendente: resolver as decisões editoriais de cada rascunho (PEDIDO e
COMPOSIÇÃO), aprovar com `preparar.py --aprovar` e então produzir as imagens.
A página 1 da Unidade 7 tem 47 itens de TEXTOS EXATOS — a mais densa até
agora neste ano — vale atenção especial na composição para não perder
legibilidade.

## Próximos passos

1. escrever a composição e resolver as decisões editoriais das 8 páginas do
   4º bimestre (Unidades 7 e 8), uma de cada vez;
2. recortar e produzir a Unidade 5 ("O mundo das histórias") do 3º bimestre,
   ainda sem recorte;
3. revisar `REGRAS.md` deste ano, que hoje é derivado, contra o que a fonte
   realmente pede.
