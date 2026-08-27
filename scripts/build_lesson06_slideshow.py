#!/usr/bin/env python3
"""Assemble lessons/lesson-06-slideshow.html from lesson06_lyric_frames.json."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRAMES = json.loads((ROOT / "scripts" / "lesson06_lyric_frames.json").read_text(encoding="utf-8"))
OUT = ROOT / "lessons" / "lesson-06-slideshow.html"


def payload() -> dict:
    return {
        "asset": "assets/lesson-06/",
        "lyricFrames": [
            {
                "index": f["index"],
                "id": f["id"],
                "section": f["section"],
                "text": f["text"],
                "audio": "audio/" + f["audio"],
                "img": f["img"],
                "alt": f["action"],
            }
            for f in FRAMES["frames"]
        ],
    }


HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Lesson 6: Picture song — Wellerman</title>
  <link rel="stylesheet" href="css/lesson.css" />
  <link rel="stylesheet" href="css/wellerman-slideshow.css" />
</head>
<body>
  <div class="app">
    <header class="top">
      <div class="brand">George English · Lesson 6</div>
      <nav class="nav-links">
        <a href="lesson-06.html#words">Song words</a>
        <a href="lesson-06.html#listen">Whole song</a>
        <a href="../index.html">All lessons</a>
      </nav>
    </header>
    <div class="progress" aria-hidden="true"><span id="progressBar"></span></div>

    <div class="slideshow-card">
      <p class="page-meta" id="slideMeta">Line 1 / 24</p>
      <label class="jump-line">Go to
        <select id="slideJump" aria-label="Jump to lyric line"></select>
      </label>
      <figure class="slideshow-figure" id="slideFigure">
        <img class="hero hero-full" id="slideImg" alt="" />
      </figure>
      <p class="lyric-text" id="slideLyric"></p>
      <p class="hint">Swipe the picture · or tap Next · Play from here sings the whole song</p>
      <div class="slideshow-controls">
        <button class="btn-ghost" type="button" id="btnPrev">◀ Prev</button>
        <button class="btn-secondary" type="button" id="btnReplay">🔊</button>
        <button class="btn-primary" type="button" id="btnNext">Next ▶</button>
      </div>
      <div class="slideshow-controls">
        <button class="btn-good" type="button" id="btnAuto">▶ Play from here</button>
        <a class="btn btn-primary" href="lesson-06.html#listen" style="text-decoration:none;display:inline-block;">Whole song ▶</a>
      </div>
    </div>
  </div>

  <script>
    window.LESSON = """

TAIL = """
  </script>
  <script src="js/wellerman-slideshow.js?v=2"></script>
</body>
</html>
"""


def main() -> None:
    body = json.dumps(payload(), ensure_ascii=False, indent=2)
    OUT.write_text(HEAD + body + ";" + TAIL, encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
