# Memória editorial — `natureza-e-sociedade`

## Identidade estável

- disciplina: Natureza e Sociedade;
- público: 3º ano do Fundamental I;
- formato: `apostila-fund1`;
- modelo padrão: xAI `grok-imagine-image-2.0`;
- modelo alternativo autorizado em projeto declarado: OpenAI `gpt-image-2`;
- linguagem visual: colagem, sketchnote e visual note-taking;
- fundo editorial: branco puro `#FFFFFF`;
- composição: colagem densa em camadas sobrepostas, com hierarquia de capa
  monumental e páginas internas de título discreto;
- representação: diversidade contemporânea, sem estereótipos ou fusão de
  elementos culturais;
- saída: sempre externa, primeiro em `_revisao`.

## Fonte inicial

A pauta “Infográfico sobre Povos Indígenas”, recuperada de uma conversa
anterior, foi consolidada em 15 de agosto de 2026. O texto recebido foi tratado
como pauta, não como fonte factual final. A fonte interna registra as consultas
a IBGE, Funai, Prefeitura de Ribeirão Preto e pesquisa acadêmica.

## Decisões do primeiro lote

> Duas destas decisões foram **revogadas em 15 de agosto de 2026**, quando o
> Felipe entregou a fonte v2 e aprovou o lote v3. Estão marcadas abaixo.
> As demais continuam valendo.

- manter a ideia de que a história do território antecede 1500;
- ~~trocar a afirmação direta “Aqui moravam os Caiapós” por uma formulação que
  explica o uso histórico e genérico do nome “Caiapó”~~ — **revogada**: a fonte
  v2 afirma a atribuição direta, e a página 2 aprovada a imprime. A conferência
  histórica segue pendente de revisão humana;
- retirar números antigos ou sem base clara;
- usar no fechamento os dados do Censo 2022: quase 1,7 milhão de indígenas,
  391 povos e 295 línguas;
- não atribuir os mesmos hábitos, formas de decisão ou práticas ambientais a
  todos os povos;
- ~~não inserir conexão bíblica na imagem enquanto o formato institucional
  correspondente permanecer em aberto~~ — **revogada para este autor**: a fonte
  v2 determina o bloco bíblico, e a página 6 aprovada imprime Atos 17:26 (NVI).
  O formato institucional geral segue em aberto para as demais disciplinas.

## Pendência obrigatória

Antes de gerar imagens, uma pessoa deve revisar fatos, dados, linguagem,
adequação ao 3º ano e todas as representações culturais. O `--dry-run` valida o
contrato técnico, não a correção histórica ou antropológica.

A regra vale para cada lote novo. O lote v3 já cumpriu essa etapa: o conteúdo
foi conferido e aprovado pelo Felipe em 15 de agosto de 2026, com o registro
do que foi verificado em cada página nos arquivos de
`conteudos/2026/3-bimestre/unidade-povos-indigenas-6paginas-v3/`.

Os avisos `[REVIEW]` do `validar.py` sobre percentuais e datas continuam
aparecendo: são heurísticos e disparam a cada execução, inclusive em prompts
antigos, sem saber que a conferência já foi feita.

## Fonte v2 e primeira página com Grok Imagine 2 — 15 de agosto de 2026

- O Felipe entregou o texto-fonte revisado da Unidade 2 (páginas 5 a 10 do
  bimestre), registrado em
  `anos/3ano/fontes/2026-2-semestre/3bim-povos-indigenas-u2-paginas-5-10-v2.md`.
  Ele reintroduz os 12.000 anos, a tabela de seis povos com regiões, a
  analogia do "europeu" e o boxe "A pergunta que fica". Esses dados foram
  conferidos e aprovados pelo Felipe em 15 de agosto de 2026, depois da
  revisão factual do lote.
- Divergências resolvidas pela direção: fundo permanece branco puro; as
  bordas usam grafismos geométricos abstratos e editoriais, sem imitar
  pintura corporal ou cerâmica de povo específico; a criança exploradora
  entra como personagem contemporânea, sem garantia de consistência com as
  páginas 1 a 4 (o repositório não guarda referência visual).
- A API xAI rejeita prompts acima de aproximadamente 5.000 caracteres
  (erro 400); manter os prompts do Grok abaixo disso.
- O Grok Imagine 2 não posiciona marcadores geográficos com precisão: pontos
  de povos no mapa saíram embaralhados em duas tentativas. Decisão: o mapa
  entra apenas como contorno ilustrado, sem pontos nem linhas; a tabela
  sustenta a informação de localização.
- O modelo tende a vazar roupa moderna (camiseta azul) para dentro da cena
  histórica quando a página também contém a criança exploradora
  contemporânea. Quatro candidatas ficaram em
  `_revisao/natureza-e-sociedade/3ano/3-bimestre/povos-indigenas-6paginas-v2/`;
  a melhor é a `grok-v3` (única falha: uma figura de camiseta azul na cena).
  A `grok-v2` grafou "Brazil" com Z. Nenhuma foi promovida.

## Lote completo da unidade v2 — 15 de agosto de 2026

- A raiz externa de saída mudou para
  `.../Drives compartilhados/Imagens` (antes ficava em
  `.../Conteudos - Colégio Eleve/SAIDAS GERADOR DE IMAGENS`); as candidatas
  da página 1 foram movidas para lá. Tudo em
  `_revisao/natureza-e-sociedade/3ano/3-bimestre/povos-indigenas-6paginas-v2/`.
- A pedido do Felipe, as páginas 2 a 6 usam seleção enxuta de texto (frases
  curtas, cortes documentados nos arquivos de conteúdo) por serem para o
  3º ano.
