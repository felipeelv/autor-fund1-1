---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-08-20
origem: unidade-06-p03-contando-de-2-5-e-10-em-10-v1.md
nota_correcao: |-
  Correção de defeito de geração (v1 -> v2), 20/08/2026. Dois defeitos: (1)
  a reta do núcleo 1 saiu como "2-4-6-14-16-20" (seis pontos, pulou 8, 10,
  12, 18) em vez dos dez números literais "2-4-6-8-10-12-14-16-18-20"; (2) o
  rótulo sobre o quinto par de meias saiu como um glifo malformado em vez de
  "10". A correção enumera explicitamente os dez pontos da reta e marca o
  quinto rótulo como número de dois algarismos.
---
Use case: scientific-educational
Asset type: página 3 de uma sequência didática de Matemática do 1º ano

## PEDIDO

Mostrar três jeitos de contar "pulando" — de 2 em 2, de 5 em 5 e de 10 em 10
— cada um com onde se usa na vida real e o padrão de final dos números. Os
três saltos formam um único assunto (contagem por saltos), por isso ficam
juntos numa página, em vez de espalhados; descobrir a regra de sequências
mais gerais fica para a página 4.

Título previsto: Contando de 2 em 2, de 5 em 5 e de 10 em 10

## SISTEMA VISUAL

Fundo branco puro `#FFFFFF`, sem creme, grade ou pontilhado contínuo. Três
núcleos de mesmo tamanho, um por salto, em faixas horizontais empilhadas —
repetição deliberada da mesma estrutura visual para a criança reconhecer o
padrão entre os três. Papel fixo por cor: azul `#2F6FD0` no bloco de 2 em 2,
amarelo `#F6C945` no de 5 em 5, laranja `#F28C32` no de 10 em 10. Tipografia
grande, caixa alta de imprensa. Cada reta numérica desenhada à mão com arcos
ligando cada par de números vizinhos, um arco por salto, sem pular nenhum
ponto da lista.

## COMPOSIÇÃO E TÍTULO

- título `CONTANDO DE 2 EM 2, DE 5 EM 5 E DE 10 EM 10` em faixa horizontal no
  topo, ocupando toda a largura — com os números `2`, `5` e `10` maiores que
  o resto, cada um na cor do bloco correspondente;
- núcleo 1, azul: a frase `Podemos contar pulando de 2 em 2. É como contar
  apenas os números pares!`; a reta com **dez pontos igualmente espaçados**,
  na ordem exata `2 — 4 — 6 — 8 — 10 — 12 — 14 — 16 — 18 — 20` (dez números,
  não seis, com nove arcos ligando cada par vizinho); separadamente, ao lado,
  a ilustração de 5 pares de meias coloridas — um dispositivo diferente da
  reta, com só 5 checagens: cada par tem dois rótulos iguais entre si (`2` e
  `2`, `4` e `4`, `6` e `6`, `8` e `8`, e no quinto par `10` e `10`, os dois
  com dois algarismos, sem confundir com outro número); o post-it `ONDE
  USAMOS CONTAR DE 2 EM 2` com as quatro situações; o post-it `📌 PADRÃO` com
  a frase do final dos números;
- núcleo 2, amarelo: a frase `Contar de 5 em 5 é muito útil! É como contar de
  mão em mão.`; a reta com dez pontos `5 — 10 — 15 — 20 — 25 — 30 — 35 — 40 —
  45 — 50`; ao lado, mãos sendo contadas — uma mão = 5, duas mãos = 10, três
  mãos = 15; o post-it `ONDE USAMOS CONTAR DE 5 EM 5` com as três situações; o
  post-it `📌 PADRÃO` com a frase do final dos números;
- núcleo 3, laranja: a frase `Contar de 10 em 10 é o jeito mais rápido de
  contar números grandes!`; a reta com cinco pontos `10 — 20 — 30 — 40 — 50`;
  ao lado, pacotes com 10 balas cada, numerados 10, 20, 30, 40, 50; o post-it
  `ONDE USAMOS CONTAR DE 10 EM 10` com as três situações; o post-it `📌
  PADRÃO` com a frase do final dos números.

## TEXTOS EXATOS

Extraídos literalmente da fonte. Revisar: remover o que não cabe na página,
ajustar a ordem e condensar onde a leitura pedir — sem trocar número, nome
próprio, unidade ou termo técnico.

- Podemos contar pulando de 2 em 2. É como contar apenas os números pares!
- 2 — 4 — 6 — 8 — 10 — 12 — 14 — 16 — 18 — 20
- ONDE USAMOS CONTAR DE 2 EM 2
- - Contar pares de meias
- - Contar sapatos (sempre em pares!)
- - Contar olhos das pessoas (cada pessoa tem 2)
- - Contar rodas de bicicleta
- 📌 PADRÃO
- Quando contamos de 2 em 2 começando do 2, os números sempre terminam em 2, 4, 6, 8 ou 0!
- Contar de 5 em 5 é muito útil! É como contar de mão em mão.
- 5 — 10 — 15 — 20 — 25 — 30 — 35 — 40 — 45 — 50
- ONDE USAMOS CONTAR DE 5 EM 5
- - Contar dedos das mãos (cada mão tem 5)
- - Contar moedas de 5 centavos
- - Contar de 5 em 5 minutos no relógio
- Quando contamos de 5 em 5, os números sempre terminam em 5 ou 0!
- Contar de 10 em 10 é o jeito mais rápido de contar números grandes!
- 10 — 20 — 30 — 40 — 50
- ONDE USAMOS CONTAR DE 10 EM 10
- - Contar os dedos das mãos de várias pessoas
- - Contar cédulas de 10 reais
- - Contar grupos grandes de objetos
- Quando contamos de 10 em 10, os números sempre terminam em 0!

## TRAVAS

Valem as travas de `autores/matematica/anos/1ano/REGRAS.md` e o `prompt_sufixo` do autor, que o gerador
injeta automaticamente.

Invioláveis, independentes de ano: não inventar número, nome próprio, data,
lugar, povo ou termo ausente da fonte; nenhum texto além da lista de TEXTOS
EXATOS.

Fundo exposto branco puro `#FFFFFF`; proibido creme, marfim, bege, grade ou
pontilhado contínuo. A reta do núcleo 1 tem exatamente dez pontos e nove
arcos, sequência completa 2,4,6,8,10,12,14,16,18,20 sem faltar nenhum
número. Repetição autorizada, e nenhuma outra: `📌 PADRÃO`, três vezes; `10`
como rótulo de par de meia, duas vezes (topo e círculo do quinto par), sempre
com dois algarismos. Todo o resto do texto aparece exatamente uma vez. Os
grupos de mãos (1, 2 e 3 mãos) e os pacotes de balas precisam ser contáveis
um a um e bater com os números da reta. Não fundir os três núcleos. Não
acrescentar salto diferente de 2, 5 ou 10. Sem fotografia, sem balão de fala,
sem mascote.
