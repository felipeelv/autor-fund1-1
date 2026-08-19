# Memória editorial — `portugues-atividades`

## Identidade estável

- disciplina: Língua Portuguesa, páginas de atividades;
- público: 1º ao 3º ano do Fundamental I;
- formato: `apostila-fund1`;
- modelo padrão: xAI `grok-imagine-image-2.0`;
- modelo alternativo autorizado em projeto declarado: OpenAI `gpt-image-2`;
- linguagem visual: a mesma do autor `portugues` — colagem editorial,
  sketchnote e visual note-taking sobre **fundo branco puro**;
- diferença de função: a página pede que o aluno escreva;
- saída: sempre externa, primeiro em `_revisao`.

## Origem do autor

Criado em 18 de agosto de 2026, junto com a separação entre conteúdo e
atividades. A disciplina não existia no repositório até então.

A direção foi derivada do autor `portugues`, que por sua vez foi derivado de
`matematica` — dezessete rodadas de produção e seis páginas conferidas. A cadeia
completa é `ingles` → `matematica` → `portugues` → este autor, sempre a mesma
linguagem visual, adaptada à disciplina e à função.

Sobre o fundo: adotado **branco puro `#FFFFFF`**. O `autor.yaml` de `matematica`
ainda pede "branco quente com grade pontilhada", mas o padrão visual e a memória
de lá registram o ajuste para branco puro como aprovado em 14/08/2026. Foi essa
a versão herdada.

## Risco conhecido, ainda não testado

Modelos de imagem tendem a "completar" o que parece incompleto. Numa página de
alfabetização isso aparece de duas formas previsíveis: preenchendo a pauta com
palavra escrita e reforçando o pontilhado de traçado até virar letra sólida.

As travas do `autor.yaml` foram escritas contra esses dois casos, mas **não
foram verificadas em produção**, porque nenhum lote foi gerado. Conferir os dois
pontos explicitamente no primeiro lote e registrar o resultado aqui.

## Primeira frente mapeada — 3º ano

Em 19/08/2026, as duas fontes curriculares do segundo semestre do 3º ano foram
mapeadas no autor-par `portugues`. Elas cobrem quatro unidades: realidade e
imaginação; criação de mundos imaginários; humor; e textos instrucionais.

O primeiro caderno planejado é a Unidade 6, "Criando mundos imaginários", com
oito páginas pareadas ao lote de conteúdo: `-OSO/-OSA`, `-EZA`, comparação dos
dois sufixos, sílaba tônica, proparoxítonas e paroxítonas, oxítonas, palavras
compostas e descrição de cenários de ficção científica.

Decisão de estado: o mapeamento curricular não transforma o conteúdo em fonte
de atividades. Antes de gerar, este autor ainda precisa de uma fonte própria
que fixe literalmente enunciados, itens, ordem, ação e espaço de resposta.
Logo, `3ano` permanece em `manifesto.anos_planejados`.

Duas pendências foram preservadas: a afirmação `ja-NE-la (penúltima = NI)` da
Unidade 6 aguarda decisão humana; e a Unidade 7 anuncia artigos, comparação,
metáfora e poesia sem desenvolver claramente esses tópicos no corpo disponível.

## Estado

**Direção provisória; base curricular do 3º ano mapeada; nenhuma fonte própria
de atividades aprovada.**

O autor está ativo porque o acervo não admite autor inativo, mas não
produz nada sem fonte própria de atividades e sem projeto. A direção precisa de
revisão humana no primeiro lote.
