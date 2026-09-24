---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-08-27
origem: unidade-06-p06-quadros-e-dialogos-v4-correcao-azul-e-numeracao.md
nota_correcao: |-
  Correção de defeito de geração (v4 -> v5), 27/08/2026. Na v4, a numeração
  do bloco "Para 6 quadros" saiu certa (2 a 6), mas o azul do parêntese
  vazou para a linha inteira: "Definidos (O, A, OS, AS) quando é algo
  específico" e "Indefinidos (UM, UMA, UNS, UMAS) quando não é algo
  específico" saíram inteiras em azul, não só o trecho entre parênteses —
  a instrução de v4 descrevia as duas frases completas no mesmo período que
  pedia a cor, e o modelo generalizou a cor para a frase toda. Reescrita
  para isolar explicitamente qual palavra é azul e qual continua preta.

  Herda os ajustes de v2 -> v4: frase "quando é qualquer" (fonte, linha
  1240) virou "quando não é algo específico" por decisão editorial do
  revisor; os quatro artigos em destaque no núcleo 3 saem em caixa baixa;
  selos de "Para 6 quadros" leem 2 a 6.
---
Use case: scientific-educational
Asset type: página 6 de uma sequência didática de Português — Fundamental I do 2º ano

## PEDIDO

Mostra o passo 3 (4 ou 6 quadros) e o passo 4 (diálogos com artigos e
pontuação), fechando com o exemplo de João e a bola. Fica de fora
onomatopeias e expressões faciais.

Título previsto: Quantos quadros e os diálogos com artigos

## SISTEMA VISUAL

Duas cores: azul #2F6FD0 (quadros) e roxo #8B5FBF (pontuação nos diálogos);
artigo em amarelo #F6C945 sempre em destaque, sempre em caixa baixa dentro
do destaque. Título numa tira de fita crepe com letras carimbadas, à
esquerda, abaixo do topo, sem ocupar a largura inteira. Colagem densa,
sombra projetada, ao menos dois elementos de fixação distintos; branco só
como fresta. As duas estruturas de quadro em papel quadriculado; os balões
de diálogo em papel liso branco com sombra própria. Setas ligam cada
lembrete ao balão que ele explica.

## COMPOSIÇÃO E TÍTULO

Título: tira de fita crepe à esquerda, sob o topo, "Quantos quadros e os
diálogos com artigos" em letras carimbadas.

Núcleo 1 (papel quadriculado, duas estruturas lado a lado, leve rotação):
"Sua HQ vai ter 4 a 6 quadros." — "Para 4 quadros": quatro caixas, selo 1 a
4 (Início / Problema aparece / Tentativa de resolver / Solução); "Para 6
quadros": cinco caixas, selo 2 a 6, sem o 1 (Desenvolvimento / Problema
aparece / Problema se complica / Tentativa de resolver / Solução). Selo
sempre igual ao número do texto da própria caixa.

Núcleo 2 (faixa central, tag pendurada por clipe): "Agora pense: o que os
personagens vão dizer?" com os três lembretes, todos em preto/grafite, exceto
um recorte só: nas duas linhas de artigos adequados, apenas o grupo entre
parênteses vira azul #2F6FD0 — `(O, A, OS, AS)` na linha "Definidos... quando
é algo específico" e `(UM, UMA, UNS, UMAS)` na linha "Indefinidos... quando
não é algo específico" — o resto de cada linha (antes e depois do parêntese)
continua preto, como pontuação expressiva (!/?/...) e diálogos curtos (2 a 6
palavras por balão, seja direto!). Cada lembrete ligado por seta a um balão
do núcleo 3.

Núcleo 3 (protagonista, rodapé, papel branco com sombra, canto dobrado):
quatro balões numerados Quadro 1 a 4, artigo em destaque amarelo #F6C945 e
em caixa baixa dentro do destaque — "Olha a minha bola nova!", "Onde está a
bola?", "Vi uma bola ali!", "Achei a sua bola!" — cada um com a explicação
entre parênteses da fonte ao lado, também em caixa baixa.

## TEXTOS EXATOS

Extraídos literalmente da fonte, com os ajustes editoriais do
`nota_correcao`. Revisar: remover o que não cabe, ajustar a ordem e
condensar onde a leitura pedir — sem trocar número, nome próprio, unidade ou
termo técnico.

- Sua HQ vai ter 4 a 6 quadros.
- Divida sua história entre os quadros:
- Para 4 quadros:
- Quadro 1: Início
- Quadro 2: Problema aparece
- Quadro 3: Tentativa de resolver
- Quadro 4: Solução
- Para 6 quadros:
- Quadro 2: Desenvolvimento
- Quadro 3: Problema aparece
- Quadro 4: Problema se complica
- Quadro 5: Tentativa de resolver
- Quadro 6: Solução
- Agora pense: o que os personagens vão dizer?
- Lembre-se de usar:
- ✓ Artigos adequados:
- Definidos (O, A, OS, AS) quando é algo específico
- Indefinidos (UM, UMA, UNS, UMAS) quando não é algo específico
- ✓ Pontuação expressiva:
- ! para surpresa, grito
- ? para perguntas
- ... para pausas, suspense
- ✓ Diálogos curtos:
- 2 a 6 palavras por balão
- Seja direto!
- Exemplo de diálogos com artigos:
- Quadro 1: "Olha a minha bola nova!" (artigo definido - bola específica dele)
- Quadro 2: "Onde está a bola?" (artigo definido - a bola específica que ele tinha)
- Quadro 3: "Vi uma bola ali!" (artigo indefinido - uma bola qualquer que encontrou)
- Quadro 4: "Achei a sua bola!" (artigo definido - a bola específica que ele procurava)

## TRAVAS

Valem as travas de `autores/portugues/anos/2ano/REGRAS.md` e o `prompt_sufixo` do autor, que o gerador
injeta automaticamente.

Invioláveis, independentes de ano: não inventar número, nome próprio, data,
lugar, povo ou termo ausente da fonte; renderizar cada texto literal exatamente
uma vez; nenhum texto além da lista de TEXTOS EXATOS. Papel, fixação, título e
setas de conexão são desenho, não texto novo.

Trava desta versão: só o texto dentro dos parênteses vira azul #2F6FD0;
tudo antes e depois deles, nas duas linhas de artigos, continua preto —
proibido azul fora do parêntese. Selos de "Para 6 quadros": 2, 3, 4, 5, 6,
sem o 1, cada um igual ao número do texto da própria caixa. Artigos do
núcleo 3 em caixa baixa — proibido A, UMA em maiúscula.
