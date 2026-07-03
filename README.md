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

## Parameters

- `model`: `step-image-edit-2` is recommended under Step Plan. `step-2x-large` and `step-1x-medium` are available on `/v1`, not Step Plan.
- `prompt`: text description, up to 512 characters.
- `size`: image size. For `step-image-edit-2`, use `1024x1024`, `768x1360`, `896x1184`, `1360x768`, or `1184x896`.
- `seed`: random seed for more repeatable results.
- `steps`: generation steps. Higher values usually refine more slowly but can add detail.
- `cfg_scale`: guidance strength, meaning how strongly the model follows the prompt.
- `negative_prompt`: unwanted features to suppress. Only `step-image-edit-2` supports it.
- `text_mode`: optimize for text-heavy scenes. Only `step-image-edit-2` supports it.
- `style_reference`: style reference for `step-1x-medium`.
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