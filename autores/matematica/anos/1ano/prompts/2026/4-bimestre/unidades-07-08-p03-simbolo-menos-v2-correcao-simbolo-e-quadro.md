---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-09-04
origem: unidades-07-08-p03-simbolo-menos-v1.md
nota_correcao: |-
  Correção de defeito de geração (v1 -> v2), 04/09/2026. O símbolo `-` do
  núcleo 1 saiu como uma barra azul vazia dentro de um retângulo arredondado
  (parece um botão de interface, não um sinal de menos). A tabela `COM
  OBJETOS` / `A CONTA` saiu embaralhada: colunas se misturaram, sinais `=`
  duplicados, e as contagens de `❌` não bateram com o segundo número da
  conta em nenhuma linha. Esta versão descreve o `-` como um traço grosso
  simples, sem moldura, e substitui a tabela por fitas fixas de quadrados
  (uma por linha, do tamanho do primeiro número), com o `-` marcado na
  divisa exata e os últimos quadrados marcados com X — mesma técnica de
  "quadro fixo" que funcionou na página 1 para o sinal `+`.
---
Use case: scientific-educational
Asset type: página 3 de uma sequência didática de Matemática do 1º ano


## PEDIDO

Apresentar o símbolo `-` para uma criança de aproximadamente 6 anos, sempre
ancorado a objetos concretos sendo retirados de um grupo, e mostrar um
exemplo de conta de separar com objetos ao lado do número. Espelha a
estrutura da página 1 (símbolo + exemplo), agora para o símbolo `-`. Os
problemas de separar e a decomposição ficam para a página 4.

Título previsto: O Símbolo - e o Símbolo de Separar

## SISTEMA VISUAL

Seguir `PADRAO-VISUAL-1ANO.md`: fundo branco puro `#FFFFFF`, ilustração
protagonista, 2 núcleos em recortes de papel separados por corredor de
branco, tipografia grande em caixa alta de imprensa. Papel fixo por cor:
azul `#2F6FD0` no símbolo `-` (conceito, espelha o azul da abertura da
página 1), amarelo `#F6C945` no exemplo de conta (destaque/"para lembrar",
mesma cor da página 1). Texto e contornos em grafite `#263238`. Colagem com
papel liso, bordas rasgadas, fita e sombra curta; sem grade digital.

## COMPOSIÇÃO E TÍTULO

- título `O SÍMBOLO - E O SÍMBOLO DE SEPARAR` em caixa alta de imprensa
  sobre papel azul rasgado, centralizado no alto — variação em relação aos
  títulos das páginas 1 e 2;
- núcleo 1, papel azul, ocupando a maior parte da página: o símbolo `-`
  desenhado como um ÚNICO TRAÇO GROSSO horizontal colorido, do mesmo estilo
  do sinal `+` da página 1 — nunca dentro de um botão, pílula ou retângulo
  com borda, nunca vazio; ao lado, 5 blocos de um grupo e uma seta mostrando
  2 deles saindo (riscados com X), ilustrando "tirar"; a frase-explicação ao
  lado (`O símbolo - se chama MENOS...` / `Quando vemos o -, sabemos que
  vamos retirar uma quantidade!`); abaixo, o post-it `📌 VEJA COMO FUNCIONA`
  com a frase-exemplo;
- núcleo 2, papel amarelo, tabela `COM OBJETOS` / `A CONTA`, quatro linhas
  (maçãs, estrelas, círculos azuis, círculos amarelos). Cada linha da coluna
  `COM OBJETOS` é uma FITA FIXA de quadrados iguais encostados lado a lado,
  cada quadrado com um único objeto da linha dentro. O tamanho da fita é o
  PRIMEIRO número da linha em `A CONTA` — nunca mais, nunca menos quadrados
  que esse número. Um sinal `-` (traço grosso, mesmo estilo do núcleo 1)
  fica marcado sobre a fita, na divisa entre dois quadrados; os quadrados à
  direita dessa divisa recebem um `❌` vermelho por cima do objeto (marcando
  "tirado"), os quadrados à esquerda ficam sem `❌` (o que sobrou). Por
  linha, contando quadrados da esquerda: maçãs — fita de 5, divisa depois do
  quadrado 3, dois últimos com `❌` (5-2=3); estrelas — fita de 4, divisa
  depois do quadrado 3, um último com `❌` (4-1=3); círculos azuis — fita de
  6, divisa depois do quadrado 3, três últimos com `❌` (6-3=3); círculos
  amarelos — fita de 7, divisa depois do quadrado 3, quatro últimos com `❌`
  (7-4=3). Abaixo da tabela, o post-it `💡 PARA LEMBRAR` com a frase final.

## TEXTOS EXATOS

Extraídos literalmente da fonte. Revisar: remover o que não cabe na página,
ajustar a ordem e condensar onde a leitura pedir — sem trocar número, nome
próprio, unidade ou termo técnico.

- O símbolo - se chama MENOS. Ele significa TIRAR ou SEPARAR.
- Quando vemos o -, sabemos que vamos retirar uma quantidade!
- 📌 VEJA COMO FUNCIONA
- 5 blocos - 2 blocos = tirar 2 blocos
- O - está no meio dizendo: "tire essa quantidade!"
- COM OBJETOS
- A CONTA
- 5 - 2 = 3
- 4 - 1 = 3
- 6 - 3 = 3
- 7 - 4 = 3
- 💡 PARA LEMBRAR
- O símbolo - significa TIRAR. O resultado sempre será MENOR que o número inicial!

## TRAVAS

Valem as travas de `autores/matematica/anos/1ano/REGRAS.md` e o `prompt_sufixo` do autor, que o gerador
injeta automaticamente.

Invioláveis, independentes de ano: não inventar número, nome próprio, data,
lugar, povo ou termo ausente da fonte; renderizar cada texto literal exatamente
uma vez; nenhum texto além da lista de TEXTOS EXATOS.

Fundo branco puro `#FFFFFF`; proibido creme, grade ou pontilhado contínuo.
Símbolo `-` é sempre um traço grosso colorido, nunca um retângulo, pílula ou
botão vazio; nunca aparece sozinho — sempre ao lado dos objetos sendo
retirados. Na tabela, cada linha é uma fita fixa de quadrados (tamanho =
primeiro número da linha) com o `-` na divisa certa e o `❌` só nos
quadrados à direita da divisa — ver COMPOSIÇÃO para o tamanho e a divisa de
cada linha. Não fundir os dois núcleos. Sem fotografia, sem balão de fala,
sem mascote.
