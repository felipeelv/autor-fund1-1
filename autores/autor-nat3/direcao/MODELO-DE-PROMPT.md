# Modelo de prompt — `autor-nat3`

Esqueleto canônico do layout aprovado em 15 de agosto de 2026
(lote `povos-indigenas-6paginas-v3`). Copie o bloco abaixo, troque o que está
entre `<>` e mantenha o resto. Leia antes o
[padrão visual](PADRAO-VISUAL-3ANO.md).

Regras de uso:

- escolha a variante CAPA apenas para a primeira página da unidade; todas as
  demais usam a variante PÁGINA INTERNA;
- mantenha o **corpo deste arquivo** abaixo de 4.800 caracteres; o gerador
  soma a ele cerca de 2.700 caracteres de prefixo e sufixo do `autor.yaml`, e
  corpos maiores já foram recusados pela API com erro 400;
- os `TEXTOS EXATOS` vêm do arquivo de conteúdo derivado da fonte, um item
  por linha, sem nada além do que será impresso;
- texto enxuto: frases curtas, uma ideia por bloco, sem simplificar as ideias.

---

```text
Use case: scientific-educational
Asset type: <capa | página interna> de uma sequência de Natureza e Sociedade do 3º ano

## PEDIDO

Página A4 vertical, proporção 210:297, <CAPA que abre a unidade | PÁGINA
INTERNA de apostila, não é capa>. Estilo: infográfico editorial contemporâneo
em colagem de mídia mista — editorial collage infographic, scrapbook
educativo sofisticado, visual note-taking. Composição densa e em camadas,
sempre legível. Assunto: <uma frase com o recorte da página>.

## HIERARQUIA

<Para CAPA:>
- título monumental no terço superior, tipografia sans-serif condensada muito
  grande, em blocos de cor sólida com recorte rasgado e leve rotação; é o
  elemento mais forte da página;
- subtítulo logo abaixo, em faixa de papel menor, com marca-texto.

<Para PÁGINA INTERNA:>
- título discreto no alto, em uma linha só, tipografia média, sobre tarja
  fina de cor ou apenas com filete colorido embaixo; nunca monumental;
- o elemento visual mais forte é <a imagem principal da página>;
- subtítulo em corpo pequeno, em itálico ou em papel vegetal.

## MÍDIA MISTA OBRIGATÓRIA

1. fotografia recortada real de <paisagem/textura pertinente>, com bordas de
   tesoura;
2. pintura em guache documental para <a cena histórica da página>;
3. textura escultórica de apoio em argila crua ou pedra bruta, superfície
   lisa, sem nenhuma marca gravada — sem inscrição, símbolo, glifo ou letra;
4. objetos recortados fotografados sobre fundo claro, corretos na forma:
   <lista de objetos>;
5. anotações manuscritas a grafite, setas à mão, círculos e sublinhados de
   marca-texto, como caderno de campo.

## COMPOSIÇÃO

- folha A4 inteira, sem sangria, margem branca contínua de 12 mm;
- fundo branco puro com camadas de papéis sobrepostos: kraft, pautado,
  milimetrado e vegetal translúcido; cada camada com sombra suave, fita
  adesiva, clipe metálico e canto dobrado;
- paleta: <dominantes da página>, com grafite para o texto;
- bordas com faixas finas de grafismos geométricos abstratos e editoriais,
  sem imitar grafismo ou cerâmica de nenhum povo;
- <núcleo principal da página: retrato, tabela, lista numerada, sequência de
  vinhetas, linha do tempo ou mosaico>;
- blocos de texto curtos em recortes de papel, em alturas diferentes;
- box <NOME DO BOXE> em moldura editorial neutra;
- densidade alta: sem grandes áreas vazias; o branco aparece como fresta
  entre as camadas;
- criança exploradora contemporânea ilustrada, pequena, colada como adesivo
  recortado FORA das cenas pintadas, sobre o papel branco da margem.

## TEXTOS EXATOS

<um item por linha, exatamente como será impresso>

## TRAVAS

<travas específicas da página: grafias, números, datas.> Dentro das cenas
pintadas não pode existir item moderno: nenhuma blusa, moletom, capuz,
camiseta, shorts, calça, boné, tênis, mochila ou pano azul; todas as pessoas
usam tangas, saias ou faixas de fibra natural em cru e terracota; sem cocar,
pintura corporal ou adereços cerimoniais; sem fotografia simulada de pessoas
do período. A criança exploradora é a única figura contemporânea e fica fora
das pinturas. Nenhum objeto da colagem traz escrita, glifo ou grafismo
cultural inventado. Não criar número, data, legenda, atividade ou frase
adicional. Nenhum texto além da lista literal.
```

---

## Projeto YAML correspondente

```yaml
modelo:
  provider: "xai"
  id: "grok-imagine-image-2.0"

parametros_api:
  tamanho: "auto"
  qualidade: "medium"
  formato: "jpeg"
  fundo: "auto"
  moderacao: "auto"
  proporcao: "2:3"
  resolucao: "2k"
  timeout: 300
```

A saída fica em `autor-nat3/3ano/<bimestre>/<lote>/<arquivo>.jpg`, sempre na
área `revisao`. Promova com `aprovar.py` somente depois da revisão humana.
