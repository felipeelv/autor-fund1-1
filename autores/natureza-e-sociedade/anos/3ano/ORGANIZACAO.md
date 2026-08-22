# Organização — Natureza e Sociedade · 3º ano

## 2026 · 2º semestre

| Bimestre | Tema | Estado |
|---|---|---|
| 3º | Unidade 1 — O Solo: Base da Vida | sem recorte |
| 3º | Unidade 2 — Povos Indígenas (posição da Unidade 6 do bimestre) | lote v3 aprovado em 15/08/2026 (fonte curta); lote v4 gerado em 22/08/2026 a partir de fonte mais rica, aguardando revisão humana |
| 4º | Unidade 1/2 — Biodiversidade e Ecossistemas | sem recorte |

Os prompts ficam em `prompts/2026/<bimestre>/`. Cada lote precisa de projeto
YAML próprio, provedor e modelo declarados e saída externa em `_revisao`.

## Povos Indígenas — v4 (22/08/2026)

Quarto lote da mesma unidade, a partir de uma fonte combinada mais rica
(`3bim-solo-e-povos-indigenas-u1-u2-v1.md`, recebida em 19/08/2026) que o v3
não usou. Detalhe completo em
`conteudos/2026/3-bimestre/unidade-povos-indigenas-6paginas-v4/COBERTURA-DA-FONTE.md`
e `PROPOSTA-PEDAGOGICA.md`.

Seis páginas geradas em `_revisao`, todas corretas — a página 2 precisou de
uma segunda rodada por defeito de geração (roupa moderna na cena histórica).
Nenhuma promovida para `aprovadas` ainda.

| Página | Título | Versão corrente |
|---|---|---|
| 1 | O Brasil não começou em 1500 (capa) | v1 |
| 2 | Aqui moravam os Caiapós | v2 (correção de roupa moderna) |
| 3 | A floresta era a escola | v1 |
| 4 | Sabiam tudo — e mesmo assim não destruíram | v1 |
| 5 | Como a aldeia se organizava | v1 |
| 6 | O que aconteceu — e o que fazemos agora | v1 |

### Três decisões que mudam o que estava aprovado no v3 — exigem confirmação humana

1. **versículo bíblico trocado**: Romanos 12:4 no lugar de Atos 17:26 — este
   não consta na fonte nova; aquele é o que a fonte liga ao tema da
   diversidade;
2. **tabela de povos da página 1**: Xavantes no lugar de Quéchuas (a fonte
   nova lista um povo andino — Peru/Bolívia — como exemplo de diversidade
   *brasileira*; substituído pelo sexto povo já usado no v3);
3. **página 2**: a fonte nova reintroduz a tese de "terra vazia" que o v3
   já havia revertido, com revisão humana registrada em `MEMORIA.md`. Este
   lote carrega a formulação do v3 ("a terra não estava vazia, ela tinha
   sido esvaziada"), não a da fonte nova.

### Pendência que se agrava

A página 5 (organização social + arte e cultura), inteiramente nova neste
lote, é construída sobre generalizações da própria fonte sobre povos
indígenas em bloco — mesma pendência que `MEMORIA.md` já registrou a partir
da página 4 do v3, agora numa página inteira. Ver `COBERTURA-DA-FONTE.md`.

### Pendência herdada

`../../direcao/PADRAO-VISUAL-3ANO.md` nomeia as páginas do v3 como "a
referência visual de comparação para as próximas unidades". Se o v4 for
aprovado, decidir se ele substitui essa referência.

### O que a página 2 ensinou

A trava de "cena anterior a 1500 sem roupa moderna" já está no
`prompt_prefixo` do autor, mas não impediu a primeira geração de vestir as
figuras da fogueira com camisa de manga e calça. Reforçar a lista explícita
de peças proibidas no corpo do prompt da página (não só confiar no prefixo)
resolveu na segunda tentativa — mesma lição já registrada em
`PADRAO-VISUAL-3ANO.md`, "travas de prompt já validadas".

### Correção ao próprio PADRAO-VISUAL-3ANO.md

A nota de orçamento de bytes ("corpo abaixo de 4.800 caracteres... prefixo e
sufixo cerca de 2.700 caracteres") estava desatualizada — não contava o
`prompt_sufixo`. Corrigida em 22/08/2026 para os valores medidos: prefixo
2.532 B + sufixo 747 B = 3.279 B fixos, ~4.721 B de orçamento por página.

## Pendência obrigatória

Antes de promover qualquer imagem do v4 para `aprovadas`, uma pessoa deve
revisar as três decisões acima e a pendência de generalização da página 5.
