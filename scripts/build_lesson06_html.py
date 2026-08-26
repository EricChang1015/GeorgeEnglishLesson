#!/usr/bin/env python3
"""Assemble lessons/lesson-06.html from tmp/lesson06_window.json."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORY = json.loads((ROOT / "scripts" / "lesson06_story.json").read_text(encoding="utf-8"))
OUT = ROOT / "lessons" / "lesson-06.html"


def audio(name: str) -> str:
    if not name or name.startswith("audio/") or name.startswith("http"):
        return name
    return "audio/" + name


def lesson_payload() -> dict:
    return {
        "asset": "assets/lesson-06/",
        "storageKey": "george-lesson-06-notes-v2",
        "youtubeId": STORY["youtubeId"],
        "roleLabel": {"narrator": "Narrator"},
        "vocab": [
            {
                "word": v["word"],
                "example": v["example"],
                "img": v["img"],
                "alt": v["alt"],
                "audio": audio(v["audio"]),
                "exampleAudio": audio(v["example_audio"]),
            }
            for v in STORY["vocab"]
        ],
        "story": [],
        "songPages": [
            {
                "title": page["title"],
                **({"img": page["img"], "alt": page.get("alt") or ""} if page.get("img") else {}),
                "lines": [{"text": ln["text"], "audio": audio(ln["audio"])} for ln in page["lines"]],
            }
            for page in STORY.get("songPages") or []
        ],
        "quiz": [],
        "phrases": [],
    }

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Lesson 6: George and the Wellerman</title>
  <link rel="stylesheet" href="css/lesson.css" />
  <style>
    body {
      background:
        radial-gradient(circle at 10% 10%, #c9e7ff 0, transparent 40%),
        radial-gradient(circle at 90% 0%, #ffe9b8 0, transparent 35%),
        var(--bg);
    }
    .line.song { background: #e7f6ff; border-color: #9ad0f0; }
    .voice-key .song { background: #e7f6ff; color: #0a5f8a; }
  </style>
</head>
<body>
  <div class="app">
    <header class="top">
      <div class="brand">George English · Lesson 6</div>
      <nav class="nav-links">
        <a href="lesson-05.html">Lesson 5</a>
        <a href="../index.html">All lessons</a>
      </nav>
    </header>
    <div class="progress" aria-hidden="true"><span id="progressBar"></span></div>

    <section class="screen active" data-screen="0">
      <img class="hero hero-full" src="assets/lesson-06/cover.webp" alt="George sings on Billy o' Tea as a whale and the Wellerman appear" />
      <h1>George and the Wellerman</h1>
      <div class="continue">George's Song Adventures · song words · sing along</div>
      <p class="hint">ORT Level 6 · Nathan Evans · Wellerman</p>
      <div class="voice-key">
        <span class="narrator">Word audio</span>
        <span class="song">Song clips</span>
      </div>
      <div class="controls">
        <button class="btn-primary" type="button" data-next>Start ▶</button>
        <button class="btn-secondary" type="button" data-audio="audio/title.mp3">🔊 Title</button>
      </div>
    </section>
"""

MID = """
    <section class="screen" data-screen="1">
      <h2>Song Words</h2>
      <p class="hint">Tap a card: hear the word, then an example from the song</p>
      <div class="vocab-grid" id="vocabGrid"></div>
      <div class="controls">
        <button class="btn-ghost" type="button" data-prev>◀ Back</button>
        <button class="btn-primary" type="button" data-next>Sing ▶</button>
      </div>
    </section>

    <section class="screen" data-screen="2" data-song="0"></section>
    <section class="screen" data-screen="3" data-song="1"></section>
    <section class="screen" data-screen="4" data-song="2"></section>

    <section class="screen" data-screen="5">
      <h2>The whole song</h2>
      <p class="hint">Nathan Evans · Wellerman · needs the internet</p>
      <div class="song-embed" id="songEmbed"></div>
      <p class="hint">If the video does not load, check the internet and try again.</p>
      <div class="controls">
        <button class="btn-ghost" type="button" data-prev>◀ Back</button>
        <a class="btn btn-primary" href="../index.html" style="text-decoration:none;display:inline-block;">Home</a>
      </div>
    </section>
  </div>

  <script>
    window.LESSON = """

TAIL = """
  </script>
  <script src="js/lesson-player.js?v=7"></script>
</body>
</html>
"""


def main() -> None:
    payload = json.dumps(lesson_payload(), ensure_ascii=False, indent=2)
    OUT.write_text(HEAD + MID + payload + ";" + TAIL, encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
