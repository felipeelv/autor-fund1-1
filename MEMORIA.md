# Memória de produção — observações e características

Lições transversais, aprendidas produzindo conteúdo real neste repositório,
que não pertencem a um único autor. O que já está registrado em
`autores/<id>/direcao/MEMORIA.md` ou `PADRAO-VISUAL-<N>ANO.md` de um autor
específico não é repetido aqui — este arquivo guarda o que vale para
qualquer autor.

## Fluxo `preparar.py` → prompt aprovado

- `--inventario` numera as seções da fonte; esses números são a entrada de
  `--recorte`, então rodar o inventário de novo depois de editar a fonte
  pode mudar a numeração — recontar antes de montar o YAML de recorte.
- o extrator de literais (`gerador_imagens/sources.py`) deduplica dentro de
  uma seção: se a mesma frase aparece duas vezes na fonte dentro da mesma
  seção (por exemplo, duas estruturas paralelas que compartilham um rótulo,
  como "Quadro 1: Início" repetido ao comparar "4 quadros" com "6 quadros"),
  ela some da lista de TEXTOS EXATOS depois da primeira ocorrência. Isso não
  significa que o texto deve desaparecer da página: se as duas estruturas
  fazem sentido lado a lado, a COMPOSIÇÃO do prompt precisa reescrever a
  segunda ocorrência manualmente. Nesse caso, repetir o rótulo nas duas
  estruturas não viola "renderizar cada texto literal exatamente uma vez" —
  essa trava é sobre não inventar repetição decorativa, não sobre proibir que
  duas listas genuinamente distintas da fonte compartilhem um rótulo.
- o gerador nunca escreve PEDIDO nem COMPOSIÇÃO por conta própria — isso é
  sempre `<<DECISÃO EDITORIAL>>` no rascunho, de propósito. Preencher essas
  duas seções é o trabalho real de transformar rascunho em `-v1`.
- conferir a lista de TEXTOS EXATOS do rascunho contra a COMPOSIÇÃO escrita:
  é fácil, ao detalhar a composição, esquecer de mencionar um item que a
  extração trouxe (aconteceu com um bloco "Em HQs" numa correção real desta
  produção — o item ficou de fora da composição na primeira escrita e só foi
  notado ao comparar as duas listas lado a lado).

## Limite de tamanho do prompt

O modelo `grok-imagine-image-2.0` rejeita com erro 400 (via OpenRouter; não
testado ainda pela xAI nativa) prompts acima de **8.000 bytes UTF-8** — não
8.000 caracteres. A diferença importa exatamente no tipo de texto que este
autor produz: cada vogal acentuada (á, é, í, ó, ú, ã, õ, â, ê, ô, ç) ocupa 2
bytes em UTF-8, não 1. Uma página sobre acentuação — cheia de sílabas
acentuadas — pode medir ~7.700 caracteres e ainda assim passar de 8.000
bytes; foi o que aconteceu numa correção real desta produção, aprovada pela
contagem de caracteres e recusada pela API. Medir sempre em bytes, somando
`prompt_prefixo` + corpo do `.md` + `prompt_sufixo` do autor:

```bash
uv run python -c "
from pathlib import Path
from gerador_imagens.renderers import render_prompt
from gerador_imagens.authors import aplicar_autor
root = Path('.')
prompt = render_prompt(root, root / '<caminho-do-prompt>.md', 'texto')
full, _ = aplicar_autor(root, '<autor>', prompt)
print('chars:', len(full), 'bytes:', len(full.encode('utf-8')))
"
```

Para o autor `portugues`, prefixo+sufixo somam ~3.200 caracteres (~3.300
bytes); o corpo do `.md` precisa deixar folga para o texto acentuado —
alvo prático de ~4.000-4.500 caracteres quando o conteúdo tem acentuação
pesada, menos do que os ~4.700 que bastam para texto sem acento.

## Densidade visual e variação entre páginas

Uma página de conteúdo pode ter todo o texto certo e ainda falhar como
material didático se o layout for fraco: núcleos em faixas horizontais
soltas, com grandes áreas brancas entre eles, lê como cartaz de slide, não
como página de apostila. Referências úteis de outro autor deste repositório
(adaptar o princípio, nunca depender do arquivo — CLAUDE.md seção 2 proíbe
isso entre repositórios diferentes, mas entre autores do mesmo repositório
vale citar e adaptar):

