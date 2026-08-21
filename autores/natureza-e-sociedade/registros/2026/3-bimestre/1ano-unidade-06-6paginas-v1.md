# Registro de produção — 1º ano · Unidade 6 · seis páginas · v1

Data: 21 de agosto de 2026.

## Origem

Primeiro lote produzido pelo autor `natureza-e-sociedade` para o **1º ano**.
Até aqui o autor só tinha material do 3º ano; `PADRAO-VISUAL-1ANO.md` e
`anos/1ano/REGRAS.md` eram derivados do 3º ano e nunca haviam sido testados
contra uma fonte real deste ano.

- fonte canônica:
  `anos/1ano/fontes/2026-2-semestre/3bim-natureza-viva-e-escola-v1.md`,
  seção "UNIDADE 6 — A ESCOLA E SEUS ARREDORES" (linhas 454–924);
- conteúdo derivado:
  `anos/1ano/conteudos/2026/3-bimestre/unidade-06-6paginas-v1/`;
- prompts: `anos/1ano/prompts/2026/3-bimestre/unidade-06-p01..p06`;
- formato: `apostila-fund1`;
- provedor e modelo: `openrouter` com `x-ai/grok-imagine-image-2.0`.

## Decisão de recorte

Seis páginas, uma intenção pedagógica por página, respeitando o limite de
2 a 3 núcleos por página que `PADRAO-VISUAL-1ANO.md` fixa para crianças de
aproximadamente 6 anos. Quatro páginas exigiriam fundir temas com propósitos
diferentes; o raciocínio completo está em `PROPOSTA-PEDAGOGICA.md`.

| Página | Tema |
|---|---|
| 1 | Abertura da unidade |
| 2 | Conhecendo minha escola |
| 3 | Quem trabalha na escola |
| 4 | As regras da escola |
| 5 | Observando como um cientista |
| 6 | Explorando os arredores da escola |

## Duas decisões editoriais

1. **Objetivo sem conteúdo.** A fonte lista "APRENDER SOBRE O TRAJETO
   CASA-ESCOLA" entre os objetivos da unidade, mas nenhuma seção desenvolve
   esse tema (busca no arquivo completo de 925 linhas). A página 1 imprime
   os quatro objetivos entregáveis; a lacuna está registrada em
   `COBERTURA-DA-FONTE.md` e aguarda decisão humana — produzir com fonte
   nova ou remover da lista de objetivos.
2. **Bloco bíblico com escopo de bimestre.** O fechamento "A Palavra de Deus
   nos ensina" abre falando de seres vivos e não vivos, conteúdo da Unidade 5,
   fora deste lote. A página 6 usa somente o que se sustenta dentro da
   Unidade 6: Gênesis 1:31, a ligação com o cuidado da escola e da natureza,
   e um trecho curto da oração.

## Correção ortográfica da fonte

A fonte traz "É ONDE VOCÊ LANCHE OU ALMOÇA NA ESCOLA" (linha 549). A página 2
imprime "É ONDE VOCÊ LANCHA OU ALMOÇA NA ESCOLA", corrigindo a conjugação sem
alterar o conteúdo.

## Trava nova, específica deste autor

O `prompt_prefixo` do `autor.yaml` deste autor foi escrito para a unidade de
povos indígenas do 3º ano: ele exige textura de argila crua ou pedra bruta,
pintura ou guache documental, e traz um bloco inteiro sobre representação de
povos indígenas e cenas anteriores a 1500. Esse prefixo entra em **toda**
página que o autor gera, inclusive nesta unidade, cujo assunto é a escola de
hoje.

O `autor.yaml` não foi alterado — ele sustenta o lote do 3º ano já aprovado.
Em vez disso, cada um dos seis prompts traz um contra-bloco explícito nas
TRAVAS: cena contemporânea de escola brasileira, proibindo cena histórica,
pintura ou guache documental, textura de argila, pedra, cerâmica ou relevo, e
qualquer elemento, adereço ou grafismo de povos indígenas. As páginas geradas
até agora não apresentaram vazamento desses elementos.

Se o autor voltar a produzir para o 1º ano em outras unidades, avaliar com uma
pessoa se vale um `prompt_prefixo` por ano em vez de contra-blocos repetidos.

## Trava de emoji

A fonte é densa em emoji (🏫 📚 🤔 💡). Nenhum caractere emoji entra nos textos
literais, e todos os prompts pedem ícones desenhados à mão — trava que já
tinha aparecido como necessária em outros autores deste repositório.

## Limite de bytes no roteamento por OpenRouter

`PADRAO-VISUAL-3ANO.md` calibrou o corpo do prompt em 4.800 **caracteres**
contra o endpoint nativo `api.x.ai`. Por OpenRouter o limite prático é em
**bytes** (~8.000), e português em caixa alta acentuada infla bytes sobre
caracteres. Os seis prompts foram medidos em bytes com prefixo e sufixo
somados; o maior ficou em 7.117 bytes, com margem de 883.

