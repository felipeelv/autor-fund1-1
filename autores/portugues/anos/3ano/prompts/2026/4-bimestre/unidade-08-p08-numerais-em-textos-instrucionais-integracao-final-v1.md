---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-09-09
origem: unidade-08-p08-numerais-em-textos-instrucionais-integracao-final-rascunho.md
---
Use case: scientific-educational
Asset type: página 8 de uma sequência didática de Português do 3º ano


## PEDIDO

Fecha a Unidade 8 mostrando cardinais e ordinais trabalhando juntos em dois
exemplos integrados. CORREÇÃO SOBRE O RASCUNHO: o parser de `preparar.py`
perdeu os passos do "MODO DE PREPARO" (Vitamina de Banana) e das
"INSTRUÇÕES" (Mochila) porque a fonte escreve esses passos em linha
corrida, sem marcador de lista — os TEXTOS EXATOS abaixo foram completados
manualmente a partir da fonte bruta (linhas 1467-1544). Densidade "mais
comprimido": o segundo exemplo (mochila) usa só 3 dos 7 passos da fonte.

Título previsto: Numerais em Textos Instrucionais: Integração Final

## SISTEMA VISUAL

Cor protagonista: metade laranja (cardinais) e metade verde (ordinais) —
fechando o contraste de cor usado nas páginas 6 e 7. Seguir
`PADRAO-VISUAL-3ANO.md` (5-7 núcleos, 6-9 recortes, corredores brancos,
sombra curta, fita/post-it variando).

## COMPOSIÇÃO E TÍTULO

Título: selo circular de fechamento de unidade no alto, "Numerais em Textos
Instrucionais: Integração Final" — mesmo formato de fechamento usado no
final da Unidade 7.

Núcleo 1: "Agora vamos ver como cardinais e ordinais trabalham juntos..." +
"Onde cada tipo aparece:" (CARDINAIS em materiais/quantidades/medidas;
ORDINAIS em passos/sequências/ordem) de TEXTOS EXATOS.

Núcleo 2 (protagonista): VITAMINA DE BANANA — INGREDIENTES (4 itens, cada
um marcado CARDINAL) + MODO DE PREPARO com os passos numerados (cada um
com seu ordinal e cardinal destacados, como na fonte) + RENDIMENTO de
TEXTOS EXATOS.

Núcleo 3 (síntese): "CARDINAIS usados" + "ORDINAIS usados" + "Integração
perfeita: os cardinais dizem QUANTO, os ordinais dizem EM QUE ORDEM" de
TEXTOS EXATOS.

Núcleo 4: COMO ORGANIZAR SUA MOCHILA ESCOLAR — MATERIAIS NECESSÁRIOS (5
itens, cada um marcado CARDINAL) + 3 dos 7 passos das INSTRUÇÕES (escolhidos
para mostrar ordinal+cardinal juntos) de TEXTOS EXATOS.

## TEXTOS EXATOS

Extraídos literalmente da fonte. Revisar: remover o que não cabe na página,
ajustar a ordem e condensar onde a leitura pedir — sem trocar número, nome
próprio, unidade ou termo técnico.

- Agora vamos ver como cardinais e ordinais trabalham juntos em textos instrucionais!
- CARDINAIS aparecem em: ✓ Materiais/Ingredientes ✓ Quantidades ✓ Medidas
- ORDINAIS aparecem em: ✓ Passos (primeiro, segundo, terceiro) ✓ Sequências ✓ Ordem de ações
- VITAMINA DE BANANA
- INGREDIENTES:
- 2 bananas maduras ← CARDINAL (quantidade)
- 1 copo de leite ← CARDINAL (quantidade)
- 3 colheres de açúcar ← CARDINAL (quantidade)
- 5 pedras de gelo ← CARDINAL (quantidade)
- MODO DE PREPARO:
- Primeiro, descasque as 2 bananas. ← ORDINAL + CARDINAL
- Terceiro, adicione o 1 copo de leite. ← ORDINAL + CARDINAL
- Sexto, bata tudo por 2 minutos. ← ORDINAL + CARDINAL
- RENDIMENTO: 2 porções ← CARDINAL
- CARDINAIS usados (quantidade):
- 2 (bananas, minutos, copos, porções)
- 1 (copo de leite)
- 3 (colheres de açúcar)
- 5 (pedras de gelo)
- ORDINAIS usados (ordem):
- Primeiro, segundo, terceiro, quarto, quinto, sexto
- Integração perfeita: Os cardinais dizem QUANTO de cada coisa. Os ordinais dizem EM QUE ORDEM fazer.
- COMO ORGANIZAR SUA MOCHILA ESCOLAR
- MATERIAIS NECESSÁRIOS:
- 1 mochila ← CARDINAL
- 5 cadernos ← CARDINAL
- 3 estojos ← CARDINAL
- 2 livros ← CARDINAL
- 1 lancheira ← CARDINAL
- INSTRUÇÕES:
- Primeiro, esvazie completamente a mochila. ← ORDINAL
- Segundo, separe os 5 cadernos por matéria. ← ORDINAL + CARDINAL
- Quinto, coloque os 3 estojos no bolso frontal. ← ORDINAL + CARDINAL

## TRAVAS

Valem as travas de `autores/portugues/anos/3ano/REGRAS.md` e o `prompt_sufixo` do autor, que o gerador
injeta automaticamente.

Invioláveis, independentes de ano: não inventar número, nome próprio, data,
lugar, povo ou termo ausente da fonte; renderizar cada texto literal exatamente
uma vez; nenhum texto além da lista de TEXTOS EXATOS.
