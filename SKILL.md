---
name: stepfun-img
description: Generate or edit images with the StepFun Step Plan image API.
---

# StepFun Image Generation

## Overview

This skill uses StepFun Step Plan image APIs through the OpenAI-compatible client.
It supports text-to-image generation and image editing with `step-image-edit-2`.

## Configuration

Create `~/.stepfun-img/secret.json` as UTF-8:

```json
{ "apiKey": "YOUR_STEP_API_KEY" }
```

The bundled scripts read that file from the current user's home directory.

Base URL: `https://api.stepfun.com/step_plan/v1`

## Generation Workflow

1. Confirm the prompt and optional generation settings.
2. Run:

```powershell
python scripts/generate_image.py "your prompt here" --model step-image-edit-2 --size 1024x1024 --out outputs/image.png
```

3. The script saves the generated image and prints the output path.

Supported `step-image-edit-2` sizes:

- `1024x1024`
- `768x1360`
- `896x1184`
- `1360x768`
- `1184x896`

## Edit Workflow

1. Confirm the source image path and edit prompt.
2. Run:

```powershell
python scripts/edit_image.py "path/to/source.png" "your edit prompt" --model step-image-edit-2 --out outputs/edited_image.png
```

3. The script saves the edited image and prints the output path.

## Script Parameters

| Flag | Type | Default | Notes |
|---|---|---|---|
| `prompt` | str | required | Text prompt for generation |
| `image` | str | required | Source image path for edit workflow |
| `--model` | str | `step-image-edit-2` | Only `step-image-edit-2` is supported under `step_plan/v1` |
| `--size` | str | `1024x1024` | Use one of the supported sizes above |
| `--steps` | int | `8` | Range `1` to `50` |
| `--seed` | int | unset | Integer seed |
| `--cfg-scale` | float | `1.0` | Guidance scale |
| `--neg-prompt` | str | `""` | Negative prompt |
| `--text-mode` | bool | `false` | Text-scene optimization |
| `--n` | int | `1` | Only `1` is supported |
| `--response-format` | str | `url` | `url` or `b64_json` |
| `--out` | str | `outputs/...` | Output path |

## Response

The API returns `created` and `data`. Use `data[0].url` or `data[0].b64_json` to save the image result.

## Encoding

- Save `secret.json` as UTF-8.
- Treat prompts, paths, and API text as UTF-8.

## Dependencies

Install before first use:

```powershell
pip install openai
```

## References

Full API spec: `references/api_spec.md`
