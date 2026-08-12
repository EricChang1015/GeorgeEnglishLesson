# George English Lessons

Interactive HTML reading lessons for George (born 2021-06-23), targeting Oxford Reading Tree Stage 2–3.

## Lesson 1

### Lesson 1 — `lessons/lesson-01.html`
**George and the Little Dragon** (ORT Level 6): George meets Pip and finds a red egg.

### Lesson 2 — `lessons/lesson-02.html`
**The Red Egg Hatches** (ORT Level 6): Ember hatches; George helps; Ember flies a little.  
George uses a boy-like AI voice (`en-CA-LiamNeural`, raised pitch).

Features: vocabulary, dialogue story, AI line audio, quiz, key phrases, tutor notes.

Regenerate audio after story edits:

```bash
python scripts/generate_lesson_audio.py --story scripts/lesson01_story.json --out lessons/assets/lesson-01/audio
python scripts/generate_lesson_audio.py --story scripts/lesson02_story.json --out lessons/assets/lesson-02/audio
```

## Character reference photos (private)

Likeness refs for consistent lesson art live locally at:

`lessons/assets/refs/george/`

- Tag index: `lessons/assets/refs/george/CATALOG.md`
- Agent rule: `.cursor/rules/character-refs.mdc`
- Cast ids: `george`, `daddy`, `mummy`, `sylvia`
- Naming: `{subjects}-{setting}-{pose-or-mood}.jpg` (George first)
- Default George face: `george-solo-bed-smile.jpg`

Photos are gitignored (only `*.md` catalogs are committed). Drop new raw photos in `ref/`, then rename into the catalog folder and update `CATALOG.md`. Never publish private photos into lesson HTML.

## Local preview

Open `index.html` in a browser, or serve the folder:

```bash
npx --yes serve .
```

## Live site

https://ericchang1015.github.io/GeorgeEnglishLesson/

- Lesson 1: https://ericchang1015.github.io/GeorgeEnglishLesson/lessons/lesson-01.html
- Lesson 2: https://ericchang1015.github.io/GeorgeEnglishLesson/lessons/lesson-02.html
- Repo: https://github.com/EricChang1015/GeorgeEnglishLesson

## Publish (GitHub Pages)

Push to `main`. Site root is the repository root.

When updating a lesson before class: edit → commit → push. The Pages URL stays the same; the tutor only needs to refresh.
