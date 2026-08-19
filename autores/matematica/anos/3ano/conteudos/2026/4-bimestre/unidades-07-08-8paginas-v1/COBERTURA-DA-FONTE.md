# Cobertura da fonte — Unidades 7 e 8 · oito páginas · v1

Fonte:
`autores/matematica/anos/3ano/fontes/2026-2-semestre/4bim-grandezas-medidas-e-estatistica-v1.md`
(66 seções, conforme `preparar.py --inventario`).

Oito páginas não cobrem uma fonte de dois bimestres inteiros. Este arquivo
existe para que a seleção editorial seja **auditável**: o que entrou, o que
ficou apenas na fonte e por quê. Nada aqui autoriza inventar conteúdo — o que
não entrou continua existindo na fonte, apenas não virou página.

Recorte declarado em `recorte.yaml`, ao lado deste arquivo.

## O que entrou

| Página | Título | Seções da fonte |
|---|---|---|
| 1 | Metro, centímetro e milímetro | 4, 5, 8, 9, 10 |
| 2 | Convertendo unidades de comprimento | 11, 13 |
| 3 | O perímetro: a medida do contorno | 15, 16, 17 |
| 4 | Capacidade e massa: qual unidade usar | 21, 25, 29 |
| 5 | Pesquisa e organização em tabelas | 31, 32, 35, 36, 37 |
| 6 | Gráfico de barras: ler e construir | 40, 41 |
| 7 | Gráfico de linhas e qual gráfico usar | 44, 45, 46 |
| 8 | Probabilidade: certo, impossível e possível | 55, 56, 57, 58 |

Quatro páginas para a Unidade 7 e quatro para a Unidade 8. As aberturas de
unidade (seções 5 e 32) entram nas páginas 1 e 5, que por isso carregam os dois
maiores títulos da sequência.

## O que ficou somente na fonte

Cortes por limite de oito páginas, sem impedimento de conteúdo:

- **12** Mais Exemplos de Conversão — a página 2 já ensina a conversão pela
  seção 11; estes exemplos adicionais são reforço.
- **14** Estimando Comprimentos — depende de manipulação em sala, rende mais
  como atividade que como página de conteúdo.
- **20, 24** O Que É Capacidade? / O Que É Massa? — as definições ficam
  implícitas nos pares de unidade da página 4, que tem uma intenção só.
- **22, 23, 26, 27, 28** Exemplos e conversões detalhadas de capacidade e
  massa, e instrumentos para medir massa.
- **30** Resumo das Unidades — a página 4 já fecha com a escolha da unidade.
- **38, 39** Construindo Tabelas / Tabela com Mais Variáveis.
- **43, 47, 48, 49** Lendo Gráficos de Barras / de Linhas, Comparando e
  Interpretando Gráficos — a leitura entra dentro das páginas 6 e 7, mas as
  baterias de perguntas ficam fora.
- **52, 53, 54** Analisando Dados, Comparando Dados, Problemas com Gráficos —
  o Capítulo 2 da Unidade 8 entra no lote apenas pela probabilidade.
- **59, 60, 61, 62, 63** Comparando Chances, Mais Provável × Menos Provável,
  Probabilidade com Dados e com Moedas, Resumo: Probabilidade.
- **64, 65, 66** Resumo do bimestre, O Que Você Precisa Lembrar e Parabéns —
  fecho do material, não conteúdo novo.

## Corte por integridade da fonte — pendência para decisão humana

- **42 Gráfico de Barras Duplas** — **não entrou, e o motivo não é espaço.**
  O gráfico está registrado na fonte como arte ASCII, e essa arte é
  internamente inconsistente: a mesma coluna aparece com o preenchimento de
  Meninos numa linha e o de Meninas na linha seguinte, e as colunas somam seis
  posições onde cinco categorias × dois grupos exigiriam dez. Não há como
  derivar os valores sem inventar número, o que a seção 6 do `CLAUDE.md`
  proíbe. Registrado aqui em vez de corrigido por conta própria.

  Para destravar, uma pessoa precisa fornecer os dez valores (cinco frutas ×
  meninos/meninas) ou autorizar outra representação. Enquanto isso, a página 6
  cobre o gráfico de barras simples, a leitura das partes e o passo a passo de
  construção — conteúdo íntegro das seções 40 e 41.

