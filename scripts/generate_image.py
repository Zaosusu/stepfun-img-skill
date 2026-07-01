"""Generate an image with the StepFun API.

Encoding note:
- Reads ~/.stepfun-img/secret.json from the current user's home directory.
- Saves generated images as binary PNG bytes.
"""

import argparse
import base64
import json
import os
from datetime import datetime
from pathlib import Path

from openai import OpenAI


def disable_proxy_env() -> None:
    for key in ["ALL_PROXY", "HTTPS_PROXY", "HTTP_PROXY"]:
        os.environ[key] = ""
    os.environ["NO_PROXY"] = "*"


disable_proxy_env()


def iter_secret_candidates() -> list[Path]:
    return [Path.home() / ".stepfun-img" / "secret.json"]


def read_secret_api_key() -> str:
    """Read the StepFun API key from the local secret file."""
    for candidate in iter_secret_candidates():
        if candidate.exists():
            try:
                data = json.loads(candidate.read_text(encoding="utf-8"))
                api_key = data.get("apiKey")
                if api_key:
                    return api_key
            except Exception:
                pass
    return ""


def build_client(api_key: str) -> OpenAI:
    import httpx

    return OpenAI(
        api_key=api_key,
        base_url="https://api.stepfun.com/step_plan/v1",
        http_client=httpx.Client(trust_env=False),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate an image with the StepFun API.")
    parser.add_argument("prompt", help="Image description.")
    parser.add_argument("--model", default="step-image-edit-2")
    parser.add_argument("--size", default="1024x1024")
    parser.add_argument("--steps", type=int, default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--cfg-scale", type=float, default=None)
    parser.add_argument("--neg-prompt", default=None)
    parser.add_argument("--text-mode", action="store_true", default=False)
    parser.add_argument("--n", type=int, default=1)
    parser.add_argument("--response-format", default="url")
    parser.add_argument("--style-reference", default=None)
    parser.add_argument("--out", default=None)
    return parser.parse_args()


def resolve_out(args: argparse.Namespace) -> Path:
    if args.out:
        return Path(args.out)
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    return Path("outputs") / f"stepfun_{now}.png"


def ensure_default_steps(model: str, steps):
    if steps is None:
        return 8 if model == "step-image-edit-2" else 50
    return steps


def ensure_default_cfg(model: str, cfg_scale):
    if cfg_scale is None:
        if model == "step-image-edit-2":
            return 1.0
        if model == "step-2x-large":
            return 6.0
        return 7.5
    return cfg_scale


def generate(args: argparse.Namespace) -> Path:
    api_key = read_secret_api_key()
    if not api_key:
        raise SystemExit("Missing StepFun API key. Please place it in ~/.stepfun-img/secret.json.")

    client = build_client(api_key)
    extra_body = {
        "steps": ensure_default_steps(args.model, args.steps),
        "cfg_scale": ensure_default_cfg(args.model, args.cfg_scale),
    }
    if args.seed is not None:
        extra_body["seed"] = args.seed
    if args.neg_prompt:
        extra_body["negative_prompt"] = args.neg_prompt
    if args.text_mode:
        extra_body["text_mode"] = True
    if args.style_reference is not None:
        extra_body["style_reference"] = args.style_reference

    response = client.images.generate(
        model=args.model,
        prompt=args.prompt,
        size=args.size,
        n=args.n,
        response_format=args.response_format,
        extra_body=extra_body,
    )
    if not response.data:
        raise SystemExit("StepFun returned no image data.")

    item = response.data[0]
    out_path = resolve_out(args)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if args.response_format == "b64_json" and item.b64_json:
        out_path.write_bytes(base64.b64decode(item.b64_json))
        return out_path

    if item.url:
        import urllib.request
        urllib.request.urlretrieve(item.url, out_path)
        return out_path

    raise SystemExit("No downloadable image URL or b64_json was returned.")


def main() -> None:
    args = parse_args()
    out_path = generate(args)
    print(out_path)


if __name__ == "__main__":
    main()
