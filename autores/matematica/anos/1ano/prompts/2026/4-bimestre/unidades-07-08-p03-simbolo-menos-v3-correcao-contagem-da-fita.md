---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-09-04
origem: unidades-07-08-p03-simbolo-menos-v2-correcao-simbolo-e-quadro.md
nota_correcao: |-
  Correção de defeito de geração (v2 -> v3), 04/09/2026. O sinal "-" ficou
  correto (traço grosso), mas a fita de quadrados errou a contagem nas
  quatro linhas: sobrou um quadrado a mais sem X em cada linha (ex.: maçãs
  saiu 4 sem X + 2 com X = 6 quadrados, deveria ser 3 sem X + 2 com X = 5).
  A instrução "divisa depois do quadrado 3" parece ter sido mal contada.
  Esta versão troca a instrução por contagem direta de cada lado (quantos
  quadrados sem X, quantos com X), sem depender de posição de divisa.
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
  cada quadrado com um único objeto da linha dentro, sem nenhum quadrado
  vazio e sem objeto fora dos quadrados. Todas as quatro linhas têm
  EXATAMENTE 3 quadrados SEM `❌` no início da fita (contar 1, 2, 3 e parar
  — nunca um quarto quadrado sem `❌`), seguidos pelos quadrados restantes
  já marcados com `❌` vermelho por cima do objeto. Contagem de quadrados
  com `❌` em cada linha, e total de quadrados da fita (3 sem `❌` + os
  quadrados com `❌`): maçãs — 2 quadrados com `❌` (fita de 5 no total);
  estrelas — 1 quadrado com `❌` (fita de 4 no total); círculos azuis — 3
  quadrados com `❌` (fita de 6 no total); círculos amarelos — 4 quadrados
  com `❌` (fita de 7 no total). Um sinal `-` (traço grosso, mesmo estilo do
  núcleo 1) fica marcado sobre a fita, logo depois do 3º quadrado, antes do
  primeiro quadrado com `❌`. Abaixo da tabela, o post-it `💡 PARA LEMBRAR`
  com a frase final.

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
retirados. Na tabela, cada linha tem EXATAMENTE 3 quadrados sem `❌` no
início — nunca 4 — e o número de quadrados com `❌` da COMPOSIÇÃO, nem mais
nem menos. Não fundir os dois núcleos. Sem fotografia, sem balão de fala,
sem mascote.
