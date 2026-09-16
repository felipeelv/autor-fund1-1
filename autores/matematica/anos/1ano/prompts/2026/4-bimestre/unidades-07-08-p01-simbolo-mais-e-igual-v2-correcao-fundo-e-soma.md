---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-09-03
origem: unidades-07-08-p01-simbolo-mais-e-igual-v1.md
nota_correcao: |-
  Correção de defeito de geração (v1 -> v2), 03/09/2026. A v1 cobriu a
  página inteira com papel colorido, sem nenhum corredor de branco puro
  entre os três núcleos nem nas bordas -- violação direta da trava de fundo,
  mesmo com a instrução já presente em SISTEMA VISUAL e TRAVAS. A tabela
  "COM OBJETOS" também saiu incompleta: mostrou só a quantidade inicial e a
  final ligadas por "=", sem o sinal "+" nem o segundo grupo de objetos --
  perdendo o sentido de "juntar" que é o objetivo da página. Esta versão
  reforça as duas instruções com linguagem mais explícita e concreta.
---
Use case: scientific-educational
Asset type: página 1 de uma sequência didática de Matemática do 1º ano


## PEDIDO

Abrir a Unidade 7 apresentando os símbolos `+` e `=` para uma criança de
aproximadamente 6 anos: os quatro objetivos da unidade, o significado de cada
símbolo (juntar / mostrar o resultado) sempre ancorado a objetos concretos, e
um exemplo de conta de juntar com objetos ao lado do número. Nenhum símbolo
aparece sozinho — está sempre ao lado da quantidade que representa. O símbolo
`-` e os problemas ficam para as páginas 2 e 3.

Título previsto: O Símbolo + e o Símbolo =

## SISTEMA VISUAL

Seguir `PADRAO-VISUAL-1ANO.md`: fundo branco puro `#FFFFFF` visível e
CONTÍNUO ao redor de toda a página e como corredor entre os três recortes de
papel — os recortes são ilhas de cor sobre o branco, nunca um mosaico que
cobre a página de ponta a ponta. Margem branca mínima de 4% da largura em
todas as bordas da página, e uma faixa branca de pelo menos 3% da altura
entre cada par de núcleos consecutivos. Ilustração protagonista, 3 núcleos
em recortes de papel, tipografia grande em caixa alta de imprensa. Papel
fixo por cor: azul `#2F6FD0` na abertura (conceito, é a primeira página da
unidade), verde `#43A66B` no núcleo dos dois símbolos (verificação — "veja
como funciona"), amarelo `#F6C945` no exemplo de conta (destaque/"para
lembrar"). Texto e contornos em grafite `#263238`. Colagem com papel liso,
bordas rasgadas, fita e sombra curta — a sombra curta só existe se houver
branco por baixo dela; sem grade digital, sem 3D decorativo.

## COMPOSIÇÃO E TÍTULO

- título `O SÍMBOLO + E O SÍMBOLO =` em caixa alta de imprensa sobre papel
  azul rasgado, alto e à esquerda — o maior título da sequência de 4 páginas
  da Unidade 7, por ser abertura;
- núcleo 1, abertura, papel azul: `O QUE VAMOS APRENDER?` com as quatro metas
  em lista; ilustração de uma criança brasileira juntando blocos coloridos ao
  lado;
- núcleo 2, papel verde: de um lado o símbolo `+` grande e colorido com 3
  blocos azuis se juntando a 2 blocos vermelhos (total 5 blocos, sem somar o
  resultado em número aqui — só o gesto de juntar), com a frase-explicação ao
  lado; do outro lado do mesmo recorte (ou recorte irmão), o símbolo `=`
  grande com uma seta apontando para o número `5`, com a frase-explicação ao
  lado;
- núcleo 3, papel amarelo, tabela `COM OBJETOS` / `A CONTA` com as quatro
  linhas de exemplos de juntar (maçãs, estrelas, círculos azuis, círculos
  amarelos). Cada linha da coluna `COM OBJETOS` desenha OBRIGATORIAMENTE
  TRÊS grupos separados, na ordem exata do texto: primeiro grupo de objetos,
  um sinal `+` desenhado entre os grupos, segundo grupo de objetos, um sinal
  `=` e o grupo final com o total de objetos — nunca apenas "grupo inicial =
  grupo final" sem o `+` e o segundo grupo. Exemplo da linha 1: 2 maçãs, o
  sinal `+`, 3 maçãs, o sinal `=`, 5 maçãs; assim para as quatro linhas,
  cada uma com sua própria contagem (ver TEXTOS EXATOS); abaixo, o post-it
  `💡 PARA LEMBRAR` com a frase final.

## TEXTOS EXATOS

Extraídos literalmente da fonte. Revisar: remover o que não cabe na página,
ajustar a ordem e condensar onde a leitura pedir — sem trocar número, nome
próprio, unidade ou termo técnico.

- O QUE VAMOS APRENDER?
- - Os símbolos + e - e o que eles significam
- - Fazer continhas simples (até 10)
- - Diferentes formas de "fazer" um número
- - Resolver problemas com registro
- O símbolo + se chama MAIS. Ele significa JUNTAR.
- Quando vemos o +, sabemos que vamos colocar quantidades juntas!
- 📌 VEJA COMO FUNCIONA
- 3 blocos + 2 blocos = juntar os blocos
- O + está no meio dizendo: "junte esses dois grupos!"
- O símbolo = se chama IGUAL. Ele significa "o resultado é" ou "ficou".
- Quando vemos o =, sabemos que depois dele vem a RESPOSTA!
- 3 + 2 = 5
- O = está dizendo: "o resultado é 5" ou "ficou 5"
- COM OBJETOS
- A CONTA
- 🍎🍎 + 🍎🍎🍎 = 🍎🍎🍎🍎🍎
- 2 + 3 = 5
- ⭐⭐⭐ + ⭐⭐ = ⭐⭐⭐⭐⭐
- 🔵🔵🔵🔵 + 🔵 = 🔵🔵🔵🔵🔵
- 4 + 1 = 5
- 🟡 + 🟡🟡🟡🟡 = 🟡🟡🟡🟡🟡
- 1 + 4 = 5
- 💡 PARA LEMBRAR
- O símbolo + significa JUNTAR. O símbolo = mostra o RESULTADO.

## TRAVAS

Valem as travas de `autores/matematica/anos/1ano/REGRAS.md` e o `prompt_sufixo` do autor, que o gerador
injeta automaticamente.

Invioláveis, independentes de ano: não inventar número, nome próprio, data,
lugar, povo ou termo ausente da fonte; renderizar cada texto literal exatamente
uma vez; nenhum texto além da lista de TEXTOS EXATOS.

Fundo branco puro `#FFFFFF` visível e contínuo nas bordas da página e entre
os três núcleos — proibido cobrir a página inteira de papel colorido de
ponta a ponta; proibido creme, grade ou pontilhado contínuo. Símbolo `+` e
símbolo `=` nunca aparecem sozinhos — sempre ao lado dos objetos ou do
número que representam. Na tabela de exemplos, cada linha da coluna
`COM OBJETOS` mostra três grupos (adendo 1, `+`, adendo 2, `=`, total) —
nunca dois grupos ligados direto por `=`. Contagem exata em cada linha:
2+3=5, 3+2=5, 4+1=5, 1+4=5 — todos os grupos somam exatamente 5 objetos, sem
objeto a mais ou a menos. Não fundir os três núcleos. Sem fotografia, sem
balão de fala, sem mascote.