- colagem em camadas densas, com sombra projetada e fixação física (fita,
  clipe, alfinete, canto dobrado) — o branco vira fresta entre camadas, não
  fundo largo;
- variar o material do recorte por núcleo (kraft, pautado, quadriculado,
  papel liso colorido) evita que a página pareça um template repetido;
- variar o estilo do título entre páginas consecutivas de uma mesma unidade
  (bloco rasgado, faixa cursiva, fita diagonal, balão de fala, selo
  circular, fita crepe, explosão de quadrinho, etiqueta de prancheta —
  testados nas 8 páginas da Unidade 6 de Português) evita que a unidade
  inteira pareça produzida por um molde único, mesmo mantendo a mesma
  paleta e a mesma trava de conteúdo.
- uma tabela que a fonte apresenta em Markdown chega ao rascunho como lista
  solta de células (o extrator não entende estrutura de tabela); a
  COMPOSIÇÃO do prompt precisa reconstituí-la explicitamente como tabela de
  N colunas, célula por célula, na ordem certa.
- pistas de ilustração da própria fonte bruta (texto entre
  `[Ilustração: ...]`) não são texto a renderizar, mas são a melhor fonte de
  referência visual disponível — usá-las para decidir pose, cenário ou
  objeto evita inventar uma composição do zero.

## O que o modelo não desenha com exatidão

Aprendido produzindo as páginas de Estatística do 3º ano (19/08/2026), depois
de cinco gerações fracassadas no mesmo tipo de elemento. Vale para qualquer
autor que peça quantidade desenhada:

- **contar marcas repetidas**: uma coluna com N traços que precisa bater com um
  número escrito sai errada com frequência. Marcas soltas erram menos que
  marcas agrupadas de cinco em cinco, mas ainda erram. Duas linhas com números
  diferentes chegaram a sair com desenho idêntico;
- **posicionar ponto em coordenada exata**: num gráfico de linhas com escala de
  2 em 2, os pontos caem entre marcas ou trocam de valor. Barras que precisam
  terminar sobre a linha da malha funcionam melhor — bastou pedir "o topo cai
  exatamente sobre a linha da malha do seu número" para corrigir de uma vez;
- **restrição negativa pode virar desenho**: escrever "o ponto NÃO fica no 28"
  veio acompanhado de um ponto órfão exatamente no 28. Vale evitar a negação e
  descrever só o estado desejado — mas atenção: reescrever a mesma página sem
  nenhuma negação **não** corrigiu o gráfico, saiu pior. Ou seja, a negação não
  era a causa principal; é uma suspeita razoável, não uma regra estabelecida;
- quando duas formulações progressivamente mais explícitas falham no mesmo
  ponto, o problema deixou de ser redação de prompt. Vale mudar o desenho
  pedido — menos pontos, escala mais simples, contagem exemplificada em vez de
  completa — ou tirar aquele elemento do gerador, em vez de gastar crédito em
  tentativas cegas.

Conferir contagem e posição por análise de pixels, não por impressão visual:
recortar e ampliar a região com pillow revela erro que passa batido na leitura
da página inteira.

## Revisão humana da imagem gerada

Antes de aprovar, conferir a imagem inteira contra a lista de TEXTOS EXATOS
do prompt, item por item — não só ler por cima. Erros que passam batido numa
leitura rápida: um item da lista que ficou de fora da imagem; uma palavra
com acento errado num recorte pequeno; uma caixinha de checklist que veio
marcada quando devia ficar vazia. `validar.py --acervo` confere estrutura e
levanta avisos de conteúdo sensível (datas, percentuais) para revisão — não
substitui olhar a imagem.

## Roteamento por OpenRouter (contexto, não repetir a decisão)

Quando não há `XAI_API_KEY` nativa mas há uma chave da OpenRouter, existe um
caminho autorizado (`modelo.provider: openrouter`, adicionado em 19/08/2026)
que chama o mesmo modelo Grok por um endpoint diferente
(`POST https://openrouter.ai/api/v1/images`, não
`client.images.generate()` do SDK da OpenAI). Detalhes técnicos e a
autorização estão em `CLAUDE.md`, seção 3 — não duplicar aqui. O ponto que
vale lembrar: uma chave de gateway de terceiro (OpenRouter, ou qualquer
outro) nunca deve ser gravada como se fosse a credencial nativa do provedor
que ela não é — os dois têm endpoint e contrato de requisição diferentes, e
tentar isso simplesmente falha na autenticação.
