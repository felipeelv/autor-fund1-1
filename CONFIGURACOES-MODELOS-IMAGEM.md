# Configurações dos modelos de imagem

Comparativo operacional de `gpt-image-2` (OpenAI), `grok-imagine-image-2.0`
(xAI) e `qwen/qwen-image-3-pro` (OpenRouter / Alibaba). Serve para montar o
projeto YAML e saber o que mudar no prompt **sem** alterar cópia pedagógica
aprovada.

O formato visual continua `apostila-fund1`, vertical **2:3**, linguagem de
colagem, sketchnote e visual note-taking. O provedor e o modelo são sempre
declarados no projeto; nenhuma chave troca o modelo em silêncio.

Estado do gerador em 2026-08-15:

- `openai` + `gpt-image-2` — implementado.
- `xai` + `grok-imagine-image-2.0` — implementado.
- `openrouter` + `qwen/qwen-image-3-pro` — implementado. Outros modelos
  OpenRouter exigem declaração explícita no projeto.

Fontes oficiais consultadas:

- [OpenAI Image generation](https://developers.openai.com/api/docs/guides/image-generation)
- [OpenAI GPT Image 2](https://developers.openai.com/api/docs/models/gpt-image-2)
- [xAI Image Generation](https://docs.x.ai/developers/model-capabilities/images/generation)
- [xAI Imagine Overview](https://docs.x.ai/developers/model-capabilities/imagine)
- [Imagine Image 2.0](https://x.ai/news/grok-imagine-image-2)
- [OpenRouter Image API](https://openrouter.ai/docs/guides/overview/multimodal/image-generation)
- [OpenRouter qwen/qwen-image-3-pro](https://openrouter.ai/qwen/qwen-image-3-pro)
- [Alibaba Qwen Image 3.0 Pro](https://help.aliyun.com/en/model-studio/qwen-image-generation-and-editing-api-reference)

## Credenciais no `.env`

Um único arquivo local basta.

| Variável | Provedor | Modelo padrão |
| --- | --- | --- |
| `OPENAI_API_KEY` | OpenAI | `gpt-image-2` |
| `XAI_API_KEY` | xAI | `grok-imagine-image-2.0` |
| `OPENROUTER_API_KEY` | OpenRouter | `qwen/qwen-image-3-pro` |

```env
OPENAI_IMAGE_MODEL=gpt-image-2
XAI_BASE_URL=https://api.x.ai/v1
XAI_IMAGE_MODEL=grok-imagine-image-2.0
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_IMAGE_MODEL=qwen/qwen-image-3-pro
```

Para testar outro modelo no OpenRouter, troque só `OPENROUTER_IMAGE_MODEL` e o
`modelo.id` do projeto. Não reaproveite essa chave como `OPENAI_API_KEY`.

## O que o prompt já faz bem

Os prompts aprovados deste repositório já seguem o contrato que os três
modelos entendem:

1. caso de uso e tipo de ativo;
2. pedido principal (uma página vertical 2:3);
3. composição e caminho de leitura;
4. textos obrigatórios, literais, um por linha;
5. restrições (não parafrasear, não acrescentar texto, sem watermark).

Isso não precisa ser reescrito para mudar de provedor. Ajuste o **YAML** e,
no máximo, um envelope curto específico do modelo. A cópia pedagógica
permanece intacta.

## Quadro de parâmetros

| Campo | OpenAI `gpt-image-2` | xAI `grok-imagine-image-2.0` | OpenRouter `qwen/qwen-image-3-pro` |
| --- | --- | --- | --- |
| Endpoint | `POST https://api.openai.com/v1/images/generations` | `POST https://api.x.ai/v1/images/generations` | `POST https://openrouter.ai/api/v1/images` |
| Auth | `OPENAI_API_KEY` | `XAI_API_KEY` | `OPENROUTER_API_KEY` |
| Como este gerador chama | SDK OpenAI nativo | SDK OpenAI com `base_url` xAI | Image API própria do OpenRouter (não é o Images da OpenAI) |
| Tamanho | `WIDTHxHEIGHT` ou `auto` | sempre `auto` + `proporcao` + `resolucao` | `auto` + `proporcao` + `resolucao`, ou `size` em pixels |
| Proporção da apostila | implícita em `2048x3072` ou `1024x1536` | `2:3` | `2:3` (aceita) |
| Resolução | pixels explícitos | `1k` ou `2k` | `1K` ou `2K` |
| Qualidade | `auto`, `low`, `medium`, `high` | só `low` ou `medium` (padrão `medium`) | não há knob de qualidade neste endpoint |
| Formato | `png`, `jpeg`, `webp` (padrão `png`) | JPEG; resposta `b64_json` ou URL | PNG no provedor Alibaba; OpenRouter devolve `b64_json` + `media_type` |
| Fundo | `auto` ou `opaque` — **sem** transparente | não se aplica | `auto` / `opaque` / `transparent` na API unificada; o endpoint Qwen não lista o campo |
| Moderação | `auto` ou `low` | política da xAI; sem parâmetro nosso | política do OpenRouter / Alibaba |
| `n` | até 10 (streaming exige 1) | até 10 | 1–6 |
| Referências | edição / várias imagens | até 3 na API de edição | 0–4 `input_references` |
| Seed | não | não documentado na geração | sim |
| Streaming | sim (`partial_images` 0–3) | não neste gerador | não neste endpoint |
| Preço de referência | por tokens de imagem (sobe com size e quality) | US$ 0,04 / imagem | US$ 0,04 / 1K; US$ 0,075 / 2K; US$ 0,003 / imagem de entrada |
| Limite de prompt | 32.000 caracteres na Images API | não publicado; os prompts atuais cabem | Alibaba recomenda até ~4.500 tokens |

Restrições de tamanho que importam:

- **OpenAI:** borda ≤ 3840 px, múltiplos de 16, razão ≤ 3:1, 655.360 a
  8.294.400 pixels. Acima de 2560×1440 a OpenAI trata como experimental.
- **xAI:** não aceita `WIDTHxHEIGHT`. Use `aspect_ratio` + `resolution`.
- **Qwen / Alibaba:** área entre 512×512 e 2048×2048. **`2048x3072` da
  produção OpenAI estoura esse teto.** No OpenRouter use `resolution: 2K` +
  `aspect_ratio: 2:3` (o provedor deriva os pixels).

## Presets deste repositório

### OpenAI — produção atual

Usado em `unidade-03-bloco-01-autonomia-guiada-4paginas-v5.yaml`.

```yaml
modelo:
  provider: "openai"
  id: "gpt-image-2"

parametros_api:
  tamanho: "2048x3072"
  qualidade: "high"
  formato: "png"
  fundo: "opaque"
  moderacao: "auto"
  timeout: 300
```

Rascunho em `compartilhado/parametros-api.yaml`: `1024x1536`, `low`, `png`.

### xAI — amostra atual

Usado em `unidades-05-06-p01-amostra-grok-v1.yaml`.

```yaml
modelo:
  provider: "xai"
  id: "grok-imagine-image-2.0"

parametros_api:
  tamanho: "auto"
  qualidade: "medium"
  formato: "jpeg"
  fundo: "auto"
  moderacao: "auto"
  proporcao: "2:3"
  resolucao: "2k"
  timeout: 300
```

O adaptador xAI recusa `qualidade: high`, formato diferente de JPEG e
`tamanho` diferente de `auto`.

### OpenRouter / Qwen — proposta para teste

O adaptador já está no `gerar.py`. O projeto deve ficar assim:

```yaml
modelo:
  provider: "openrouter"
  id: "qwen/qwen-image-3-pro"

parametros_api:
  tamanho: "auto"
  formato: "png"
  proporcao: "2:3"
  resolucao: "2k"
  timeout: 300
```

Corpo HTTP esperado pela Image API do OpenRouter:

```json
{
  "model": "qwen/qwen-image-3-pro",
  "prompt": "<prompt da página>",
  "n": 1,
  "resolution": "2K",
  "aspect_ratio": "2:3",
  "output_format": "png"
}
```

Para outro modelo OpenRouter, troque só `modelo.id`. Consulte
`GET https://openrouter.ai/api/v1/images/models/{id}/endpoints` antes:
cada endpoint publica `supported_parameters`.

Parâmetros que o endpoint Alibaba do Qwen Image 3 Pro aceita hoje:

- `resolution`: `1K`, `2K`
- `aspect_ratio`: `1:1`, `1:2`, `1:4`, `2:1`, `2:3`, `3:2`, `3:4`, `4:1`,
  `4:3`, `4:5`, `5:4`, `9:16`, `16:9`
- `n`: 1–6
- `input_references`: 0–4
- `seed`: sim

Não envie `qualidade: high` nem `tamanho: 2048x3072` para o Qwen.

## Ajustes de prompt por modelo

Não altere prompts aprovados só para mudar de API. Se o modelo precisar de
instrução extra, acrescente um envelope no projeto ou um prompt versionado
novo.

### `gpt-image-2`

A estrutura atual (pedido + composição + textos literais + restrições) é a
adequada. A OpenAI admite que o modelo ainda falha em colocação precisa de
texto e em layouts densos.

Ajustes úteis:

- manter cada frase obrigatória em uma linha, entre aspas ou como item;
- pedir corpo grande e entrelinha folgada;
- não pedir fundo transparente;
- usar `high` só na produção; `low` para rascunho;
- prompts densos podem levar até ~2 minutos — `timeout: 300` está certo;
- não inventar estatísticas, traduções ou contas no prompt.

### `grok-imagine-image-2.0`

O anúncio oficial enfatiza tipografia, layout multipartes e texto pequeno
nítido. O exemplo da API é um cartaz com “bold retro typography, sharp
small print”. Infográficos e páginas de apostila são o caso de uso.

Ajustes úteis:

- reutilizar o mesmo prompt OpenAI;
- reforçar, se necessário, “tipografia nítida, texto pequeno legível,
  hierarquia de títulos”;
- não mandar `size` em pixels, `output_format: png` nem `quality: high`;
- a saída é JPEG — a revisão de OCR precisa aceitar compressão;
- edição com até 3 referências existe na API, mas este gerador ainda só
  faz text-to-image.

### `qwen/qwen-image-3-pro`

Ponto forte declarado: texto e detalhes até ~10 px, layouts densos,
chinês e inglês. É o candidato natural para páginas com muita cópia.

Ajustes obrigatórios:

1. **Desligar reescrita de prompt.** Na API Alibaba, `prompt_extend`
   vem ligado por padrão e o modelo reescreve o texto. Para cópia
   pedagógica literal isso é inaceitável. No adaptador OpenRouter, não
   encaminhe reescrita; se o endpoint aceitar passthrough, force
   `prompt_extend: false`.
2. **Não usar `2048x3072`.** Use `2K` + `2:3`.
3. **Não pedir watermark.** Na API Alibaba o padrão já é `false`.
4. **Envelope curto**, sem mexer na cópia:

```text
Render the following educational page exactly.
Do not rewrite, translate, summarize or add any text.
Quote every required string once, with original accents and punctuation.
Editorial collage + professional sketchnote + visual note-taking.
Vertical 2:3 printed worksheet. No logo, page number, signature or watermark.
```

5. **Opcional:** `negative_prompt` com o que as restrições já proíbem
   (fotografia, 3D, neon, mascote, cards digitais, texto deformado,
   watermark). Só se o adaptador passar o campo.
6. Se o texto da página for muito longo, o teto Alibaba (~4.500 tokens)
   é mais apertado que o da OpenAI. Não corte a cópia; se estourar,
   divida a página, não resuma.

Qwen aceita chinês e inglês. Português nas apostilas deve permanecer
literal; o modelo não deve “corrigir” para inglês.

## O que não muda entre os três

- um autor, uma fonte, um prompt versionado por página;
- textos obrigatórios conferidos caractere a caractere;
- matemática: números, sinais e classificação;
- inglês: palavras e traduções literais;
- Natureza e Sociedade: fontes internas, sem estereótipo;
- saída em `_revisao`; promoção só com revisão humana;
- `--dry-run` antes de qualquer chamada.

## Checklist ao trocar de modelo

1. Declarar `provider` e `id` no YAML — nunca inferir pela chave.
2. Aplicar o bloco `parametros_api` do preset acima.
3. Conferir extensão da saída (`.png` vs `.jpg`).
4. Rodar `--dry-run`.
5. Gerar uma página de amostra, não o lote inteiro.
6. Conferir OCR de todos os textos obrigatórios.
7. Se o Qwen parafrasear, o adaptador ainda está reescrevendo o prompt.
8. Para outro modelo OpenRouter, ler os `supported_parameters` do
   endpoint antes de copiar o YAML do Qwen.

## Exemplo mínimo de chamada (referência)

OpenAI:

```bash
curl -X POST "https://api.openai.com/v1/images/generations" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2",
    "prompt": "...",
    "size": "2048x3072",
    "quality": "high",
    "output_format": "png",
    "background": "opaque",
    "moderation": "auto"
  }'
```

xAI:

```bash
curl -X POST "https://api.x.ai/v1/images/generations" \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "grok-imagine-image-2.0",
    "prompt": "...",
    "quality": "medium",
    "n": 1,
    "response_format": "b64_json",
    "aspect_ratio": "2:3",
    "resolution": "2k"
  }'
```

OpenRouter / Qwen:

```bash
curl -X POST "https://openrouter.ai/api/v1/images" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen/qwen-image-3-pro",
    "prompt": "...",
    "n": 1,
    "resolution": "2K",
    "aspect_ratio": "2:3",
    "output_format": "png"
  }'
```
