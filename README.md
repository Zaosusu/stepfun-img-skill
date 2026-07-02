# stepfun-img-skill

StepFun 图片生成 / 图像编辑 Skill，支持中文搜索关键词：StepFun 文生图、StepFun 图像编辑、StepFun AI 作图、Step Plan 图像接口、step-image-edit-2、OpenAI SDK 图片生成。

如果你在找这些内容，这个仓库就是：
- StepFun 图片生成
- StepFun 图像编辑
- StepFun 文生图
- StepFun AI 作图
- Step Plan 接入示例
- step-image-edit-2 使用示例
- OpenAI SDK 调用 StepFun 图片接口
- Codex skill 图像生成

## 简介

这是一个给 Codex 使用的 StepFun 图像 skill，基于 Step Plan 的图像生成与图像编辑接口：
- 生成接口：`https://api.stepfun.com/step_plan/v1/images/generations`
- 编辑接口：`https://api.stepfun.com/step_plan/v1/images/edits`
- 支持模型：`step-image-edit-2`

你可以把它理解成一个轻量的 StepFun 文生图 / 图像编辑工具包，适合直接拿来改 prompt、做图片生成测试、或者集成到自己的 Codex 工作流里。

## 快速开始

1. 在本机准备密钥文件：`~/.stepfun-img/secret.json`
2. 填入你的 StepFun API Key：

```json
{ "apiKey": "YOUR_STEP_API_KEY" }
```

3. 生成图片：

```powershell
python scripts/generate_image.py "your prompt here" --model step-image-edit-2 --size 1024x1024 --out outputs/image.png
```

4. 编辑图片：

```powershell
python scripts/edit_image.py "path/to/source.png" "your edit prompt" --model step-image-edit-2 --out outputs/edited_image.png
```

## 适合搜索的关键词

StepFun 图片生成, StepFun 图像编辑, StepFun 文生图, StepFun AI 作图, Step Plan 图像接口, step-image-edit-2, OpenAI SDK 图片生成, Codex skill, 中文提示词, 图像生成, 图像编辑, AI 绘图, 生成图片, 编辑图片

## 文件说明

- `SKILL.md`: skill 使用说明
- `scripts/generate_image.py`: 文生图脚本
- `scripts/edit_image.py`: 图像编辑脚本
- `references/api_spec.md`: API 参考

## 说明

- 这个仓库默认面向 `step_plan/v1`
- 目前只支持 `step-image-edit-2`
- 适合中文 prompt、英文 prompt 和中英混合 prompt