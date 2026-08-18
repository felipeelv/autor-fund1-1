# CLAUDE.md — Gerador de imagens dos anos iniciais

Este arquivo é a **fonte única de regras** deste repositório. Não existe
`AGENTS.md`: o que valeria lá vale aqui.

Antes de alterar código, conteúdo, prompts, projetos ou modelos YAML:

1. leia este arquivo;
2. leia `README.md`;
3. identifique o autor em uso;
4. leia `autores/<id>/direcao/AUTOR.md`;
5. leia `autores/<id>/direcao/MEMORIA.md`.

Responda e documente sempre em português brasileiro.

---

## 1. Identidade e escopo

Gerador oficial de imagens pedagógicas dos **anos iniciais** do Colégio Eleve —
Educação Infantil 4 e 5 até o 3º ano do Ensino Fundamental.

Cada disciplina tem **dois autores**: um de conteúdo, que apresenta e explica, e
um de atividades, que entrega enunciado e espaço de resposta. A separação é de
função, não de assunto: o par cobre o mesmo currículo, com a mesma linguagem
visual. Nunca misture os dois num autor só.

| Conteúdo | Atividades | Disciplina | Anos com material |
|---|---|---|---|
| `ingles` | `ingles-atividades` | Inglês | 1º ano / 3º ano |
| `matematica` | `matematica-atividades` | Matemática | 3º ano / — |
| `natureza-e-sociedade` | `natureza-e-sociedade-atividades` | Natureza e Sociedade | 3º ano / — |
| `portugues` | `portugues-atividades` | Português | — / — |

Os oito atendem o 1º, o 2º e o 3º ano: `manifesto.anos` declara o escopo
completo e `manifesto.anos_planejados`, os anos que ainda não têm material.

Os autores sem fonte têm direção editorial **provisória**, marcada no topo de
`direcao/AUTOR.md` e no `estado` do `manifesto.yaml`. Ficam `ativo: true` porque
o acervo não admite autor inativo, mas não produzem nada sem fonte e sem
projeto. Ajuste a direção com uma pessoa antes do primeiro lote.

A regra que define um autor de atividades: **nada aparece respondido** — nenhuma
resposta escrita, alternativa assinalada, lacuna completada, conta efetuada,
tabela preenchida ou quadro de desenho com desenho dentro.

Formato autorizado: `apostila-fund1`. Etapas canônicas: `compartilhado/series.yaml`.

Não introduza autor, disciplina, ano, formato, modelo ou provedor novo sem
autorização explícita. Preserve a linguagem visual do grupo — colagem,
sketchnote e visual note-taking sobre fundo branco puro.

## 2. Independência

Este repositório é autônomo. Não dependa de código, prompt, fonte, credencial,
configuração ou artefato de nenhum outro repositório — `~/gerador-de-imagens`
incluído.

Aquele repositório atende o 4º ano em diante e serve **apenas como referência
de padrão organizacional**. Copiar arquivo, regra editorial ou trecho de código
de lá cria dependência e é proibido. Se um documento aqui citar blueprint,
framework, kit, capítulo em Google Docs, LaTeX/MathJax, Vida e Propósito ou
disciplina do 6º ano em diante, é resíduo de migração e deve ser removido, não
seguido.

A raiz externa de saída é compartilhada com aquele repositório. Por isso o ID
de um autor daqui **nunca pode colidir** com um ID de lá.

## 3. Provedores e modelos

Provedor padrão: **xAI Images API** com `grok-imagine-image-2.0`.
Provedor preservado: **OpenAI Images API** com `gpt-image-2`.

- todo projeto declara `modelo.provider` e `modelo.id` explicitamente;
- nenhum projeto herda provedor de configuração global;
- nunca troque um provedor pelo outro silenciosamente, nem em mudança
  puramente técnica;
- credenciais ficam separadas em `.env.grok.local` e `.env.openai.local`;
- referência de parâmetros por provedor: `compartilhado/parametros-api.yaml`.

Restrições do adaptador xAI, validadas em `gerador_imagens/projects.py`:
qualidade `low` ou `medium`, formato JPEG, `tamanho: auto` com `proporcao` e
`resolucao` explícitas, `resolucao` em `1k` ou `2k`, sem streaming.

## 4. Nomenclatura

