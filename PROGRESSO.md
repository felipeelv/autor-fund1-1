# Progresso de produção

Índice de continuidade entre sessões de trabalho. **Não é fonte de verdade**:
o estado real de cada autor/ano vive em
`autores/<id>/anos/<ano>/ORGANIZACAO.md` e em `autores/<id>/manifesto.yaml`
(`anos_planejados`). Este arquivo só resume, para retomar o trabalho sem
precisar reler tudo do zero — e deve ser atualizado a cada lote aprovado.

Antes de qualquer trabalho novo, leia `CLAUDE.md` e, para o autor em uso,
`direcao/AUTOR.md` e `direcao/MEMORIA.md` — este arquivo não substitui isso.

## Snapshot por autor (19/08/2026)

| Autor | Anos com fonte | Anos com material aprovado | Próximo passo natural |
|---|---|---|---|
| `ingles` | 1º, 3º | 1º, 3º | ver `autores/ingles/anos/*/ORGANIZACAO.md` |
| `matematica` | 3º | 3º | 4º bimestre (Unidades 7-8, 8 páginas) em `_revisao`: 6 corretas, p5 e p7 pendentes |
| `natureza-e-sociedade` | 1º, 2º, 3º | 3º | 1º/2º ano ainda sem recorte |
| `portugues` | 1º, 2º, 3º | 2º (Unidade 6) | Unidade 6 do 3º ano em `_revisao`, falta aprovar; 1º ano e Unidade 5 dos outros dois sem recorte |
| `*-atividades` (par de cada disciplina) | — | — | nenhum lote iniciado ainda |

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

## Natureza e Sociedade — 3º ano — 3º bimestre — Povos Indígenas (v4)

**Status: 6 páginas geradas em `_revisao`, todas corretas, aguardando
revisão humana** (22/08/2026). Quarto lote da mesma unidade (v1/v2/v3
usaram fonte mais curta; v3 foi aprovado em 15/08/2026 e é a referência
visual canônica do autor). A fonte combinada recebida em 19/08/2026 é bem
mais rica — duas seções novas (organização social, arte e cultura) sem
equivalente no v3 — por isso este não é uma correção, é uma refeitura.

| Página | Título | Estado |
|---|---|---|
| 1 | O Brasil não começou em 1500 (capa) | correta |
| 2 | Aqui moravam os Caiapós | correta (v2; v1 tinha roupa moderna na cena histórica) |
| 3 | A floresta era a escola | correta |
| 4 | Sabiam tudo — e mesmo assim não destruíram | correta |
| 5 | Como a aldeia se organizava | correta, com pendência de generalização registrada |
| 6 | O que aconteceu — e o que fazemos agora | correta |

Três decisões mudam o que estava aprovado no v3 e exigem confirmação
humana explícita: o versículo bíblico (Romanos 12:4 no lugar de Atos
17:26 — este não está na fonte nova), a tabela de povos da página 1
(Xavantes no lugar de Quéchuas, que não são um povo brasileiro), e a
página 2 (carrega a formulação já corrigida do v3 sobre "a terra não
estava vazia", revertendo o que a fonte nova reintroduzia). Detalhe
completo em
`autores/natureza-e-sociedade/anos/3ano/ORGANIZACAO.md` e
`registros/2026/3-bimestre/povos-indigenas-6paginas-v4.md`.

Pendente: revisão humana das três decisões, decisão sobre se o v4
substitui o v3 como referência visual, aprovação com `aprovar.py`; a
Unidade 1 (O Solo) do mesmo bimestre, ainda sem recorte.

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
- **22/08/2026** — Natureza e Sociedade 3º ano, Povos Indígenas refeito em
  6 páginas (v4), a partir de uma fonte mais rica que o v3 aprovado. Três
  decisões editoriais mudam o que estava aprovado (versículo bíblico,
  tabela de povos, formulação sobre "terra vazia") e aguardam confirmação
  humana antes de `aprovar.py`. Uma correção de defeito de geração (roupa
  moderna em cena anterior a 1500, página 2).
