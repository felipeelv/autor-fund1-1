# Padrão geral de escrita — texto dentro da página-imagem

> **O que é:** referência única, para todos os autores deste repositório, de
> como escrever o texto que será renderizado *dentro* de uma página gerada por
> IA, nas faixas atendidas — Infantil 4 ao 3º ano do Fundamental.
>
> **Como usar:** este arquivo diz *como escrever*. A fonte interna versionada
> diz *o quê* e *até onde*. O `AUTOR.md` de cada disciplina diz o que é
> específico dela. Em conflito, a ordem de precedência é: fonte interna →
> `AUTOR.md` do autor → este arquivo.

---

## 1. A regra que muda tudo

Aqui o texto não é diagramado depois: ele **nasce dentro da imagem**. Isso
impõe três consequências que não existem em texto de livro.

1. **Todo texto visível precisa estar literal no prompt.** O modelo não resume,
   não completa e não traduz sem errar. O que não estiver escrito por extenso
   vai sair inventado ou deformado.
2. **Cada trecho literal é renderizado exatamente uma vez.** Repetir um trecho
   no prompt faz o modelo duplicá-lo na página.
3. **Errar sai caro.** Não existe correção de acento depois: corrigir é gerar
   de novo. Por isso a conferência ortográfica acontece *antes*, contra
   [CONVENCOES.md](CONVENCOES.md).

---

## 2. Registro de escrita por faixa

| | Infantil 4–5 | 1º–2º ano | 3º ano |
|---|---|---|---|
| **Idade** | ~4 a 5 anos | ~6 a 7 anos | ~8 anos |
| **Leitura** | ainda não lê sozinho | lê palavra e frase curta | lê frase e enunciado curto |
| **Unidade de texto** | palavra solta e rótulo | palavra e frase-modelo | frase completa curta |
| **Extensão máxima por bloco** | 1 a 3 palavras | 1 linha | 2 linhas |
| **Enunciado** | mediado pelo adulto, não escrito na página | direto, verbo no imperativo | direto, uma instrução por vez |
| **Papel da ilustração** | carrega o sentido sozinha | dá a pista do sentido | apoia, não substitui a leitura |
| **Vocabulário técnico** | nenhum | só o nome, depois de ver | nome + explicação curta |
| **Blocos por página** | 3 a 5 | 4 a 7 | 5 a 7 |

**Infantil 4–5 tem uma regra própria:** a criança ainda não lê. Palavra na
página serve como rótulo do que está desenhado, para o adulto ler junto. Nunca
escreva instrução dirigida à criança nessa faixa.

---

## 3. Regras transversais

- **Uma intenção pedagógica por página.** Se há duas, são duas páginas.
- **Concreto antes de abstrato.** Objeto, cena ou fenômeno observável primeiro;
  nome, regra ou definição depois.
- **Uma ideia por bloco.** Núcleos conceitualmente diferentes não dividem o
  mesmo recorte de papel.
- **Frase curta, ordem direta.** Sujeito, verbo, complemento. Sem oração
  subordinada, sem inversão, sem voz passiva.
- **Palavra comum.** Se existe uma palavra que a criança já usa, é ela.
- **Nada de diminutivo afetivo, personagem falante ou narrador em primeira
  pessoa.** Simplicidade não é infantilização.
- **Todo texto ancorado.** Cada trecho precisa estar visualmente ligado a uma
  representação — objeto, seta, quantidade, ser vivo, lugar. Texto solto no
  branco não entra.
- **Não inventar.** Nome, número, data, tradução, definição, propriedade,
  espécie, lugar ou fato que a fonte não traga não existe.
- **Título curto e literal.** Pode ser dividido em duas linhas, desde que a
  ordem de leitura seja preservada.

---

## 4. Densidade

A densidade da página vem de **relações curtas encadeadas**, não de parágrafo
longo. O encadeamento típico é:

```text
observar  →  nomear  →  relacionar  →  verificar
```

Cinco a sete núcleos visuais por página, distribuídos em seis a nove recortes
físicos, com corredores de fundo branco entre eles. Um núcleo que precise de
mais de duas linhas de texto provavelmente é uma página inteira, não um bloco.

---

## 5. O que nunca entra no texto da página

- palavra ou frase que não esteja literal no prompt;
- rótulo de estrutura visível ao aluno — "Box 1", "Card 2", "Atividade A";
- identificação de disciplina, ano, série, unidade ou capítulo;
- numeração de página, marca, logotipo, assinatura, crédito;
- estatística, citação, versículo ou fonte sem revisão humana registrada;
- texto em outra língua fora do autor de Inglês;
- abreviação que a criança não conheça.

---

## 6. Protocolo antes de gerar

1. Conferir cada trecho literal contra a fonte interna versionada.
2. Rodar a verificação ortográfica de [CONVENCOES.md](CONVENCOES.md) §7.
3. Conferir a extensão por bloco contra a tabela da seção 2.
4. Verificar que todo texto tem âncora visual declarada no prompt.
5. Rodar `--dry-run`.
6. Gerar em `_revisao` e conferir a página inteira e o OCR, contra
   [REVISAO-PEDAGOGICA.md](../REVISAO-PEDAGOGICA.md).

Nenhuma dessas etapas substitui a revisão humana. O OCR é triagem, não
aprovação.

---

*Escrito em ago/2026 para os anos iniciais. Substitui a escala N1–N4 herdada do
fluxo de capítulos em Google Docs de outro repositório, que descrevia produção
de texto corrido do 6º ano em diante e não tinha aplicação na geração de
imagens desta faixa.*
