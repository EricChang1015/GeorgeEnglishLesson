#!/usr/bin/env python3
"""Generate Lesson 2 story page videos via Poe image-to-video (local output only)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from poe_media import DEFAULT_VIDEO_MODEL, PoeClient  # noqa: E402

ASSET_DIR = ROOT / "lessons" / "assets" / "lesson-02"
DEFAULT_OUT_DIR = ROOT / "_local" / "pending-videos" / "lesson-02"

# Motion-only prompts — never include story dialogue (audio is separate MP3s).
MOTION = {
    1: "Static camera, very slow push-in. George runs gently up the hill. Pip waves one tiny wing. Soft breeze in grass.",
    2: "Static camera. The red egg on moss shakes gently. A crack slowly widens. Warm cave light flickers softly.",
    3: "Static camera. Ember peeks out of the hatching egg and blinks once. Pip nods slightly. Gentle celebration mood.",
    4: "Static camera. Ember shivers and rubs tiny wings. George and Pip lean in with caring expressions. Soft moss rustles.",
    5: "Static camera. George gathers moss, Pip offers berries. Ember watches happily. Leaves sway lightly.",
    6: "Static camera. Ember stretches tiny wings slowly. Pip gestures encouragingly. George watches with a supportive smile.",
    7: "Static camera. Ember flaps twice and rises slightly above the moss. George and Pip make small happy jumps.",
    8: "Very slow camera pull-back. All three friends laugh together in warm sunlight. Peaceful friendship mood.",
}

SILENT_SUFFIX = (
    " Children's picture-book animation, gentle and warm, age 5 friendly, no scary content. "
    "Silent video: no speech, no dialogue, no talking, no lip sync, ambient motion only. "
    "Seamless loop, end pose similar to start."
)


def page_prompt(page_num: int) -> str:
    return f"Motion: {MOTION[page_num]}.{SILENT_SUFFIX}"


def generate_page(
    client: PoeClient,
    page_num: int,
    out_dir: Path,
    *,
    seconds: int,
    force: bool,
) -> Path:
    png = ASSET_DIR / f"story-{page_num:02d}.png"
    if not png.is_file():
        raise FileNotFoundError(f"Missing illustration: {png}")
    out = out_dir / f"story-{page_num:02d}.mp4"
    if out.is_file() and not force:
        print(f"SKIP {out.name} (exists)")
        return out
    prompt = page_prompt(page_num)
    print(f"Generating video story-{page_num:02d}.mp4 ({DEFAULT_VIDEO_MODEL}, {seconds}s)...")
    return client.generate_video(
        prompt,
        out,
        input_image=png,
        seconds=seconds,
        size="1280x720",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Lesson 2 page videos (Poe video API only)")
    parser.add_argument("--page", type=int, help="One page (1-8)")
    parser.add_argument("--all", action="store_true", help="All 8 pages")
    parser.add_argument("--seconds", type=int, default=6)
    parser.add_argument("--force", action="store_true")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=DEFAULT_OUT_DIR,
        help=f"Output folder (default: {DEFAULT_OUT_DIR.relative_to(ROOT)})",
    )
    args = parser.parse_args()
    client = PoeClient()
    pages = [args.page] if args.page else (list(range(1, 9)) if args.all else [])
    if not pages:
        parser.error("Specify --page N or --all")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for n in pages:
        generate_page(client, n, args.out_dir, seconds=args.seconds, force=args.force)
    print(f"Done. Output: {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
