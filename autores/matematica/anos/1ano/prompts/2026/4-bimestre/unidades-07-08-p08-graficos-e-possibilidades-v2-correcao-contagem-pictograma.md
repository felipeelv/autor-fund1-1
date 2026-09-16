---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-09-04
origem: unidades-07-08-p08-graficos-e-possibilidades-v1.md
nota_correcao: |-
  Correção de defeito de geração (v1 -> v2), 04/09/2026. No pictograma,
  maçã (5) e laranja (2) saíram com a contagem certa, mas banana saiu com 4
  ícones em vez de 3, e uva saiu com 5 em vez de 6 — limite conhecido do
  modelo para contagem de marcas repetidas. Esta versão reforça a contagem
  linha a linha com instrução de contar 1, 2, 3... e parar, em vez de só
  declarar o número.
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
  da Turma`; tabela `FRUTA` / `QUANTIDADE` com quatro linhas — desenhar cada
  ícone de fruta um a um, contando em voz alta enquanto desenha, e PARAR
  assim que chegar no número da linha, sem continuar nem faltar:
  maçã — desenhar 1, 2, 3, 4, 5 e parar (5 maçãs, nunca 4 nem 6); banana —
  desenhar 1, 2, 3 e parar (3 bananas, nunca 2 nem 4); uva — desenhar 1, 2,
  3, 4, 5, 6 e parar (6 uvas, nunca 5 nem 7); laranja — desenhar 1, 2 e
  parar (2 laranjas, nunca 1 nem 3). Depois de desenhar cada linha, recontar
  os ícones antes de passar para a próxima. Abaixo, box
  `PERGUNTAS SOBRE O GRÁFICO` com as três perguntas e respostas entre
  parênteses;
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
- 🍎🍎🍎🍎🍎 (5 crianças)
- 🍌 Banana
- 🍌🍌🍌 (3 crianças)
- 🍇 Uva
- 🍇🍇🍇🍇🍇🍇 (6 crianças)
- 🍊 Laranja
- 🍊🍊 (2 crianças)
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
Contagem exata no pictograma, contada uma a uma: 5 maçãs, 3 bananas, 6
uvas, 2 laranjas — nem um ícone a mais, nem um a menos em nenhuma linha.
Exatamente 1 exemplo por categoria de possibilidade (certeza, impossível,
depende), sem acrescentar os demais exemplos da fonte. Não fundir os dois
núcleos. Sem fotografia, sem balão de fala, sem mascote.
