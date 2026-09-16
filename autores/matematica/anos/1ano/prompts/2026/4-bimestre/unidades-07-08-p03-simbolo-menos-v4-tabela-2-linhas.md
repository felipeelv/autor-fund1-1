---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-09-04
origem: unidades-07-08-p03-simbolo-menos-v3-correcao-contagem-da-fita.md
nota_correcao: |-
  Correção de defeito de geração (v3 -> v4), 04/09/2026. A v3 acertou a
  contagem da fita fixa em 2 das 4 linhas (maçãs 5-2=3 e estrelas 4-1=3);
  círculos azuis (6-3=3) e círculos amarelos (7-4=3) erraram a contagem em
  duas tentativas seguidas (v2 e v3) — limite conhecido do modelo para
  contagem exata de marcas repetidas. Em vez de insistir na mesma correção,
  esta versão reduz a tabela para as duas linhas que já saíram corretas,
  evitando o ponto onde o modelo erra, a pedido do revisor.
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
- núcleo 2, papel amarelo, tabela `COM OBJETOS` / `A CONTA`, DUAS linhas
  apenas (maçãs, estrelas). Cada linha da coluna `COM OBJETOS` é uma FITA
  FIXA de quadrados iguais encostados lado a lado, cada quadrado com um
  único objeto da linha dentro, sem quadrado vazio e sem objeto fora dos
  quadrados: linha 1 (maçãs) — exatamente 3 quadrados sem `❌` seguidos de
  exatamente 2 quadrados com `❌` vermelho por cima da maçã (fita de 5 no
  total, 5-2=3); linha 2 (estrelas) — exatamente 3 quadrados sem `❌`
  seguidos de exatamente 1 quadrado com `❌` (fita de 4 no total, 4-1=3). Um
  sinal `-` (traço grosso, mesmo estilo do núcleo 1) fica marcado sobre cada
  fita, logo depois do 3º quadrado, antes do primeiro quadrado com `❌`.
  Abaixo da tabela, o post-it `💡 PARA LEMBRAR` com a frase final.

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
retirados. Na tabela, apenas as DUAS linhas descritas em COMPOSIÇÃO — não
adicionar círculos azuis nem amarelos. Não fundir os dois núcleos. Sem
fotografia, sem balão de fala, sem mascote.
