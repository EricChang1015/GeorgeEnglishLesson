#!/usr/bin/env python3
"""Trial clips: MiniMax Speech 2.8 via Poe (emotion + voice casting).

Outputs stay under lessons/assets/lesson-03/voice-tests/ (gitignored).
Open http://localhost:3456/lessons/assets/lesson-03/voice-tests/index.html
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from poe_media import PoeClient, UsageRecord, _download_url, _extract_urls, _message_text, log_usage  # noqa: E402

OUT_DIR = ROOT / "lessons" / "assets" / "lesson-03" / "voice-tests"
MODEL = "MiniMax-Speech-2.8"


def extra_body(
    *,
    voice: str,
    emotion: str | None = None,
    speed: float = 1.0,
    volume: float = 1.0,
    pitch: int = 0,
) -> dict:
    body: dict = {
        # Poe / Novita official field is voice_id; `voice` alone often stays on the default adult.
        "voice_id": voice,
        "voice": voice,
        "speed": speed,
        "volume": volume,
        "vol": volume,
        "pitch": pitch,
        "language_boost": "English",
    }
    if emotion:
        body["emotion"] = emotion
    return body


def synthesize(client: PoeClient, text: str, body: dict, out: Path) -> Path:
    payload = {
        "model": MODEL,
        "stream": False,
        "messages": [{"role": "user", "content": text}],
        "extra_body": body,
    }
    _, _, data = client._request("POST", "/chat/completions", json_body=payload, timeout=180)
    if not data:
        raise RuntimeError("Empty MiniMax Speech response")
    choice = (data.get("choices") or [{}])[0]
    message = choice.get("message", {})
    content = _message_text(message.get("content"))
    urls = [u.rstrip(")'\".,") for u in _extract_urls(content) if "poecdn.net" in u or u.lower().endswith((".mp3", ".wav"))]
    if not urls:
        raise RuntimeError(f"No audio URL in MiniMax response: {json.dumps(data)[:900]}")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(_download_url(urls[0]))
    log_usage(UsageRecord("speech", MODEL, f"{body.get('voice')} {body.get('emotion') or 'auto'} {text}", data.get("usage"), out.name))
    print(
        f"OK  {out.name}  ({out.stat().st_size} bytes)  "
        f"voice={body.get('voice')}  emotion={body.get('emotion') or 'auto'}  "
        f"speed={body.get('speed')} pitch={body.get('pitch')}"
    )
    return out


SAMPLES = [
    {
        "file": "01-ember-fearful.mp3",
        "label": "Ember · fearful · PlayfulGirl",
        "text": "George… is that bear dangerous?",
        "voice": "English_PlayfulGirl",
        "emotion": "fearful",
        "speed": 0.92,
    },
    {
        "file": "02-ember-happy.mp3",
        "label": "Ember · happy (same line, contrast)",
        "text": "George… is that bear dangerous?",
        "voice": "English_PlayfulGirl",
        "emotion": "happy",
        "speed": 1.05,
    },
    {
        "file": "03-george-calm-firm.mp3",
        "label": "George · calm · Strong-WilledBoy",
        "text": "Yes. Stay quiet. Don't run. That is very important.",
        "voice": "English_Strong-WilledBoy",
        "emotion": "calm",
        "speed": 0.9,
    },
    {
        "file": "04-pip-surprised.mp3",
        "label": "Pip · surprised · WhimsicalGirl",
        "text": "Now! Walk carefully. The cave is close. It is our shelter!",
        "voice": "English_WhimsicalGirl",
        "emotion": "surprised",
        "speed": 1.15,
    },
    {
        "file": "05-narrator-fearful.mp3",
        "label": "Narrator · fearful · CaptivatingStoryteller",
        "text": "Suddenly, George stopped. A huge brown bear was on the path ahead.",
        "voice": "English_CaptivatingStoryteller",
        "emotion": "fearful",
        "speed": 0.88,
    },
    {
        "file": "06-george-happy.mp3",
        "label": "George · happy · Strong-WilledBoy",
        "text": "We did it together. We stayed calm!",
        "voice": "English_Strong-WilledBoy",
        "emotion": "happy",
        "speed": 1.12,
    },
    {
        "file": "07-daddy-calm.mp3",
        "label": "Daddy · calm · Gentle-voiced man",
        "text": "Well done. You were very brave today.",
        "voice": "English_Gentle-voiced_man",
        "emotion": "calm",
        "speed": 0.95,
    },
    {
        "file": "08-narrator-auto.mp3",
        "label": "Narrator · auto emotion · Expressive Narrator",
        "text": "Far away, thunder rumbled like a giant drum.",
        "voice": "English_expressive_narrator",
        "emotion": None,
        "speed": 0.9,
    },
]


def write_index(rows: list[dict]) -> Path:
    items = []
    for row in rows:
        items.append(
            f"""<section>
  <h2>{row['label']}</h2>
  <p class="meta">{row['voice']} · emotion={row.get('emotion') or 'auto'} · speed={row['speed']}</p>
  <p class="line">“{row['text']}”</p>
  <audio controls src="{row['file']}"></audio>
</section>"""
        )
    html = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>MiniMax Speech 2.8 試聽 · Lesson 3</title>
  <style>
    body {{ font-family: Georgia, serif; max-width: 40rem; margin: 2rem auto; padding: 0 1rem; background: #f6f1e6; color: #222; }}
    h1 {{ font-size: 1.35rem; }}
    section {{ background: #fff; border-radius: 12px; padding: 1rem 1.1rem; margin: 1rem 0; box-shadow: 0 1px 4px #0001; }}
    h2 {{ font-size: 1.05rem; margin: 0 0 .35rem; }}
    .meta {{ color: #666; font-size: .85rem; margin: 0 0 .4rem; }}
    .line {{ margin: 0 0 .7rem; }}
    audio {{ width: 100%; }}
  </style>
</head>
<body>
  <h1>MiniMax Speech 2.8 試聽（未發佈）</h1>
  <p>同一句「George… is that bear dangerous?」有 fearful / happy 對照。其餘為 Lesson 3 需要情緒的句子。</p>
  {"".join(items)}
</body>
</html>
"""
    path = OUT_DIR / "index.html"
    path.write_text(html, encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", help="Generate only this output filename")
    args = parser.parse_args()
    client = PoeClient()
    rows = [r for r in SAMPLES if not args.only or r["file"] == args.only]
    if not rows:
        print("No matching sample")
        return 1
    for i, row in enumerate(rows):
        if i:
            time.sleep(0.4)
        synthesize(
            client,
            row["text"],
            extra_body(voice=row["voice"], emotion=row["emotion"], speed=row["speed"]),
            OUT_DIR / row["file"],
        )
    write_index(SAMPLES)
    print(f"\nListen: http://localhost:3456/lessons/assets/lesson-03/voice-tests/index.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
