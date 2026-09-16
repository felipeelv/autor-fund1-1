# Memória editorial — `portugues`

## Identidade estável

- disciplina: Língua Portuguesa, páginas de conteúdo;
- público: 1º ao 3º ano do Fundamental I;
- formato: `apostila-fund1`;
- modelo padrão: xAI `grok-imagine-image-2.0`;
- modelo alternativo autorizado em projeto declarado: OpenAI `gpt-image-2`;
- linguagem visual: colagem editorial, sketchnote e visual note-taking sobre
  **fundo branco puro**, com o branco visível como corredor entre os recortes;
- saída: sempre externa, primeiro em `_revisao`.

## Origem do autor

Criado em 18 de agosto de 2026, junto com a separação entre conteúdo e
atividades. A disciplina não existia no repositório até então.

A primeira direção foi escrita do zero e substituída no mesmo dia por uma
**derivada do autor `matematica`**, que é o mais maduro do repositório —
dezessete rodadas de produção e seis páginas conferidas. Vieram de lá a
estrutura do `AUTOR.md`, o DNA visual, a paleta com um papel fixo por cor, a
hierarquia de núcleos, as regras de variação de título e de divisão de boxes.

O próprio `matematica` nasceu derivado do autor `ingles`, o que torna essa a
terceira geração da mesma linguagem visual.

## Decisão sobre o fundo

Adotado **branco puro `#FFFFFF`**, sem creme, grade ou pontilhado contínuo.

Vale registrar de onde vem a decisão: o `PADRAO-VISUAL-3ANO.md` e a memória do
autor `matematica` registram esse ajuste como aprovado em 14 de agosto de 2026
("evitar fundos quentes e cabeçalhos repetitivos"), mas o `prompt_prefixo` do
`autor.yaml` de lá ainda pede "fundo branco quente com grade pontilhada muito
sutil". Português foi derivado da versão aprovada, não da desatualizada.

## O que muda em relação a Matemática

A trava central da disciplina não é numérica, é tipográfica: **a letra é
conteúdo**. Onde Matemática confere quantidades, sinais e classificações,
Português confere desenho de letra, tipo de letra, acentuação, segmentação
silábica e correspondência entre palavra e imagem.

As "regras matemáticas visuais" do padrão de origem foram substituídas pelas
"regras linguísticas visuais", com a mesma função: são os pontos que mais erram
na geração e os primeiros que a conferência humana precisa olhar.

## Estado

**Fonte recebida (18-19/08/2026) para 1º, 2º e 3º ano.** Primeiro lote real:
2º ano, 3º bimestre, Unidade 6 ("Criando Quadrinhos"), 8 páginas, aprovadas em
19/08/2026 por Nicolas Basso. A direção segue derivada do `matematica`, mas o
ajuste humano que faltava (ver seção acima) já aconteceu na prática, dentro
desse lote — registrado em `PADRAO-VISUAL-2ANO.md`.

O que esse lote confirmou para o 2º ano: minúscula de imprensa já em uso no
corpo do texto (caixa alta só em onomatopeia, ênfase e sigla, como a própria
fonte já grafa); 3-4 núcleos por página funcionam bem quando a colagem é
densa, sem faixas horizontais soltas; material e formato do recorte devem
variar página a página, inclusive o estilo do título; tabela solta na fonte
precisa ser reconstituída como tabela real na composição, não como lista.

Continuam em aberto para 1º e 3º ano, que ainda não têm recorte:

- quais eixos o material cobre em cada ano;
- se a alfabetização segue método específico e qual;
- quais gêneros textuais entram, e em que ano;
- se a letra cursiva entra em algum momento, e quando.

## Segundo lote do 2º ano (Unidades 7-8, 4º bimestre) — 08/09/2026

12 páginas aprovadas por Nicolas Basso. Confirma tudo do primeiro lote e
acrescenta:

