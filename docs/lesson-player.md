# Lesson player, images, and loading

Shared runtime for every lesson. **Agent rule:** `.cursor/rules/lesson-design.mdc`.

| Path | Role |
|------|------|
| `lessons/js/lesson-player.js` | Page jump, swipe, lazy images, audio, quiz A/B/C, Auto read |
| `lessons/css/lesson.css` | Shared layout and colours |
| `lessons/lesson-XX.html` | Cover, notes, and `window.LESSON` data only |
| `scripts/optimize_lesson_images.py` | PNG → display WebP |
| `scripts/generate_lesson_audio.py` | Story + vocab + quiz TTS |

## Images

Each illustration has two files in `lessons/assets/lesson-XX/`:

| File | Purpose |
|------|---------|
| `story-01.png` | Original art (keep for redraws; **do not** put in `src`) |
| `story-01.webp` | What the page loads |

Rules:

- **One display format:** WebP only. Do not generate JPG fallbacks.
- Story / cover: max width **1000px**. Vocab cards: max width **800px**. Keep aspect ratio.
- After adding or replacing a PNG:

```bash
python scripts/optimize_lesson_images.py --lesson lesson-01
```

Omit `--lesson` to process every `lesson-XX` folder.

Index cards and cover `<img>` tags must use `.webp` (see `index.html`).

The player converts names like `story-01.png` in `window.LESSON` to `.webp` and sets `src` only for the **current screen**, then preloads the next.

## Audio

```bash
python scripts/generate_lesson_audio.py --story scripts/lesson01_story.json --out lessons/assets/lesson-01/audio
python scripts/generate_lesson_audio.py --quiz-only --story scripts/lesson01_story.json --out lessons/assets/lesson-01/audio
```

Quiz clips (narrator): `quiz-01.mp3`, `quiz-01-a.mp3` … `quiz-01-c.mp3`, plus `quiz-choose.mp3`.

If `window.LESSON.youtubeId` is set, a screen with `#songEmbed` lazy-loads the official YouTube player (full song). Screens with `data-song` are sing-along pages: tap a lyric line to play a short original-audio clip. Deep links: `#sing=1`, `#listen`.

Lesson 6 slim player has no `data-song` pages: Cover → Song words → `lesson-06-slideshow.html` (one lyric line, one picture), then `#listen` for the full song.

On the quiz page, **Read question** speaks the question, then A/B/C. Options stay disabled until that finishes.

If `window.LESSON.quizPick` is set (Lesson 3 uses `5`), the player shuffles the pool and shows that many questions per visit. Audio files stay numbered by **pool order** (`quiz-01` …), not session order. Lessons without `quizPick` still play the full list.

## Navigation

| Control | Behaviour |
|---------|-----------|
| Swipe / ← → | Previous / next page |
| **Go to** | Jump to Cover, Words / Song words, Story, Sing, Full song, Quiz, Phrases, Notes |
| **Auto read** | Read the current page, turn, continue; at quiz, wait for A/B/C |

Deep links (updated as the child moves):

- `#story=3` — story page 3
- `#sing=1` — first sing-along page (lessons that still use `data-song`)
- `#listen` — full-song YouTube embed
- Lesson 6 picture song: `lessons/lesson-06-slideshow.html#line=1` … `#line=24`
- `#quiz` `#words` `#phrases` `#notes` `#cover`
- `#p=4` or `?page=4` — screen index (0 = cover)

## New lesson checklist

1. Add PNG art under `lessons/assets/lesson-XX/`.
2. Run `optimize_lesson_images.py` so WebP exists before preview.
3. Point cover / index images at `.webp`.
4. Put vocab, story, quiz, and phrases on `window.LESSON`; do not duplicate player JS.
5. Generate audio (including quiz) when text changes.
6. Browser smoke test (cover + Story 1 + Quiz, clean console) before commit. See `.cursor/rules/delivery.mdc`.
