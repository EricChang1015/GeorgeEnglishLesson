#!/usr/bin/env python3
"""Generate lessons/lesson-04.html from scripts/lesson04_story.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
d = json.loads((ROOT / "scripts/lesson04_story.json").read_text(encoding="utf-8"))

phrase_map = {
    "Hold my hand": "p10-03.mp3",
    "Stay close to me": "p05-04.mp3",
    "You are home now": "p11-03.mp3",
    "One step at a time": "p09-03.mp3",
    "I heard a strange sound": "p03-03.mp3",
    "We can be brave together": "p10-03.mp3",
}

vocab_js = []
for v in d["vocab"]:
    vocab_js.append(
        f'        {{ word: {json.dumps(v["word"])}, example: {json.dumps(v["example"])}, '
        f'img: {json.dumps(v["img"])}, alt: {json.dumps(v["alt"])}, '
        f'audio: "audio/{v["audio"]}", exampleAudio: "audio/{v["example_audio"]}" }},'
    )

story_js = []
for page in d["pages"]:
    lines = []
    for ln in page["lines"]:
        text = ln["text"].replace("…", "...")
        lines.append(
            f'            {{ role: {json.dumps(ln["role"])}, text: {json.dumps(text)}, audio: "audio/{ln["audio"]}" }},'
        )
    story_js.append(
        "        {\n"
        f'          img: {json.dumps(page["img"])},\n'
        f'          alt: {json.dumps(page["alt"])},\n'
        "          lines: [\n"
        + "\n".join(lines)
        + "\n          ]\n        },"
    )

quiz_js = []
for q in d["quiz"]:
    opts = ", ".join(json.dumps(o) for o in q["options"])
    quiz_js.append(
        f'        {{ q: {json.dumps(q["q"])}, options: [{opts}], answer: {q["answer"]} }},'
    )

phrase_js = []
for p in d["phrases"]:
    phrase_js.append(
        f'        {{ text: {json.dumps(p)}, audio: "audio/{phrase_map[p]}" }},'
    )

story_screens = "\n".join(
    f'    <section class="screen" data-screen="{i + 2}" data-story="{i}"></section>'
    for i in range(len(d["pages"]))
)
quiz_screen = len(d["pages"]) + 2
phrases_screen = quiz_screen + 1
notes_screen = phrases_screen + 1

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Lesson 4: George and the Dinosaur Under the Blanket</title>
  <link rel="stylesheet" href="css/lesson.css" />
  <style>
    body {{
      background:
        radial-gradient(circle at 10% 10%, #e8e0ff 0, transparent 40%),
        radial-gradient(circle at 90% 0%, #d4f0e8 0, transparent 35%),
        var(--bg);
    }}
  </style>
</head>
<body>
  <div class="app">
    <header class="top">
      <div class="brand">🐉 George English · Lesson 4</div>
      <nav class="nav-links">
        <a href="lesson-03.html">Lesson 3</a>
        <a href="../index.html">All lessons</a>
      </nav>
    </header>
    <div class="progress" aria-hidden="true"><span id="progressBar"></span></div>

    <section class="screen active" data-screen="0">
      <img class="hero hero-full" src="assets/lesson-04/cover.webp" alt="George smiles in bed holding a small Mike plush" />
      <h1>George and the Dinosaur Under the Blanket</h1>
      <div class="continue">Mike Dreams · George · Mike · Nibble · Daddy</div>
      <p class="hint">ORT Level 6 · Bedtime · Blanket hill · Brave whisper</p>
      <div class="voice-key">
        <span class="narrator">Narrator</span>
        <span class="george">George (boy)</span>
        <span class="mike">Mike</span>
        <span class="nibble">Nibble</span>
        <span class="daddy">Daddy</span>
      </div>
      <div class="controls">
        <button class="btn-primary" type="button" data-next>Start ▶</button>
        <button class="btn-secondary" type="button" data-audio="audio/title.mp3">🔊 Title</button>
      </div>
    </section>

    <section class="screen" data-screen="1">
      <h2>New Words</h2>
      <p class="hint">Tap a card: hear the word, then an example sentence</p>
      <div class="vocab-grid" id="vocabGrid"></div>
      <div class="controls">
        <button class="btn-ghost" type="button" data-prev>◀ Back</button>
        <button class="btn-primary" type="button" data-next>Story ▶</button>
      </div>
    </section>

{story_screens}

    <section class="screen" data-screen="{quiz_screen}">
      <h2>Let's Check!</h2>
      <p class="hint">5 questions this time · Listen, then choose A, B or C</p>
      <div id="quizArea"></div>
      <div class="controls">
        <button class="btn-ghost" type="button" data-prev>◀ Back</button>
        <button class="btn-primary" type="button" data-next id="quizNext" disabled>Next ▶</button>
      </div>
    </section>

    <section class="screen" data-screen="{phrases_screen}">
      <h2>Key Phrases</h2>
      <p class="hint">Tap each phrase and say it with George &amp; Mike</p>
      <div class="sight-grid" id="sightGrid"></div>
      <p class="feedback" id="sightFeedback"></p>
      <div class="controls">
        <button class="btn-ghost" type="button" data-prev>◀ Back</button>
        <button class="btn-primary" type="button" data-next>Notes ▶</button>
      </div>
    </section>

    <section class="screen" data-screen="{notes_screen}">
      <h2>Follow-up Notes</h2>
      <p class="hint">For tutor / parent (saved on this device)</p>
      <div class="learning-box">
        <strong>Learning focus</strong>
        <ul>
          <li>Word → sentence practice (e.g. blanket → Something moved under the blanket.)</li>
          <li>Observation: footprint · tiny footprints · I can see</li>
          <li>Ask: What was under the blanket? (Nibble, not a monster)</li>
          <li>Ask: What proof was left in the morning? (a tiny fern leaf, like Nibble's nest)</li>
        </ul>
      </div>
      <div class="notes" id="notesForm">
        <label><input type="checkbox" data-note="read_aloud" /> Tried reading aloud</label>
        <label><input type="checkbox" data-note="used_ai_audio" /> Used AI line audio / Read page</label>
        <label><input type="checkbox" data-note="vocab_sentence" /> Echoed vocab example sentences</label>
        <label><input type="checkbox" data-note="bedtime_phrases" /> Practised key phrases (Hold my hand / Stay close to me)</label>
        <label><input type="checkbox" data-note="mystery_talk" /> Talked about the mysterious adventure</label>
        <label><input type="checkbox" data-note="followed_dialogue" /> Followed the dialogue well</label>
        <label><input type="checkbox" data-note="quiz_ok" /> Got quiz answers right</label>
        <label><input type="checkbox" data-note="needs_review" /> Needs review next time</label>
        <p style="margin:14px 0 6px;font-weight:800;">Comments</p>
        <textarea id="noteComment" placeholder="What went well? What to practice next?"></textarea>
        <div class="controls" style="margin-top:14px;">
          <button class="btn-good" type="button" id="saveNotes">💾 Save notes</button>
          <button class="btn-secondary" type="button" id="clearNotes">Clear</button>
          <a class="btn btn-primary" href="../index.html" style="text-decoration:none;display:inline-block;">Home</a>
        </div>
        <p class="save-msg" id="saveMsg"></p>
      </div>
      <footer class="note">Sweet dreams, George! 🌙</footer>
    </section>
  </div>

  <script>
    window.LESSON = {{
      asset: "assets/lesson-04/",
      storageKey: "george-lesson-04-notes-v1",
      videoDir: "video/",
      videoPages: [],
      roleLabel: {{ narrator: "Narrator", george: "George", mike: "Mike", nibble: "Nibble", daddy: "Daddy" }},
      vocab: [
{chr(10).join(vocab_js)}
      ],
      story: [
{chr(10).join(story_js)}
      ],
      quizPick: 5,
      quiz: [
{chr(10).join(quiz_js)}
      ],
      phrases: [
{chr(10).join(phrase_js)}
      ]
    }};
  </script>
  <script src="js/lesson-player.js?v=4"></script>
</body>
</html>
"""

out = ROOT / "lessons" / "lesson-04.html"
out.write_text(html, encoding="utf-8")
print(f"Wrote {out}")
print(f"screens: cover + vocab + {len(d['pages'])} story + quiz + phrases + notes")
