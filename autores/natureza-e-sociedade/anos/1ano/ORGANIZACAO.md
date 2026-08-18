# Organização — Natureza e Sociedade · 1º ano

## Estado

**Fonte recebida, nada produzido ainda.**

| Fonte | Unidades |
|---|---|
| `3bim-natureza-viva-e-escola-v1.md` | UNIDADE 5 — A NATUREZA VIVA; UNIDADE 6 — A ESCOLA E SEUS ARREDORES |
| `4bim-trabalho-e-mundo-em-que-vivemos-v1.md` | UNIDADE 7 — O TRABALHO E AS PROFISSÕES; UNIDADE 8 — O MUNDO EM QUE VIVEMOS |

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
