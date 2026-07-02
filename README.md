# stepfun-img-skill

StepFun image generation and editing skill for Codex, built on Step Plan and `step-image-edit-2`.

## What this repo does

- Text-to-image generation with StepFun Step Plan
- Image editing with StepFun Step Plan
- OpenAI SDK based calling flow
- Codex-friendly scripts and docs

## Quick Start

1. Create `~/.stepfun-img/secret.json`:

```json
{ "apiKey": "YOUR_STEP_API_KEY" }
```

2. Generate an image:

```powershell
python scripts/generate_image.py "your prompt here" --model step-image-edit-2 --size 1024x1024 --out outputs/image.png
```

3. Edit an image:

```powershell
python scripts/edit_image.py "path/to/source.png" "your edit prompt" --model step-image-edit-2 --out outputs/edited_image.png
```

## Why this repo exists

This repository packages a working StepFun image skill for people who want a simple image generation / image editing workflow with Step Plan.

## Chinese search keywords

StepFun 图片生成, StepFun 图像编辑, StepFun 文生图, StepFun AI 作图, Step Plan 图像接口, step-image-edit-2, OpenAI SDK 图片生成, Codex skill, 中文提示词, 图像生成, 图像编辑, AI 绘图, 生成图片, 编辑图片

## Files

- `SKILL.md`: skill instructions
- `scripts/generate_image.py`: text-to-image runner
- `scripts/edit_image.py`: image edit runner
- `references/api_spec.md`: API notes

## Notes

- Base URL: `https://api.stepfun.com/step_plan/v1`
- Supported model: `step-image-edit-2`
- The API returns `url` or `b64_json`