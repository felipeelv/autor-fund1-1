# Registro de produção — Unidades 7 e 8 · oito páginas · v1

Data: 19/08/2026
Estado: **imagens em `_revisao`, aguardando conferência humana.** Nada foi
promovido com `aprovar.py`.

## Origem

Primeiro lote do 4º bimestre do 3º ano, a partir de
`anos/3ano/fontes/2026-2-semestre/4bim-grandezas-medidas-e-estatistica-v1.md`.
Quatro páginas de Grandezas e Medidas (Unidade 7) e quatro de Estatística e
Probabilidade (Unidade 8).

Recorte, cobertura da fonte, cortes dentro de seção e valores decodificados dos
gráficos em `../../conteudos/2026/4-bimestre/unidades-07-08-8paginas-v1/`.

## Execução

- provider: `openrouter` → `x-ai/grok-imagine-image-2.0` (não há `XAI_API_KEY`
  nativa neste ambiente; rota autorizada em `CLAUDE.md` §3);
- qualidade `medium`, JPEG, proporção `2:3`, resolução `2k`, tamanho `auto`;
- dimensões entregues: 1664×2496;
- um projeto YAML por página, em `../../projetos/2026/4-bimestre/`, para
  permitir gerar em ondas e regerar uma página isolada;
- custo ~US$ 0,08 por imagem.

## Versão final de cada página

| Página | Prompt final | Por que não é `-v1` |
|---|---|---|
| 1 Metro, centímetro e milímetro | `-v1` | — |
| 2 Convertendo unidades | `-v2-sem-emoji` | glifos de lâmpada/percevejo na lista de literais, e a composição mandava desenhá-los "no lugar" do glifo — instrução contraditória |
| 3 O perímetro | `-v2-sem-emoji` | idem |
| 4 Capacidade e massa | `-v1` | — |
| 5 Pesquisa e tabelas | `-v2-sem-emoji` | idem |
| 6 Gráfico de barras | `-v3-barras-na-malha` | ver abaixo |
| 7 Gráfico de linhas | `-v1` | — |
| 8 Probabilidade | `-v1` | — |

A página 6 teve três versões. A `-v2` corrigiu a tabela do passo a passo, que
o corte de bytes havia degradado em paráfrase, violando a trava de "célula por
célula". A `-v3` nasceu da conferência da imagem gerada pela `-v2`: as barras
da Uva e do Morango terminavam **entre** duas linhas da malha (Uva em ~4,4 em
vez de 4), o que numa página que ensina a ler valor exato num gráfico é erro de
conteúdo, não de estética. A `-v3` acrescenta a trava de que o topo de cada
barra cai exatamente sobre a linha da malha do seu número. A imagem da `-v2`
foi preservada.

## Conferência já feita pela orquestração

As oito imagens foram conferidas item a item contra os TEXTOS EXATOS. Seis
páginas saíram com o conteúdo correto: **p1, p2, p3, p4, p6 e p8**. Nelas,
todos os literais estão presentes e corretos, os números e unidades batem com a
fonte, as tabelas foram reconstituídas na ordem certa, o fundo é branco puro e
não há glifo de emoji.

Duas páginas têm defeito **de renderização quantitativa** que sobreviveu a mais
de uma tentativa. O texto do prompt está certo nas duas; o que falha é a
capacidade do modelo de posicionar ou contar marcas com exatidão.

### p5 — a coluna CONTAGEM não bate com os números

A fonte pede N marcas iguais por linha, batendo com a coluna TOTAL. Duas
gerações falharam:

- `-v2-sem-emoji`: marcas agrupadas de cinco em cinco, contagens muito erradas,
  e Maçã e Banana com desenho idêntico apesar de totais diferentes (6 e 8);
- `-v3-contagem-avulsa`: marcas soltas e contáveis, como pedido, mas ainda
  erradas em três linhas — Banana com 7 traços para o total 8, Laranja com 6
  para 5, Morango com 8 para 7. Os traços somam 31 contra os 30 declarados.
  Maçã (6) e Uva (4) saíram certas.

A coluna TOTAL está internamente correta nas duas versões (6+8+4+5+7 = 30). O
mesmo render trouxe ainda `Exemplos de pesquiras:` no lugar de
`Exemplos de pesquisas:`.

### p7 — os pontos do gráfico de linhas

- `-v1`: Qua e Qui em 28 (deviam ser 30) e Sex em ~31 (devia ser 32). O formato
  da curva estava certo, com o pico na sexta;
