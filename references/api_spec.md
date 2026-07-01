# StepFun Step Plan Image API

## Endpoint

``POST https://api.stepfun.com/step_plan/v1/images/generations``

``POST https://api.stepfun.com/step_plan/v1/images/edits``

## Supported Model

- `step-image-edit-2`

## Generation

Use the generation endpoint to create a new image from a text prompt.

Required fields:
- `model`
- `prompt`

Optional fields:
- `size`
- `n`
- `response_format`
- `seed`
- `steps`
- `cfg_scale`
- `negative_prompt`
- `text_mode`

Supported sizes for `step-image-edit-2`:
- `1024x1024`
- `768x1360`
- `896x1184`
- `1360x768`
- `1184x896`

## Editing

Use the edit endpoint to modify an existing image.

Required fields:
- `model`
- `image`
- `prompt`

Optional fields:
- `seed`
- `steps`
- `cfg_scale`
- `size`
- `negative_prompt`
- `text_mode`
- `response_format`

## Response

Both endpoints return `created` and `data`.
Use `data[0].url` or `data[0].b64_json` to save the result.

## Notes

- `step_plan/v1` currently supports only `step-image-edit-2`.
- The API returns temporary download URLs when `response_format` is `url`.
