# Derivação de direção editorial entre anos

Regra compartilhada por todos os autores dos anos iniciais.

Quando um ano já tem direção editorial pronta e validada por produção, os
demais anos do mesmo autor **derivam dele** em vez de nascer do zero. Este
documento define o que muda entre um ano e outro, e o que nunca muda.

A derivação é **ponto de partida, não substituto**. Quando a fonte do ano chegar,
ela manda: o recorte real pode contrariar o que foi derivado, e nesse caso quem
cede é a derivação.

## Ano de referência de cada autor

O ano de referência é aquele que já produziu página aprovada. Ele não é o mesmo
em todos os autores, e a derivação corre em direções diferentes:

| Autor | Referência | Deriva para |
|---|---|---|
| `ingles` | 1º ano | 2º e 3º — subindo |
| `ingles-atividades` | 3º ano | 1º e 2º — descendo |
| `matematica` | 3º ano | 1º e 2º — descendo |
| `natureza-e-sociedade` | 3º ano | 1º e 2º — descendo |
| `matematica-atividades` | par de conteúdo | 1º, 2º e 3º |
| `natureza-e-sociedade-atividades` | par de conteúdo | 1º, 2º e 3º |
| `portugues` | autor `matematica` | derivação entre autores — ver abaixo |
| `portugues-atividades` | autor `portugues` | derivação entre autores — ver abaixo |

Quando um autor de atividades não tem ano de referência próprio, deriva do par
de conteúdo do mesmo ano e acrescenta as travas de atividade.

## Derivação entre autores

Quando um autor inteiro nasce sem nenhum ano de referência, ele deriva de **outro
autor** já maduro, e só então distribui a direção entre os seus anos.

A cadeia atual do repositório é `ingles` → `matematica` → `portugues` →
`portugues-atividades`. O padrão visual de `matematica` declara, no próprio
cabeçalho, ter nascido do formato do autor de Inglês; `portugues` derivou de
`matematica`, que é hoje o mais maduro — dezessete rodadas de produção e seis
páginas conferidas.

O que se herda numa derivação entre autores:

- o DNA visual e a composição — colagem, sketchnote, recortes, respiro branco;
- a paleta, com um papel semântico fixo por cor;
- a hierarquia de núcleos e a densidade por página;
- as regras de variação de título e de divisão de boxes;
- a estrutura do `AUTOR.md` e do padrão visual.

O que **não** se herda, e precisa ser reescrito para a disciplina de destino:

- os princípios pedagógicos;
- a trava central da disciplina;
- as regras específicas de conferência visual.

Esse último ponto é o que mais importa. Cada disciplina tem uma família de erros
que a geração comete com frequência, e o padrão precisa nomeá-la: em
`matematica` são as "regras matemáticas visuais" — quantidade que não bate com o
número, sinal trocado, face apontando para a parte errada. Em `portugues`, o
lugar equivalente é ocupado pelas "regras linguísticas visuais" — letra
espelhada, mistura de caixa alta com minúscula, acento fora de lugar, palavra
que não corresponde à imagem.

Herdar a seção sem reescrevê-la para a disciplina de destino produz um padrão
que parece completo e não protege contra nada.

Uma derivação entre autores herda também o que estiver **desatualizado** na
origem. Antes de derivar, confira se o `autor.yaml`, o padrão visual e a memória
do autor de origem concordam entre si; quando divergirem, derive da decisão
aprovada mais recente e registre a escolha.

## Os sete eixos que variam por ano

### 1. Autonomia de leitura

| Ano | Quem lê |
|---|---|
| 1º | o professor lê o enunciado em voz alta; a criança reconhece |
| 2º | a criança lê com apoio da imagem |
| 3º | a criança lê sozinha |

Esse eixo comanda os demais: uma página do 1º ano precisa funcionar mesmo
quando a criança ainda não decodifica o texto.

### 2. Extensão e estrutura do texto

Palavra isolada → frase curta → texto curto de gênero reconhecível.

### 3. Densidade da página

| Ano | Núcleos por página |
|---|---|
| 1º | 2 a 3 |
| 2º | 3 a 4 |
| 3º | 4 a 6 |

Núcleo é um bloco com uma intenção pedagógica própria. Descer de ano não é
apagar texto: é **remover núcleos inteiros** e desenvolver melhor os que ficam.

### 4. Tipografia e espaço de escrita

Corpo de texto e altura de pauta diminuem conforme a idade sobe, porque o traço
fica menor e mais firme. No 1º ano, pauta alta e poucas linhas; no 3º, pauta de
frase.

### 5. Nível de abstração

Objeto concreto → representação → símbolo e registro.

No 1º ano, a quantidade aparece como objeto contável; no 3º, o mesmo conteúdo
admite o símbolo sozinho. Descer de ano exige **reancorar no concreto**, não só
simplificar a frase.

### 6. Papel da ilustração

| Ano | Papel |
|---|---|
| 1º | protagonista: sustenta o sentido sozinha |
| 2º | apoio: dá a pista, o texto conclui |
| 3º | suporte: ancora o que já está escrito |

### 7. Proporção entre imagem e texto na composição

A área ocupada por imagem diminui conforme a idade sobe, e a área de texto e de
registro aumenta. A página do 1º ano é majoritariamente visual.

## O que nunca varia por ano

As travas invioláveis de cada disciplina valem igualmente do 1º ao 3º ano e não
podem ser afrouxadas em nome da idade:

- não inventar dado, espécie, nome científico, data, lugar, povo ou fato ausente
  da fonte;
- não antropomorfizar seres vivos;
- em páginas de atividade, **nada aparece respondido**;
- a letra impressa tem desenho correto, sem deformação nem espelhamento;
- todo texto visível está literal no prompt e é renderizado exatamente uma vez;
- representação de pessoas e comunidades sem estereótipo.

Simplificar para a criança menor nunca significa distorcer. Uma simplificação
que torna a informação falsa não é simplificação: é erro.

## Como derivar, na prática

1. partir do ano de referência do autor, não do modelo genérico;
2. percorrer os sete eixos e escrever o que muda naquele ano — só o delta;
3. copiar integralmente as travas invioláveis, sem afrouxar nenhuma;
4. marcar o arquivo derivado como **derivado**, indicando de qual ano veio;
5. deixar em aberto, explicitamente, o que só a fonte pode decidir.

Um arquivo derivado que não diz de onde veio vira, com o tempo, indistinguível
de direção validada por produção. Ele precisa dizer.
