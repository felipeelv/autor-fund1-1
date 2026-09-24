Use case: scientific-educational
Asset type: página 1 de uma sequência didática de Inglês do 1º ano

> **RASCUNHO gerado por `preparar.py`.** Não é prompt aprovado.
>
> Fonte: `autores/ingles/anos/1ano/fontes/2026-2-semestre/4bim-bloco1.md`
> Trechos: THE FAMILY (linhas 14-15), VOCABULÁRIO (linhas 26-41), VOCÊ SABIA? (linhas 42-50), ESTRUTURA: THIS IS MY... (linhas 51-67)
> Autor: `ingles` · ano: `1ano` · unidade: unidade-04-bloco-01
>
> Antes de gerar imagem: resolver os pontos marcados como decisão editorial,
> conferir os textos exatos contra a fonte e salvar como `-v1` sem o aviso.

## PEDIDO

Criar uma única página vertical 2:3, pronta para impressão, que apresente os
seis membros da família em inglês (mom, dad, brother, sister, grandma,
grandpa) por meio de ilustração concreta, tradução e a estrutura "This is
my...". Fecha com uma curiosidade sobre apelidos carinhosos dos pais e avós.
Fica de fora desta página: a música "This is my Family" e os pronomes
he/she, que pertencem às páginas seguintes da unidade.

Título previsto: The Family

## SISTEMA VISUAL

Seguir integralmente `autores/ingles/direcao/PADRAO-VISUAL-1ANO.md`: papel
branco quente, colagem de papel recortado com pintura guache, sketchnote
profissional (setas, círculos, conectores) e visual note-taking orgânico,
sem grade rígida. Ilustração semirrealista de contornos orgânicos, títulos
grandes em sans-serif arredondada, seis cores didáticas vivas sobre estrutura
em grafite. Uma criança brasileira pode aparecer apontando para um membro da
família, sem ocupar mais de um quinto da página.

## COMPOSIÇÃO E TÍTULO

- topo compacto com o título "THE FAMILY";
- núcleo central "MEET THE FAMILY" com os seis membros, cada um como um
  recorte de colagem com a ilustração da pessoa, a palavra em inglês em
  destaque e a tradução logo abaixo: MOM (mamãe), DAD (papai), BROTHER
  (irmão), SISTER (irmã), GRANDMA (vovó), GRANDPA (vovô);
- faixa "DID YOU KNOW?" com a curiosidade sobre apelidos carinhosos (mommy,
  daddy, granny/nana, grandad/papa), em corpo menor, como nota lateral;
- bloco "THIS IS MY..." com a estrutura e as seis frases-exemplo, uma por
  membro da família, cada frase próxima ao recorte correspondente do núcleo
  central (seta ou linha curta ligando frase e ilustração);
- caminho de leitura: título → seis membros da família → curiosidade →
  estrutura "This is my...".

## TEXTOS EXATOS

Renderizar cada um exatamente uma vez, na ordem abaixo. Preservar acentos,
maiúsculas, pontuação e negrito conforme indicado.

- THE FAMILY
- MOM — mamãe
- DAD — papai
- BROTHER — irmão
- SISTER — irmã
- GRANDMA — vovó
- GRANDPA — vovô
- DID YOU KNOW?
- Em inglês, existem várias formas carinhosas de chamar os pais: MOM também
  pode ser MOMMY (mamãe), DAD também pode ser DADDY (papai), GRANDMA também
  pode ser GRANNY ou NANA, e GRANDPA também pode ser GRANDAD ou PAPA. Cada
  família escolhe como prefere chamar!
- THIS IS MY...
- This is my mom. (Esta é minha mãe)
- This is my dad. (Este é meu pai)
- This is my brother. (Este é meu irmão)
- This is my sister. (Esta é minha irmã)
- This is my grandma. (Esta é minha avó)
- This is my grandpa. (Este é meu avô)

### Nota de correção

O extrator de literais (`gerador_imagens/sources.py`) não capturou o
vocabulário da seção VOCABULÁRIO da fonte, porque cada item está no formato
`*[Ilustração: ...]* **PALAVRA** - tradução`, sem marcador de lista — o mesmo
tipo de lacuna já registrado em `MEMORIA.md` da raiz. Os seis pares
palavra/tradução acima (MOM–GRANDPA) foram copiados manualmente da fonte
bruta (seção VOCABULÁRIO de `4bim-bloco1.md`) e conferidos contra o original.

## TRAVAS

Valem as travas de `autores/ingles/anos/1ano/REGRAS.md` e o `prompt_sufixo` do autor, que o gerador
injeta automaticamente.

Invioláveis, independentes de ano: não inventar número, nome próprio, data,
lugar, povo ou termo ausente da fonte; renderizar cada texto literal exatamente
uma vez; nenhum texto além da lista de TEXTOS EXATOS. Não usar mascote,
logotipo, número de página, fotografia de banco de imagens ou estética de
desenho animado comercial. Não trocar a correspondência entre palavra em
inglês e ilustração/tradução.
