---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-09-09
origem: unidades-07-08-p05-dinheiro-brasileiro-moedas-e-cedulas-v2-correcao-valor-e-cores.md
nota_correcao: |-
  Correção de defeito de geração (v2 -> v3), 09/09/2026. A v2 corrigiu a
  coluna VALOR das moedas, mas a tabela de cédulas (4 colunas: CÉDULA /
  VALOR / COR / ANIMAL) saiu com uma coluna extra de texto duplicado e
  confuso (ex.: "Azal" em vez de repetir "Azul", "Amareda" em vez de
  "Amarela") e as cores das cédulas continuaram sem bater com a coluna COR.
  A correção abandona o formato de tabela de 4 colunas para as cédulas —
  que parece ser a origem da confusão — e usa 7 fileiras simples (ilustração
  + valor + cor + animal em uma linha só, sem cabeçalhos de coluna), mais
  fácil de o modelo manter alinhado.
---
Use case: scientific-educational
Asset type: página 5 de uma sequência didática de Matemática do 2º ano


## PEDIDO

Apresentar o dinheiro brasileiro (o Real, R$) e para que serve, depois as
moedas (centavos e a moeda especial de 1 real) e as cédulas, cada uma com sua
cor e o animal brasileiro que carrega — fechando com a ideia de que cédulas
valem mais que moedas. Nada da fonte desta seleção fica de fora.

Título previsto: Dinheiro Brasileiro: Moedas e Cédulas

## SISTEMA VISUAL

Fundo branco puro `#FFFFFF`. 3 núcleos em papel colado, corredores de
branco entre eles (densidade 2º ano: 3 a 4). Papel fixo por cor: azul
`#2F6FD0` na abertura sobre o que é dinheiro, amarelo `#F6C945` nas moedas,
laranja `#F28C32` nas cédulas — progressão azul→amarelo→laranja acompanha
conceito→menor valor→maior valor. Caixa alta de imprensa em REAL, MOEDAS e
CÉDULAS, minúscula no corpo, pauta média.

Regra de cor à prova de erro: cada moeda e cada cédula é pintada
EXATAMENTE na cor escrita na própria linha da tabela ao lado dela — nunca
uma cor decorativa livre, nunca a cor de uma nota real diferente. R$ 2 =
predominantemente AZUL; R$ 5 = predominantemente ROXA/LILÁS; R$ 10 =
predominantemente VERMELHA; R$ 20 = predominantemente AMARELA; R$ 50 =
predominantemente MARROM; R$ 100 = predominantemente AZUL-TURQUESA; R$ 200
= predominantemente CINZA.

## COMPOSIÇÃO E TÍTULO

- título `DINHEIRO BRASILEIRO: MOEDAS E CÉDULAS`, caixa alta, papel azul
  rasgado, alto e à esquerda;
