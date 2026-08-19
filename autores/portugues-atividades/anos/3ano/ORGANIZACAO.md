# Organização — atividades de Português · 3º ano

## Estado

**Base curricular mapeada; primeiro caderno definido; nenhuma página de
atividade produzida.** As fontes de conteúdo vivem no autor-par `portugues`:

- `../../../portugues/anos/3ano/fontes/2026-2-semestre/3bim-realidade-e-imaginacao-v1.md`;
- `../../../portugues/anos/3ano/fontes/2026-2-semestre/4bim-humor-poesia-e-escrever-para-ensinar-v1.md`.

As pastas `fontes/`, `conteudos/`, `prompts/`, `projetos/` e `registros/` deste
ano ainda não existem fisicamente neste autor. Por isso o 3º ano permanece em
`manifesto.anos_planejados`: mapear o currículo não equivale a receber ou
aprovar uma fonte própria de atividades.

## Currículo disponível

| Fonte | Unidade | Escopo curricular |
|---|---|---|
| 3º bimestre | 5 — Entre a realidade e a imaginação | ficção e realidade, ficção científica, leitura episódica, prefixos intensificadores, sufixos de profissões e polissemia |
| 3º bimestre | 6 — Criando mundos imaginários | sufixos `-OSO/-OSA` e `-EZA`, sílaba tônica, classificação tônica, acentuação, palavras compostas e descrição de cenários |
| 4º bimestre | 7 — Humor e poesia na infância | humor, HQ, discurso direto e indireto, verbos, tempos verbais e conectivos temporais |
| 4º bimestre | 8 — Escrevendo para ensinar | receitas, manuais, imperativo, conectivos de sequência e numerais cardinais e ordinais |

## Primeiro caderno planejado

Começar pelo **3º bimestre, Unidade 6 — "Criando mundos imaginários"**, em oito
páginas de atividades, pareadas pela ordem com o lote de conteúdo que já está
em `_revisao/portugues/3ano/3-bimestre/unidade-06/`:

| Página | Base da página de conteúdo |
|---|---|
| 1 | sufixo `-OSO/-OSA`: sempre com S |
| 2 | sufixo `-EZA`: sempre com Z |
| 3 | comparação e transformação com `-OSO` e `-EZA` |
| 4 | identificação da sílaba tônica |
| 5 | proparoxítonas e paroxítonas |
| 6 | oxítonas e resumo da classificação tônica |
| 7 | palavras compostas |
| 8 | palavras compostas na ficção científica e descrição de cenários |

Esta tabela define a cobertura e a ordem, não os enunciados. Antes de escrever
prompts, uma fonte própria de atividades precisa enumerar literalmente cada
atividade, seus itens e o espaço de resposta esperado. O autor de conteúdo
apresenta; este autor pede que o aluno leia, complete, classifique e escreva,
sem mostrar respostas.

## Pendências editoriais conhecidas

- a fonte da Unidade 6 traz `ja-NE-la (penúltima = NI)`, provável erro de
  digitação; não transportar a afirmação para uma atividade antes de decisão
  humana explícita;
- a abertura da Unidade 7 anuncia artigos, comparação, metáfora e poesia, mas
  o corpo disponível desenvolve principalmente humor, discurso e verbos; não
  criar atividades desses quatro tópicos sem cobertura textual confirmada.

## Próximos passos

1. escrever e aprovar uma fonte versionada de atividades para as oito páginas
   da Unidade 6, com enunciados, itens e respostas esperadas para conferência;
2. derivar o recorte editorial em `conteudos/2026/3-bimestre/` e registrar a
   cobertura da fonte;
3. escrever os prompts em `prompts/2026/3-bimestre/`, sempre versionados com
   sufixo `-vN`;
4. declarar o lote em `../../projetos/2026/3-bimestre/`, com provedor e modelo
   explícitos e saída externa em `_revisao`;
5. executar `--dry-run`, gerar e conferir especialmente a trava de nada
   respondido e os espaços de escrita;
6. após o primeiro lote real, revisar as regras derivadas, tirar `3ano` de
   `manifesto.anos_planejados` e registrar o aprendizado de produção.
