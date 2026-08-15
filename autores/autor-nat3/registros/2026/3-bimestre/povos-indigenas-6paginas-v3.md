# Registro de produção — Povos indígenas — 6 páginas — lote v3

- autor: `autor-nat3`;
- fonte: `3bim-povos-indigenas-u2-paginas-5-10-v2.md` (entregue pelo Felipe em
  15 de agosto de 2026);
- provedor e modelo: xAI `grok-imagine-image-2.0`;
- parâmetros: JPEG, `tamanho: auto`, proporção 2:3, resolução 2k;
- saída: 1664×2496 px;
- revisor: Felipe Rosa;
- aprovação: 15 de agosto de 2026.

## Páginas aprovadas

| Página | Prompt | Arquivo |
|---|---|---|
| 1 — capa | `...p01-...-v7.md` | `p01-capa-o-brasil-nao-comecou-em-1500-grok-v2.jpg` |
| 2 | `...p02-...-v5.md` | `p02-aqui-moravam-os-caiapos-grok-v3.jpg` |
| 3 | `...p03-...-v4.md` | `p03-a-floresta-era-a-escola-grok-v3.jpg` |
| 4 | `...p04-...-v5.md` | `p04-sabiam-tudo-e-nao-destruiram-grok-v3.jpg` |
| 5 | `...p05-...-v2.md` | `p05-um-dia-na-aldeia-grok-v1.jpg` |
| 6 | `...p06-...-v4.md` | `p06-o-que-aconteceu-e-o-que-fazemos-agora-grok-v2.jpg` |

## Iterações até a aprovação

A produção passou por três direções visuais. As duas primeiras ficaram em
`_revisao` como histórico; a terceira, de colagem densa, foi aprovada e virou
o layout canônico do autor.

Defeitos do modelo que exigiram nova geração, e a trava que resolveu cada um:

| Defeito | Página | Trava |
|---|---|---|
| pontos de povos embaralhados no mapa | 1 | mapa vira contorno ilustrado, sem marcadores |
| "Brazil" com Z | 1 | grafia exata na trava |
| relevo de pedra com glifos de escrita | 1 e 2 | pedra, argila e cerâmica lisas |
| moletom e mochila dentro da pintura | 2 | criança exploradora colada fora da cena |
| "indigenas" sem acento em corpo pequeno | 2 e 3 | reescrever a frase evitando a palavra |
| guaraná e urucum botanicamente errados | 3 | descrição botânica no prompt |
| objeto ilustrando o item errado da lista | 4 | dizer qual objeto pertence a cada número |

## Revisão factual posterior à primeira aprovação

Uma revisão feita no mesmo dia, depois da primeira rodada de aprovação,
encontrou dois problemas de conteúdo e as páginas 4 e 6 foram regeradas:

- **página 4:** a estatística "menos de 10% das terras / 80% da
  biodiversidade" foi retirada. O número de 80% não tem base científica —
  nasceu de um documento da ONU de 2002 sem citação e foi contestado
  publicamente em 2024 por Nature, Mongabay, The Conversation e CIFOR. O "menos
  de 10% das terras" aparenta ser confusão com a estimativa de população
  (cerca de 5%). Entrou no lugar o dado do MapBiomas, série 1985–2023,
  com instituição e período impressos na página;
- **página 6:** a violência do período colonial havia sumido da unidade, o que
  deixava o colapso demográfico atribuído apenas a doenças. Voltaram a captura
  para escravização, a explicação da ausência de imunidade prévia e a tese da
  fonte "A terra não estava vazia. Ela tinha sido esvaziada". Também entraram a
  frase sobre indígenas que vivem em aldeias e em cidades, a instituição do
  Censo (IBGE) e a versão da tradução bíblica (NVI).

As versões substituídas foram removidas de `aprovadas`; permanecem em
`_revisao` como histórico.

## Pendências que seguem abertas

- conferência histórica da atribuição direta dos Caiapós à região de Ribeirão
  Preto (página 2);
- generalização dos cinco princípios a povos indígenas em bloco (página 4);
- cotidiano de aldeia descrito em tom geral (página 5);
- proporção da arte: 2:3 gerado contra A4 pedido no prompt — decisão do Felipe;
- adequação de vocabulário na analogia do "europeu" (página 1), a frase mais
  longa da unidade.
