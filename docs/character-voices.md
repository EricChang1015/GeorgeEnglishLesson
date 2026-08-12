# Character AI voices

Canonical voice settings for George English Lessons. **Keep every returning character identical** across lessons so George, Pip, Ember, and family sound the same every time.

- **Machine-readable source:** `scripts/voices.json`
- **Agent rule:** `.cursor/rules/character-voices.mdc`
- **Per-lesson copy:** each `scripts/lessonXX_story.json` has a `"voices"` block — must match this doc when a role appears

Engine: [Microsoft Edge TTS](https://github.com/rany2/edge-tts) via `edge-tts` (Python).

---

## Established roles

| Role key | Character | Voice | Rate | Pitch | Sound |
|----------|-----------|-------|------|-------|-------|
| `narrator` | Narrator | `en-GB-SoniaNeural` | `-10%` | `+0Hz` | Calm British adult; reads story + vocab words |
| `george` | George (~5) | `en-US-AnaNeural` | `+12%` | `-10Hz` | Child boy (parent-approved picker **E**) |
| `pip` | Pip (green dragon) | `en-US-AnaNeural` | `+5%` | `+20Hz` | Young dragon; brighter/higher than George |
| `ember` | Ember (red dragon) | `en-GB-MaisieNeural` | `+8%` | `+15Hz` | Baby sister dragon; soft British child |
| `daddy` | Daddy | `en-GB-RyanNeural` | `-5%` | `-5Hz` | Warm British adult male |

### Distinguishing similar voices

George and Pip both use `en-US-AnaNeural` but **different rate/pitch** — always keep both settings exact so listeners can tell them apart.

---

## Reserved (not yet cast)

| Role key | Character | Status |
|----------|-----------|--------|
| `mummy` | Mummy | TBD — choose a warm adult female; must not sound like the narrator |
| `sylvia` | Sylvia (older sister) | TBD — child/teen girl; must differ from George, Pip, and Ember |

When a new family member speaks for the first time: agree voice with parent → add to `scripts/voices.json` → update this table → copy into the lesson story JSON.

---

## New lesson checklist

1. Open `scripts/voices.json`.
2. For every speaking role in the story, copy that role's `{ "voice", "rate", "pitch" }` into `scripts/lessonXX_story.json` → `"voices"`.
3. Generate audio:

   ```bash
   python scripts/generate_lesson_audio.py --story scripts/lessonXX_story.json --out lessons/assets/lesson-XX/audio
   ```

4. In lesson HTML, keep the **voice-key** legend colours aligned with roles (George = blue, Pip = green, Ember = red, Daddy = purple, narrator = gold, etc.).
5. Vocab: each word should have an `example` sentence + `example_audio`; the lesson page plays **word → sentence**.

---

## Changing a voice

1. Generate samples (see `scripts/sample_boy_voice.py` or a new sample script).
2. Parent picks a option.
3. Update `scripts/voices.json`, this doc, `.cursor/rules/character-voices.mdc`, and **regenerate all lessons** where that character speaks.

---

## Lesson usage so far

| Lesson | Roles with dialogue |
|--------|---------------------|
| 1 | narrator, george, pip |
| 2 | narrator, george, pip, ember |
| 3 | narrator, george, pip, ember, daddy |
