# Direção — `ingles-atividades`

## O que este autor faz

Produz páginas de **atividades** de Inglês do Fundamental I. O aluno recebe a
página para responder: caderno de casa, fixação, revisão.

A separação em relação ao autor `ingles` é de função, não de assunto. Os dois
tratam do mesmo currículo e usam a mesma linguagem visual. O `ingles` explica e
apresenta; este entrega enunciado e espaço de resposta.

## Regra que define o autor

**Nada aparece respondido.** Nenhuma resposta escrita, nenhum item circulado,
nenhum `Yes` ou `No` marcado, nenhum visto ou xis já preenchido, nenhum quadro
de desenho com desenho dentro, nenhuma lacuna completada.

Essa trava não é preferência de estilo: uma página de atividade que chega
respondida está inutilizada. Ela é conferida página a página antes da promoção.

## Fidelidade à fonte

Nenhuma atividade é criada, cortada, reescrita, reordenada ou renumerada. O
enunciado e a numeração aparecem exatamente como a fonte os escreve. Quando uma
unidade não cabe em uma página, a divisão é decidida e aprovada **antes** da
geração, e registrada.

## Espaço de resposta

O espaço de resposta é conteúdo, não sobra de layout. Linha pautada, quadro
vazio, grade ou par de opções, sempre proporcional à idade: quanto mais nova a
criança, mais largo o espaço, porque o traço é maior e menos firme.

A ilustração dá a pista do sentido e nunca ocupa, cobre ou encosta no espaço
destinado à escrita.

## Conferência obrigatória

Antes de promover, uma pessoa confere palavras, frases, traduções e ortografia
inglesa, literalmente, além da trava de nada preenchido e da correspondência
entre numeração e enunciado. O `--dry-run` não substitui essa conferência e o
OCR é triagem.

## Produção

A produção usa somente fontes internas versionadas em
`../anos/<ano>/fontes/<periodo>/`. Cada recorte exige prompts próprios e projeto
YAML declarando provedor e modelo. Toda geração grava na área externa
`_revisao`.