- núcleo 1, papel azul: "O DINHEIRO é o que usamos para comprar coisas. No
  Brasil, nossa moeda se chama REAL." com o símbolo `R$` e `PARA QUE SERVE
  O DINHEIRO?` (3 itens);
- núcleo 2, papel amarelo: "MOEDAS são feitas de metal e servem para
  valores menores." com "O REAL é dividido em 100 partes chamadas
  CENTAVOS." e a tabela `MOEDA / VALOR / COR` com as 4 linhas de centavos —
  a coluna MOEDA leva só o desenho da moeda (sem nenhum texto dentro dela),
  a coluna VALOR leva o texto "5 centavos" / "10 centavos" / "25 centavos"
  / "50 centavos" por extenso (nunca "...", nunca vazia), a coluna COR leva
  "Dourada (bronze)" nas três primeiras linhas e "Prateada" na última;
  fecha com "📌 IMPORTANTE: 100 centavos = 1 real!" e, ao lado, a moeda
  especial: "A moeda de 1 REAL é especial - ela tem duas cores!" com
  `MOEDA / VALOR / CARACTERÍSTICA` (1 real, dourada por fora e prateada por
  dentro) e "💡 PARA LEMBRAR: a moeda de 1 real vale o mesmo que 100
  centavos!";
- núcleo 3, protagonista por reunir mais itens, papel laranja: "CÉDULAS são
  feitas de papel especial e servem para valores maiores." Sem tabela de
  colunas — 7 fileiras horizontais empilhadas, do menor para o maior valor,
  cada fileira com a cédula ilustrada à esquerda (na cor exata da regra de
  cor do SISTEMA VISUAL) e, ao lado, os três textos dessa cédula em uma
  linha só: (1) R$ 2, Azul, Tartaruga marinha; (2) R$ 5, Roxa/Lilás, Garça;
  (3) R$ 10, Vermelha, Arara; (4) R$ 20, Amarela, Mico-leão-dourado; (5) R$
  50, Marrom, Onça-pintada; (6) R$ 100, Azul-turquesa, Garoupa; (7) R$ 200,
  Cinza, Lobo-guará — sem cabeçalho de coluna nenhum, cada fileira é
  independente e completa em si mesma; fecha com "📌 DICA PARA LEMBRAR:
  cada cédula tem uma COR e um ANIMAL brasileiro!" e "💡 as cédulas valem
  mais que as moedas — a menor cédula (R$ 2) já vale mais que a maior
  moeda (R$ 1)."

## TEXTOS EXATOS

Extraídos literalmente da fonte. Revisar: remover o que não cabe na página,
ajustar a ordem e condensar onde a leitura pedir — sem trocar número, nome
próprio, unidade ou termo técnico.

- O DINHEIRO é o que usamos para comprar coisas. No Brasil, nossa moeda se chama REAL.
- O símbolo do Real é: R$
- PARA QUE SERVE O DINHEIRO?
- - Comprar comida, brinquedos, roupas
- - Pagar por serviços (ônibus, cinema)
- - Guardar para usar depois (poupar)
- MOEDAS são feitas de metal e servem para valores menores.
- O REAL é dividido em 100 partes chamadas CENTAVOS.
- MOEDA
- VALOR
- COR
- 5 centavos
- Dourada (bronze)
- 10 centavos
- 25 centavos
- 50 centavos
- Prateada
- 📌 IMPORTANTE
- 100 centavos = 1 real
- Precisamos de 100 centavos para formar 1 real!
- A moeda de 1 REAL é especial - ela tem duas cores!
- CARACTERÍSTICA
- 1 real
- Dourada por fora, prateada por dentro
- 💡 PARA LEMBRAR
- A moeda de 1 real é a moeda de maior valor. Ela vale o mesmo que 100 centavos!
- CÉDULAS são feitas de papel especial e servem para valores maiores.
- R$ 2
- Azul
- Tartaruga marinha
- R$ 5
- Roxa/Lilás
- Garça
- R$ 10
- Vermelha
- Arara
- R$ 20
- Amarela
- Mico-leão-dourado
- R$ 50
- Marrom
- Onça-pintada
- R$ 100
- Azul-turquesa
- Garoupa
- R$ 200
- Cinza
- Lobo-guará
- 📌 DICA PARA LEMBRAR
- Cada cédula tem uma COR diferente e um ANIMAL brasileiro! Isso ajuda a identificar rapidamente.
- As cédulas valem mais que as moedas. A menor cédula (R$ 2) já vale mais que a maior moeda (R$ 1).

## TRAVAS

Valem as travas de `autores/matematica/anos/2ano/REGRAS.md` e o `prompt_sufixo` do autor, que o gerador
injeta automaticamente.

Invioláveis, independentes de ano: não inventar número, nome próprio, data,
lugar, povo ou termo ausente da fonte; renderizar cada texto literal exatamente
uma vez; nenhum texto além da lista de TEXTOS EXATOS.
