# Organização — Português · 2º ano

## Estado

**Unidade 6 (3º bimestre) completa e aprovada em 19/08/2026** (8 páginas).
**Unidades 7-8 (4º bimestre) completas e aprovadas em 08/09/2026** (12
páginas). Primeiro material produzido por este autor em qualquer ano — o 2º
ano saiu de `manifesto.anos_planejados` por isso. Revisor de ambos os lotes:
Nicolas Basso.

| Fonte | Unidades |
|---|---|
| `3bim-historias-em-quadrinhos-v1.md` | UNIDADE 5 — O MUNDO DAS HISTÓRIAS EM QUADRINHOS; UNIDADE 6 — CRIANDO QUADRINHOS |
| `4bim-contos-e-criadores-de-historias-v1.md` | UNIDADE 7 — O MUNDO DOS CONTOS; UNIDADE 8 — CRIADORES DE HISTÓRIAS |

UNIDADE 6 (Capítulos 1 e 2), 8 páginas:

- prompts `-v1` em `prompts/2026/3-bimestre/unidade-06-p01..08-*-v1.md`,
  aprovados a partir dos rascunhos de `preparar.py`;
- prompts `-v2-mais-densidade` nos mesmos, ajuste de layout (densidade de
  colagem, materiais de recorte variados por página, estilo de título
  variado entre páginas — ver `PADRAO-VISUAL-2ANO.md`, "Densidade e camadas");
- projetos YAML em `projetos/2026/3-bimestre/unidade-06-p01..08-*-grok-v2-mais-densidade.yaml`,
  `provider: openrouter` → `x-ai/grok-imagine-image-2.0`;
- imagens aprovadas em
  `aprovadas/portugues/2ano/3-bimestre/unidade-06/p01..08-*-grok-v2-mais-densidade.jpg`
  (raiz externa); registros em `registros/aprovacoes/portugues/2ano/3-bimestre/unidade-06/`
  (raiz deste repositório, fora de `autores/`).

UNIDADES 7-8 (Unidade 7, Capítulos 1-2; Unidade 8, Capítulo 1), 12 páginas:

- recorte declarado em
  `conteudos/2026/4-bimestre/unidades-07-08-12paginas-v1/recorte.yaml`,
  com a decisão de cortar as seções "Hora de Conversar" (roteiro de sala,
  não conteúdo de página) e reduzir bancos de palavras/vocabulário e o
  checklist de revisão a um subconjunto por categoria (mesmas palavras da
  fonte, corte de densidade);
- prompts `-v1` em `prompts/2026/4-bimestre/unidades-07-08-p01..12-*-v1.md`;
  p01, p03 e p12 tiveram correção de conteúdo e ganharam `-v2-correcao-*`
  (capa da unidade que faltava; título de página inventado pelo modelo;
  texto corrompido/duplicado num checklist denso — corrigido trocando grade
  de 3 colunas por lista vertical de 1 coluna); p09 precisou de uma segunda
  tentativa com o mesmo prompt (erro de geração: "Alegro" em vez de
  "Alegre");
- projetos YAML em
  `../../projetos/2026/4-bimestre/2ano-unidade-07-08-p01..12-*-grok-v1.yaml`
  (ou `-v2-correcao-*`/`-tentativa2`, conforme o caso), `provider: openrouter`
  → `x-ai/grok-imagine-image-2.0`;
- imagens aprovadas em
  `aprovadas/portugues/2ano/4-bimestre/unidades-07-08/p01..12-*.jpg` (raiz
  externa); registros em
  `registros/aprovacoes/portugues/2ano/4-bimestre/unidades-07-08/` (raiz
  deste repositório, fora de `autores/`);
- pendência de polimento (não bloqueou a aprovação): pontuação solta no fim
  de linha (vírgula ou aspas de fechamento sobrando) observada em p05, p06 e
  p10 — defeito pontual do modelo, não do prompt.

UNIDADE 5 continua sem recorte.

## Próximos passos (Unidade 5 e demais bimestres)

1. mapear a fonte com `uv run preparar.py --inventario <fonte>`;
2. declarar o recorte em YAML e gerar rascunhos com `uv run preparar.py --recorte`;
3. resolver as decisões editoriais de cada rascunho e aprovar com
   `uv run preparar.py --aprovar --revisor "Nome"`;
4. declarar o lote em `../../projetos/<ano-letivo>/<bimestre>/`, com provedor e
   modelo explícitos;
5. `--dry-run`, gerar em `_revisao`, conferir, aprovar com `aprovar.py`.
