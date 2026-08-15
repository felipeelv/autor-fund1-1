# Registro de produção — 3º ano · Unidade 2 · caderno de atividades para casa · 2 páginas · v1

Data: 13/08/2026  
Estado: em revisão humana; não promovida para `aprovadas`.

## Pedido aprovado

Distribuir em duas páginas verticais as nove atividades do caderno de
atividades para casa da Unidade 2 do 3º ano, sobre esportes e o verbo `can`.
Nenhuma atividade foi criada, cortada ou reescrita: a divisão em páginas foi
apresentada e aprovada antes da geração.

## Organização

1. atividades 1 a 5 — reconhecer vocabulário e praticar a estrutura;
2. atividades 6 a 9 — aplicar, produzir texto e entrevistar.

O corte entre a 5 e a 6 equilibra os dois blocos mais pesados: a grade de doze
itens da Atividade 1 fica na página 1 e os três quadros de desenho da Atividade
7 ficam na página 2.

## Execução

- projeto: `projetos/2026/2-bimestre/unidade-02-homework-2paginas-v1.yaml`;
- provider: OpenAI;
- modelo: `gpt-image-2`;
- tamanho: `2048x3072`;
- qualidade: `high`;
- formato: PNG opaco;
- área: `_revisao` externa.

## Saídas

| Página | Caminho relativo externo | SHA-256 |
|---|---|---|
| Atividades 1 a 5 | `autor-fund1/3ano/2-bimestre/unidade-02-homework-v1/p01-sports-and-can-atividades-1-a-5-v1.png` | `8c4b1b3e73f968ff5141bb5c21d556755c319189e9b067fd159b97bacf09b860` |
| Atividades 6 a 9 | `autor-fund1/3ano/2-bimestre/unidade-02-homework-v1/p02-sports-and-can-atividades-6-a-9-v1.png` | `d45456241c27c60cc9c275dfd256cda4d898171e5e5a10419588e792fb70572c` |

## Verificação

- `dry-run` aprovado antes da geração;
- bytes, PNG e dimensões `2048x3072` validados individualmente;
- inspeção visual das duas páginas confirmou o texto integral, sem cortes e sem
  sobreposição sobre linha de resposta;
- trava principal do lote cumprida nas duas páginas: nenhuma resposta
  preenchida, nenhum item da Atividade 1 circulado, nenhum `Yes / No` marcado e
  os três quadros de desenho da Atividade 7 completamente vazios;
- Atividade 4 com o par visto/xis na ordem correta — visto em 1, 3, 4 e 6; xis
  em 2 e 5;
- Atividade 9 com as cinco perguntas na ordem da fonte;
- auditoria do acervo sem erros e sem imagens dentro do repositório;
- nenhuma saída foi promovida para `aprovadas`.

## Desvios observados, para decisão humana

- **A faixa de topo não é igual nas duas páginas.** A página 1 usa marcador
  amarelo com texto grafite; a página 2 usa faixa azul sólida com texto branco.
  O prompt da página 2 pede faixa idêntica à da página 1.
- **O marcador de atividade difere entre as páginas.** A página 1 usa estrelas
  desenhadas; a página 2 usa selos numerados `6`, `7`, `8` e `9`, que repetem o
  número já presente em `ATIVIDADE 6` e não constam da lista literal.
- **O travessão do título varia:** meia-risca na página 1 e travessão na
  página 2.
- Fundo levemente mais quente na página 1 que na página 2.

Os quatro pontos são de continuidade visual entre páginas, não de conteúdo. Uma
v2 dirigida à página 2 resolveria os quatro de uma vez.
