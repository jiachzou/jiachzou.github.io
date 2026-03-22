#!/usr/bin/env python3
"""
Generate a comic-style thumbnail PNG for a blog post.

Pipeline:
  1. (Prompt crafting is done by Claude Code in-conversation — see usage below)
  2. Call an image generation API with the supplied prompt
  3. Save PNG to images/blog/<slug>-thumb.png
  4. Auto-update the post's front matter with the thumbnail path

Supported backends (set IMAGE_BACKEND env var, default: hf):
  hf          Hugging Face Inference API  — free tier, needs HF_TOKEN
  replicate   Replicate                   — free credits, needs REPLICATE_API_TOKEN
  gemini      Google Gemini / Imagen 3    — $300 free credit, needs GEMINI_API_KEY
  local       Local diffusers (CPU/GPU)   — free, no account needed

Usage:
  # Hugging Face (recommended — free)
  HF_TOKEN=hf_xxx python scripts/generate_thumbnail.py \\
      _posts/2026-03-22-my-post.md \\
      "Single-panel comic illustration, vibrant flat colours: <your prompt here>"

  # Local (no API key at all)
  IMAGE_BACKEND=local python scripts/generate_thumbnail.py \\
      _posts/2026-03-22-my-post.md \\
      "<prompt>"
"""

import sys
import os
import re
from pathlib import Path


# ---------------------------------------------------------------------------
# Front-matter helpers
# ---------------------------------------------------------------------------

def parse_frontmatter(content: str) -> tuple[dict, str]:
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    import yaml
    return yaml.safe_load(parts[1]) or {}, parts[2].strip()


def serialize_frontmatter(fm: dict, body: str) -> str:
    import yaml
    fm_str = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return f"---\n{fm_str}---\n\n{body}\n"


def slug_from_path(post_path: str) -> str:
    stem = Path(post_path).stem
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem)


def update_thumbnail_in_post(post_path: str, thumbnail_rel: str) -> None:
    content = Path(post_path).read_text()
    fm, body = parse_frontmatter(content)
    fm["thumbnail"] = thumbnail_rel
    Path(post_path).write_text(serialize_frontmatter(fm, body))


# ---------------------------------------------------------------------------
# Image generation backends
# ---------------------------------------------------------------------------

def generate_hf(prompt: str) -> bytes:
    """Hugging Face Inference API — free tier, FLUX.1-schnell."""
    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN")
    if not token:
        sys.exit("Set HF_TOKEN to your Hugging Face access token.\n"
                 "Get one free at: https://huggingface.co/settings/tokens")
    try:
        from huggingface_hub import InferenceClient
    except ImportError:
        sys.exit("Run: pip install huggingface_hub")

    print("  → Hugging Face FLUX.1-schnell…")
    client = InferenceClient(token=token)
    image = client.text_to_image(
        prompt,
        model="black-forest-labs/FLUX.1-schnell",
        width=1344,
        height=768,
    )
    import io
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    return buf.getvalue()


def generate_replicate(prompt: str) -> bytes:
    """Replicate — free credits on signup, FLUX.1-schnell."""
    token = os.environ.get("REPLICATE_API_TOKEN")
    if not token:
        sys.exit("Set REPLICATE_API_TOKEN.\nGet free credits at: https://replicate.com")
    try:
        import replicate
    except ImportError:
        sys.exit("Run: pip install replicate")

    print("  → Replicate FLUX.1-schnell…")
    output = replicate.run(
        "black-forest-labs/flux-schnell",
        input={
            "prompt": prompt,
            "aspect_ratio": "16:9",
            "output_format": "png",
        },
    )
    import urllib.request
    url = str(output[0]) if isinstance(output, list) else str(output)
    with urllib.request.urlopen(url) as r:
        return r.read()


def generate_gemini(prompt: str) -> bytes:
    """Google Gemini 2.0 Flash image generation — free on AI Studio."""
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("Set GEMINI_API_KEY.\nGet a free key at: https://aistudio.google.com/apikey")
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        sys.exit("Run: pip install google-genai")

    print("  → Google Gemini 2.0 Flash (image generation)…")
    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"]
        ),
    )

    import base64
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            data = part.inline_data.data
            # SDK may return raw bytes or a base64 string depending on version
            if isinstance(data, (bytes, bytearray)):
                return bytes(data)
            return base64.b64decode(data)

    raise RuntimeError("Gemini returned no image. Response: " + str(response))


def generate_local(prompt: str) -> bytes:
    """Local diffusers — no API key, needs GPU for speed (works on CPU, slowly)."""
    try:
        import torch
        from diffusers import FluxPipeline
    except ImportError:
        sys.exit("Run: pip install diffusers transformers accelerate torch")

    print("  → Local FLUX.1-schnell via diffusers (this may take a while on CPU)…")
    pipe = FluxPipeline.from_pretrained(
        "black-forest-labs/FLUX.1-schnell",
        torch_dtype=torch.bfloat16,
    )
    device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
    pipe = pipe.to(device)
    image = pipe(prompt, width=1344, height=768, num_inference_steps=4).images[0]
    import io
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    return buf.getvalue()


BACKENDS = {
    "hf":        generate_hf,
    "replicate": generate_replicate,
    "gemini":    generate_gemini,
    "local":     generate_local,
}


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    post_path = sys.argv[1]
    prompt    = sys.argv[2]

    if not Path(post_path).exists():
        sys.exit(f"Error: file not found — {post_path}")

    backend_name = os.environ.get("IMAGE_BACKEND", "hf")
    if backend_name not in BACKENDS:
        sys.exit(f"Unknown IMAGE_BACKEND '{backend_name}'. Choose from: {', '.join(BACKENDS)}")

    repo_root  = Path(__file__).parent.parent
    slug       = slug_from_path(post_path)
    image_dir  = repo_root / "images" / "blog"
    image_dir.mkdir(parents=True, exist_ok=True)
    image_path = image_dir / f"{slug}-thumb.png"
    thumb_rel  = f"/images/blog/{slug}-thumb.png"

    print(f"\n[1/3] Backend: {backend_name}")
    print(f"      Prompt:  {prompt[:120]}{'…' if len(prompt) > 120 else ''}")

    print(f"[2/3] Generating image…")
    png_bytes = BACKENDS[backend_name](prompt)

    print(f"[3/3] Saving…")
    image_path.write_bytes(png_bytes)
    print(f"      Saved  → {image_path}")

    update_thumbnail_in_post(post_path, thumb_rel)
    print(f"      Updated thumbnail in post: {thumb_rel}")
    print(f"\nDone!")


if __name__ == "__main__":
    main()
