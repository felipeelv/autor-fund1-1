---
estado: aprovado
revisor: Nicolas Basso
aprovado_em: 2026-09-17
origem: unidade-04-bloco-01-p02-what-time-is-it-rascunho.md
---
Use case: scientific-educational
Asset type: página 2 de uma sequência didática de Inglês do 3º ano


## PEDIDO

Criar uma única página vertical 2:3, pronta para impressão, que ensine a
estrutura "It's... o'clock" com uma amostra de relógios ilustrados e a
pergunta "What time is it?" com três diálogos de prática. Fica de fora: a
tabela completa dos 12 horários (já coberta pela tabela de números da p1) e
o exercício de completar lacunas, que é atividade.

Título previsto: What Time Is It?

## SISTEMA VISUAL

Seguir integralmente `autores/ingles/direcao/PADRAO-VISUAL-3ANO.md` e o que
se mantém de `PADRAO-VISUAL-1ANO.md`. Para o 3º ano: 4 a 6 núcleos por
página (estrutura "it's o'clock", amostra de relógios, estrutura "what time
is it", três diálogos), corpo legível para leitura autônoma, ilustração de
relógio como suporte que ancora o texto.

## COMPOSIÇÃO E TÍTULO

- topo com o título "WHAT TIME IS IT?";
- núcleo "IT'S... O'CLOCK" com a definição e quatro relógios ilustrados de
  amostra (3h, 7h, 9h, 12h), cada um com sua frase "It's [number] o'clock.";
- núcleo "WHAT TIME IS IT?" com a definição da pergunta e resposta-modelo;
- faixa "LET'S TALK!" com os três diálogos de prática, em balão de fala
  entre duas crianças, cada um repetindo a pergunta "What time is it?"
  seguida da resposta;
- caminho de leitura: título → it's o'clock (com relógios) → what time is
  it? → diálogos.

## TEXTOS EXATOS

Renderizar cada um exatamente uma vez, na ordem abaixo.

- WHAT TIME IS IT?
- IT'S... O'CLOCK
- O'clock (o'clók) = horas (hora cheia)
- It's three o'clock. (São três horas.)
- It's seven o'clock.
- It's nine o'clock.
- It's twelve o'clock.
- WHAT TIME IS IT?
- What time is it? (uót táim is it?) = Que horas são?
- LET'S TALK!
- What time is it?
- It's seven o'clock.
- What time is it?
- It's twelve o'clock.
- What time is it?
- It's nine o'clock.

### Nota de correção

O extrator deduplica frases repetidas dentro da mesma seção (registrado em
`MEMORIA.md` da raiz): a pergunta "What time is it?" dos diálogos 2 e 3
tinha sumido do rascunho, restando só a resposta. Restaurada manualmente nos
três diálogos, conferida contra a fonte bruta (`4bim-bloco1.md`, seção
ASKING AND ANSWERING). Da tabela "TELLING TIME - HOURS" da fonte (12
relógios), a composição usa quatro como amostra ilustrada (3, 7, 9 e 12
horas) — corte de densidade: a tabela completa duplicaria a lista de
números já ensinada na p1.

## TRAVAS

Valem as travas de `autores/ingles/anos/3ano/REGRAS.md` e o `prompt_sufixo` do autor, que o gerador
injeta automaticamente.

Invioláveis, independentes de ano: não inventar número, nome próprio, data,
lugar, povo ou termo ausente da fonte; renderizar cada texto literal exatamente
uma vez; nenhum texto além da lista de TEXTOS EXATOS. Não usar mascote,
logotipo, número de página, fotografia de banco de imagens ou estética de
desenho animado comercial. Os relógios devem mostrar o ponteiro exatamente
sobre a hora indicada (topo = 12, sem minutos).
