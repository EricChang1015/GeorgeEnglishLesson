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
| `george` | George (~5) | MiniMax `cute_boy` (L3+) / Edge Ana (L1–2) | `1.30` / `+12%` | `0` / `-10Hz` | L3 lock **F2** · baseline **1.30×** (2026-08-21) |
| `pip` | Pip (green dragon) | `en-US-AnaNeural` | `+5%` | `+20Hz` | Young dragon; brighter/higher than George |
| `ember` | Ember (red dragon) | `en-GB-MaisieNeural` | `+8%` | `+15Hz` | Baby sister dragon; soft British child |
| `daddy` | Daddy | `en-GB-RyanNeural` | `-5%` | `-5Hz` | Warm British adult male |
| `mike` | Mike (plush) | `en-US-AnaNeural` | `+5%` | `+20Hz` | Same lock as Pip (different chapter) |
| `nibble` | Nibble (baby dino) | `en-GB-MaisieNeural` | `+12%` | `+8Hz` | Soft peep-like baby dinosaur |
| `jojo` | Jojo (caving coach) | `en-US-AvaNeural` | `-8%` | `+5Hz` | Young warm female coach; parent pick 2026-08-26 (audition E) |
| `mummy` | Mummy | `en-US-AriaNeural` | `+5%` | `+5Hz` | Warm adult female; parent pick 2026-08-26 (audition B) |
| `sylvia` | Sylvia (sister) | MiniMax `English_Kind-heartedGirl` | `1.05` | `+2` | Older sister; parent pick 2026-09-02 (audition F) |
| `horn` | Horn | MiniMax `English_ManWithDeepVoice` | `0.82` | `-6` | Rough, extremely deep; parent pick 2026-09-02 (E) |
| `beak` | Beak | MiniMax `English_Comedian` | `1.16` | `+4` | Rough, high; parent pick 2026-09-02 (F) |
| `goat` | Goat | `en-US-SteffanNeural` | `-12%` | `-14Hz` | Rough, low, gentler than Horn; parent pick 2026-09-02 (B) |

### Distinguishing similar voices

George and Pip (and Mike) use `en-US-AnaNeural` — George keeps his own settings; **Pip and Mike share the same rate/pitch** (`+5%` / `+20Hz`). Distinguish them by story context and per-line `emotion`, not a different voice lock.

| Role | Rate | Pitch |
|------|------|-------|
| George (Edge fallback) | `+12%` | `-10Hz` |
| Pip | `+5%` | `+20Hz` |
| Mike | `+5%` | `+20Hz` |

Ember and Nibble both use `en-GB-MaisieNeural` but **different rate/pitch**:

| Role | Rate | Pitch |
|------|------|-------|
| Ember | `+8%` | `+15Hz` |
| Nibble | `+12%` | `+8Hz` |

---

## Reserved (not yet cast)

None. Sylvia / Horn / Beak / Goat parent-locked 2026-09-02.

When a new family member speaks for the first time: agree voice with parent → add to `scripts/voices.json` → update this table → copy into the lesson story JSON.

---

## New lesson checklist

1. Open `scripts/voices.json`.
2. For every speaking role in the story, copy that role's `{ "voice", "rate", "pitch" }` into `scripts/lessonXX_story.json` → `"voices"`.
3. Generate audio:

   ```bash
   python scripts/generate_lesson_audio.py --story scripts/lessonXX_story.json --out lessons/assets/lesson-XX/audio
   ```

   Quiz question/option audio is included; use `--quiz-only` to regenerate just those MP3s.

4. In lesson HTML, keep the **voice-key** legend colours aligned with roles (George = blue, Pip = green, Ember = red, Daddy = purple, narrator = gold, etc.).
5. Vocab: each word should have an `example` sentence + `example_audio`; the lesson page plays **word → sentence**.

---

## Line emotion (not yet in the generator)

Parent review (Lessons 1–3): role voices are stable, but **speed / tone / feeling often miss the beat**. Picture-book lines need a clear emotion.

- Plan: add per-line `emotion` in each `scripts/lessonXX_story.json` (`wonder`, `worried`, `whisper`, `happy`, …).
- **Lesson 3 George:** MiniMax `cute_boy` F2 · baseline speed **1.30×** + optional per-line `delivery`. Use **`delivery.segments`** for clause-level speed (intonation); keep **pitch at ±1–2** only. Whisper/tense = fearful + slightly lower volume, not deep pitch.
- **Lesson 4 George:** same MiniMax `cute_boy` F2 lock, baseline speed **1.50×** in `scripts/lesson04_story.json` (L3 stays 1.30×). The generator scales per-line delivery speed from this baseline.
- Edge TTS has no usable custom `express-as` SSML.

Full notes: `docs/lesson-01-03-review.md`.

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
| 4 | narrator, george, daddy, mike, nibble |
| 5 | narrator, george, jojo, mummy, daddy |
| 6 | narrator, george, daddy |
| 7 | narrator, george, mummy, daddy, sylvia, horn, beak, goat |
