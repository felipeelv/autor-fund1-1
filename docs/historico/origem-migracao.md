# Origem e unificação

Registro de onde veio o conteúdo deste repositório e de como as duas linhas de
trabalho paralelas foram unificadas em 18 de agosto de 2026.

## O repositório

Gerador oficial de imagens pedagógicas dos anos iniciais do Colégio Eleve.
Remoto único: `https://github.com/felipeelv/autor-fund1-1.git`.

A pasta de trabalho é `~/gerador-imagens-anos-iniciais`. Não deve existir
segunda cópia local: foi exatamente isso que causou a divergência descrita
abaixo.

## A divergência

Entre 13 e 15 de agosto de 2026 o mesmo repositório foi trabalhado em duas
pastas ao mesmo tempo, e as duas renomearam os autores de formas diferentes.

| Momento | O que aconteceu |
|---|---|
| 13/08 15:50 | `~/gerador-imagens-anos-iniciais` criada; primeiro commit às 16:03 |
| 14/08 | autor de Matemática entra, com suporte a xAI |
| 15/08 12:40 | `16a8251` reorganiza o repositório: `autor-teste-fund1` → `ingles`, `autor-teste-mat3` → `matematica` |
| 15/08 13:11 | `~/Documents/Codex/autor-fund1-1` criada, a partir de `main` |
| 15/08 13:33 | `e1d58e0` renomeia os mesmos autores para `autor-fund1` e `autor-mat3`, sem conhecer o `16a8251` |
| 15/08 17:55 → 19:55 | `autor-nat3` é criado e produzido inteiro na pasta nova |

O `16a8251` nunca chegou ao `main`, e os seis commits do `main` nunca chegaram
ao branch. Cada lado ficou com metade do trabalho: a organização de um lado, a
produção do outro.

## O que a unificação fez

`origin/main` foi incorporado com `merge -s ours`, preservando os dois
históricos e mantendo a árvore reorganizada. O conteúdo que só existia do outro
lado entrou em seguida, já renomeado.

Veio de `origin/main`:

- `autores/natureza-e-sociedade/` — 31 prompts, 13 projetos, conteúdos das três
  versões da unidade, fontes, `MODELO-DE-PROMPT.md` e o registro do lote v3.
  Todas as referências a `autor-nat3` passaram a `natureza-e-sociedade`; nenhum
  prompt foi alterado, porque nenhum citava o ID do autor;
- `registros/aprovacoes/natureza-e-sociedade/` — os 12 arquivos que documentam a
  conferência humana das seis páginas, em 15 de agosto de 2026.

Ficou como estava aqui:

- `ingles` e `matematica`, completos e idênticos nos dois lados a menos do nome;
- a nomenclatura por disciplina exigida pelo `CLAUDE.md`;
- o `CLAUDE.md` como fonte única de regras.

Fusões pontuais, onde os dois lados tinham conteúdo real:

- `anos/3ano/REGRAS.md` — a estrutura daqui (Conteúdo, Representação, Produção)
  com as regras sobre povos indígenas e sobre dados numéricos nascidas da
  produção, agora em seção própria;
- `adaptacoes.yaml` — a direção visual de colagem densa validada na produção,
  com os eixos `natureza` e `sociedade` separados;
- `autor.yaml` — o `prompt_prefixo` e o `prompt_sufixo` corrigidos na produção,
  com os `parametros_api` daqui. Os parâmetros do outro lado eram de OpenAI
  (`high`, `png`, `2160x3056`); os metadados das imagens aprovadas mostram
  `medium`, `jpeg`, `2:3` e `2k` em xAI, que é o que ficou;
- `manifesto.yaml` — modelo padrão `grok-imagine-image-2.0`.

## O que ficou de fora, deliberadamente

- **OpenRouter e `qwen/qwen-image-3-pro`**, introduzidos no `main` por
  `2e3bf9a`. O `CLAUDE.md` proíbe provedor novo sem autorização explícita e
  nenhum projeto precisava dele: dos 13 projetos de Natureza, 12 declaram xAI e
  1 declara OpenAI. As credenciais seguem separadas em `.env.grok.local` e
  `.env.openai.local`; o `.env` unificado não foi adotado;
- **`_validate_four_page_series`**, que exigia `projeto.autor == estudos-sociais`
  e anos 4 a 9. Resíduo do gerador do 4º ano em diante, removido no `16a8251` e
  não reintroduzido.

## Registros de aprovação

Os `.approval.json` e `.metadata.json` foram movidos de pasta, mas o **conteúdo
não foi tocado**. Eles citam caminhos com `autor-nat3` e um diretório de
usuário diferente, porque descrevem onde os arquivos estavam no momento da
aprovação. Editá-los descaracterizaria o registro da conferência humana.

## Raiz externa

A raiz de saída configurada em `config.local.yaml` é compartilhada com
`~/gerador-de-imagens`, o gerador do 4º ano em diante. Por isso o ID de um autor
daqui nunca pode colidir com um ID de lá.

As imagens de Natureza produzidas em 15/08 estavam sob `autor-nat3/` no Drive e
foram renomeadas em 18/08 para `natureza-e-sociedade/`, acompanhando o ID do
repositório: 50 arquivos em `_revisao` e 6 em `aprovadas`. Sem esse rename, uma
nova geração gravaria em `natureza-e-sociedade/` e o histórico ficaria partido
em duas pastas.

## A pasta antiga

`~/Documents/Codex/autor-fund1-1` foi arquivada em 18/08 como
`autor-fund1-1_ARQUIVADO-2026-08-18`, com um `LEIA-ME-ARQUIVADO.md` dentro. Todo
o seu conteúdo commitado está aqui: o `HEAD` dela era `edcb040`, que faz parte
deste histórico. Ela ficava
dentro de `~/Documents`, que sincroniza com o iCloud, e por isso acumulou pastas
duplicadas de conflito (`anos 2`, `projetos 2`, `registros 2`) e ficou lenta para
operações de git.
