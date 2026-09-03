#!/usr/bin/env python3
"""Generate F2 cute_boy baseline speed options for parent listen test."""

from __future__ import annotations

import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from poe_media import PoeClient  # noqa: E402
from sample_minimax_speech import OUT_DIR, extra_body, synthesize  # noqa: E402

VOICE = "cute_boy"
PITCH = 0
VOLUME = 1.0
EMOTION = "happy"

# Same lines as Lesson 3 George (single-pass, no segments — baseline only).
CLIPS = [
    {
        "group": "p01-02 · excited hello",
        "text": "Hello! Shall we look for berries near the cave?",
        "speeds": [1.10, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45],
        "prefix": "f2-p01",
    },
    {
        "group": "p03-02 · worried storm",
        "text": "Is a storm coming, Pip?",
        "speeds": [1.10, 1.20, 1.25, 1.30, 1.35],
        "prefix": "f2-p03",
        "emotion": "fearful",
    },
]


def speed_tag(speed: float) -> str:
    return f"{int(round(speed * 100)):03d}"


def main() -> int:
    client = PoeClient()
    rows: list[dict] = []
    for block in CLIPS:
        emotion = block.get("emotion") or EMOTION
        for speed in block["speeds"]:
            tag = speed_tag(speed)
            name = f"{block['prefix']}-spd{tag}.mp3"
            out = OUT_DIR / name
            if rows:
                time.sleep(0.35)
            synthesize(
                client,
                block["text"],
                extra_body(
                    voice=VOICE,
                    emotion=emotion,
                    speed=speed,
                    volume=VOLUME,
                    pitch=PITCH,
                ),
                out,
            )
            rows.append(
                {
                    "group": block["group"],
                    "file": name,
                    "title": f"speed {speed:.2f}×",
                    "meta": f"cute_boy · pitch {PITCH} · {emotion}",
                    "text": block["text"],
                    "speed": speed,
                }
            )
    print(f"\nListen: {OUT_DIR / 'index.html'} (gitignored voice-tests)")
    print(f"Files: {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
