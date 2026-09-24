---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-09-17
origem: unidade-04-bloco-01-p01-my-toys-rascunho.md
---
Use case: scientific-educational
Asset type: página 1 de uma sequência didática de Inglês do 2º ano


## PEDIDO

Criar uma única página vertical 2:3, pronta para impressão, que abra a
unidade com o que a criança vai aprender e apresente os seis brinquedos em
inglês (ball, doll, car, teddy bear, kite, robot) por meio de ilustração
concreta, tradução e a estrutura "I have a...". Fecha com a curiosidade
sobre a origem do nome "teddy bear". Fica de fora: a estrutura "My favorite
toy is..." e o vocabulário de cores, que pertencem à página seguinte.

Título previsto: My Toys

## SISTEMA VISUAL

Seguir integralmente `autores/ingles/direcao/PADRAO-VISUAL-2ANO.md` e o que
se mantém de `PADRAO-VISUAL-1ANO.md`: página vertical 2:3, papel branco
quente, colagem de papel recortado com pintura guache, sketchnote
profissional. Para o 2º ano: 3 a 4 núcleos por página (aqui: abertura da
unidade, vocabulário de brinquedos, estrutura "I have a...", curiosidade),
tipografia em corpo grande com minúscula de imprensa, ilustração como apoio
que dá a pista do sentido enquanto o texto conclui. Uma criança brasileira
pode aparecer segurando ou apontando para um dos brinquedos, sem ocupar mais
de um quinto da página.

## COMPOSIÇÃO E TÍTULO

- topo com o título "MY TOYS";
- logo abaixo, faixa "IN THIS UNIT, YOU WILL LEARN" com os quatro itens da
  lista (brinquedos, cores, estruturas, músicas e gestos), em corpo pequeno;
- núcleo central "MEET THE TOYS" com os seis brinquedos, cada um como um
  recorte de colagem com a ilustração do objeto, a palavra em inglês em
  destaque e a tradução logo abaixo: BALL (bola), DOLL (boneca), CAR
  (carrinho), TEDDY BEAR (ursinho), KITE (pipa), ROBOT (robô);
- bloco "I HAVE A..." com a estrutura e as seis frases-exemplo, uma por
  brinquedo, cada frase próxima ao recorte correspondente;
- faixa "DID YOU KNOW?" com a curiosidade sobre o nome "teddy bear", em corpo
  menor, como nota lateral;
- caminho de leitura: título → o que você vai aprender → seis brinquedos →
  estrutura "I have a..." → curiosidade.

## TEXTOS EXATOS

Renderizar cada um exatamente uma vez, na ordem abaixo.

- MY TOYS
- IN THIS UNIT, YOU WILL LEARN
- Brinquedos: ball, doll, car, teddy bear, kite, robot
- Cores: red, blue, yellow, green, orange, purple, pink, brown, black, white
- Estruturas: I have a... / My favorite... is...
- Músicas e gestos para aprender brincando
- MEET THE TOYS
- BALL — bola
- DOLL — boneca
- CAR — carrinho
- TEDDY BEAR — ursinho
- KITE — pipa
- ROBOT — robô
- I HAVE A...
- I have a ball. (Eu tenho uma bola)
- I have a doll. (Eu tenho uma boneca)
- I have a car. (Eu tenho um carrinho)
- I have a teddy bear. (Eu tenho um ursinho)
- I have a kite. (Eu tenho uma pipa)
- I have a robot. (Eu tenho um robô)
- DID YOU KNOW?
- A palavra "teddy bear" (ursinho de pelúcia) vem do presidente americano
  Theodore "Teddy" Roosevelt! Em 1902, ele se recusou a atirar em um urso
  durante uma caçada, e alguém criou um ursinho de brinquedo em sua
  homenagem!

### Nota de correção

O extrator não capturou o vocabulário da seção VOCABULÁRIO - TOYS (mesmo
formato `*[Ilustração: ...]* **PALAVRA** - tradução` sem marcador de lista já
registrado em `MEMORIA.md` da raiz); os seis pares palavra/tradução acima
foram copiados manualmente da fonte bruta e conferidos contra o original. A
quebra de linha "Cores - .../ white" é artefato de largura do extrator, unida
em uma frase só sem alterar palavra alguma.

## TRAVAS

Valem as travas de `autores/ingles/anos/2ano/REGRAS.md` e o `prompt_sufixo` do autor, que o gerador
injeta automaticamente.

Invioláveis, independentes de ano: não inventar número, nome próprio, data,
lugar, povo ou termo ausente da fonte; renderizar cada texto literal exatamente
uma vez; nenhum texto além da lista de TEXTOS EXATOS. Não usar mascote,
logotipo, número de página, fotografia de banco de imagens ou estética de
desenho animado comercial.
