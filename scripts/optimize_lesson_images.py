#!/usr/bin/env python3
"""Create display-sized WebP copies of lesson PNGs.

Original PNGs are kept and never overwritten. Lesson HTML should load
.webp, not the source PNG.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "lessons" / "assets"

STORY_WIDTH = 1000
VOCAB_WIDTH = 800
WEBP_QUALITY = 78


def display_width(name: str) -> int:
    if name.startswith("vocab-"):
        return VOCAB_WIDTH
    return STORY_WIDTH


def resize_keep_ratio(im: Image.Image, max_w: int) -> Image.Image:
    if im.width <= max_w:
        return im
    h = round(im.height * (max_w / im.width))
    return im.resize((max_w, h), Image.Resampling.LANCZOS)


def to_rgb(im: Image.Image) -> Image.Image:
    if im.mode in ("RGB",):
        return im
    if im.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGB", im.size, (255, 255, 255))
        converted = im.convert("RGBA")
        bg.paste(converted, mask=converted.split()[-1])
        return bg
    return im.convert("RGB")


def optimize_one(src: Path) -> int:
    max_w = display_width(src.name)
    with Image.open(src) as im:
        rgb = to_rgb(resize_keep_ratio(im, max_w))
        webp = src.with_suffix(".webp")
        rgb.save(webp, "WEBP", quality=WEBP_QUALITY, method=6)
        return webp.stat().st_size


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lesson",
        default="",
        help="Only one folder, e.g. lesson-01. Default: all lesson-XX folders.",
    )
    args = parser.parse_args()

    folders = (
        [ASSETS / args.lesson]
        if args.lesson
        else sorted(p for p in ASSETS.glob("lesson-*") if p.is_dir())
    )
    missing = [p for p in folders if not p.is_dir()]
    if missing:
        raise SystemExit(f"Folder not found: {missing[0]}")

    total_png = 0
    total_out = 0
    count = 0
    for folder in folders:
        for src in sorted(folder.glob("*.png")):
            png_size = src.stat().st_size
            webp_size = optimize_one(src)
            total_png += png_size
            total_out += webp_size
            count += 1
            print(
                f"OK  {folder.name}/{src.stem:16}  "
                f"png {png_size/1024:7.0f} KB -> webp {webp_size/1024:6.1f} KB"
            )

    if count:
        print(
            f"\nDone: {count} images. "
            f"PNG {total_png/1024/1024:.1f} MB -> "
            f"display WebP {total_out/1024/1024:.1f} MB "
            f"({100 * total_out / total_png:.1f}% of original)"
        )


if __name__ == "__main__":
    main()
