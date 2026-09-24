---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-08-21
origem: unidade-06-p01-contando-ate-50-v3-correcao-barra-de-dez.md
nota_correcao: |-
  Correção de defeito de geração (v3 -> v4), 21/08/2026. As barras de dez
  (v3) resolveram o problema anterior -- em duas das três gerações de teste,
  todos os grupos (5+3+4+5) saíram com a contagem certa. Mas a régua do
  núcleo 3 quebrou em duas das três gerações, sempre no mesmo ponto: "0 — 5
  — 20 — 15 — 20 — 25 — 30 — 35 — 40 — 45 — 50" (duplica o 20 no lugar do
  10). Não é mais sorte aleatória -- é o mesmo ponto falhando repetidamente,
  então a correção muda o que está sendo pedido: em vez de destacar
  10/20/30/40/50 com círculos coloridos sobre a reta (decoração que não é
  texto literal e parece confundir o modelo sobre qual número vai em qual
  posição), a reta passa a ser desenhada simples, sem nenhum círculo ou
  cor sobre os números -- a ideia de "números especiais" já está garantida
  pelo texto literal do post-it OBSERVE, que não depende da reta.
---
Use case: scientific-educational
Asset type: página 1 de uma sequência didática de Matemática do 1º ano

## PEDIDO

Abrir a Unidade 6 apresentando os números de 21 a 50 para uma criança de
aproximadamente 6 anos: os quatro objetivos da unidade, o padrão de nome dos
números de 21 a 30 (a base que se repete até 50) e os números redondos 40 e
50 como grupos completos de dez, apoiados pela régua numérica. Agrupamento
com objetos soltos (feijões, lápis) fica para a página 2; contagem por saltos
de 2, 5 e 10, para a página 3.

Título previsto: Números até 50

## SISTEMA VISUAL

Fundo branco puro `#FFFFFF`, sem creme, grade ou pontilhado contínuo. Página
dominada pela ilustração — ela é protagonista, com a tabela e a régua como
apoio menor. Três núcleos apenas, cada um em seu recorte de papel colado, com
corredores de branco puro entre eles. Papel fixo por cor: azul `#2F6FD0` no
título e na abertura (conceito), amarelo `#F6C945` na tabela 21-30 e no "para
lembrar" (destaque do padrão), laranja `#F28C32` nas âncoras 40/50 e na régua
(agrupamento de dez), grafite `#263238` no texto e nos contornos. Tipografia
grande, caixa alta de imprensa, sem serifa, pauta alta e larga. Todo grupo de
dez é uma **barra de dez**: um bloco sólido retangular de cantos arredondados,
cor única e chapada, sem subdivisão, listra, ponto ou marca interna — nada
dentro da barra para contar; o número `10` fica escrito embaixo de cada
barra, como rótulo de texto, nunca como soma de bolinhas ou células. A régua
numérica é uma linha simples com os onze números escritos na ordem, sem
círculo, cor extra ou qualquer marca sobre os números — só a linha e o texto.
Colagem com papel liso, bordas rasgadas, fita e sombra curta; sem grade
digital.

## COMPOSIÇÃO E TÍTULO

- título `NÚMEROS ATÉ 50` — o maior título da sequência de 4 páginas, por ser
  abertura de unidade — em caixa alta de imprensa sobre papel azul rasgado,
  alto e à esquerda, com uma criança brasileira contando objetos ao lado;
- núcleo 1, abertura: `O QUE VAMOS APRENDER?` com as quatro metas em lista, e
  abaixo a frase `Você já conhece os números até 20. Agora vamos descobrir os
  números até 50!`; ilustração grande ao fundo do núcleo — cinco barras de dez
  iguais lado a lado (blocos sólidos azuis, sem subdivisão interna), rotuladas
  `10`, `20`, `30`, `40` e `50` na ordem: cada barra é um novo grupo de dez que
  soma ao anterior, não um total dentro de uma só barra; a criança apontando
  para a última;
