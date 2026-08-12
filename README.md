# George English Lessons

Interactive HTML reading lessons for George (born 2021-06-23), targeting Oxford Reading Tree Level 6.

## Lessons

### Lesson 1 — `lessons/lesson-01.html`
**George and the Little Dragon** (ORT Level 6): George meets Pip and finds a red egg.

### Lesson 2 — `lessons/lesson-02.html`
**The Red Egg Hatches** (ORT Level 6): Ember hatches; George helps; Ember flies a little.

### Lesson 3 — `lessons/lesson-03.html`
**George and the Storm on the Hill** (ORT Level 6): berry path, storm, bear, cave shelter; Daddy climbs up. Safety phrases + Daddy voice.

Features: vocabulary (word + example sentence), dialogue story, AI line audio, quiz, key phrases, tutor notes.

## Character AI voices

Each story character has a fixed Edge TTS voice (George, Pip, Ember, Daddy, narrator, …).  
**Do not change per lesson** — copy from the canonical file when writing a new lesson.

| Doc | Purpose |
|-----|---------|
| `scripts/voices.json` | Machine-readable voice settings per role |
| `docs/character-voices.md` | Full table, checklist, reserved roles |
| `.cursor/rules/character-voices.mdc` | Agent rule for consistent casting |

Regenerate audio after story edits:

```bash
python scripts/generate_lesson_audio.py --story scripts/lesson01_story.json --out lessons/assets/lesson-01/audio
python scripts/generate_lesson_audio.py --story scripts/lesson02_story.json --out lessons/assets/lesson-02/audio
python scripts/generate_lesson_audio.py --story scripts/lesson03_story.json --out lessons/assets/lesson-03/audio
```

Vocab entries may include `example` + `example_audio`; the generator speaks the word, then the example sentence (narrator voice).

## Character reference photos (private)

Likeness refs for consistent lesson art live locally at:

`lessons/assets/refs/george/`

- Tag index: `lessons/assets/refs/george/CATALOG.md`
- Agent rule: `.cursor/rules/character-refs.mdc`
- Cast ids: `george`, `daddy`, `mummy`, `sylvia`
- Naming: `{subjects}-{setting}-{pose-or-mood}.jpg` (George first)
- Default George face: `george-solo-bed-smile.jpg`
- Cover / close face: `george-solo-sofa-alphabet-smile.jpg`
- Daddy face: `george-daddy-outdoors-pavilion-neutral.jpg`

Photos are gitignored (only `*.md` catalogs are committed). Put new photos **directly** into `lessons/assets/refs/george/` and update `CATALOG.md`. Do not use `ref/` for new drops. Never publish private photos into lesson HTML.

## Local preview

Open `index.html` in a browser, or serve the folder:

```bash
npx --yes serve .
```

## Live site

https://ericchang1015.github.io/GeorgeEnglishLesson/

- Lesson 1: https://ericchang1015.github.io/GeorgeEnglishLesson/lessons/lesson-01.html
- Lesson 2: https://ericchang1015.github.io/GeorgeEnglishLesson/lessons/lesson-02.html
- Lesson 3: https://ericchang1015.github.io/GeorgeEnglishLesson/lessons/lesson-03.html
- Repo: https://github.com/EricChang1015/GeorgeEnglishLesson

## Publish (GitHub Pages)

Push to `main`. Site root is the repository root.

When updating a lesson before class: edit → commit → push. The Pages URL stays the same; the tutor only needs to refresh.
