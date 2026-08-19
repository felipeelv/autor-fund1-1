# Organização — Matemática · 3º ano

## 2026 · 2º semestre

| Bimestre | Unidades | Estado |
|---|---|---|
| 3º | 5 e 6 | seis páginas conferidas e promovidas para `aprovadas` em 18/08/2026, por Felipe Rosa |
| 4º | 7 e 8 | oito páginas geradas em 19/08/2026, em `_revisao`. Seis conferidas e corretas (p1, p2, p3, p4, p6, p8); p5 e p7 com defeito de renderização quantitativa, pendentes de decisão |

Os prompts de produção ficam em `prompts/2026/<bimestre>/`. Cada lote precisa
de projeto YAML próprio e saída externa em `_revisao`.

## 3º bimestre — Unidades 5 e 6

Seis páginas sobre divisão com resto, as quatro operações e geometria. O lote
não saiu de um projeto único: é a **seleção**, página a página, da melhor
versão entre dezessete rodadas, o que explica os números de versão desiguais
(`v14`, `v15`, `v16`, `v17`). O detalhe completo, com SHA-256 por página, está
em `../../registros/2026/3-bimestre/unidades-05-06-branco-colagem-variada-selecionada-v1.md`.

Recorte e cobertura da fonte em
`conteudos/2026/3-bimestre/unidade-05-06-6paginas-v1/`.

Observação de infraestrutura, não de conteúdo: as imagens promovidas não estão
na raiz externa atual (`aprovadas/matematica/` não existe lá). O registro de
aprovação assinado continua íntegro no repositório; o que falta é o arquivo de
imagem, provavelmente por troca da raiz externa configurada em
`config.local.yaml`. Não bloqueia produção nova.

## 4º bimestre — Unidades 7 e 8

Oito páginas — quatro de Grandezas e Medidas, quatro de Estatística e
Probabilidade:

| Página | Título |
|---|---|
| 1 | Metro, centímetro e milímetro (abertura da Unidade 7) |
| 2 | Convertendo unidades de comprimento |
| 3 | O perímetro: a medida do contorno |
| 4 | Capacidade e massa: qual unidade usar |
| 5 | Pesquisa e organização em tabelas (abertura da Unidade 8) |
| 6 | Gráfico de barras: ler e construir |
| 7 | Gráfico de linhas e qual gráfico usar |
| 8 | Probabilidade: certo, impossível e possível |

Recorte, cobertura da fonte e os valores decodificados dos dois gráficos em
`conteudos/2026/4-bimestre/unidades-07-08-8paginas-v1/`. Projetos em
`../../projetos/2026/4-bimestre/`, um por página, para permitir gerar em ondas
e regerar uma página isolada.

Versões finais: p1, p4, p7 e p8 em `-v1`; p2, p3 e p5 em `-v2-sem-emoji` ou
posterior; p6 em `-v3-barras-na-malha`. O detalhe de cada rodada, com o que
falhou e por quê, está em
`../../registros/2026/4-bimestre/unidades-07-08-8paginas-v1.md`.

Três pendências registradas, não resolvidas:

1. o **Gráfico de Barras Duplas** (seção 42 da fonte) ficou de fora porque a
   arte ASCII que o representa é internamente inconsistente — a mesma coluna
   troca de grupo entre linhas — e reproduzi-lo exigiria inventar valores. Ver
   `COBERTURA-DA-FONTE.md`;
2. a **p5** tem a coluna CONTAGEM com número de traços diferente do total
   escrito em três das cinco linhas, e um `pesquiras` no lugar de `pesquisas`.
   Duas gerações falharam no mesmo ponto;
3. a **p7** não tem versão aprovável: a `-v1` acerta a forma da curva e erra
   três valores; a `-v2` acerta quase todos os valores e perde o pico da
   sexta; a `-v3` saiu quebrada. Três gerações.

As duas últimas são limite do modelo em posicionar e contar com exatidão, não
falha de redação de prompt — por isso pararam aqui, em vez de consumir mais
crédito em tentativas cegas.
