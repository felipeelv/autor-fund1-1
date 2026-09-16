---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-09-04
origem: unidades-07-08-p08-graficos-e-possibilidades-v2-correcao-contagem-pictograma.md
nota_correcao: |-
  Correção de defeito de geração (v2 -> v3), 04/09/2026. A instrução de
  "contar 1, 2, 3... e parar" não corrigiu a contagem — banana piorou (saiu
  5 em vez de 3, era 4 na v1) e uva continuou errada (5 em vez de 6).
  Confirma o limite conhecido do modelo para contagem solta. Esta versão
  troca a técnica: usa uma fita fixa de 6 quadrados (o maior valor da
  tabela) em cada linha, preenchendo só os primeiros N quadrados com o
  ícone da fruta e deixando os demais em branco — mesma técnica que
  funcionou nas páginas 1 e 3 desta unidade (referência espacial fixa em vez
  de contagem solta).
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

- título `GRÁFICOS E POSSIBILIDADES` em duas linhas, caixa alta de imprensa,
  centralizado no alto sobre papel amarelo e verde rasgados — fechamento do
  bimestre;
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

Fundo branco puro `#FFFFFF`; proibido creme, grade ou pontilhado contínuo.
No pictograma, cada linha é uma fita fixa de exatamente 6 quadrados — nunca
mais, nunca menos — com o número de quadrados preenchidos com ícone da
COMPOSIÇÃO (5 maçã, 3 banana, 6 uva, 2 laranja) e o restante vazio. Exatamente
1 exemplo por categoria de possibilidade (certeza, impossível, depende), sem
acrescentar os demais exemplos da fonte. Não fundir os dois núcleos. Sem
fotografia, sem balão de fala, sem mascote.
