# GATE 3 Face D — Browser walkthrough (Composer 2.5 / CP5)

**Lesson:** 07 — *George and the Wild Parade*  
**Model:** composer-2.5 (CP5)  
**URL tested:** http://127.0.0.1:4177/lessons/lesson-07.html  
**Date:** 2026-09-03  
**Method:** Headless Chrome via Puppeteer + curl HTTP verification (no image generation)

## Environment

- Local server: `npx serve -l 4177 .` (already running; HTTP 200 on root)
- Browser: Puppeteer / Chrome headless (linux-131)
- Player: `lessons/js/lesson-player.js?v=4`
- Story pages in HTML: 19 (`data-story="0"` … `data-story="18"`)

---

## Checklist

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | **Cover** — title, cover.webp, Start / Go to / Auto read | **PASS** | H1 `George and the Wild Parade`; cover img `assets/lesson-07/cover.webp`; **Start ▶** on cover; toolbar **Go to** (`#pageJump`, 24 options incl. Story 1–19); **▶ Auto read** in toolbar (`#autoReadBtn`) plus cover **▶ Auto read** (`[data-auto-start]`). |
| 2 | **Console** — zero JS errors on load; no lesson asset 404 | **PASS** | `pageerror`: none. Console shows only generic `Failed to load resource: 404` for `/favicon.ico` (not a lesson asset). No `ReferenceError` or player JS failures. |
| 3 | **Story 1–19** — illustration `.webp`, loads (not broken) | **PASS** | Hash walk `#story=1`…`#story=19`: every active img `story-NN.webp` (naturalWidth 1000), `png: false`, `broken: false`. curl HEAD: cover + story-01…19.webp all **200**. |
| 4 | **Quiz** — question + A/B/C; options disabled until Read | **PASS** | `#quiz`: sample Q1 *Who put the vine crown on George?*; 3 options (A/B/C) all `disabled`; hint *Tap Read, then choose A, B or C*; **🔊 Read question** (`[data-read-quiz]`) present. Random 5-of-10 pool active (`quizPick: 5`). |
| 5 | **Spot-check `#story=2`** | **PASS** | `#story=2` → `story-02.webp`; line roles `mummy, george, mummy, sylvia` match page JSON. |
| 6 | **Next from story 2** | **PASS** | Click `.screen.active [data-next]` on `#story=2` → navigates to `#story=3`, `story-03.webp`, `data-story="2"`. |
| 7 | **Audio** — 3 sentence clips, different roles, no 404 | **PASS** | Line taps: George `p01-02.mp3` (206), Goat `p12-01.mp3` (206), Mummy `p19-02.mp3` (206). Direct fetch: all three **200** `audio/mpeg`, sizes 73260 / 29376 / 21024 bytes. |
| 8 | **Go to dropdown** — Story 1–19 listed | **PASS** | `#pageJump` lists Story 1 through Story 19 (19 entries). |

---

## Story page walk (runtime img src)

| Page | Hash | Loaded image | naturalWidth |
|------|------|--------------|--------------|
| 1 | `#story=1` | `story-01.webp` | 1000 |
| 2 | `#story=2` | `story-02.webp` | 1000 |
| 3 | `#story=3` | `story-03.webp` | 1000 |
| 4 | `#story=4` | `story-04.webp` | 1000 |
| 5 | `#story=5` | `story-05.webp` | 1000 |
| 6 | `#story=6` | `story-06.webp` | 1000 |
| 7 | `#story=7` | `story-07.webp` | 1000 |
| 8 | `#story=8` | `story-08.webp` | 1000 |
| 9 | `#story=9` | `story-09.webp` | 1000 |
| 10 | `#story=10` | `story-10.webp` | 1000 |
| 11 | `#story=11` | `story-11.webp` | 1000 |
| 12 | `#story=12` | `story-12.webp` | 1000 |
| 13 | `#story=13` | `story-13.webp` | 1000 |
| 14 | `#story=14` | `story-14.webp` | 1000 |
| 15 | `#story=15` | `story-15.webp` | 1000 |
| 16 | `#story=16` | `story-16.webp` | 1000 |
| 17 | `#story=17` | `story-17.webp` | 1000 |
| 18 | `#story=18` | `story-18.webp` | 1000 |
| 19 | `#story=19` | `story-19.webp` | 1000 |

---

## curl verification (supplement)

```
cover.webp + story-01.webp … story-19.webp → all HTTP 200
lesson-07.html → 301 redirect to /lessons/lesson-07 (serve clean URLs)
audio/p01-02.mp3, p12-01.mp3, p19-02.mp3 → HTTP 200, non-zero Content-Length
```

---

## Not exercised in this run

- Full vocab card tap-through (screen 1)
- Key Phrases screen tap-through
- Follow-up Notes save/clear
- Quiz **Read question** playback + option enable after read (structure verified; read-then-enable rule confirmed via disabled state + hint)
- Auto read full-page playback
- Swipe gesture (Next button and hash navigation verified instead)
- Audible playback quality (network fetch only)

---

## Static notes (non-blocking)

- `<title>` is `Lesson 7: George's Wild Parade` while cover H1 is `George and the Wild Parade` — cosmetic.
- Go to label **Song words** vs on-page **New Words** — navigation works; label mismatch only.
- `/favicon.ico` 404 — browser default request; does not affect lesson.

---

## OVERALL: **PASS**

All required smoke and full 19-page story walk pass. Console clean for JS; lesson images and sampled audio load without 404. Quiz gating and navigation (hash, Next, Go to) work as expected.