| Artefato | Convenção | Exemplo |
|---|---|---|
| ID de autor | minúscula, hífen, sem etapa nem ano | `natureza-e-sociedade` |
| Pasta de ano | `<n>ano` ou `infantil<n>` | `3ano`, `infantil5` |
| Período de fonte | `<ano-letivo>-<n>-semestre` | `2026-2-semestre` |
| Bimestre | `<n>-bimestre` | `3-bimestre` |
| Prompt | `<unidade>-p<NN>-<tema>-v<N>.md` | `unidade-03-p01-capa-v2.md` |
| Projeto | `<unidade>-<escopo>-v<N>.yaml` | `unidades-05-06-6paginas-v1.yaml` |
| Saída externa | `<autor>/<ano>/<bimestre>/<unidade>/<arquivo>` | `matematica/3ano/3-bimestre/…` |

O ID do autor é o nome da pasta **e** o campo `autor.id` do `autor.yaml` — os
dois precisam ser idênticos, e o mesmo ID nomeia a pasta na raiz externa.

Prompt e projeto são **versionados por sufixo `-vN`, nunca sobrescritos**. Uma
correção cria `-v2` ao lado do `-v1`. Prompt aprovado não é reescrito: ganha
versão nova.

## 5. Armazenamento

O repositório não pode conter imagem gerada, imagem de referência, PDF de
produção ou prévia. Só código e artefato textual.

- toda saída vai para a raiz externa configurada em `config.local.yaml`;
- caminho relativo gera primeiro em `_revisao`;
- promoção para `aprovadas` exige revisão humana e passa por `aprovar.py`;
- nunca crie saída local de contingência;
- versões anteriores são preservadas; sobrescrever exige autorização e
  `--forcar`.

## 6. Conteúdo e identidade editorial

- **não invente.** Estatística, fonte, tradução, definição, propriedade,
  espécie, nome científico, data, lugar, povo ou fato ausente da fonte interna
  versionada não existe;
- a fonte interna versionada determina o conteúdo; o autor organiza
  visualmente;
- não misture conteúdo, fonte, prompt ou saída entre autores;
- não altere prompt aprovado durante mudança puramente técnica;
- todo texto visível na página precisa estar literal no prompt e ser
  renderizado exatamente uma vez;
- padrão de escrita: `compartilhado/direcao-editorial/PADRAO-GERAL-DE-ESCRITA.md`;
- ortografia: `compartilhado/direcao-editorial/CONVENCOES.md`;
- conferência: `compartilhado/REVISAO-PEDAGOGICA.md`.

Conferência obrigatória por disciplina:

- **Inglês** — palavras, frases, traduções e ortografia inglesa, literalmente;
- **Matemática** — números, sinais, cálculos, unidades e classificações
  geométricas;
- **Natureza e Sociedade** — nomes de espécies, partes do corpo, lugares,
  povos, ofícios e períodos; anatomia e habitat reais; representação de
  pessoas e comunidades sem estereótipo.

Dado factual e citação exigem revisão humana registrada.

## 7. Fluxo editorial

1. selecionar autor, fonte, conteúdo e prompt versionado;
2. declarar ou revisar o projeto YAML do autor correto;
3. executar `--dry-run`;
4. gerar na área externa `_revisao` do respectivo autor;
5. conferir imagem, metadados, conteúdo, cálculos e OCR;
6. promover com `aprovar.py` somente após revisão humana;
7. manter versões anteriores; sobrescrever apenas com autorização e `--forcar`.

O `--dry-run` não substitui revisão humana. O OCR é triagem, não aprovação.

## 8. Código e segurança

- Python mínimo: 3.10;
- dependências diretas fixadas em `pyproject.toml`, com `uv.lock` acompanhando;
- nunca exponha ou registre `XAI_API_KEY` ou `OPENAI_API_KEY`;
- retries apenas para falha transitória;
- valide bytes, formato e dimensões antes de salvar;
- preserve gravação atômica e proteção contra sobrescrita;
- funcionalidade nova exige teste sem chamada real à API;
- teste e dry-run não podem chamar a API nem consumir crédito;
- não duplique o núcleo Python, `.env` ou ambiente virtual dentro de um autor.

## 9. Verificação

```bash
uv sync --locked
uv run python -m unittest discover -s tests -v
uv run gerar.py --help
uv run gerar.py --listar-autores
uv run validar.py --acervo
uv run gerar.py \
  --projeto autores/matematica/projetos/2026/3-bimestre/unidades-05-06-6paginas-v1.yaml \
  --dry-run
```

`--check-auth` acessa a API mas não gera imagem. Use somente quando houver
necessidade explícita de verificar credencial e acesso ao modelo.

## 10. Criar um autor novo

O procedimento está em `autores/README.md`. Comece por `autores/_modelo/autor.yaml`.
