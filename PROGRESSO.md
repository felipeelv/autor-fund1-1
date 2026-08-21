# Progresso de produção

Índice de continuidade entre sessões de trabalho. **Não é fonte de verdade**:
o estado real de cada autor/ano vive em
`autores/<id>/anos/<ano>/ORGANIZACAO.md` e em `autores/<id>/manifesto.yaml`
(`anos_planejados`). Este arquivo só resume, para retomar o trabalho sem
precisar reler tudo do zero — e deve ser atualizado a cada lote aprovado.

Antes de qualquer trabalho novo, leia `CLAUDE.md` e, para o autor em uso,
`direcao/AUTOR.md` e `direcao/MEMORIA.md` — este arquivo não substitui isso.

## Snapshot por autor (21/08/2026)

| Autor | Anos com fonte | Anos com material aprovado | Próximo passo natural |
|---|---|---|---|
| `ingles` | 1º, 3º | 1º, 3º | ver `autores/ingles/anos/*/ORGANIZACAO.md` |
| `matematica` | 3º | 3º | 4º bimestre (Unidades 7-8, 8 páginas) em `_revisao`: 6 corretas, p5 e p7 pendentes |
| `natureza-e-sociedade` | 1º, 2º, 3º | 2º, 3º | 1º ano ainda sem recorte; Unidade 5 do 2º ano sem recorte |
| `portugues` | 1º, 2º, 3º | 1º (Unidade 6), 2º (Unidade 6) | Unidade 6 do 3º ano em `_revisao`, falta aprovar; Unidade 5 dos três anos sem recorte |
| `*-atividades` (par de cada disciplina) | — | — | nenhum lote iniciado ainda |

## Português — 1º ano — 3º bimestre — Unidade 6 ("Somos escritores")

**Status: completo e aprovado em 20/08/2026** (revisor: Nicolas Basso).
Primeiro lote real deste ano. A fonte rotula a unidade como "UNIDADE 8", mas
ela ocupa a posição da Unidade 6 do 3º bimestre — rótulo da própria fonte,
não corrigido; ver `autores/portugues/anos/1ano/ORGANIZACAO.md`.

Reorganizado de 6 para 4 páginas a pedido de Nicolas Basso (crianças do 1º
ano ainda leem pouco; menos páginas mais densas concentram melhor a
atenção): cada página junta dois sub-temas que a própria fonte já encadeia.
O recorte original de 6 páginas e seus prompts continuam no repositório como
histórico, sem uso ativo.

| Página | Título | Recorte da fonte |
|---|---|---|
| 1 | Vamos criar nossa própria história! + índice da unidade + regra de S/Z | Cap. 1, abertura |
| 2 | O roteiro da história + início, meio e fim | Cap. 1, planejamento |
| 3 | C e Ç: quando usar? | Cap. 2, abertura |
| 4 | Nunca existe ÇE nem ÇI! + quadro comparativo + palavras do livro | Cap. 2, fecho |

A página 1 passou por uma correção de defeito de geração antes da aprovação:
o cartão da palavra MESA saiu com um livro em vez de uma mesa (v1 →
`v2-correcao-mesa`, especificando o móvel explicitamente no prompt).

Caminhos: prompts em
`autores/portugues/anos/1ano/prompts/2026/3-bimestre/unidade-06-p01..04-*-v1.md`
(p01 final é `v2-correcao-mesa`); projetos com prefixo `1ano-4paginas-` em
`autores/portugues/projetos/2026/3-bimestre/`; imagens aprovadas em
`aprovadas/portugues/1ano/3-bimestre/unidade-06-4paginas/`; registros de
aprovação em
`registros/aprovacoes/portugues/1ano/3-bimestre/unidade-06-4paginas/`.

Pendente: Unidade 5 ("O mundo das histórias") do mesmo bimestre e fonte,
ainda sem recorte.

## Português — 2º ano — 3º bimestre — Unidade 6 ("Criando Quadrinhos")

**Status: completo e aprovado em 19/08/2026** (revisor: Nicolas Basso). Foi o
primeiro lote real deste autor, em qualquer ano — ver
`autores/portugues/direcao/MEMORIA.md` para o que essa produção confirmou
sobre a direção editorial do autor.

8 páginas, todas com prompt `-v2-mais-densidade` (layout revisado após
feedback sobre densidade e variedade de título/material) e imagem aprovada:

| Página | Título | Recorte da fonte |
|---|---|---|
| 1 | Como a pontuação mostra emoção | Cap. 1, abertura |
| 2 | Exclamação e interrogação | Cap. 1 |
| 3 | Reticências e combinações de pontuação | Cap. 1 |
| 4 | Tamanho das letras, volume da voz e pontuação × emoção | Cap. 1, fecho |
| 5 | Planejando a história e os personagens | Cap. 2, passos 1-2 |
| 6 | Quantos quadros e os diálogos com artigos | Cap. 2, passos 3-4 |
| 7 | Onomatopeias, expressões faciais e o roteiro completo | Cap. 2, passos 5-6 |
| 8 | Checklist de revisão da HQ | Cap. 2, fecho |

