# Registro de produção — Unidade 3 · Colors · amostra v1

Data: 13/08/2026  
Estado: em revisão humana; não promovida para `aprovadas`.

## Escopo

- 1º ano do Ensino Fundamental;
- uma capa e duas páginas internas;
- fonte interna: `anos/1ano/fontes/2026-2-semestre/3bim-bloco1.md`;
- projeto: `projetos/2026/3-bimestre/unidade-03-bloco-01-amostra-3paginas-v1.yaml`.

## Execução

- provider: OpenAI;
- modelo: `gpt-image-2`;
- tamanho: `1024x1536`;
- qualidade: `high`;
- formato: PNG opaco;
- área: `_revisao` externa.

## Saídas

| Página | Caminho relativo externo | SHA-256 |
|---|---|---|
| Capa | `autor-teste-fund1/1ano/3-bimestre/unidade-03-bloco-01/p01-capa-v1.png` | `5261e56c9021610f74b0650e403d0f3cc2197d401332067f7f4a45cfbfd1198b` |
| The Colors | `autor-teste-fund1/1ano/3-bimestre/unidade-03-bloco-01/p02-the-colors-v1.png` | `57f657a4b8cf69fa2f82bd4deb2dcd1743df4dc532723611412606c16604057c` |
| What Color Is It? | `autor-teste-fund1/1ano/3-bimestre/unidade-03-bloco-01/p03-what-color-is-it-v1.png` | `03c4add907cb947bd4cdd2325f8d195e6c29715b32945c3b00f1f1cde33b62c4` |

## Verificação

- 196 testes automatizados aprovados antes da geração;
- `dry-run` aprovado para as três tarefas;
- bytes, formato e dimensões validados individualmente;
- inspeção visual confirmou hierarquia, correspondência das seis cores e
  ortografia aparente dos textos;
- OCR complementar executado em inglês; o layout ilustrado reduziu a detecção
  automática, portanto a leitura humana continua obrigatória;
- nenhuma imagem foi salva no repositório;
- nenhuma saída foi promovida para `aprovadas`.
