# Organização — Português · 3º ano

## Estado

**Unidade 6 completa (8 páginas) em `_revisao`, aguardando aprovação final
das imagens.** Primeiro lote real deste ano.

| Fonte | Unidades |
|---|---|
| `3bim-realidade-e-imaginacao-v1.md` | UNIDADE 5 — Entre a realidade e a imaginação; UNIDADE 6 — Criando mundos imaginários |
| `4bim-humor-poesia-e-escrever-para-ensinar-v1.md` | UNIDADE 7 — Humor e poesia na infância; UNIDADE 8 — Escrevendo para ensinar |

UNIDADE 6 (Capítulos 1 e 2), 8 páginas — sufixos -OSO/-EZA, sílaba tônica e
classificação tônica (Cap. 1); palavras compostas e descrição de cenários
(Cap. 2):

- prompts `-v1` em `prompts/2026/3-bimestre/unidade-06-p01..08-*-v1.md`;
- páginas 1 e 3 tiveram correção de defeito de geração (rótulo inventado
  "Dar N" nos cartões da p1; par de transformação repetido na p3) — versões
  finais em `-v2-correcao-rotulos.md` e `-v2-correcao-repeticao.md`;
- páginas 4, 5 e 6 tiveram uma segunda rodada a pedido de Nicolas Basso:
  removido o método de bater palma, substituído por "chamar a palavra de
  longe" (ondas de som), e adicionada a regra real de acentuação de cada
  tipo (proparoxítona/paroxítona/oxítona) — conteúdo gramatical
  complementar à fonte, autorizado nessa sessão. Versões finais em
  `-v2-sem-palma.md` (p4) e `-v2-regra-de-acentuacao.md` (p5);
- a página 6 teve uma terceira rodada: a escada do título (aberta na p5)
  sumiu na geração v2 e voltou como elemento estrutural obrigatório, e a
  densidade cresceu com exemplos de oxítona acentuada em -EM/-ENS (também,
  parabéns), um passo a passo "Como decidir?" em 3 etapas e o exemplo
  resolvido "você → vo-CÊ";
- a página 6 teve uma quarta rodada, a pedido de Nicolas Basso (19/08/2026):
  o título composto "Oxítona e o resumo da classificação" foi separado —
  "Oxítona" virou o título da página, morando no degrau do topo da escada,
  e "Resumo da classificação" virou título de seção da tabela na base. Os
  degraus ganharam rótulos (Proparoxítona ✓, Paroxítona ✓, Oxítona no topo,
  sem check), corrigindo o defeito da v3 (degraus vazios, três checks), e a
  regra do post-it foi harmonizada com o fraseado da p5 ("só acentua
  terminada em…"). Versão final em `-v4-titulo-separado.md`;
- imagens finais em
  `_revisao/portugues/3ano/3-bimestre/unidade-06/`: páginas 2, 7 e 8 na v1
  original; páginas 1, 3, 4 e 5 na v2 de correção/ajuste; página 6 na v4
  (`p06-oxitona-e-resumo-grok-v4-titulo-separado.jpg`);
- projetos YAML nomeados com prefixo `3ano-` em `../../projetos/2026/3-bimestre/`,
  já que a pasta de projetos é compartilhada entre anos deste autor.

Pendência registrada, não resolvida: a página 5 preserva "ja-NE-la
(penúltima = NI)" tal como está na fonte bruta (provável erro de digitação
da fonte — o correto seria NE), porque não há contradição interna no
documento que justifique corrigir sem uma decisão humana explícita.

`conteudos/` e `registros/` ainda não existem fisicamente aqui: são áreas
lógicas declaradas em `../../manifesto.yaml`. UNIDADE 5 continua sem
recorte.

## Próximos passos

1. aprovar as imagens da Unidade 6 com `aprovar.py` (ou pedir mais ajustes);
2. ao aprovar a primeira, tirar o 3º ano de `manifesto.anos_planejados`;
3. revisar `REGRAS.md` deste ano contra o que esta unidade real ensinou
   (por exemplo, "núcleos por página: 4 a 6" já se confirmou funcional);
4. Unidade 5 ("Entre a realidade e a imaginação") segue os mesmos passos de
   `preparar.py --inventario` → `--recorte` → `--aprovar`.