- **checklist ou lista longa de itens: sempre em coluna única, nunca em
  grade fixa de 3 colunas.** Numa página de revisão com 5 sub-listas de
  tamanhos diferentes (7, 6, 9, 5 e 7 itens), pedir grade 3x3 fez o modelo
  inventar item para completar a última linha (texto corrompido tipo "OJ
  problerma?" e "Uetra miáscuiro ruviodo?"), duplicar item ou omitir um. A
  correção — trocar para lista vertical de 1 coluna e declarar a contagem
  exata de itens por bloco — resolveu de primeira;
- **"Nesta unidade, você vai:" (capa/objetivos no início da fonte de cada
  unidade) precisa entrar na primeira página.** Ficou de fora por engano na
  Unidade 6 (nunca usado) e de novo na v1 deste lote; passa a ser regra:
  todo primeiro recorte de uma unidade nova inclui esse bloco;
- limite de 8.000 bytes do prompt (ver `PADRAO-VISUAL-2ANO.md`) aperta
  bastante em página com banco de palavras grande — a prosa de SISTEMA
  VISUAL/COMPOSIÇÃO precisa ficar telegráfica para sobrar espaço para a
  lista de TEXTOS EXATOS, que não pode ser cortada;
- o parser de `preparar.py --inventario`/`--recorte` pode perder um trecho
  de fonte dentro de uma seção (aconteceu com o exemplo do "Passo 6:
  Planejar a Solução" — só a palavra "Exemplo:" foi extraída, a frase entre
  aspas ficou de fora). Conferir sempre o rascunho contra a fonte bruta
  antes de escrever o prompt final, não só contra a lista de TEXTOS EXATOS
  gerada automaticamente;
- defeito recorrente e de baixa severidade: vírgula ou aspas de fechamento
  sobrando no fim da última linha de uma lista/citação. Não vale regenerar
  a página inteira por isso — é item de revisão humana final, não de
  correção de prompt.

## Unidades 7-8 do 3º ano, 4º bimestre (09/09/2026)

16 páginas aprovadas por Nicolas Basso (Unidade 7 — humor, discurso
direto/indireto e verbos; Unidade 8 — textos instrucionais e numerais).
Ver `../anos/3ano/ORGANIZACAO.md` para o detalhamento por página. O que
este lote acrescenta às regras já registradas:

- **erro ortográfico pontual que resiste a um simples aviso de correção
  no prompt pode precisar de isolamento visual, não só texto de aviso.**
  Três palavras (verbo "Misture", "xícaras", "Ordem") saíram erradas duas
  vezes seguidas mesmo com "CORREÇÃO SOBRE O V1/V2" explicando o defeito
  em prosa. Só resolveu quando a composição pediu a palavra isolada,
  sozinha, em destaque (selo, letras grandes) imediatamente antes da frase
  completa — o modelo copia corretamente a partir do próprio destaque
  vizinho. Vale como segunda tentativa de correção quando a primeira
  (só descrever o defeito) não resolver;
- **quando o volume de conteúdo entre unidades do mesmo bimestre é muito
  desigual, a divisão de páginas não precisa ser simétrica.** A Unidade 8
  tinha ~60% mais conteúdo extraível que a Unidade 7 no primeiro capítulo;
  dividir 4+4 teria comprimido desproporcionalmente o capítulo maior. A
  divisão ficou 5+3, proporcional ao volume real de cada capítulo;
- condensação editorial (remover exemplo, reduzir lista a amostra
  representativa) é diferente de inventar — mas precisa ficar registrada
  no `recorte.yaml` e no `PEDIDO` de cada prompt, com a contagem explícita
  do que ficou de fora (ex.: "amostra de 12 verbos, dos 20 da fonte");
- o parser de `preparar.py --recorte` perde passos escritos em linha
  corrida sem marcador de lista (não só o caso já registrado de frase
  dentro de seção) — conferir sempre contra a fonte bruta, seção a seção,
  antes de fechar o prompt final;
- prompt no limite de 8000 bytes: adicionar uma nota de correção
  ("CORREÇÃO SOBRE O V1") a um prompt já denso pode ele mesmo estourar o
  limite — cortar prosa de SISTEMA VISUAL/COMPOSIÇÃO antes de cortar
  TEXTOS EXATOS.
