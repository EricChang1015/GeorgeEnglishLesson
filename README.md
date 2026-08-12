# George English Lessons

Interactive HTML reading lessons for George (born 2021-06-23), targeting Oxford Reading Tree Stage 2–3.

## Lesson 1

**Ben and the Little Dragon** — `lessons/lesson-01.html` (ORT Level 6)

- Vocabulary with pictures + AI voice
- Dialogue-rich picture story (Narrator / Ben / Pip)
- Pre-generated neural TTS MP3s (edge-tts); tap a line or “Read page”
- Comprehension quiz with instant feedback
- Key-phrase practice
- Tutor / parent follow-up notes (`localStorage`)

Regenerate audio after story edits:

```bash
python scripts/generate_lesson_audio.py
```

## Local preview

Open `index.html` in a browser, or serve the folder:

```bash
npx --yes serve .
```

## Live site

https://ericchang1015.github.io/GeorgeEnglishLesson/

- Lesson 1: https://ericchang1015.github.io/GeorgeEnglishLesson/lessons/lesson-01.html
- Repo: https://github.com/EricChang1015/GeorgeEnglishLesson

## Publish (GitHub Pages)

Push to `main`. Site root is the repository root.

When updating a lesson before class: edit → commit → push. The Pages URL stays the same; the tutor only needs to refresh.
