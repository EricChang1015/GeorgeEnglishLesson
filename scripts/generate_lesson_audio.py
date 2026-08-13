#!/usr/bin/env python3
"""Generate role-based neural TTS MP3s for a lesson story JSON."""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parents[1]
LETTERS = "abc"


async def save_line(text: str, out: Path, voice: str, rate: str, pitch: str) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    communicate = edge_tts.Communicate(text, voice=voice, rate=rate, pitch=pitch)
    await communicate.save(str(out))
    print(f"OK  {out.name}  ({voice})  {text[:56]}{'…' if len(text) > 56 else ''}")


def collect_jobs(data: dict, audio_dir: Path, quiz_only: bool) -> list[tuple[str, str, str, str, Path]]:
    voices = data["voices"]
    jobs: list[tuple[str, str, str, str, Path]] = []
    narrator = voices["narrator"]

    if not quiz_only:
        for item in data.get("vocab", []):
            jobs.append((item["word"], narrator["voice"], narrator["rate"], narrator["pitch"], audio_dir / item["audio"]))
            example = item.get("example")
            example_audio = item.get("example_audio")
            if example and example_audio:
                jobs.append((example, narrator["voice"], narrator["rate"], narrator["pitch"], audio_dir / example_audio))

        for page in data["pages"]:
            for line in page["lines"]:
                cfg = voices[line["role"]]
                jobs.append((line["text"], cfg["voice"], cfg["rate"], cfg["pitch"], audio_dir / line["audio"]))

        praise = [
            ("Great job!", "praise-great.mp3"),
            ("Nice try! Let's learn it.", "praise-try.mp3"),
            (data.get("title", "George and the Little Dragon"), "title.mp3"),
        ]
        for text, name in praise:
            jobs.append((text, narrator["voice"], narrator["rate"], narrator["pitch"], audio_dir / name))

    quiz = data.get("quiz") or []
    if quiz:
        jobs.append(
            (
                "Now choose A, B, or C.",
                narrator["voice"],
                narrator["rate"],
                narrator["pitch"],
                audio_dir / "quiz-choose.mp3",
            )
        )
        for i, item in enumerate(quiz, start=1):
            nn = f"{i:02d}"
            jobs.append(
                (item["q"], narrator["voice"], narrator["rate"], narrator["pitch"], audio_dir / f"quiz-{nn}.mp3")
            )
            for oi, opt in enumerate(item["options"][:3]):
                letter = LETTERS[oi]
                spoken = f"{letter.upper()}. {opt}"
                jobs.append(
                    (
                        spoken,
                        narrator["voice"],
                        narrator["rate"],
                        narrator["pitch"],
                        audio_dir / f"quiz-{nn}-{letter}.mp3",
                    )
                )

    return jobs


async def generate(
    story_path: Path,
    audio_dir: Path,
    *,
    quiz_only: bool = False,
    skip_existing: bool = False,
) -> None:
    data = json.loads(story_path.read_text(encoding="utf-8"))
    jobs = collect_jobs(data, audio_dir, quiz_only)
    written = 0
    for text, voice, rate, pitch, out in jobs:
        if skip_existing and out.exists():
            print(f"SKIP  {out.name}")
            continue
        await save_line(text, out, voice, rate, pitch)
        written += 1
    print(f"\nDone: {written} new files ({len(jobs)} jobs) -> {audio_dir}")


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
    parser.add_argument("--quiz-only", action="store_true", help="Only generate quiz question/option audio")
    parser.add_argument("--skip-existing", action="store_true", help="Do not overwrite MP3s that already exist")
    args = parser.parse_args()
    asyncio.run(
        generate(
            Path(args.story),
            Path(args.out),
            quiz_only=args.quiz_only,
            skip_existing=args.skip_existing,
        )
    )


if __name__ == "__main__":
    main()
