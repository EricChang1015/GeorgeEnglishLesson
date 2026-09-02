#!/usr/bin/env python3
"""Pre-delivery audio acceptance check for a lesson.

Verifies, for every clip the story JSON expects:
  1. the MP3 exists and is not truncated/empty
  2. its duration is plausible for the text length (catches cut-off or garbage TTS)
  3. each role's voice settings match the canonical scripts/voices.json

Usage:
  python scripts/check_lesson_audio.py --story scripts/lesson04_story.json \
      --audio lessons/assets/lesson-04/audio

Exit code 0 = all pass; 1 = at least one FAIL (do not deliver).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LETTERS = "abc"
MIN_BYTES = 1024  # anything smaller is a broken/empty synth

try:
    from mutagen.mp3 import MP3  # type: ignore

    def mp3_seconds(path: Path) -> float:
        return float(MP3(str(path)).info.length)

except ImportError:
    # Edge TTS default output is 48 kbit/s mono MP3 -> ~6000 bytes/second.
    def mp3_seconds(path: Path) -> float:
        return path.stat().st_size / 6000.0


def expected_clips(data: dict) -> list[tuple[str, str]]:
    """Return (filename, spoken_text) pairs mirroring generate_lesson_audio.py."""
    clips: list[tuple[str, str]] = []
    for item in data.get("vocab", []):
        clips.append((item["audio"], item["word"]))
        if item.get("example") and item.get("example_audio"):
            clips.append((item["example_audio"], item["example"]))
    for page in data.get("pages", []):
        for line in page.get("lines", []):
            clips.append((line["audio"], line["text"]))
    for page in data.get("songPages") or []:
        for line in page.get("lines", []):
            audio = line.get("audio")
            if audio:
                clips.append((audio, line.get("text") or audio))
    clips.append(("praise-great.mp3", "Great job!"))
    clips.append(("praise-try.mp3", "Nice try! Let's learn it."))
    clips.append(("title.mp3", data.get("title", "")))
    quiz = data.get("quiz") or []
    if quiz:
        clips.append(("quiz-choose.mp3", "Now choose A, B, or C."))
        for i, item in enumerate(quiz, start=1):
            nn = f"{i:02d}"
            clips.append((f"quiz-{nn}.mp3", item["q"]))
            for oi, opt in enumerate(item["options"][:3]):
                clips.append((f"quiz-{nn}-{LETTERS[oi]}.mp3", f"{LETTERS[oi].upper()}. {opt}"))
    return clips


def is_minimax(cfg: dict) -> bool:
    return str(cfg.get("engine") or "").startswith("minimax") or bool(cfg.get("voice_id"))


def check_voices(data: dict) -> list[str]:
    problems: list[str] = []
    canonical = json.loads((ROOT / "scripts" / "voices.json").read_text(encoding="utf-8"))["roles"]
    for role, cfg in data.get("voices", {}).items():
        if role not in canonical:
            problems.append(f"voice: role '{role}' is not in scripts/voices.json (reserved/uncast?)")
            continue
        want = canonical[role]
        story_mm = is_minimax(cfg)
        canon_mm = is_minimax(want)
        if story_mm or canon_mm:
            if role == "george":
                # voices.json still lists Edge Ana as fallback; published L3+ lock is cute_boy.
                if (cfg.get("voice_id") or cfg.get("voice")) != "cute_boy":
                    problems.append(
                        f"voice: role 'george' uses unapproved MiniMax voice {cfg.get('voice_id') or cfg.get('voice')}"
                    )
                continue
            if not canon_mm:
                problems.append(f"voice: role '{role}' uses MiniMax but voices.json is Edge")
                continue
            for key in ("engine", "voice_id", "speed", "pitch"):
                if cfg.get(key) != want.get(key):
                    problems.append(
                        f"voice: role '{role}' {key}={cfg.get(key)!r} but voices.json says {want.get(key)!r}"
                    )
            continue
        for key in ("voice", "rate", "pitch"):
            if cfg.get(key) != want.get(key):
                problems.append(
                    f"voice: role '{role}' {key}={cfg.get(key)!r} but voices.json says {want.get(key)!r}"
                )
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--story", required=True, help="scripts/lessonXX_story.json")
    ap.add_argument("--audio", required=True, help="lessons/assets/lesson-XX/audio")
    args = ap.parse_args()

    data = json.loads(Path(args.story).read_text(encoding="utf-8"))
    audio_dir = Path(args.audio)
    failures: list[str] = []

    clips = expected_clips(data)
    for name, text in clips:
        path = audio_dir / name
        if not path.is_file():
            failures.append(f"missing: {name}  ({text[:40]!r})")
            continue
        size = path.stat().st_size
        if size < MIN_BYTES:
            failures.append(f"broken: {name} is only {size} bytes")
            continue
        secs = mp3_seconds(path)
        chars = max(len(text), 1)
        # Very wide plausibility band: catches cut-off clips and runaway synth,
        # not minor pacing differences.
        lo, hi = chars / 30.0, chars / 3.0 + 4.0
        if not (lo <= secs <= hi):
            failures.append(
                f"duration: {name} is {secs:.1f}s for {chars} chars "
                f"(expected {lo:.1f}-{hi:.1f}s) -- listen before delivering"
            )

    failures.extend(check_voices(data))

    known = {name for name, _ in clips}
    extras = sorted(p.name for p in audio_dir.glob("*.mp3") if p.name not in known)
    if extras:
        print(f"note: {len(extras)} mp3(s) in folder not referenced by story JSON: {', '.join(extras[:8])}"
              + (" ..." if len(extras) > 8 else ""))

    print(f"checked {len(clips)} expected clips in {audio_dir}")
    if failures:
        for f in failures:
            print(f"FAIL  {f}")
        print(f"\n{len(failures)} problem(s). DO NOT deliver until fixed.")
        return 1
    print("PASS  all clips present, sized, duration-plausible; voices match voices.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
