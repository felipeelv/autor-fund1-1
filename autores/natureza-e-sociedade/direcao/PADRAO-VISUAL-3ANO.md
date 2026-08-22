# Padrão visual — Natureza e Sociedade · 3º ano

> **Layout canônico:** o formato descrito aqui foi aprovado pelo Felipe em
> 15 de agosto de 2026, a partir do lote `povos-indigenas-6paginas-v3`, e
> passa a valer para **todas as páginas deste autor**. As páginas aprovadas
> desse lote são a referência visual de comparação. Não voltar ao layout
> anterior, de núcleos soltos sobre grandes áreas brancas.

## Base

- página vertical com fundo branco puro `#FFFFFF`;
- **proporção 2:3** (1664×2496 px), decidida pelo Felipe em 15 de agosto de
  2026: é a proporção vertical que o `grok-imagine-image-2.0` oferece, e a
  adaptação para A4 é feita na diagramação, fora do gerador. Os prompts pedem
  “página vertical, proporção 2:3”; não peça A4 nem 210:297;
- folha inteira visível, sem sangria, com margem branca contínua equivalente a
  12 mm nos quatro lados e todos os elementos dentro da área segura — essa
  margem também é a folga que a diagramação usa ao ajustar para A4;
- infográfico editorial contemporâneo: editorial collage infographic com
  scrapbook educativo sofisticado e visual note-taking;
- pelo menos um box informativo claramente reconhecível por página, usando
  somente texto literal do prompt;
- setas, linhas do tempo, círculos e mapas esquemáticos apenas quando ajudam a
  explicar uma relação;
- tipografia sans-serif arredondada, grande e de alto contraste.

## Densidade e camadas

A página é uma colagem em camadas, não um cartaz com elementos soltos.

- camadas de papéis sobrepostos: kraft, pautado, milimetrado e vegetal
  translúcido, cada um com sombra suave projetada, fita adesiva, clipe
  metálico, alfinete ou canto dobrado;
- os recortes entram com leve rotação e em alturas diferentes, nunca
  alinhados em grade rígida;
- densidade alta: o branco aparece como fresta entre as camadas, não como
  fundo largo; sem grandes áreas vazias;
- a legibilidade vence a densidade: nenhum texto pode ficar sobre imagem
  concorrida ou espremido contra outro recorte.

## Cinco naturezas de imagem por página

Toda página combina, de forma reconhecível:

1. **fotografia recortada real** de paisagem, textura ou objeto natural, com
   bordas de tesoura;
2. **pintura em guache documental** para cenas históricas — nunca simulando
   fotografia de pessoas do período;
3. **textura escultórica de apoio** em argila crua ou pedra bruta, de
   superfície lisa;
4. **objetos recortados fotografados** sobre fundo claro, botanicamente e
   materialmente corretos;
5. **anotações manuscritas a grafite**, setas à mão, círculos e sublinhados
   de marca-texto, como caderno de campo.

## Hierarquia por posição na unidade

- **capa** (primeira página da unidade): título monumental em blocos de cor
  sólida com recorte rasgado e leve rotação, ocupando o terço superior; é o
  elemento mais forte da página;
- **páginas internas**: título discreto em uma única linha, tipografia média,
  sobre tarja fina de cor ou apenas com filete colorido embaixo, ocupando no
  máximo duas linhas de altura; nelas o elemento mais forte é sempre a imagem
  principal, nunca o título;
- o subtítulo das internas vem em corpo pequeno, em itálico ou papel vegetal;
- variar, entre páginas consecutivas, a posição do título e o caminho de
  leitura, sem alterar essa hierarquia.

## Personagem recorrente

A criança exploradora contemporânea entra **colada como adesivo recortado
fora das cenas históricas**, sobre o papel branco da margem. Ela nunca pisa
dentro de uma pintura de período anterior a 1500 — é o que impede o modelo de
vestir as figuras históricas com roupa atual.

## Paleta

- grafite `#263238` para texto;
- verde mata `#2F7D4A` para território e cuidado;
- azul rio `#2F6FD0` para deslocamento, água e conexão;
- amarelo sol `#F6C945` para destaques;
- terracota `#C9653B` e vermelho urucum `#C9473D` para tempo e alertas;
- roxo `#7552A3` para diversidade e memória.

As cores são recursos editoriais. Não devem imitar grafismos de um povo sem
fonte e autorização.

## Representação responsável

- não existe “aparência indígena” única;
- não usar cocar genérico, pintura corporal inventada, nudez ou fantasia;
- não misturar objetos cerimoniais, casas ou grafismos de povos diferentes;
- preferir cenas cotidianas e contemporâneas quando não houver referência
  específica;
- usar fotografia de pessoas somente quando o período e a fonte permitirem;
  cenas anteriores à fotografia devem ser pintura ou desenho documental;
- usar mapas apenas como localização aproximada, nunca como demarcação;
- representar território como espaço de vida, memória e conhecimento, não como
  cenário vazio;
- variar idades, gêneros, tons de pele, ambientes e modos de vida;
- evitar composição de “antes civilizado × depois indígena”.

## Sequência

Cada página deve ter identidade própria e continuidade cromática. Alternar:

1. linha do tempo e paisagem;
2. mapa esquemático e nota histórica;
3. percurso de aprendizagem;
4. ciclos de observação e cuidado;
5. mosaico de modos de vida atuais;
6. dados e chamada de respeito.

## Mídia mista e boxes

- fotografias recortadas entram como paisagem, textura ou objeto real;
- pinturas e guaches representam cenas históricas sem simular fotografia;
- relevos de papel e argila devem ser editoriais, não cópias inventadas de
  artefatos ou grafismos indígenas;
- pedra, argila e cerâmica entram **lisas**: sem inscrição, símbolo, glifo,
  letra ou número gravado, e sem pintura decorativa;
- objetos recortados precisam apoiar uma ideia, nunca funcionar como fantasia;
- objetos naturais precisam estar corretos: uma planta citada no texto é
  desenhada como ela é de verdade;
- o box informativo deve destacar uma frase central da página sem acrescentar
  títulos, rótulos ou legendas.

## Travas de prompt já validadas

Aprendidas na produção do lote `povos-indigenas-6paginas-v3` com xAI
`grok-imagine-image-2.0`. Repetir em todo prompt novo:

- **limite de tamanho:** o cap de 8.000 bytes UTF-8 da OpenRouter cobre a
  string **montada** por `aplicar_autor` (`gerador_imagens/authors.py:78`) —
  `prompt_prefixo` + corpo da página + `prompt_sufixo`. Medido em 21/08/2026:
  prefixo 2.532 B + sufixo 747 B = 3.279 B fixos, sobrando **~4.721 B para o
  corpo**. Contar só o prefixo (esquecendo o sufixo) já causou um erro 400 com
  um corpo que a conta de cabeça dizia caber;
- **artefato com escrita:** pedir “relevo escultórico” sem qualificar faz o
  modelo gravar glifos que parecem escrita; exigir superfície lisa;
- **roupa moderna na cena histórica:** listar explicitamente as peças
  proibidas dentro da moldura da pintura (blusa, moletom, capuz, camiseta,
  shorts, calça, boné, tênis, mochila, pano azul) e manter a criança
  exploradora fora da cena;
- **objeto na linha errada:** em listas numeradas, dizer qual objeto pertence
  a cada número, ligado por seta curta e reta;
- **acentuação em corpo pequeno:** a palavra “indígenas” sai sem acento com
  frequência em texto miúdo; preferir reescrever a frase (“esses povos”) a
  insistir na trava de grafia.
