# Organização — Natureza e Sociedade · 2º ano

## Estado

**Em produção.** As quatro páginas da Unidade 6 do 3º bimestre foram geradas
em 21/08/2026 — primeiro lote deste ano neste autor. Nenhuma imagem promovida
para `aprovadas` ainda; as quatro aguardam revisão humana em `_revisao`.

| Fonte | Unidades | Estado |
|---|---|---|
| `3bim-plantas-e-agua-v1.md` | Unidade 5 — As Plantas ao Nosso Redor | não produzida, sem recorte |
| `3bim-plantas-e-agua-v1.md` | Unidade 6 — A Água e Suas Transformações | 4 páginas geradas, aguardando revisão |
| `4bim-animais-e-ambiente-v1.md` | Unidade 7 — Classificação e Transformação dos Animais; Unidade 8 — O Ser Humano e o Ambiente | não produzidas |

Este ano continua em `manifesto.anos_planejados`: sai da lista quando a
primeira página for promovida para `aprovadas`.

Material da Unidade 6:

| Página | Título | Versão corrente | Estado |
|---|---|---|---|
| 1 | A água é vida | `v2-correcao-percentual-adulto` | correta |
| 2 | Onde tem água e os três estados | `v3-icones-explicitos` | correta |
| 3 | Como a água muda de estado | `v1` | correta |
| 4 | Cuidando da água | `v1` | correta |

- conteúdo: `conteudos/2026/3-bimestre/unidade-06-4paginas-v1/`;
- prompts: `prompts/2026/3-bimestre/unidade-06-p01..p04-*.md` (versão corrente
  de cada uma na tabela acima; as demais são histórico de correção);
- projetos: `../../projetos/2026/3-bimestre/2ano-4paginas-unidade-06-p01..p04-*`;
- imagens em revisão:
  `_revisao/natureza-e-sociedade/2ano/3-bimestre/unidade-06-4paginas/`.

## Por que quatro páginas

Contagem par, pedida por Nicolas Basso. Os 14 blocos da unidade dão 3,75
núcleos por página em quatro — dentro da banda de 3 a 4 do
`../../direcao/PADRAO-VISUAL-2ANO.md`. Em seis páginas cairia para 2,3, abaixo
da banda. O raciocínio completo, com a medição do teto de densidade, está em
`conteudos/2026/3-bimestre/unidade-06-4paginas-v1/PROPOSTA-PEDAGOGICA.md`.

## O que a página 1 ensinou sobre este ano

1. **O orçamento de prompt é de ~4.717 bytes**, não os 5.468 que sobram depois
   do `prompt_prefixo`. O cap de 8.000 bytes da OpenRouter cobre a string
   montada por `aplicar_autor` (`gerador_imagens/authors.py:78`), que é
   prefixo (2.532 B) + página + **sufixo (747 B)**. A primeira geração tomou
   400 por ter contado só o prefixo;
2. como o prefixo e o sufixo já fixam paleta, camadas, 2:3, margem e a regra
   de renderizar uma vez, o corpo do prompt só precisa carregar o **delta**.
   Cortar a repetição liberou ~875 bytes sem tocar em texto visível;
3. **percentual em rótulo de figura duplica o número da frase.** Pedir "cada
   silhueta rotulada com o seu percentual" e ter o mesmo número dentro de um
   texto literal fez o modelo imprimir "78%" duas vezes, contra a regra de
   renderizar exatamente uma vez. A v2 resolveu deixando o número só na frase;
4. o contra-bloco anti-povos-indígenas nas TRAVAS **funcionou** — nenhum
   elemento do prefixo do 3º ano vazou para a página. Confirma a pendência já
   registrada no 1º ano: vale avaliar um `prompt_prefixo` por ano;
5. a trava de margem de 12 mm do `prompt_sufixo` **não é cumprida** nem aqui
   nem nas páginas já aprovadas do 1º ano, onde elementos também encostam nas
   quatro bordas. Decidir se a trava vale ou se sai do sufixo;
6. **ícone errado em grade de rótulos curtos não é estável entre gerações.**
   Nomear o ícone de uma única linha errada e regenerar corrigiu aquela linha
   mas embaralhou ~8 outras que já estavam certas (página 2, tentativa
   `v2-correcao-icone-torneira`). O que funcionou foi nomear o ícone de
   **todas** as linhas de uma vez (`v3-icones-explicitos`): de 8 ícones
   errados para nenhum claramente errado, restando só um termômetro
   duplicado onde devia haver um ícone de forma — imperfeição cosmética,
   sem nova rodada.

## Pendências deste ano

1. `REGRAS.md` e `../../direcao/PADRAO-VISUAL-2ANO.md` continuam **derivados**
   do 3º ano. A Unidade 6 é o primeiro teste real deles contra uma fonte deste
   ano, mas eles ainda não foram revisados por uma pessoa com a fonte em mãos;
2. decidir se o fundo da página 1 saiu com cast creme demais — o `CLAUDE.md`
   §1 e a `MEMORIA.md` fixam branco puro `#FFFFFF`. O prompt do 1º ano traz
   uma trava explícita ("sem creme") que o desta página não tem;
3. o termo *fotossíntese*, impresso na página 1, é definido na Unidade 5, que
   não faz parte deste lote.

## Próximos passos

1. aprovar o estilo da página 1 e escrever os prompts das páginas 2 a 4;
2. gerar, conferir e promover as quatro com `aprovar.py`;
3. tirar o ano de `manifesto.anos_planejados` e atualizar o `PROGRESSO.md`;
4. produzir a Unidade 5 do 3º bimestre e as Unidades 7 e 8 do 4º bimestre;
5. revisar `REGRAS.md` deste ano contra o que as fontes realmente pedem.
