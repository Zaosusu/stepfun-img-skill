"""Edit an image with the StepFun API.

Encoding note:
- Reads ~/.stepfun-img/secret.json from the current user's home directory.
- Saves edited images as binary PNG bytes.
"""

import argparse
import base64
import json
import os
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
    parser = argparse.ArgumentParser(description="Edit an image with the StepFun API.")
    parser.add_argument("image", help="Source image path to edit.")
    parser.add_argument("prompt", help="Edit instructions.")
    parser.add_argument("--model", default="step-image-edit-2")
    parser.add_argument("--steps", type=int, default=8)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--cfg-scale", type=float, default=1.0)
    parser.add_argument("--neg-prompt", default="")
    parser.add_argument("--text-mode", action="store_true", default=False)
    parser.add_argument("--response-format", default="b64_json")
    parser.add_argument("--out", default=None)
    return parser.parse_args()


def resolve_out(args: argparse.Namespace, source_path: Path) -> Path:
    if args.out:
        return Path(args.out)
    stem = source_path.stem
    suffix = source_path.suffix or ".png"
    now = __import__("datetime").datetime.now().strftime("%Y%m%d_%H%M%S")
    return Path("outputs") / f"stepfun_edit_{stem}_{now}{suffix}"


def edit(args: argparse.Namespace) -> Path:
    api_key = read_secret_api_key()
    if not api_key:
        raise SystemExit("Missing StepFun API key. Please place it in ~/.stepfun-img/secret.json.")

    source_path = Path(args.image)
    if not source_path.exists():
        raise SystemExit(f"Source image not found: {source_path}")

    client = build_client(api_key)
    extra_body = {
        "steps": args.steps,
        "cfg_scale": args.cfg_scale,
    }
    if args.seed is not None:
        extra_body["seed"] = args.seed
    if args.neg_prompt:
        extra_body["negative_prompt"] = args.neg_prompt
    if args.text_mode:
        extra_body["text_mode"] = True

    with source_path.open("rb") as image_file:
        response = client.images.edit(
            model=args.model,
            image=image_file,
            prompt=args.prompt,
            response_format=args.response_format,
            extra_body=extra_body,
        )

    if not response.data:
        raise SystemExit("StepFun returned no image data.")

    item = response.data[0]
    out_path = resolve_out(args, source_path)
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
    out_path = edit(args)
    print(out_path)


if __name__ == "__main__":
    main()
