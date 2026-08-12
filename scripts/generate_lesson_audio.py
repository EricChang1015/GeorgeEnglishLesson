#!/usr/bin/env python3
"""Generate role-based neural TTS MP3s for a lesson story JSON."""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parents[1]


async def save_line(text: str, out: Path, voice: str, rate: str, pitch: str) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    communicate = edge_tts.Communicate(text, voice=voice, rate=rate, pitch=pitch)
    await communicate.save(str(out))
    print(f"OK  {out.name}  ({voice})  {text[:56]}{'…' if len(text) > 56 else ''}")


async def generate(story_path: Path, audio_dir: Path) -> None:
    data = json.loads(story_path.read_text(encoding="utf-8"))
    voices = data["voices"]
    jobs: list[tuple[str, str, str, str, Path]] = []

    for item in data.get("vocab", []):
        cfg = voices["narrator"]
        jobs.append((item["word"], cfg["voice"], cfg["rate"], cfg["pitch"], audio_dir / item["audio"]))

    for page in data["pages"]:
        for line in page["lines"]:
            cfg = voices[line["role"]]
            jobs.append((line["text"], cfg["voice"], cfg["rate"], cfg["pitch"], audio_dir / line["audio"]))

    # short praise cues
    praise = [
        ("Great job!", "praise-great.mp3"),
        ("Nice try! Let's learn it.", "praise-try.mp3"),
        (data.get("title", "George and the Little Dragon"), "title.mp3"),
    ]
    for text, name in praise:
        cfg = voices["narrator"]
        jobs.append((text, cfg["voice"], cfg["rate"], cfg["pitch"], audio_dir / name))

    for text, voice, rate, pitch, out in jobs:
        await save_line(text, out, voice, rate, pitch)

    print(f"\nDone: {len(jobs)} files -> {audio_dir}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--story",
        default=str(ROOT / "scripts" / "lesson01_story.json"),
        help="Path to lesson story JSON",
    )
    parser.add_argument(
        "--out",
        default=str(ROOT / "lessons" / "assets" / "lesson-01" / "audio"),
        help="Output audio directory",
    )
    args = parser.parse_args()
    asyncio.run(generate(Path(args.story), Path(args.out)))


if __name__ == "__main__":
    main()
