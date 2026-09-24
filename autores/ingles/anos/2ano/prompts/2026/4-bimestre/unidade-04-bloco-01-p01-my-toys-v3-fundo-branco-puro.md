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
puro (fundo `#FFFFFF`, sem tom creme ou amarelado), colagem de papel
recortado com pintura guache, sketchnote profissional. Para o 2º ano: 3 a 4
núcleos por página (aqui: abertura da unidade, vocabulário de brinquedos,
estrutura "I have a...", curiosidade), tipografia em corpo grande com
minúscula de imprensa, ilustração como apoio que dá a pista do sentido
enquanto o texto conclui. Uma criança brasileira pode aparecer segurando ou
apontando para um dos brinquedos, sem ocupar mais de um quinto da página.

## COMPOSIÇÃO E TÍTULO

- fundo da página inteira branco puro, sem faixa, painel ou textura colorida
  cobrindo grandes áreas — cor entra só nos recortes de colagem e acentos;
- topo com o título "MY TOYS";
- logo abaixo, faixa "NESTA UNIDADE VOCÊ VAI APRENDER" com os quatro itens
  da lista (brinquedos, cores, estruturas, músicas e gestos), em corpo
  pequeno;
- núcleo central "MEET THE TOYS" com os seis brinquedos, cada um como um
  recorte de colagem com a ilustração do objeto, a palavra em inglês em
  destaque e a tradução logo abaixo: BALL (bola), DOLL (boneca), CAR
  (carrinho), TEDDY BEAR (ursinho), KITE (pipa), ROBOT (robô);
- bloco "I HAVE A..." com a estrutura e as seis frases-exemplo, uma por
  brinquedo, cada frase acompanhada do MESMO ícone do brinquedo já usado em
  "MEET THE TOYS" logo acima — a frase "I have a ball" precisa ficar ao lado
  da bola, "I have a doll" ao lado da boneca, e assim por diante, sem trocar
  nenhum ícone entre frases;
- faixa "DID YOU KNOW?" com a curiosidade sobre o nome "teddy bear", em corpo
  menor, como nota lateral;
- caminho de leitura: título → o que você vai aprender → seis brinquedos →
  estrutura "I have a..." → curiosidade.

## TEXTOS EXATOS

Renderizar cada um exatamente uma vez, na ordem abaixo.

- MY TOYS
- NESTA UNIDADE VOCÊ VAI APRENDER
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

Correção sobre a v2 (17/09/2026), depois de três tentativas de geração com
defeitos diferentes: (1) o fundo estava especificado como "papel branco
quente", em desacordo com `CLAUDE.md` seção 1 — corrigido para branco puro
`#FFFFFF`; (2) em duas das três gerações da v2, os ícones ao lado de cada
frase "I have a X" não correspondiam ao brinquedo citado (ex.: ícone de pipa
ao lado de "I have a teddy bear") — a composição agora pede explicitamente
que cada frase reaproveite o mesmo ícone já usado em "MEET THE TOYS", em vez
de desenhar um novo ícone livre; (3) em todas as três gerações da v2, o nome
"Theodore 'Teddy' Roosevelt" saiu com a grafia errada ("Rooseveit") — mantido
aqui como está na fonte, grafia correta é ROOSEVELT.

## TRAVAS

Valem as travas de `autores/ingles/anos/2ano/REGRAS.md` e o `prompt_sufixo` do autor, que o gerador
injeta automaticamente.

Invioláveis, independentes de ano: não inventar número, nome próprio, data,
lugar, povo ou termo ausente da fonte; renderizar cada texto literal exatamente
uma vez; nenhum texto além da lista de TEXTOS EXATOS. Não usar mascote,
logotipo, número de página, fotografia de banco de imagens ou estética de
desenho animado comercial. Grafar "Roosevelt" exatamente assim, sem trocar
nem omitir nenhuma letra.
