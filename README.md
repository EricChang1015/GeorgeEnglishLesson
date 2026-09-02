# George English Lessons

Interactive HTML reading lessons for George (born 2021-06-23), targeting Oxford Reading Tree Level 6.

## Lessons

Lessons 1–3 are one story chapter (**Pip and Ember**). **Lesson 4** starts **Mike Dreams**. **Lesson 5** starts **George's Real Adventures** (real family trips). Homepage grouping, a slightly harder vocab bar, line emotion, a cast/scene bible, and 5-question quiz sampling are recorded in [`docs/lesson-01-03-review.md`](docs/lesson-01-03-review.md) (not all built yet). Visual locks: [`docs/cast-bible.md`](docs/cast-bible.md). Mike chapter: [`docs/big-eye-chapter.md`](docs/big-eye-chapter.md). Real adventures: [`docs/real-adventures-chapter.md`](docs/real-adventures-chapter.md).

### Lesson 1 — `lessons/lesson-01.html`
**George and the Little Dragon** (ORT Level 6): George meets Pip and finds a red egg.

### Lesson 2 — `lessons/lesson-02.html`
**The Red Egg Hatches** (ORT Level 6): Ember hatches; George helps; Ember flies a little.

### Lesson 3 — `lessons/lesson-03.html`
**George and the Storm on the Hill** (ORT Level 6): berry path, storm, bear, cave shelter; Daddy climbs up. Safety phrases + Daddy voice.

### Lesson 4 — `lessons/lesson-04.html`
**George and the Dinosaur Under the Blanket** (ORT Level 6, **Mike Dreams** ch.1): bedtime with Mike, blanket thump, dream adventure, help Nibble find her nest; morning fern leaf. See [`docs/big-eye-chapter.md`](docs/big-eye-chapter.md).

### Lesson 5 — `lessons/lesson-05.html`
**George's Big Cave Adventure** (ORT Level 6, **George's Real Adventures** ch.1): Sansheng Cave with Coach Jojo — muddy puddles, via ferrata, stone forest of stalactites, cave paddle board, hotel ending. See [`docs/real-adventures-chapter.md`](docs/real-adventures-chapter.md).

Features: vocabulary (word + example sentence), dialogue story, AI line audio, quiz with A/B/C voice, Auto read, swipe / jump-to-page, tutor notes.

Pages load **WebP** one screen at a time (original PNGs stay in the folder but are not fetched). Player how-to: [`docs/lesson-player.md`](docs/lesson-player.md).

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
python scripts/generate_lesson_audio.py --story scripts/lesson04_story.json --out lessons/assets/lesson-04/audio
python scripts/generate_lesson_audio.py --story scripts/lesson05_story.json --out lessons/assets/lesson-05/audio
```

Vocab entries may include `example` + `example_audio`; the generator speaks the word, then the example sentence (narrator voice). Quiz A/B/C clips are generated from the `quiz` block (`--quiz-only` to refresh those only).

After new or replaced PNG art:

```bash
python scripts/optimize_lesson_images.py
```

## Character reference photos

Likeness refs for consistent lesson art:

- George + family group: `lessons/assets/refs/george/` — `lessons/assets/refs/george/CATALOG.md`
- Sylvia solo: `lessons/assets/refs/sylvia/` — `lessons/assets/refs/sylvia/CATALOG.md`
- Mummy solo: `lessons/assets/refs/mummy/` — `lessons/assets/refs/mummy/CATALOG.md`
- Daddy solo: `lessons/assets/refs/daddy/` — `lessons/assets/refs/daddy/CATALOG.md`
- Agent rule: `.cursor/rules/character-refs.mdc`
- Cast ids: `george`, `daddy`, `mummy`, `sylvia`
- Naming: `{subjects}-{setting}-{pose-or-mood}.jpg` (George first when he is in frame)
- Default George face: `george-solo-bed-smile.jpg`
- Default Sylvia face: `sylvia-solo-outdoors-graduation-smile.jpg`
- Default Mummy face: `mummy-solo-indoor-smile.png`
- Default Daddy face: `daddy-solo-indoor-vehicle-neutral.png` (solo); `george-daddy-outdoors-pavilion-neutral.jpg` (with George)
- Cover / close face: `george-solo-sofa-alphabet-smile.jpg`

Photos in `lessons/assets/refs/george/`, `lessons/assets/refs/sylvia/`, `lessons/assets/refs/mummy/`, and `lessons/assets/refs/daddy/` are **tracked in git**. Put new photos in the matching folder and update that folder's `CATALOG.md`. Do not use `ref/` for new drops. Do not embed raw ref photos in published lesson HTML — only drawn/AI lesson art goes under `lessons/assets/lesson-XX/`.

## Local preview

Open `index.html` in a browser, or serve the folder:

```bash
npx --yes serve .
```

## Live site

**https://george.macau-tech.com/**

- Lesson 1: https://george.macau-tech.com/lessons/lesson-01.html
- Lesson 2: https://george.macau-tech.com/lessons/lesson-02.html
- Lesson 3: https://george.macau-tech.com/lessons/lesson-03.html
- Lesson 4: https://george.macau-tech.com/lessons/lesson-04.html
- Lesson 5: https://george.macau-tech.com/lessons/lesson-05.html
- Repo: https://github.com/EricChang1015/GeorgeEnglishLesson

Legacy GitHub Pages URL (still works): https://ericchang1015.github.io/GeorgeEnglishLesson/

Custom domain setup (Cloudflare + GitHub): [`docs/custom-domain.md`](docs/custom-domain.md)

## Publish (GitHub Pages)

Push to `main`. Site root is the repository root.

When updating a lesson before class: edit → commit → push, then hard-refresh **https://george.macau-tech.com/**.