Caminhos: prompts em
`autores/portugues/anos/2ano/prompts/2026/3-bimestre/unidade-06-p01..08-*-v2-mais-densidade.md`;
projetos em
`autores/portugues/projetos/2026/3-bimestre/unidade-06-p01..08-*-grok-v2-mais-densidade.yaml`;
imagens aprovadas na raiz externa,
`aprovadas/portugues/2ano/3-bimestre/unidade-06/`; registros de aprovação em
`registros/aprovacoes/portugues/2ano/3-bimestre/unidade-06/` (dentro deste
repositório).

Pendente: Unidade 5 ("O Mundo das Histórias em Quadrinhos") do mesmo
bimestre e fonte, ainda sem recorte nem prompt.

## Português — 3º ano — 3º bimestre — Unidade 6 ("Criando Mundos Imaginários")

**Status: 8 páginas em `_revisao`, ainda sem aprovação final das imagens**
(19/08/2026). Primeiro lote real deste ano. Duas páginas passaram por
correção de defeito de geração (rótulo inventado na p1; repetição na p3) e
três passaram por uma segunda rodada de conteúdo (p4, p5, p6: removido o
método de bater palma, adicionada a regra real de acentuação de cada tipo
tônico — conteúdo gramatical complementar à fonte, não citação literal).
A p6 teve ainda uma terceira rodada (v3): a escada do título voltou como
elemento obrigatório e ganhou exemplos de -EM/-ENS (também, parabéns) e um
passo a passo de decisão com exemplo resolvido. Uma quarta rodada (v4,
a pedido de Nicolas Basso) separou o título composto: "Oxítona" é o título
da página, no degrau do topo da escada (degraus agora rotulados), e
"Resumo da classificação" é título de seção da tabela na base.
Ver `autores/portugues/anos/3ano/ORGANIZACAO.md` para o detalhe completo,
inclusive a pendência registrada sobre "ja-NE-la (penúltima = NI)" na
página 5 (provável erro de digitação da fonte, não corrigido sem decisão
humana).

| Página | Título | Recorte da fonte |
|---|---|---|
| 1 | Sufixo -OSO/-OSA: sempre com S | Cap. 1 |
| 2 | Sufixo -EZA: sempre com Z | Cap. 1 |
| 3 | -OSO vs -EZA: comparando e transformando | Cap. 1 |
| 4 | Sílaba tônica: a sílaba mais forte | Cap. 1 |
| 5 | Proparoxítona e paroxítona | Cap. 1 |
| 6 | Oxítona (título) + seção "Resumo da classificação" | Cap. 1 |
| 7 | Palavras compostas | Cap. 2 |
| 8 | Palavras compostas na ficção científica e descrição de cenários | Cap. 2 |

Caminhos: prompts em
`autores/portugues/anos/3ano/prompts/2026/3-bimestre/unidade-06-p01..08-*.md`
(versões finais indicadas no `ORGANIZACAO.md` do ano); projetos com prefixo
`3ano-` em `autores/portugues/projetos/2026/3-bimestre/` (a pasta de
projetos é compartilhada entre anos deste autor, por isso o prefixo);
imagens em `_revisao/portugues/3ano/3-bimestre/unidade-06/`.

Pendente: aprovação final das imagens; Unidade 5 do mesmo bimestre e fonte,
ainda sem recorte.

## Natureza e Sociedade — 2º ano — 3º bimestre — Unidade 6 ("A Água e Suas Transformações")

