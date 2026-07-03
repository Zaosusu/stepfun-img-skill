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
| `prompt` | str | required | Text prompt for generation. Maximum 512 characters. |
| `image` | str | required | Source image path for edit workflow. |
| `--model` | str | `step-image-edit-2` | Supported models: `step-image-edit-2` (recommended), `step-2x-large`, `step-1x-medium`. Only `step-image-edit-2` is supported under `step_plan/v1`. |
| `--size` | str | `1024x1024` | Image size. `step-image-edit-2` supports `1024x1024`, `768x1360`, `896x1184`, `1360x768`, `1184x896`. `step-2x-large` and `step-1x-medium` support `256x256`, `512x512`, `768x768`, `1024x1024`, `1280x800`, `800x1280`. |
| `--steps` | int | model-dependent | Generation steps. `step-image-edit-2`: `1` to `50`, default `8`. `step-2x-large` and `step-1x-medium`: `1` to `50`, default `50`. |
| `--seed` | int | unset | Random seed. `step-image-edit-2`: `0` to `2147483647`. `step-2x-large` and `step-1x-medium`: `0` means system-random seed. |
| `--cfg-scale` | float | model-dependent | Guidance scale. `step-image-edit-2`: `1.0` to `10.0`, default `1.0`. `step-2x-large`: `1.0` to `10.0`, default `6.0`. `step-1x-medium`: `1.0` to `10.0`, default `7.5`. |
| `--neg-prompt` | str | `""` | Negative prompt. Only `step-image-edit-2` supports this. Max 512 characters. |
| `--text-mode` | bool | `false` | Text-scene optimization. Only `step-image-edit-2` supports this. |
| `--n` | int | `1` | Number of images. Only `1` is currently supported. |
| `--response-format` | str | `url` | `url` or `b64_json`. |
| `--style-reference` | object | unset | Style reference for `step-1x-medium`. `source_url` is required; `weight` is optional and ranges `(0, 2]`. |
| `--out` | str | `outputs/...` | Output path. |

## Parameter Notes

- `seed` helps make results more repeatable when you want to compare prompt changes.
- `steps` controls how long the model spends refining the image.
- `cfg_scale` controls how strongly the model follows the prompt.
- `negative_prompt` helps suppress unwanted visual features.
- `text_mode` is useful when the image needs prominent or accurate text rendering.
- `style_reference` lets `step-1x-medium` borrow style from a reference image URL or base64 payload.

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
