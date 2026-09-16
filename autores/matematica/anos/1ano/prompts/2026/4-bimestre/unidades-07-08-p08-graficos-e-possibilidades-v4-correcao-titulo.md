---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-09-04
origem: unidades-07-08-p08-graficos-e-possibilidades-v3-quadro-fixo-de-6.md
nota_correcao: |-
  Correção de defeito de geração (v3 -> v4), 04/09/2026. A tabela de
  pictograma ficou perfeita (fita fixa de 6 corrigiu as quatro linhas). Mas
  o título saiu sem o "E": "GRÁFICOS" numa linha e "POSSIBILIDADES" na
  outra, faltando o conectivo. Esta versão especifica a quebra de linha
  exata — "GRÁFICOS E" na primeira linha, "POSSIBILIDADES" na segunda — para
  garantir que o "E" apareça.
---
Use case: scientific-educational
Asset type: página 8 de uma sequência didática de Matemática do 1º ano


## PEDIDO

Fechar a Unidade 8 (e o bimestre) com um pictograma de frutas favoritas da
turma e a distinção entre "vai acontecer com certeza", "é impossível" e "pode
acontecer ou não". "Como Ler um Gráfico" fica fora — as perguntas do próprio
pictograma já ensinam o procedimento; cada categoria de possibilidade fica
com 1 exemplo em vez dos 3 da fonte.

Título previsto: Gráficos e Possibilidades

## SISTEMA VISUAL

Seguir `PADRAO-VISUAL-1ANO.md`: fundo branco puro `#FFFFFF`, ilustração
protagonista, 2 núcleos em recortes de papel separados por corredor de
branco, tipografia grande em caixa alta de imprensa. Papel fixo por cor:
amarelo `#F6C945` no pictograma (destaque, é a tabela protagonista da
página), verde `#43A66B` nas possibilidades (verificação de raciocínio).
Texto e contornos em grafite `#263238`. Colagem com papel liso, bordas
rasgadas, fita e sombra curta; sem grade digital.

## COMPOSIÇÃO E TÍTULO

- título em DUAS linhas exatas, caixa alta de imprensa, centralizado no
  alto: linha 1 `GRÁFICOS E` sobre papel amarelo rasgado (o "E" aparece no
  fim desta linha, nunca omitido); linha 2 `POSSIBILIDADES` sobre papel
  verde rasgado — fechamento do bimestre;
- núcleo 1, papel amarelo, protagonista: frase `PICTOGRAMA é um gráfico que
  usa FIGURAS para mostrar quantidades.`; título `Exemplo: Frutas Favoritas
  da Turma`; tabela `FRUTA` / `QUANTIDADE` com quatro linhas. Cada linha da
  coluna `QUANTIDADE` é uma FITA FIXA de exatamente 6 quadrados iguais
  encostados lado a lado (6 é o maior valor da tabela, o mesmo número de
  quadrados em toda linha). Nas primeiras N posições da fita (contando da
  esquerda), desenhar o ícone da fruta dentro do quadrado; as posições
  restantes, até completar os 6 quadrados, ficam com o quadrado vazio (sem
  ícone, sem X, só o contorno). N por linha: maçã — 5 quadrados com ícone,
  1 vazio; banana — 3 quadrados com ícone, 3 vazios; uva — 6 quadrados com
  ícone, 0 vazio (fita cheia); laranja — 2 quadrados com ícone, 4 vazios.
  Abaixo, box `PERGUNTAS SOBRE O GRÁFICO` com as três perguntas e respostas
  entre parênteses;
- núcleo 2, papel verde: três colunas curtas lado a lado, cada uma com seu
  título e uma única linha `EVENTO` / `POR QUÊ` (ou `DEPENDE...` na
  terceira) de exemplo — `COM CERTEZA VAI ACONTECER` com `☀️ O sol vai nascer
  amanhã` / `Acontece todos os dias`; `IMPOSSÍVEL DE ACONTECER` com `🐷 Um
  porco vai voar` / `Porcos não têm asas`; `PODE ACONTECER OU NÃO` com
  `🌧️ Vai chover amanhã` / `Do tempo`; post-it `💡 PARA LEMBRAR` com a frase
  final sobre pensar "isso pode acontecer?".

## TEXTOS EXATOS

Extraídos literalmente da fonte. Revisar: remover o que não cabe na página,
ajustar a ordem e condensar onde a leitura pedir — sem trocar número, nome
próprio, unidade ou termo técnico.

- GRÁFICOS E POSSIBILIDADES
- PICTOGRAMA é um gráfico que usa FIGURAS para mostrar quantidades.
- Exemplo: Frutas Favoritas da Turma
- FRUTA
- QUANTIDADE
- 🍎 Maçã
- (5 crianças)
- 🍌 Banana
- (3 crianças)
- 🍇 Uva
- (6 crianças)
- 🍊 Laranja
- (2 crianças)
- PERGUNTAS SOBRE O GRÁFICO
- - Qual fruta é a favorita? (Uva - tem mais desenhos)
- - Qual fruta menos crianças escolheram? (Laranja - tem menos)
- - Quantas crianças escolheram maçã? (5 crianças)
- COM CERTEZA VAI ACONTECER
- EVENTO
- POR QUÊ
- ☀️ O sol vai nascer amanhã
- Acontece todos os dias
- IMPOSSÍVEL DE ACONTECER
- 🐷 Um porco vai voar
- Porcos não têm asas
- PODE ACONTECER OU NÃO
- DEPENDE...
- 🌧️ Vai chover amanhã
- Do tempo
- 💡 PARA LEMBRAR
- Aprender a pensar "isso pode acontecer?" ajuda você a entender melhor o mundo!

## TRAVAS

Valem as travas de `autores/matematica/anos/1ano/REGRAS.md` e o `prompt_sufixo` do autor, que o gerador
injeta automaticamente.

Invioláveis, independentes de ano: não inventar número, nome próprio, data,
lugar, povo ou termo ausente da fonte; renderizar cada texto literal exatamente
uma vez; nenhum texto além da lista de TEXTOS EXATOS.

Fundo branco puro `#FFFFFF`; proibido creme, grade ou pontilhado contínuo. O
título tem duas linhas — "GRÁFICOS E" e "POSSIBILIDADES" — o "E" no fim da
primeira linha nunca pode ser omitido. No pictograma, cada linha é uma fita
fixa de exatamente 6 quadrados — nunca mais, nunca menos — com o número de
quadrados preenchidos com ícone da COMPOSIÇÃO (5 maçã, 3 banana, 6 uva, 2
laranja) e o restante vazio. Exatamente 1 exemplo por categoria de
possibilidade (certeza, impossível, depende), sem acrescentar os demais
exemplos da fonte. Não fundir os dois núcleos. Sem fotografia, sem balão de
fala, sem mascote.
