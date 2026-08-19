# Organização — Português · 2º ano

## Estado

**Unidade 6 completa e aprovada em 19/08/2026** (8 páginas, revisor Nicolas
Basso). Primeiro material produzido por este autor em qualquer ano — o 2º ano
saiu de `manifesto.anos_planejados` por isso.

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

`conteudos/` ainda não existe fisicamente: é área lógica declarada em
`../../manifesto.yaml`, criada com o primeiro arquivo real. UNIDADE 5 continua
sem recorte.

## Próximos passos (Unidade 5 e demais bimestres)

1. mapear a fonte com `uv run preparar.py --inventario <fonte>`;
2. declarar o recorte em YAML e gerar rascunhos com `uv run preparar.py --recorte`;
3. resolver as decisões editoriais de cada rascunho e aprovar com
   `uv run preparar.py --aprovar --revisor "Nome"`;
4. declarar o lote em `../../projetos/<ano-letivo>/<bimestre>/`, com provedor e
   modelo explícitos;
5. `--dry-run`, gerar em `_revisao`, conferir, aprovar com `aprovar.py`.