- Na página 6, os números atuais da fonte foram substituídos pelos dados do
  Censo 2022 já aprovados; o bloco bíblico entrou reduzido a Atos 17:26,
  porque o texto-fonte v2 o determina.
- Estado das candidatas: P4 (`grok-v2`) e P6 (`grok-v1`) sem erros; P3
  (`grok-v1`) boa, com uma frase omitida pelo modelo; P5 (`grok-v1`) boa,
  com o ancião de camisa azul na vinheta noturna; P2 tem duas candidatas
  (`grok-v1` com "indigenas" sem acento; `grok-v2` com acento correto, mas
  túnicas coloridas nas figuras da aldeia); P1 segue com `grok-v3` como
  melhor. Nenhuma promovida — todas aguardam revisão humana.

## Direção visual v3 — colagem densa — 15 de agosto de 2026

Aprovada pelo Felipe depois de comparar com o lote v2, e **fixada como layout
canônico do autor** em `PADRAO-VISUAL-3ANO.md`, com esqueleto pronto em
`MODELO-DE-PROMPT.md`. As seis páginas do lote `povos-indigenas-6paginas-v3`
foram revisadas e promovidas para `aprovadas` no mesmo dia; elas são a
referência visual de comparação para as próximas unidades. Vale para todas as
páginas seguintes deste autor:

- **Hierarquia por posição na unidade.** A página 1 é CAPA: título monumental
  em blocos de cor rasgados, o elemento mais forte da página. As páginas
  internas usam título discreto em uma linha, sobre tarja fina ou filete
  colorido; nelas o elemento mais forte é sempre a imagem principal, nunca o
  título.
- **Densidade.** Camadas sobrepostas de papéis (kraft, pautado, milimetrado,
  vegetal) com sombra, fita adesiva, clipe e canto dobrado. O branco aparece
  como fresta entre as camadas, não como fundo largo.
- **Cinco naturezas de imagem obrigatórias por página:** fotografia recortada
  real; pintura em guache documental; textura escultórica de apoio;
  objetos recortados fotografados; anotações manuscritas a grafite com setas
  e marca-texto.
- **Texto por página reduzido** a pedido do Felipe, sem simplificar as
  ideias; os cortes ficam registrados nos arquivos de conteúdo.
- **Proporção 2:3**, decidida pelo Felipe em 15 de agosto de 2026: é a
  proporção vertical que o Grok oferece, e o ajuste para A4 acontece na
  diagramação, fora do gerador. Os prompts do lote v3 ainda pedem A4 no texto,
  porque prompts aprovados não são alterados depois da aprovação; os próximos
  já nascem em 2:3.

### Revisão factual de 15 de agosto de 2026

Depois da primeira aprovação, uma revisão do lote encontrou dois problemas de
conteúdo, e as páginas 4 e 6 foram regeradas e reaprovadas:

- a estatística "menos de 10% das terras / 80% da biodiversidade" saiu da
  página 4. O número de 80% não tem base científica e foi contestado
  publicamente em 2024; o de 10% aparenta ser confusão com a estimativa de
  população. Entrou o dado do MapBiomas, série 1985–2023, com instituição e
  período impressos na própria página;
- a violência do período colonial havia desaparecido da unidade, deixando o
  colapso demográfico atribuído apenas a doenças. A página 6 voltou a trazer a
  captura para escravização, a ausência de imunidade prévia e a tese da fonte
  "A terra não estava vazia. Ela tinha sido esvaziada".

Lição para os próximos lotes: **todo número que entra no texto visível precisa
nascer com instituição e ano impressos na página**. Número herdado de pauta,
sem origem, não passa — mesmo quando soa favorável ao argumento.

O conteúdo canônico do que foi impresso passou a viver em
`conteudos/2026/3-bimestre/unidade-povos-indigenas-6paginas-v3/`. As pastas v1
e v2 são histórico e não descrevem o material aprovado.

### Defeitos recorrentes do Grok Imagine 2 e como travar

- **Artefato com escrita.** Pedir "relevo escultórico" fez o modelo desenhar
  uma placa de pedra com glifos parecidos com escrita — o que contradiz o
  conteúdo ("nada estava escrito") e viola a regra de não inventar artefatos.
  Trava que funcionou: exigir superfície lisa, sem inscrição, símbolo, glifo
  ou letra, e cerâmica sem pintura.
- **Roupa moderna vazando para a cena histórica.** Quando a criança
  exploradora contemporânea está na mesma página, o modelo veste as figuras
  da pintura com moletom, capuz e mochila. Trava que funcionou: colar a
  criança como adesivo recortado FORA da pintura, sobre o papel branco, e
  listar explicitamente as peças proibidas dentro da moldura.
- **Objeto na linha errada.** Em listas numeradas, o modelo troca os objetos
  de linha. Trava que funcionou: dizer qual objeto pertence a cada número.
- **"indigenas" sem acento.** Reincidiu três vezes em corpo pequeno, mesmo
  com trava explícita de grafia. Solução adotada: reescrever a frase para
  evitar a palavra em corpo pequeno ("esses povos"). A palavra sai correta em
  corpo maior.

## Ajuste visual aprovado em 15 de agosto de 2026

As páginas devem seguir linguagem de editorial collage infographic, scrapbook
educativo sofisticado e visual note-taking. A colagem combina fotografias de
paisagens e objetos, pinturas documentais, relevos escultóricos neutros e
objetos recortados. Cada página contém pelo menos um box informativo. Em cenas
anteriores a 1500, evitar roupas modernas e fotografia simulada de pessoas;
usar reconstrução pintada com coberturas corporais simples e respeitosas, sem
uniformizar os povos nem inventar adereços cerimoniais.
