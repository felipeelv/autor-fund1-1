Use case: scientific-educational
Asset type: página 3 de uma sequência didática de Inglês do 3º ano

## PEDIDO

Criar uma única página vertical 2:3, pronta para impressão, que abra o
bloco com o que a criança vai aprender e ensine os quatro períodos do dia em
inglês, com pronúncia, horário e a estrutura "In the.../At night". Fica de
fora: "I...at...o'clock" e a linha do tempo, que pertencem à página
seguinte.

Título previsto: Parts of the Day

## SISTEMA VISUAL

Seguir integralmente `autores/ingles/direcao/PADRAO-VISUAL-3ANO.md` e o que
se mantém de `PADRAO-VISUAL-1ANO.md`: papel branco puro (fundo `#FFFFFF`,
sem tom creme ou amarelado). Para o 3º ano: 4 a 6 núcleos por página
(abertura do bloco, vocabulário dos 4 períodos, estrutura "in the/at
night", atenção sobre a exceção de night). Ilustração de céu em quatro
momentos (nascer do sol, sol alto, pôr do sol, lua e estrelas) como suporte
visual de cada período.

## COMPOSIÇÃO E TÍTULO

- fundo da página inteira branco puro, sem faixa, painel ou textura colorida
  cobrindo grandes áreas — cor entra só nas ilustrações de céu e acentos;
- topo com o título "PARTS OF THE DAY";
- logo abaixo, faixa "NESTE BLOCO VOCÊ VAI APRENDER" com os quatro itens da
  lista (períodos do dia, estruturas, gênero textual, músicas e gestos);
- núcleo central "PARTS OF THE DAY" com os quatro períodos, cada um com sua
  ilustração de céu, pronúncia e horário: MORNING (6:00-12:00), AFTERNOON
  (12:00-18:00), EVENING (18:00-21:00), NIGHT (21:00-6:00);
- bloco "IN THE... / AT NIGHT" com as quatro frases-estrutura e, logo
  abaixo, a faixa "ATENÇÃO" com exatamente quatro linhas — IN the morning,
  IN the afternoon, IN the evening, AT night — cada uma aparecendo **uma
  única vez**, sem repetir nenhuma delas;
- caminho de leitura: título → o que você vai aprender → quatro períodos do
  dia → estrutura "in the.../at night" → atenção.

## TEXTOS EXATOS

Renderizar cada um exatamente uma vez, na ordem abaixo.

- PARTS OF THE DAY
- NESTE BLOCO VOCÊ VAI APRENDER
- Períodos do dia: morning, afternoon, evening, night
- Estruturas: I... at... o'clock. / In the morning/afternoon/evening/night
- Gênero textual: linha do tempo do dia
- Músicas e gestos para aprender brincando
- MORNING (mórning) — manhã (6:00 - 12:00)
- AFTERNOON (afternúun) — tarde (12:00 - 18:00)
- EVENING (ívining) — fim da tarde / início da noite (18:00 - 21:00)
- NIGHT (náit) — noite (21:00 - 6:00)
- IN THE MORNING = De manhã / Na parte da manhã
- IN THE AFTERNOON = De tarde / Na parte da tarde
- IN THE EVENING = No fim da tarde / No início da noite
- AT NIGHT = À noite
- ATENÇÃO:
- IN the morning
- IN the afternoon
- IN the evening
- AT night (não usamos "in" com night!)

### Nota de correção

Duas correções sobre a v2 (17/09/2026): (1) o fundo não tinha o hex
explícito no prompt e a imagem saiu com fundo creme — corrigido para
`#FFFFFF`; (2) a faixa "ATENÇÃO" saiu com "IN the afternoon" duplicado (5
linhas em vez de 4) na geração da v2 — a lista de TEXTOS EXATOS já estava
correta (4 itens, sem duplicata), então o defeito era de render, não de
prompt; adicionada instrução explícita pedindo exatamente quatro linhas,
cada uma uma única vez.

## TRAVAS

Valem as travas de `autores/ingles/anos/3ano/REGRAS.md` e o `prompt_sufixo` do autor, que o gerador
injeta automaticamente.

Invioláveis, independentes de ano: não inventar número, nome próprio, data,
lugar, povo ou termo ausente da fonte; renderizar cada texto literal exatamente
uma vez; nenhum texto além da lista de TEXTOS EXATOS. Não usar mascote,
logotipo, número de página, fotografia de banco de imagens ou estética de
desenho animado comercial.