**Status: completo e aprovado em 21/08/2026** (revisor: Nicolas Basso).
Primeiro lote real deste autor no 2º ano. Contagem par (pedida por Nicolas
Basso), 4 páginas, 3,75 núcleos por página — dentro da banda de 3 a 4 do
`PADRAO-VISUAL-2ANO.md`. A Unidade 5 da mesma fonte ("As Plantas ao Nosso
Redor") não faz parte deste lote.

A fonte trazia seis números sem instituição nem ano — proibido pela
`MEMORIA.md` deste autor. Cinco foram cortados; o "70% do corpo humano" foi
substituído pelos valores do USGS (2019), impressos na página 1.

| Página | Título | Estado |
|---|---|---|
| 1 | A água é vida | correta (v2: corrigiu percentual do adulto e duplicação de número) |
| 2 | Onde tem água e os três estados | correta (v3: corrigiu ícones de característica, ver `ORGANIZACAO.md` do ano) |
| 3 | Como a água muda de estado | correta na primeira geração |
| 4 | Cuidando da água | correta na primeira geração |

Caminhos: conteúdo em
`autores/natureza-e-sociedade/anos/2ano/conteudos/2026/3-bimestre/unidade-06-4paginas-v1/`;
prompts em
`autores/natureza-e-sociedade/anos/2ano/prompts/2026/3-bimestre/unidade-06-p01..04-*.md`
(versão corrente de cada página no `ORGANIZACAO.md` do ano); projetos com
prefixo `2ano-4paginas-` em
`autores/natureza-e-sociedade/projetos/2026/3-bimestre/`; imagens aprovadas em
`aprovadas/natureza-e-sociedade/2ano/3-bimestre/unidade-06-4paginas/`;
registros de aprovação em
`registros/aprovacoes/natureza-e-sociedade/2ano/3-bimestre/unidade-06-4paginas/`.

Pendente: Unidade 5 do mesmo bimestre e fonte, ainda sem recorte; Unidades 7
e 8 do 4º bimestre.

## Matemática — 3º ano — 4º bimestre — Unidades 7 e 8

**Status: 8 páginas em `_revisao`, seis corretas e duas pendentes**
(19/08/2026). Primeiro lote do 4º bimestre deste autor. Quatro páginas de
Grandezas e Medidas e quatro de Estatística e Probabilidade.

| Página | Título | Estado |
|---|---|---|
| 1 | Metro, centímetro e milímetro | correta |
| 2 | Convertendo unidades de comprimento | correta |
| 3 | O perímetro: a medida do contorno | correta |
| 4 | Capacidade e massa: qual unidade usar | correta |
| 5 | Pesquisa e organização em tabelas | contagem da tabela não bate |
| 6 | Gráfico de barras: ler e construir | correta |
| 7 | Gráfico de linhas e qual gráfico usar | pontos fora do valor |
| 8 | Probabilidade: certo, impossível e possível | correta |

Recorte e cobertura da fonte em
`autores/matematica/anos/3ano/conteudos/2026/4-bimestre/unidades-07-08-8paginas-v1/`;
prompts em `anos/3ano/prompts/2026/4-bimestre/`; um projeto por página em
`projetos/2026/4-bimestre/`; registro completo do lote em
`registros/2026/4-bimestre/unidades-07-08-8paginas-v1.md`.

Pendente: decisão sobre p5 e p7; o Gráfico de Barras Duplas da fonte, cujo
ASCII é inconsistente; e a aprovação das seis páginas corretas com `aprovar.py`.

## Como continuar um autor/ano parado

1. ler `autores/<id>/anos/<ano>/ORGANIZACAO.md` — estado real, não este arquivo;
2. se não houver recorte: `uv run preparar.py --inventario <fonte>`, depois
   `--recorte`;
3. resolver as decisões editoriais dos rascunhos e aprovar com
   `uv run preparar.py --aprovar --revisor "Nome"`;
4. declarar o projeto YAML, `--dry-run`, gerar em `_revisao`, conferir,
   aprovar com `aprovar.py --revisor "Nome"`;
5. atualizar o `ORGANIZACAO.md` do ano e, se for o primeiro lote do ano, tirar
   o ano de `manifesto.anos_planejados` e atualizar este arquivo.

## Histórico

- **19/08/2026** — Português 2º ano, Unidade 6 completa (8 páginas): recorte,
  rascunhos, aprovação de prompt, geração via `openrouter` →
  `x-ai/grok-imagine-image-2.0` (chave nativa da xAI ainda não configurada
  neste ambiente), ajuste de densidade/título/material em duas rodadas de
  feedback, aprovação final das 8 imagens.
- **19/08/2026** — Português 3º ano, Unidade 6 gerada (8 páginas), ainda sem
  aprovação final: duas correções de defeito de geração (rótulo inventado,
  repetição de par de transformação) e uma rodada de mais densidade em 3
  páginas (regra de acentuação por tipo tônico, método de identificação
  trocado). Também descoberto: o limite de tamanho do prompt é em **bytes
  UTF-8**, não caracteres — texto acentuado pesa mais em bytes; ver
  `MEMORIA.md`.
- **20/08/2026** — Português 1º ano, Unidade 6 completa e aprovada (4
  páginas): recorte inicial em 6 páginas, reorganizado para 4 a pedido de
  Nicolas Basso (crianças do 1º ano leem pouco; menos páginas mais densas
  concentram a atenção — cada página junta dois sub-temas que a fonte já
  encadeia). Uma rodada de correção de defeito de geração (cartão MESA saiu
  com um livro em vez de uma mesa). Aprovação final das 4 imagens.
- **21/08/2026** — Natureza e Sociedade 2º ano, Unidade 6 completa e
  aprovada (4 páginas): primeiro lote deste autor no 2º ano. Contagem par
  pedida por Nicolas Basso; seis números da fonte sem instituição nem ano
  foram cortados ou substituídos pelos valores do USGS (2019). Duas rodadas
  de correção: percentual do adulto e duplicação de número na página 1;
  ícone de característica errado espalhado por regeneração na página 2 —
  corrigido nomeando o ícone de todas as linhas de uma vez, não só a errada.
  Descoberto: o cap de 8.000 bytes da OpenRouter cobre a string montada por
  `aplicar_autor` (prefixo **+ sufixo**, não só o prefixo); ver
  `autores/natureza-e-sociedade/anos/2ano/ORGANIZACAO.md`.
