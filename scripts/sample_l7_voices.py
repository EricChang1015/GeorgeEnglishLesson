#!/usr/bin/env python3
"""Lesson 7 voice audition: Sylvia + Horn / Beak / Goat.

Outputs stay under lessons/assets/lesson-07/voice-tests/ (gitignored).
Open lessons/l7-voice-picker.html via the local server.
"""

from __future__ import annotations

import argparse
import asyncio
import sys
import time
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

OUT = ROOT / "lessons" / "assets" / "lesson-07" / "voice-tests"

LINES = {
    "sylvia": "George, stop chasing me with that silly wooden fork!",
    "horn": "Who dares land on our island with small blue shoes?",
    "beak": "Look at those teeth on his hood! Show your claws!",
    "goat": "Kings can leave whenever their hearts pull homeward.",
}

# (letter, slug, engine, voice, rate_or_speed, pitch, extra)
# Edge: rate like "+8%", pitch like "-25Hz"
# MiniMax: speed float, pitch int -12..12
CANDIDATES = {
    "sylvia": [
        ("A", "now-libby", "edge", "en-GB-LibbyNeural", "+8%", "+8Hz", "現在課裡這把"),
        ("B", "libby-natural", "edge", "en-GB-LibbyNeural", "+0%", "+0Hz", "Libby 原速，少一點童聲"),
        ("C", "clara", "edge", "en-CA-ClaraNeural", "+5%", "+5Hz", "加拿大女孩，溫暖清楚"),
        ("D", "emma", "edge", "en-US-EmmaNeural", "+8%", "+5Hz", "美國少年女聲"),
        ("E", "molly", "edge", "en-NZ-MollyNeural", "+8%", "+8Hz", "紐西蘭女孩，偏亮"),
        ("F", "kind-girl", "minimax", "English_Kind-heartedGirl", 1.05, 2, "MiniMax 好心姐姐"),
    ],
    "horn": [
        ("A", "now-thomas", "edge", "en-GB-ThomasNeural", "+0%", "-8Hz", "現在課裡這把（偏男童）"),
        ("B", "guy-deep", "edge", "en-US-GuyNeural", "-18%", "-28Hz", "Guy 壓低：粗糙低沉"),
        ("C", "eric-xdeep", "edge", "en-US-EricNeural", "-22%", "-35Hz", "Eric 極低：最沉的一把"),
        ("D", "christopher", "edge", "en-US-ChristopherNeural", "-15%", "-22Hz", "Christopher 低沉大人"),
        ("E", "deep-man", "minimax", "English_ManWithDeepVoice", 0.82, -6, "MiniMax 深男聲，較有 rumble"),
        ("F", "magnetic", "minimax", "English_magnetic_voiced_man", 0.84, -5, "MiniMax 磁性男聲"),
    ],
    "beak": [
        ("A", "now-jenny", "edge", "en-US-JennyNeural", "+12%", "+10Hz", "現在課裡這把（偏亮、不糙）"),
        ("B", "jenny-sharp", "edge", "en-US-JennyNeural", "+20%", "+28Hz", "Jenny 再拉高：尖、快"),
        ("C", "michelle", "edge", "en-US-MichelleNeural", "+16%", "+22Hz", "Michelle 高亢"),
        ("D", "clara-high", "edge", "en-CA-ClaraNeural", "+18%", "+24Hz", "Clara 高而利"),
        ("E", "upset-girl", "minimax", "English_UpsetGirl", 1.18, 5, "MiniMax 急躁高女聲"),
        ("F", "comedian", "minimax", "English_Comedian", 1.16, 4, "MiniMax 喜劇高亢，較糙"),
    ],
    "goat": [
        ("A", "now-natasha", "edge", "en-AU-NatashaNeural", "-5%", "+5Hz", "現在課裡這把（溫柔、不糙）"),
        ("B", "steffan", "edge", "en-US-SteffanNeural", "-12%", "-14Hz", "Steffan 低沉男聲"),
        ("C", "william", "edge", "en-AU-WilliamMultilingualNeural", "-12%", "-12Hz", "澳洲男聲，比 Natasha 粗"),
        ("D", "roger", "edge", "en-US-RogerNeural", "-10%", "-16Hz", "Roger 低、穩"),
        ("E", "aussie", "minimax", "English_Aussie_Bloke", 0.90, -3, "MiniMax 澳洲大叔，偏低糙"),
        ("F", "trust", "minimax", "English_Trustworth_Man", 0.88, -4, "MiniMax 沉穩男聲"),
    ],
}


def filename(role: str, letter: str, slug: str) -> str:
    return f"{role}-{letter}-{slug}.mp3"


async def save_edge(text: str, voice: str, rate: str, pitch: str, path: Path) -> None:
    last_err: Exception | None = None
    for attempt in range(3):
        try:
            await edge_tts.Communicate(text, voice=voice, rate=rate, pitch=pitch).save(str(path))
            print(f"OK  {path.name}  edge {voice} {rate} {pitch}")
            return
        except Exception as err:
            last_err = err
            print(f"RETRY {path.name} ({attempt + 1}/3): {err}")
            await asyncio.sleep(1.2)
    raise RuntimeError(f"edge failed for {path.name}: {last_err}") from last_err


def save_minimax(client, text: str, voice: str, speed: float, pitch: int, path: Path, emotion: str) -> None:
    from sample_minimax_speech import extra_body, synthesize

    synthesize(
        client,
        text,
        extra_body(voice=voice, emotion=emotion, speed=speed, pitch=pitch),
        path,
    )


def generate_minimax(rows: list[tuple]) -> None:
    from poe_media import PoeClient

    client = PoeClient()
    emotions = {"sylvia": "happy", "horn": "angry", "beak": "angry", "goat": "calm"}
    for i, (role, letter, slug, voice, speed, pitch) in enumerate(rows):
        if i:
            time.sleep(0.4)
        path = OUT / filename(role, letter, slug)
        if path.exists() and path.stat().st_size > 0:
            print(f"SKIP {path.name}")
            continue
        save_minimax(client, LINES[role], voice, float(speed), int(pitch), path, emotions[role])


async def generate_edge(rows: list[tuple]) -> None:
    for role, letter, slug, voice, rate, pitch in rows:
        path = OUT / filename(role, letter, slug)
        if path.exists() and path.stat().st_size > 0:
            print(f"SKIP {path.name}")
            continue
        await save_edge(LINES[role], voice, str(rate), str(pitch), path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--edge-only", action="store_true")
    parser.add_argument("--minimax-only", action="store_true")
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)

    edge_rows = []
    mini_rows = []
    for role, opts in CANDIDATES.items():
        for letter, slug, engine, voice, a, b, _label in opts:
            if engine == "edge":
                edge_rows.append((role, letter, slug, voice, a, b))
            else:
                mini_rows.append((role, letter, slug, voice, a, b))

    if not args.minimax_only:
        asyncio.run(generate_edge(edge_rows))
    if not args.edge_only:
        generate_minimax(mini_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
