# AUTOR — Português · anos iniciais · Fundamental I

> Consulte o
> [padrão compartilhado](../../../compartilhado/direcao-editorial/PADRAO-GERAL-DE-ESCRITA.md)
> antes de preparar qualquer página.
>
> **Direção derivada** do autor `matematica`, em 18/08/2026, conforme
> `compartilhado/direcao-editorial/DERIVACAO-ENTRE-ANOS.md`. Fonte recebida em
> 18-19/08/2026 para os três anos. Primeiro lote real produzido e aprovado em
> 19/08/2026 — 2º ano, Unidade 6, 8 páginas — e é nesse lote que o ajuste
> humano da direção aconteceu na prática; ver
> `PADRAO-VISUAL-2ANO.md`, seção "Densidade e camadas". 1º e 3º ano ainda sem
> recorte.

Este autor produz páginas de apoio visual de Língua Portuguesa para crianças dos
anos iniciais. A fonte interna versionada determina letras, palavras, frases,
textos, exemplos e vocabulário. O autor organiza visualmente o material, mas não
cria palavra, exemplo, frase, verso ou texto novo.

## Princípios pedagógicos

- partir da palavra falada e do objeto nomeado antes da regra;
- apresentar uma intenção pedagógica principal por página;
- mostrar a construção da palavra e da frase em etapas curtas e na ordem correta;
- manter a palavra escrita junto da imagem que sustenta o seu sentido;
- diferenciar conceito, exemplo, regra e verificação pela hierarquia visual;
- usar repetição apenas para evidenciar um padrão ortográfico ou sonoro;
- não criar exercícios, respostas, exemplos ou textos ausentes da fonte;
- tratar ortografia, acentuação e segmentação silábica como itens de revisão
  humana.

## A trava que define a disciplina

**A letra é conteúdo, não decoração.** Numa página de Matemática, uma letra
malformada é defeito estético; aqui é erro de conteúdo, porque é exatamente
aquele desenho que a criança está aprendendo e vai copiar.

Cada letra aparece com desenho correto e completo, no tipo pedido — caixa alta
ou minúscula de imprensa —, sem espelhamento, sem deformação, sem glifo
inventado e sem misturar tipos dentro da mesma palavra. Acento, cedilha e til
aparecem inteiros e na posição certa.

## Princípios visuais

- seguir o `PADRAO-VISUAL-<N>ANO.md` do ano em produção;
- usar fundo branco puro como base da página, sem tom creme, grade ou
  pontilhado contínuo;
- separar explicações, exemplos, regras e sínteses em recortes de papel
  distintos, com respiro branco entre eles;
- variar escala, alinhamento, posição e tratamento dos títulos entre páginas
  consecutivas, evitando repetir o mesmo cabeçalho centralizado;
- manter tipografia grande e caminho de leitura evidente;
- dar à letra ou à palavra em estudo escala de protagonista, isolada do resto da
  composição;
- preservar literalmente a grafia, a acentuação e a pontuação da fonte;
- proibir texto além da lista literal de cada prompt;
- conferir a imagem inteira, a ortografia e o OCR antes da entrega.

## Fonte operacional

A produção usa somente fontes internas em `../anos/<ano>/fontes/<periodo>/`.
Cada novo recorte exige conteúdo derivado, prompts próprios e projeto YAML. Cada
projeto declara xAI `grok-imagine-image-2.0` ou OpenAI `gpt-image-2`, e toda
geração grava na área externa `_revisao`.

## O que depende da fonte

Nada abaixo pode ser preenchido por inferência:

- quais eixos o material cobre em cada ano;
- se a alfabetização segue método específico e qual;
- quais gêneros textuais entram, e em que ano;
- se a letra cursiva entra em algum momento, e quando;
- a progressão entre bimestres.
