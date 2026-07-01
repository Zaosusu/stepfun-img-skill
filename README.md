# stepfun-img-skill

A small Codex skill for generating and editing images with StepFun Step Plan.

## What it does

- Text-to-image generation through `step_plan/v1`
- Image editing through `step_plan/v1`
- Saves the generated image to a local output path

## Setup

Create `~/.stepfun-img/secret.json` with your StepFun API key:

```json
{ "apiKey": "YOUR_STEP_API_KEY" }
```

## Generate an image

```powershell
python scripts/generate_image.py "your prompt here" --model step-image-edit-2 --size 1024x1024 --out outputs/image.png
```

## Edit an image

```powershell
python scripts/edit_image.py "path/to/source.png" "your edit prompt" --model step-image-edit-2 --out outputs/edited_image.png
```

## Files

- `SKILL.md`: skill instructions
- `scripts/generate_image.py`: text-to-image runner
- `scripts/edit_image.py`: image edit runner
- `references/api_spec.md`: API notes

## Notes

- The skill uses `https://api.stepfun.com/step_plan/v1`
- Only `step-image-edit-2` is supported under Step Plan