- núcleo 2, protagonista: tabela `NÚMERO` / `NOME` / `COMO FALAR` com as dez
  linhas de 21 a 30 completas, em papel amarelo; ao lado da linha `30`, três
  barras de dez lado a lado (blocos sólidos verdes, sem subdivisão interna,
  sem pote ou recipiente ao redor), cada uma rotulada `10`, mostrando o "3
  grupos de 10" da tabela; abaixo, o post-it `💡 PARA LEMBRAR` com a frase do
  padrão;
- núcleo 3, âncoras e régua, em papel laranja: as linhas redondas `40 /
  QUARENTA / 4 grupos de 10` e `50 / CINQUENTA / 5 grupos de 10` lado a lado;
  sob a primeira, 4 barras de dez rotuladas `10`; sob a segunda, 5 barras de
  dez rotuladas `10` — mesmo bloco sólido do núcleo 2; abaixo, a régua `0 — 5
  — 10 — 15 — 20 — 25 — 30 — 35 — 40 — 45 — 50` desenhada à mão como uma
  linha simples, onze números na ordem, sem círculo nem cor sobre nenhum
  deles; o post-it `📌 OBSERVE` com a frase sobre grupos de 10 ao lado.

## TEXTOS EXATOS

Extraídos literalmente da fonte. Renderizar cada um exatamente uma vez.

- NÚMEROS ATÉ 50
- O QUE VAMOS APRENDER?
- Contar até 50
- Agrupar de 10 em 10
- Contar de 2 em 2, de 5 em 5 e de 10 em 10
- Descobrir padrões em sequências numéricas
- Você já conhece os números até 20. Agora vamos descobrir os números até 50!
- NÚMERO
- NOME
- COMO FALAR
- 21
- VINTE E UM
- 20 + 1
- 22
- VINTE E DOIS
- 20 + 2
- 23
- VINTE E TRÊS
- 20 + 3
- 24
- VINTE E QUATRO
- 20 + 4
- 25
- VINTE E CINCO
- 20 + 5
- 26
- VINTE E SEIS
- 20 + 6
- 27
- VINTE E SETE
- 20 + 7
- 28
- VINTE E OITO
- 20 + 8
- 29
- VINTE E NOVE
- 20 + 9
- 30
- TRINTA
- 3 grupos de 10
- 💡 PARA LEMBRAR
- De 21 a 29, todos começam com "VINTE E..." e terminam com o número que você já conhece!
- 40
- QUARENTA
- 4 grupos de 10
- 50
- CINQUENTA
- 5 grupos de 10
- 0 — 5 — 10 — 15 — 20 — 25 — 30 — 35 — 40 — 45 — 50
- 📌 OBSERVE
- Os números 10, 20, 30, 40 e 50 são especiais! Eles representam grupos completos de 10.

## TRAVAS

Valem as travas de `autores/matematica/anos/1ano/REGRAS.md` e o `prompt_sufixo`
do autor, injetado automaticamente.

Invioláveis: não inventar número, nome próprio, data, lugar, povo ou termo
ausente da fonte; renderizar cada texto literal exatamente uma vez; nenhum
texto além da lista de TEXTOS EXATOS.

Fundo branco puro `#FFFFFF`; proibido creme, marfim, bege, grade ou
pontilhado contínuo. Todo grupo de dez é uma barra sólida e opaca, sem
subdivisão, listra, ponto ou bolinha interna. A régua tem exatamente onze
números na ordem `0,5,10,15,20,25,30,35,40,45,50`, sem repetir nem pular
nenhum, e sem nenhum círculo, cor ou destaque sobre eles — texto plano.
Contagem exata de barras: 5 no núcleo 1, 3 no núcleo 2, 4 e 5 no núcleo 3.
`10` repete-se sob cada barra (5+3+4+5 vezes) — única repetição autorizada.
Não incluir linha das tabelas 31-39 nem 41-49. Não fundir os três núcleos.
Não acrescentar número acima de 50 nem abaixo de 21. Sem fotografia, sem
balão de fala, sem mascote.
