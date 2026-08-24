#!/usr/bin/env python3
"""Generate role-based neural TTS MP3s for a lesson story JSON.

Edge TTS is the default. Roles with engine "minimax-speech-2.8" (see
scripts/minimax_voices.json) go through Poe MiniMax Speech.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from poe_media import PoeClient  # noqa: E402
from sample_minimax_speech import extra_body, synthesize  # noqa: E402

LETTERS = "abc"

# Story emotion tag -> MiniMax prosody defaults. Pitch stays subtle (±1–2).
MINIMAX_DELIVERY = {
    "excited": {"minimax_emotion": "happy", "speed": 1.34, "pitch": 1, "volume": 1.0},
    "happy": {"minimax_emotion": "happy", "speed": 1.30, "pitch": 1, "volume": 1.0},
    "surprised": {"minimax_emotion": "surprised", "speed": 1.28, "pitch": 1, "volume": 1.0},
    "worried": {"minimax_emotion": "fearful", "speed": 1.30, "pitch": 1, "volume": 0.88},
    "fearful": {"minimax_emotion": "fearful", "speed": 1.28, "pitch": 1, "volume": 0.86},
    "whisper": {"minimax_emotion": "fearful", "speed": 1.0, "pitch": -1, "volume": 0.78},
    "soft": {"minimax_emotion": "fearful", "speed": 1.30, "pitch": 0, "volume": 0.82},
    "calm": {"minimax_emotion": "calm", "speed": 1.30, "pitch": 0, "volume": 0.88},
    "proud": {"minimax_emotion": "happy", "speed": 1.26, "pitch": 1, "volume": 0.95},
    "wonder": {"minimax_emotion": "surprised", "speed": 1.24, "pitch": 1, "volume": 0.95},
}


def is_minimax(cfg: dict) -> bool:
    engine = str(cfg.get("engine") or "")
    return engine.startswith("minimax") or bool(cfg.get("voice_id"))


def collect_jobs(data: dict, audio_dir: Path, quiz_only: bool) -> list[dict]:
    voices = data["voices"]
    jobs: list[dict] = []
    narrator = voices["narrator"]

    if not quiz_only:
        for item in data.get("vocab", []):
            jobs.append(
                {
                    "text": item["word"],
                    "role": "narrator",
                    "cfg": narrator,
                    "out": audio_dir / item["audio"],
                }
            )
            example = item.get("example")
            example_audio = item.get("example_audio")
            if example and example_audio:
                jobs.append(
                    {
                        "text": example,
                        "role": "narrator",
                        "cfg": narrator,
                        "out": audio_dir / example_audio,
                    }
                )

        for page in data["pages"]:
            for line in page["lines"]:
                cfg = voices[line["role"]]
                jobs.append(
                    {
                        "text": line["text"],
                        "role": line["role"],
                        "cfg": cfg,
                        "emotion": line.get("emotion"),
                        "delivery": line.get("delivery") or {},
                        "out": audio_dir / line["audio"],
                    }
                )

        praise = [
            ("Great job!", "praise-great.mp3"),
            ("Nice try! Let's learn it.", "praise-try.mp3"),
            (data.get("title", "George and the Little Dragon"), "title.mp3"),
        ]
        for text, name in praise:
            jobs.append({"text": text, "role": "narrator", "cfg": narrator, "out": audio_dir / name})

    quiz = data.get("quiz") or []
    if quiz:
        jobs.append(
            {
                "text": "Now choose A, B, or C.",
                "role": "narrator",
                "cfg": narrator,
                "out": audio_dir / "quiz-choose.mp3",
            }
        )
        for i, item in enumerate(quiz, start=1):
            nn = f"{i:02d}"
            jobs.append(
                {
                    "text": item["q"],
                    "role": "narrator",
                    "cfg": narrator,
                    "out": audio_dir / f"quiz-{nn}.mp3",
                }
            )
            for oi, opt in enumerate(item["options"][:3]):
                letter = LETTERS[oi]
                jobs.append(
                    {
                        "text": f"{letter.upper()}. {opt}",
                        "role": "narrator",
                        "cfg": narrator,
                        "out": audio_dir / f"quiz-{nn}-{letter}.mp3",
                    }
                )

    return jobs


async def save_edge(text: str, out: Path, voice: str, rate: str, pitch: str) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    communicate = edge_tts.Communicate(text, voice=voice, rate=rate, pitch=pitch)
    await communicate.save(str(out))
    print(f"OK  {out.name}  (edge {voice})  {text[:56]}{'…' if len(text) > 56 else ''}")


def resolve_minimax_delivery(job: dict) -> dict:
    cfg = job["cfg"]
    tag = (job.get("emotion") or "calm").lower()
    preset = MINIMAX_DELIVERY.get(tag, MINIMAX_DELIVERY["calm"])
    override = job.get("delivery") or {}
    base_speed = float(cfg.get("speed", 1.30))
    scale = base_speed / 1.30
    preset_speed = float(preset.get("speed", base_speed)) * scale
    return {
        "minimax_emotion": override.get("minimax_emotion") or preset["minimax_emotion"],
        "speed": float(override.get("speed", preset_speed)),
        "pitch": int(override.get("pitch", preset.get("pitch", cfg.get("pitch", 0)))),
        "volume": float(override.get("volume", preset.get("volume", cfg.get("volume", 1.0)))),
    }


def resolve_segment_delivery(segment: dict, base: dict) -> dict:
    return {
        "text": segment["text"],
        "minimax_emotion": segment.get("minimax_emotion") or base["minimax_emotion"],
        "speed": float(segment.get("speed", base["speed"])),
        "pitch": int(segment.get("pitch", base["pitch"])),
        "volume": float(segment.get("volume", base["volume"])),
    }


def concat_mp3(parts: list[Path], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("wb") as dst:
        for part in parts:
            dst.write(part.read_bytes())


def save_minimax(client: PoeClient, job: dict) -> None:
    cfg = job["cfg"]
    delivery = resolve_minimax_delivery(job)
    voice = cfg.get("voice_id") or cfg.get("voice")
    out: Path = job["out"]
    segments = (job.get("delivery") or {}).get("segments")

    if not segments:
        synthesize(
            client,
            job["text"],
            extra_body(
                voice=voice,
                emotion=delivery["minimax_emotion"],
                speed=delivery["speed"],
                volume=delivery["volume"],
                pitch=delivery["pitch"],
            ),
            out,
        )
        return

    tmp_dir = out.parent / "_tmp_minimax"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    parts: list[Path] = []
    for i, raw in enumerate(segments):
        seg = resolve_segment_delivery(raw, delivery)
        part = tmp_dir / f"{out.stem}-seg{i:02d}.mp3"
        synthesize(
            client,
            seg["text"],
            extra_body(
                voice=voice,
                emotion=seg["minimax_emotion"],
                speed=seg["speed"],
                volume=seg["volume"],
                pitch=seg["pitch"],
            ),
            part,
        )
        parts.append(part)
        time.sleep(0.35)

    concat_mp3(parts, out)
    for part in parts:
        part.unlink(missing_ok=True)
    print(
        f"OK  {out.name}  ({len(parts)} segments, {out.stat().st_size} bytes)  "
        f"voice={voice}"
    )


async def generate(
    story_path: Path,
    audio_dir: Path,
    *,
    quiz_only: bool = False,
    skip_existing: bool = False,
    roles: set[str] | None = None,
) -> None:
    data = json.loads(story_path.read_text(encoding="utf-8"))
    jobs = collect_jobs(data, audio_dir, quiz_only)
    if roles:
        jobs = [j for j in jobs if j["role"] in roles]
    written = 0
    minimax_client: PoeClient | None = None
    for job in jobs:
        out = job["out"]
        if skip_existing and out.exists():
            print(f"SKIP  {out.name}")
            continue
        if is_minimax(job["cfg"]):
            if minimax_client is None:
                minimax_client = PoeClient()
            save_minimax(minimax_client, job)
            time.sleep(0.35)
        else:
            cfg = job["cfg"]
            await save_edge(job["text"], out, cfg["voice"], cfg["rate"], cfg["pitch"])
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
    parser.add_argument("--roles", help="Comma-separated roles to generate (e.g. george)")
    args = parser.parse_args()
    role_set = {r.strip() for r in args.roles.split(",") if r.strip()} if args.roles else None
    asyncio.run(
        generate(
            Path(args.story),
            Path(args.out),
            quiz_only=args.quiz_only,
            skip_existing=args.skip_existing,
            roles=role_set,
        )
    )


if __name__ == "__main__":
    main()