- `-v2-pontos-na-malha`: Qua e Qui corrigidos para 30, mas Sex caiu para 30 —
  o pico da semana desapareceu — e surgiu um ponto órfão em Qui/28, exatamente
  o valor que a trava mandava evitar;
- `-v3-so-afirmacoes`: reescrita sem nenhuma restrição negativa, porque a
  negação parece ter sido renderizada como conteúdo na v2. **Saiu pior**: a
  linha se partiu em dois caminhos sobrepostos, com mais de sete pontos e
  cruzamentos. Descartada.

Nenhuma das três serve como está. A `-v1` conta a história certa — sobe ao
longo da semana, pico na sexta, mínimo no domingo — com três valores errados.
A `-v2` acerta seis dos sete valores, mas achata o pico da sexta, que é
justamente o que a página ensina a ler. Escolher entre elas é decisão
editorial, não técnica.

**Sobre a hipótese da negação:** a v2 trouxe um ponto órfão exatamente no valor
que a trava mandava evitar, o que sugeria que restrição negativa vira desenho.
A v3 testou a hipótese removendo toda negação — e saiu pior. Então a negação
não era a causa principal. Fica como suspeita razoável, não como regra: vale
preferir a descrição afirmativa, mas não vale gastar geração para "consertar"
uma página só trocando negação por afirmação.

## Decisão pendente

Os defeitos da p5 e da p7 não parecem resolvíveis por reescrita de prompt:
cinco gerações no total (duas da p5, três da p7), com formulações
progressivamente mais explícitas, e nenhuma acertou. Posicionar ponto em
coordenada exata e contar marcas repetidas são limites do modelo, não falhas de
redação. Em vez de gastar crédito às cegas, os caminhos para decisão humana:

**p5 — coluna CONTAGEM**

1. redesenhar a coluna para algo que o modelo acerte — por exemplo, uma única
   linha com a contagem exemplificada e as demais só com o número;
2. aceitar a página e corrigir a coluna à mão na diagramação;
3. manter como está, se a coluna for considerada ilustrativa — o que colide com
   "quantidades desenhadas devem coincidir com os números" do
   `PADRAO-VISUAL-3ANO.md`.

Em qualquer caminho, `Exemplos de pesquiras:` precisa virar
`Exemplos de pesquisas:`.

**p7 — pontos do gráfico**

1. escolher entre a `-v1` (forma certa, valores errados) e a `-v2` (valores
   quase certos, sem pico) e corrigir o resto à mão;
2. simplificar o gráfico para menos pontos ou uma escala de 1 em 1 grau, que
   dá menos margem para o modelo errar;
3. desenhar o gráfico fora do gerador e compor a página com ele.

## Conferência humana — o que olhar primeiro

Por disciplina, `CLAUDE.md` §6 exige conferir números, sinais, cálculos,
unidades e classificações geométricas. Nesta unidade, os pontos de maior risco:

- **p6** — as cinco alturas: Maçã 6, Banana 8, Uva 4, Laranja 5, Morango 7,
  cada topo sobre a linha da malha. Banana é a mais alta; Uva, a mais baixa.
- **p7** — os sete pontos: Seg 26, Ter 28, Qua 30, Qui 30, Sex 32, Sáb 26,
  Dom 24. Sobe até sexta, quarta e quinta na mesma altura, mínimo no domingo.
- **p5** — a tabela de frequência: contagens 6, 8, 4, 5 e 7, somando 30, com o
  número de traços desenhados igual ao número escrito em cada linha. Confere
  com `ENTREVISTADOS: 30`.
- **p3** — o número de lados desenhados igual ao de parcelas da soma (3 no
  triângulo, 4 no retângulo, 4 no quadrado) e os resultados 12 cm, 20 cm,
  20 cm e 80 metros.
- **p1 e p2** — as equivalências (`1 metro = 100 centímetros`,
  `1 centímetro = 10 milímetros`, `1 metro = 1.000 milímetros`) e os seis
  exemplos de conversão, dígito por dígito.
- **p8** — cada evento na classificação que a fonte dá; trocar um exemplo entre
  certo, impossível e possível é erro de conteúdo.

Vale conferir também que nenhuma página traz glifo de emoji e que o fundo é
branco puro — o `prompt_prefixo` do `autor.yaml` ainda pede "branco quente com
grade pontilhada", contrariando o ajuste aprovado em 14/08/2026, e cada prompt
anula isso nas TRAVAS. Corrigir o prefixo na origem continua pendente de
decisão humana, porque muda a identidade visual de todos os lotes futuros.
