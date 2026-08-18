#!/usr/bin/env python3
"""Generate one lesson story-page video via Poe /v1/videos (default: Veo-3.1-Fast)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from poe_media import DEFAULT_VIDEO_MODEL, PoeClient  # noqa: E402

SILENT_SUFFIX = (
    " Children's picture-book animation, gentle and warm, age 5 friendly, no scary content. "
    "Silent video: no speech, no dialogue, no talking, no lip sync, ambient motion only. "
    "Seamless loop, end pose similar to start."
)

# Motion-only prompts per lesson/page (no story dialogue — audio is separate MP3s).
MOTION: dict[tuple[int, int], str] = {
    (3, 2): (
        "Static camera, very slow push-in. George, Pip and Ember pick red berries on a short path "
        "near a cave entrance. Gentle hand movements reaching for berries. Sky slowly darkens to "
        "soft grey. Cold wind rustles grass and leaves. Mood shifts from sunny to cloudy, calm not scary."
    ),
}


def page_prompt(lesson: int, page: int) -> str:
    motion = MOTION.get((lesson, page))
    if not motion:
        raise KeyError(f"No motion prompt for lesson {lesson} page {page}. Add to MOTION dict.")
    return f"Motion: {motion}.{SILENT_SUFFIX}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate one story-page video (Poe /v1/videos)")
    parser.add_argument("--lesson", type=int, required=True, help="Lesson number, e.g. 3")
    parser.add_argument("--page", type=int, required=True, help="Story page 1-8")
    parser.add_argument("--model", default=DEFAULT_VIDEO_MODEL, help=f"Poe video model (default: {DEFAULT_VIDEO_MODEL})")
    parser.add_argument("--seconds", type=int, default=6)
    parser.add_argument("--size", default="1280x720")
    parser.add_argument("--force", action="store_true")
    parser.add_argument(
        "--out-dir",
        type=Path,
        help="Output directory (default: lessons/assets/lesson-NN/video/)",
    )
    args = parser.parse_args()

    if "kling" in args.model.lower():
        print("Kling API is retired for this project (high cost, unsatisfactory pilot).")
        print("See docs/ai-video-lessons-learned.md — use Veo-3.1-Fast instead.")
        return 1

    asset_dir = ROOT / "lessons" / "assets" / f"lesson-{args.lesson:02d}"
    out_dir = args.out_dir or (asset_dir / "video")
    png = asset_dir / f"story-{args.page:02d}.png"
    out = out_dir / f"story-{args.page:02d}.mp4"

    if not png.is_file():
        raise FileNotFoundError(f"Missing illustration: {png}")
    if out.is_file() and not args.force:
        print(f"SKIP {out.name} (exists; use --force to regenerate)")
        return 0

    prompt = page_prompt(args.lesson, args.page)
    client = PoeClient()
    print(f"Lesson {args.lesson} story-{args.page:02d} | {args.model} | {args.seconds}s")
    print(f"Prompt: {prompt[:120]}...")
    client.generate_video(
        prompt,
        out,
        input_image=png,
        model=args.model,
        seconds=args.seconds,
        size=args.size,
    )
    print(f"Done: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