## Cortes dentro de seção

A tabela acima diz quais seções entraram. Dentro delas, ainda houve seleção —
por densidade da página, nunca por impedimento de conteúdo. Registrado aqui
porque uma ausência não explicada é indistinguível de um esquecimento:

- **p1 e p5** — o bloco `O QUE VAMOS APRENDER NESTA UNIDADE?` e seus seis
  tópicos, nas duas aberturas de unidade. É uma lista tudo-ou-nada: truncá-la
  afirmaria algo falso sobre a unidade, e mantê-la inteira importaria para a
  página conteúdo que pertence às páginas seguintes. Segue o precedente da
  abertura aprovada da Unidade 5, no 3º bimestre.
- **p3** — a figura em L e sua dica, o problema da moldura, a forma
  `2 × 6 + 2 × 4`, os rótulos `Problema 1:`/`Problema 3:` e a linha
  `Calcule o perímetro desta figura:`.
- **p4** — a subtabela `Para comprimento:` (mm/cm/m/km) da seção 29: é conteúdo
  das páginas 1 e 2 e quebraria a intenção única desta página.
- **p5** — o `PARA LEMBRAR` da seção 32, para não passar do teto de sete
  núcleos do `PADRAO-VISUAL-3ANO.md`. O passo a passo da pesquisa virou fita de
  seis etiquetas numeradas em vez de tabela, para que a página tenha uma única
  grade e essa grade seja a tabela de frequência, que é o assunto.
- **p8** — a tabela `PALAVRA | SIGNIFICA` inteira (`Provável`, `Improvável` e
  demais), que pertence à escala de probabilidade e não aos três tipos de
  evento; mais três linhas de exemplo que duplicavam raciocínio já presente
  (`Dezembro vem depois de novembro`, `Água líquida a -20°C`, `Ganhar um jogo`).

## Literais recuperados da fonte

O extrator não captura títulos de seção nem toda célula de tabela. Os itens
abaixo **estão na fonte**, nas linhas indicadas, e foram devolvidos à lista de
TEXTOS EXATOS — não são invenção:

- `UNIDADE 7` (linha 32), `GRANDEZAS E MEDIDAS` (34) e
  `MEDIDAS DE COMPRIMENTO` (54), sem os quais a página 1 não teria título;
- `UNIDADE 8` (567), `ESTATÍSTICA E PROBABILIDADE` (569),
  `Organizando com Tabelas` (638) e o segundo `TOTAL` (651), rótulo da linha
  final da tabela, que o achatamento havia engolido;
- `GRÁFICO DE BARRAS` como título do selo da página 6 e a escala vertical
  `0 1 2 3 4 5 6 7 8`, licenciada pelo passo 3 da própria seção 41.

Os marcadores de exportação da fonte — os glifos de lâmpada e percevejo que
abrem os boxes, e o traço duplo de lista — não são conteúdo e não são
renderizados: viram desenho à mão na colagem. As páginas 2, 3 e 5 receberam
uma versão `-v2-sem-emoji` só para isso.

## Gráficos decodificados e conferidos

Os dois gráficos que entraram no lote foram decodificados da arte ASCII da
fonte e conferidos posição a posição. Os prompts das páginas 6 e 7 carregam
estes valores como restrição explícita, porque sem eles a imagem volta com
barras e curvas arbitrárias e não há o que conferir:

- **Página 6 — FRUTA FAVORITA DA TURMA:** Maçã 6, Banana 8, Uva 4, Laranja 5,
  Morango 7. Banana é a barra mais alta; Uva, a mais baixa.
- **Página 7 — TEMPERATURA MÁXIMA DA SEMANA (°C):** Seg 26, Ter 28, Qua 30,
  Qui 30, Sex 32, Sáb 26, Dom 24. A linha sobe até sexta, que é o pico, e cai
  até domingo, que é o ponto mais baixo; quarta e quinta ficam na mesma altura.