## Página 1 — duas versões

A `v1` trazia apenas título, ilustração e a lista de objetivos. O Nicolas
apontou que faltava conteúdo na página; a `v2` acrescenta como terceiro
núcleo o gancho de abertura de "Minha Escola" — a pergunta "VOCÊ CONHECE BEM
SUA ESCOLA?", a frase sobre a escola ser um lugar especial e a chamada "VAMOS
EXPLORAR A ESCOLA?" — todos literais da fonte. A `v2` é a versão escolhida.

## Execução

- provider: `openrouter`;
- modelo: `x-ai/grok-imagine-image-2.0`;
- dimensões: 1664×2496;
- qualidade: `medium`; formato JPEG;
- proporção `2:3`, resolução `2k`, tamanho `auto`;
- área: `_revisao` externa, em
  `natureza-e-sociedade/1ano/3-bimestre/unidade-06-6paginas/`.

## Página 6 — três versões, e uma lição sobre aspas

- **`v1`**: aspas desbalanceadas no bloco bíblico. O modelo acrescentou uma
  aspa de fechamento na frase "QUANDO CUIDAMOS DA NATUREZA…" e uma aspa de
  abertura na oração — nenhuma das duas pedida. Não promovida.
- **`v2`**: trava explícita nomeando qual texto leva aspa e afirmando que as
  outras duas frases não levam nenhuma. Corrigiu a oração, mas **sobrou uma
  aspa órfã** depois de "DEUS FEZ": o modelo fechou, no bloco seguinte, a
  aspa que havia aberto no versículo. Não promovida.
- **`v3`**: em vez de mais uma trava negativa, a construção foi eliminada. O
  versículo saiu de dentro das aspas e passou a ser identificado por cor
  verde mais a referência `(GÊNESIS 1:31)` ao lado. Com zero aspas pedidas na
  página, não há aspa para vazar. Saiu limpa e foi promovida.

**Lição para os próximos lotes:** quando o modelo erra pontuação emparelhada
(aspas, parênteses), reforçar a trava negativa tende a falhar — ele fecha em
outro lugar o par que abriu. Remover a construção do prompt resolve. Vale
para qualquer autor deste repositório.

A `v2` também trouxe duas mudanças não pedidas que valem registro: nomeou os
três animais individualmente com setas, em vez do rótulo único (melhor
pedagogicamente), e acrescentou uma bandeira do Brasil no prédio. A `v3`
voltou ao rótulo único da lista literal e não trouxe bandeira.

## Defeitos cosméticos registrados

Presentes nas páginas promovidas, conhecidos e aceitos no momento da
promoção:

- **travessões acrescentados** ligando rótulo e descrição nas páginas 2, 3, 4
  e 5 (por exemplo "SALA DE AULA — É ONDE VOCÊ TEM AS AULAS"). Não estavam na
  lista de textos literais; o modelo os inseriu como ligação visual e o
  resultado lê bem. A `v2` da página 6 já traz trava contra travessão
  acrescentado, para os próximos lotes;
- **rabiscos soltos sem função**: um na etiqueta da merendeira (página 3), um
  no rodapé abaixo da tarja amarela (página 4) e um pequeno traço à direita da
  flor no cartão do olfato (página 5). Nenhum forma letra ou palavra legível.

Nenhum defeito de conteúdo foi encontrado nas páginas promovidas: textos
literais, acentuação, contagens (cinco dependências, seis profissionais, cinco
regras, quatro sentidos mais o alerta isolado, três animais, três símbolos de
céu) e ligação rótulo-imagem estão corretos, e nenhuma página apresentou
vazamento de cena histórica, textura de argila ou elemento de povos indígenas
vindo do `prompt_prefixo`.

## Conferência humana

O Nicolas conferiu as páginas 1 a 6 nesta sessão, página por página, e
autorizou a promoção em 21 de agosto de 2026. A conferência cobriu o que a
disciplina exige: nomes de espécies e animais, lugares, ofícios,
representação de pessoas sem estereótipo, e a citação bíblica.

Promovidas em 21/08/2026, com `aprovar.py --revisor "Nicolas Basso"`:

| Página | Versão promovida |
|---|---|
| 1 — Abertura da unidade | `grok-v2` |
| 2 — Conhecendo minha escola | `grok-v1` |
| 3 — Quem trabalha na escola | `grok-v1` |
| 4 — As regras da escola | `grok-v1` |
| 5 — Observando como um cientista | `grok-v1` |
| 6 — Explorando os arredores | `grok-v3` |

Registros assinados em
`registros/aprovacoes/natureza-e-sociedade/1ano/3-bimestre/unidade-06-6paginas/`.

Com esta promoção o 1º ano saiu de `manifesto.anos_planejados`.
