# Padrão visual — Português · 2º ano

> **Derivado** do `PADRAO-VISUAL-3ANO.md` deste autor, em 18/08/2026, seguindo
> `compartilhado/direcao-editorial/DERIVACAO-ENTRE-ANOS.md`. O 3º ano, por sua
> vez, foi derivado do autor `matematica`.
>
> **Ajustado com Nicolas Basso em 19/08/2026**, no primeiro lote real deste
> ano (Unidade 6, 8 páginas) — ver seção "Densidade e camadas" abaixo, que é
> o resultado desse ajuste e passa a valer para todas as páginas seguintes.

## O que muda neste ano

| Eixo | 2º ano |
|---|---|
| público | crianças de aproximadamente 7 anos |
| autonomia de leitura | a criança lê com apoio da imagem |
| núcleos por página | 3 a 4, em 4 a 7 recortes |
| tipografia | corpo grande; **minúscula de imprensa entra**, sem misturar tipos na mesma palavra |
| unidade em foco | palavra e frase curta completa |
| papel da ilustração | apoio: dá a pista do sentido, o texto conclui |
| composição | imagem e texto em equilíbrio |

## A transição tipográfica

Este é o ano em que a minúscula de imprensa entra, e é a fonte que decide
quando. Enquanto a decisão não vier, tratar caixa alta e minúscula como dois
registros distintos: uma mesma palavra nunca mistura os dois, e a página deixa
claro qual registro está em uso.

Quando a página compara os dois registros, eles aparecem lado a lado, na mesma
escala e com a mesma palavra — a comparação é o conteúdo, não um efeito visual.

## Ortografia em foco

Palavras que compartilham o mesmo padrão ortográfico ficam visualmente
agrupadas, com o padrão destacado sempre da mesma forma dentro do agrupamento.
Exceções recebem a cor de alerta, e não se misturam ao grupo regular.

## O que se mantém

Tudo o que `PADRAO-VISUAL-3ANO.md` define e não aparece acima, além das travas
invioláveis, que não variam com a idade.

## Densidade e camadas (ajuste de 19/08/2026)

> Correção de Nicolas Basso sobre a página 1 da Unidade 6 (rascunho v1): o
> material didático precisa de mais densidade explicativa. Referência de
> layout adotada: `autores/natureza-e-sociedade/direcao/PADRAO-VISUAL-3ANO.md`,
> aprovado pelo Felipe para aquele autor — adaptado aqui, não copiado.

O layout de v1 organizava os núcleos em faixas horizontais empilhadas, com
áreas brancas grandes entre elas. Isso lê como cartaz de slide, não como
página de apostila. A partir deste ajuste:

- **densidade alta, como colagem em camadas**: os recortes se sobrepõem em
  alturas e rotações levemente diferentes, nunca alinhados em grade rígida
  nem em faixas horizontais estritas; o branco aparece como fresta entre
  camadas, não como fundo largo — sem grandes áreas vazias;
- **camadas físicas mais ricas**: sombra suave projetada por recorte, e ao
  menos dois elementos de fixação por página entre fita adesiva, clipe
  metálico, alfinete ou canto dobrado — variando quais aparecem página a
  página;
- **mais conexão visual entre os núcleos**: setas à mão, círculos e
  sublinhados de marca-texto ligando um recorte ao outro, mostrando a relação
  entre eles — por exemplo, a pergunta motivadora ligada ao recorte que a
  responde. Esses elementos são desenho, nunca texto novo: continuam proibidos
  criar frase, rótulo ou legenda fora da lista de TEXTOS EXATOS do prompt;
- a legibilidade continua vencendo a densidade: nenhum texto fica sobre imagem
  concorrida ou espremido contra outro recorte — a criança de 7 anos precisa
  ler sem esforço.

Este ajuste vale para todas as páginas produzidas a partir de agora por este
autor, em qualquer ano; páginas já aprovadas antes desta data não precisam ser
refeitas só por isto.

**Limite de tamanho, aprendido no mesmo ajuste**: o prompt enviado ao
`grok-imagine-image-2.0` (nativo ou via OpenRouter) é rejeitado com erro 400
acima de **8.000 bytes UTF-8** — não 8.000 caracteres; texto com muita
acentuação (comum em Português) pesa mais em bytes do que em caracteres.
Somando `prompt_prefixo` + corpo do `.md` + `prompt_sufixo` do autor
(prefixo e sufixo juntos somam ~3.200 caracteres / ~3.300 bytes), manter o
corpo do `.md` por volta de 4.000-4.700 caracteres ao pedir mais densidade
visual, medindo sempre em bytes — ver `MEMORIA.md` na raiz do repositório
para o comando de medição.
