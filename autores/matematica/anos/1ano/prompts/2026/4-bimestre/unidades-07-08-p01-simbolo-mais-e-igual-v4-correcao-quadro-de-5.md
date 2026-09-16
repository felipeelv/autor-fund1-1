---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-09-04
origem: unidades-07-08-p01-simbolo-mais-e-igual-v3-correcao-tabela-de-objetos.md
nota_correcao: |-
  Correção de defeito de geração (v3 -> v4), 04/09/2026. A v3 piorou o
  defeito da v2: as quatro linhas da tabela `COM OBJETOS` perderam o sinal
  "+" e o segundo grupo por completo, e duas frases obrigatórias do núcleo 2
  ("3 blocos + 2 blocos = juntar os blocos" e "O + está no meio dizendo...")
  não foram renderizadas. Contagem exata de objetos soltos é um limite
  conhecido do modelo (ver MEMORIA.md), e mais uma instrução explícita sobre
  o mesmo formato não converge. Esta versão muda o desenho: cada linha vira
  uma fita fixa de 5 quadrados (referência espacial fixa, como um quadro de
  5), com o sinal + marcado numa posição exata da fita — mesma técnica que
  funcionou para barras sobre linha de grade em outra unidade. Evita pedir
  ao modelo para desenhar e contar dois grupos soltos e um terceiro grupo
  total separado.
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
  lado, incluindo literalmente "3 blocos + 2 blocos = juntar os blocos" e "O +
  está no meio dizendo: junte esses dois grupos!"; do outro lado, o símbolo
  `=` grande com uma seta apontando para o número `5`, com a frase-explicação
  ao lado;
- núcleo 3, papel amarelo, tabela `COM OBJETOS` / `A CONTA`, quatro linhas
  (maçãs, estrelas, círculos azuis, círculos amarelos). Cada linha da coluna
  `COM OBJETOS` é desenhada como uma FITA FIXA de exatamente 5 quadrados
  iguais, encostados lado a lado, cada quadrado com contorno fino desenhado
  e um único emoji do objeto da linha dentro — nunca objetos soltos
  flutuando, sempre presos aos 5 quadrados da fita. Um sinal `+` fica
  desenhado sobre a fita, marcando a divisa exata entre o quadrado N e o
  quadrado N+1 (a fronteira entre o primeiro grupo, à esquerda, e o segundo
  grupo, à direita, até completar os 5 quadrados). Posição do `+` em cada
  linha, contando quadrados da esquerda: maçãs — depois do quadrado 2 (2+3);
  estrelas — depois do quadrado 3 (3+2); círculos azuis — depois do quadrado
  4 (4+1); círculos amarelos — depois do quadrado 1 (1+4). A fita inteira
  tem sempre 5 quadrados, nunca mais nem menos — ela já é o grupo total, sem
  desenhar um quarto grupo separado depois dela. Abaixo da tabela, o post-it
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
- 2 + 3 = 5
- 3 + 2 = 5
- 4 + 1 = 5
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
número que representam. Na tabela de exemplos, cada linha é uma fita de
exatamente 5 quadrados fixos com o sinal `+` na divisa certa (ver
COMPOSIÇÃO) — nunca objetos soltos sem os quadrados, nunca fita com mais ou
menos de 5 quadrados. Não fundir os três núcleos. Sem fotografia, sem balão
de fala, sem mascote.
