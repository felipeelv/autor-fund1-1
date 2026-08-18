# Organização — Português · 1º ano

## Estado

**Fonte recebida, nada produzido ainda.**

| Fonte | Unidades |
|---|---|
| `3bim-mundo-das-historias-e-somos-escritores-v1.md` | UNIDADE 5 — O MUNDO DAS HISTÓRIAS; UNIDADE 8 — SOMOS ESCRITORES |
| `4bim-cantigas-e-poesia-v1.md` | UNIDADE 7 — O MUNDO DAS CANTIGAS; UNIDADE 8 — BRINCANDO DE POETA |

`conteudos/`, `prompts/`, `projetos/` e `registros/` ainda não existem
fisicamente: são áreas lógicas declaradas em `../../manifesto.yaml` e devem ser
criadas com o primeiro arquivo real, sem `.gitkeep`.

Este ano continua em `manifesto.anos_planejados`, que lista os anos do escopo
sem material produzido. Ter fonte não é ter material: sai da lista quando a
primeira página for aprovada.

## Próximos passos

1. mapear a fonte com `uv run preparar.py --inventario <fonte>`;
2. derivar o recorte editorial em `conteudos/<ano-letivo>/<bimestre>/`;
3. escrever os prompts em `prompts/<ano-letivo>/<bimestre>/`, versionados com
   sufixo `-vN`;
4. declarar o lote em `../../projetos/<ano-letivo>/<bimestre>/`, com provedor e
   modelo explícitos e saída externa em `_revisao`;
5. revisar `REGRAS.md` deste ano, que hoje é derivado, contra o que a fonte
   realmente pede;
6. tirar o ano de `manifesto.anos_planejados`.
