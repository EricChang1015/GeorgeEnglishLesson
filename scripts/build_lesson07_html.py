#!/usr/bin/env python3
"""Generate lessons/lesson-07.html from scripts/lesson07_story.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
d = json.loads((ROOT / "scripts/lesson07_story.json").read_text(encoding="utf-8"))
learn = d.get("learning") or {}

phrase_map = {
    "Look into my eyes": "p09-01.mp3",
    "wild thing": "p02-01.mp3",
    "First royal rule": "p14-01.mp3",
    "I choose home": "p17-01.mp3",
    "still hot": "p19-02.mp3",
    "friendly bow": "p14-02.mp3",
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

focus_items = "\n".join(f"          <li>{item}</li>" for item in learn.get("focus_en", []))
tutor_items = "\n".join(f"          <li>{item}</li>" for item in learn.get("tutor_prompts_zh", []))

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
  <title>Lesson 7: George's Wild Parade</title>
  <link rel="stylesheet" href="css/lesson.css" />
  <style>
    body {{
      background:
        radial-gradient(circle at 10% 10%, #f3e6c8 0, transparent 40%),
        radial-gradient(circle at 90% 0%, #d8e8c8 0, transparent 35%),
        var(--bg);
    }}
    .voice-key .mummy {{ background: #ffe8f0; color: #c92a6a; }}
    .voice-key .sylvia {{ background: #e8f6e4; color: #2b7a2b; }}
    .voice-key .horn {{ background: #efe4d4; color: #7a4a12; }}
    .voice-key .beak {{ background: #fff3d6; color: #b36b00; }}
    .voice-key .goat {{ background: #ececec; color: #4a4a4a; }}
    .line.mummy {{ background: #ffe8f0; border-color: #ffb3d1; }}
    .line.sylvia {{ background: #e8f6e4; border-color: #b6e6b8; }}
    .line.horn {{ background: #efe4d4; border-color: #e0c4a0; }}
    .line.beak {{ background: #fff3d6; border-color: #ffd48a; }}
    .line.goat {{ background: #ececec; border-color: #c8c8c8; }}
  </style>
</head>
<body>
  <div class="app">
    <header class="top">
      <div class="brand">🐉 George English · Lesson 7</div>
      <nav class="nav-links">
        <a href="lesson-06.html">Lesson 6</a>
        <a href="../index.html">All lessons</a>
      </nav>
    </header>
    <div class="progress" aria-hidden="true"><span id="progressBar"></span></div>

    <section class="screen active" data-screen="0">
      <img class="hero hero-full" src="assets/lesson-07/cover.webp" alt="George in a T-rex onesie with a vine crown stands before three huge wild things" />
      <h1>George and the Wild Parade</h1>
      <div class="continue">George and the Wild Things · George · Sylvia · Horn · Beak · Goat</div>
      <p class="hint">ORT Level 6 · Living room · Jungle room · Wild parade</p>
      <div class="voice-key">
        <span class="narrator">Narrator</span>
        <span class="george">George (boy)</span>
        <span class="mummy">Mummy</span>
        <span class="sylvia">Sylvia</span>
        <span class="daddy">Daddy</span>
        <span class="horn">Horn</span>
        <span class="beak">Beak</span>
        <span class="goat">Goat</span>
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
      <p class="hint">Tap each phrase and say it with George</p>
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
        <p>{learn.get("summary_zh", "")}</p>
        <ul>
{focus_items}
        </ul>
        <strong>Tutor prompts</strong>
        <ul>
{tutor_items}
        </ul>
      </div>
      <div class="notes" id="notesForm">
        <label><input type="checkbox" data-note="read_aloud" /> Tried reading aloud</label>
        <label><input type="checkbox" data-note="used_ai_audio" /> Used AI line audio / Read page</label>
        <label><input type="checkbox" data-note="vocab_sentence" /> Echoed vocab example sentences</label>
        <label><input type="checkbox" data-note="wild_phrases" /> Practised key phrases (I am not afraid / Kings can leave)</label>
        <label><input type="checkbox" data-note="story_talk" /> Talked about the wild parade</label>
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
      <footer class="note">Welcome home, wild thing! 👑</footer>
    </section>
  </div>

  <script>
    window.LESSON = {{
      asset: "assets/lesson-07/",
      storageKey: "george-lesson-07-notes-v1",
      videoDir: "video/",
      videoPages: [],
      roleLabel: {{ narrator: "Narrator", george: "George", mummy: "Mummy", sylvia: "Sylvia", daddy: "Daddy", horn: "Horn", beak: "Beak", goat: "Goat" }},
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

out = ROOT / "lessons" / "lesson-07.html"
out.write_text(html, encoding="utf-8")
print(f"Wrote {out}")
print(f"screens: cover + vocab + {len(d['pages'])} story + quiz + phrases + notes")
