# GATE 3 Face D — Player smoke (Composer 2.5)

**Lesson:** 07 — *George and the Wild Parade*  
**Model:** composer-2.5 (CP5)  
**URL tested:** http://localhost:4177/lessons/lesson-07.html  
**Also read:** `lessons/lesson-07.html`, `index.html`  
**Date:** 2026-09-01

## Environment

- Local server: `http://localhost:4177`
- Browser: Cursor IDE browser MCP (CDP + accessibility snapshot)
- Player script: `lessons/js/lesson-player.js?v=4`

---

## Checklist

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | **Cover** — title, cover.webp, Start / Go to / Auto read | **PASS** | H1 `George and the Wild Parade`; cover img `assets/lesson-07/cover.webp` (runtime src `http://localhost:4177/lessons/assets/lesson-07/cover.webp`); buttons **Start ▶**, combobox **Go to** (Cover … Notes), **▶ Auto read** visible in snapshot. |
| 2 | **Console** — zero JS errors on load | **PASS** | CDP `Runtime.evaluate` after load: `consoleErrors: []`; resource perf check: no zero-size lesson-07 failures; no errors during 12-page hash walk. |
| 3 | **Go to Story 1** — illustration is `.webp` not `.png` | **PASS** | `#story=1` active screen img: `…/story-01.webp`; `webp: true`, `png: false`. Player maps JSON `story-01.png` → `.webp` via `lesson-player.js`. |
| 4 | **Quiz** — question + A/B/C; options disabled until Read | **PASS** | `#quiz`: heading *What did Mummy call George?*; options **A** A careful king, **B** A wild thing, **C** A little lamp — all `states: [disabled]`; hint *Tap Read, then choose A, B or C*; **🔊 Read question** present. |
| 5 | **Spot-check `#story=2`** — `story-02.webp` loads | **PASS** | `#story=2` active img: `…/story-02.webp`; Go to dropdown value **Story 2**; Mummy/Sylvia dialogue lines render. |
| 6 | **Vocab, phrases, notes screens exist** | **PASS** | `#vocab` → h2 **New Words** (screen 1); `#phrases` → **Key Phrases** (screen 15); `#notes` → **Follow-up Notes** + `#notesForm` (screen 16). |
| 7 | **All 12 story screens in HTML** | **PASS** | `lesson-07.html` sections `data-story="0"` … `data-story="11"` (12 sections); DOM count `[data-story]` = 12; Go to lists Story 1–12. |
| 8 | **Role colors** mummy / sylvia / horn / beak / goat | **PASS** | Inline CSS in `lesson-07.html` lines 15–24 (`.voice-key` + `.line` for all five); computed backgrounds present on cover voice-key spans. |
| 9 | **index.html** Lesson 7 card → lesson-07.html + cover.webp | **PASS** | Card `href="lessons/lesson-07.html"`, img `lessons/assets/lesson-07/cover.webp`, h2 **George and the Wild Parade**; browser snapshot on `/` shows same card. |
| 10 | **Story walk** — all pages `.webp`, no console errors | **PASS** | Hash walk `#story=1`…`#story=12`: every active img `story-NN.webp` (01–12), none `.png`. HEAD requests: all 12 story webps + cover return **200** `image/webp`. |

---

## Story page walk (runtime img src)

| Page | Hash | Loaded image |
|------|------|--------------|
| 1 | `#story=1` | `story-01.webp` |
| 2 | `#story=2` | `story-02.webp` |
| 3 | `#story=3` | `story-03.webp` |
| 4 | `#story=4` | `story-04.webp` |
| 5 | `#story=5` | `story-05.webp` |
| 6 | `#story=6` | `story-06.webp` |
| 7 | `#story=7` | `story-07.webp` |
| 8 | `#story=8` | `story-08.webp` |
| 9 | `#story=9` | `story-09.webp` |
| 10 | `#story=10` | `story-10.webp` |
| 11 | `#story=11` | `story-11.webp` |
| 12 | `#story=12` | `story-12.webp` |

---

## Static HTML notes (non-blocking)

- `<title>` is `Lesson 7: George's Wild Parade` while cover H1 is `George and the Wild Parade` — cosmetic only; cover title check uses H1.
- Go to dropdown labels vocab screen **Song words** (player default) while on-page heading is **New Words** — navigation works; label mismatch only.

---

## OVERALL: **PASS**

No FAIL items. Player loads cleanly; cover and all 12 story pages serve WebP; quiz gating works; index card links correctly; vocab / phrases / notes screens present.
