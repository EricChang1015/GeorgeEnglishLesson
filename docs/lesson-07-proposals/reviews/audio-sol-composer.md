# Audio review — Lesson 7 Sol staging (`audio-sol`)

**Lesson:** 07 — *George and the Wild Parade* (19-page Sol expansion)  
**Reviewer:** Composer 2.5 (independent audio/player reviewer; no audio generated)  
**Rubric:** `docs/lesson-07-proposals/reviews/AUDIO-RUBRIC.md`  
**Story JSON:** `scripts/lesson07_story.json`  
**Voices lock:** `scripts/voices.json`  
**Staging dir:** `lessons/assets/lesson-07/audio-sol/` (not copied to official `audio/`)  
**Date:** 2026-09-02

## Automated check

```text
python3 scripts/check_lesson_audio.py \
  --story scripts/lesson07_story.json \
  --audio lessons/assets/lesson-07/audio-sol

checked 136 expected clips in lessons/assets/lesson-07/audio-sol
PASS  all clips present, sized, duration-plausible; voices match voices.json
```

Exit code **0**. No missing, broken, or duration-out-of-range clips reported.

---

## Rubric checklist

| # | Item | Result | Evidence |
|---|------|--------|----------|
| 1 | **Voices** match `voices.json` | **PASS** | Story `voices` block checked field-by-field against canonical roles: `narrator` Sonia `-10%/+0Hz`; `george` MiniMax `cute_boy` 1.3/0; `mummy` Aria `+5%/+5Hz`; `daddy` Ryan `-5%/-5Hz`; `sylvia` Kind-heartedGirl 1.05/2; `horn` ManWithDeepVoice 0.82/-6; `beak` Comedian 1.16/4; `goat` Steffan `-12%/-14Hz`. `check_lesson_audio.py` voice pass confirms. |
| 2 | **Island / expansion story lines** p07–p19 | **PASS** | Full story = **76** lines (p01–p19 × 4). New island block p07–p19 = **52/52** mp3s present (`p07-01` … `p19-04`). Expansion tail p13–p19 = **28/28** mp3s present. |
| 3 | **Vocab rule clips** | **PASS** | `vocab-rule.mp3` (10 656 B, ~1.8 s) and `vocab-rule-ex.mp3` (25 632 B, ~4.3 s) exist in staging; referenced by vocab entry `rule` in story JSON. |
| 4 | **Key phrase / emotion pairing** | **PASS** | JSON line + staging file confirmed (duration plausible, ≥1 KB): `p09-01` george `steady` — *Look into my eyes…* (4.57 s); `p14-01` george `kindly` — *First royal rule: big feet wait…* (4.57 s); `p17-01` george `resolved` — *I choose home…* (4.57 s); `p19-02` mummy `soft` — *Your supper is still hot…* (3.50 s). |
| 5 | **No 12-page-only gaps** (p13–p19) | **PASS** | All 28 clips p13-01 … p19-04 on disk. Official `lessons/assets/lesson-07/audio/` has **no** p13–p19 files (108 legacy clips only) — staging holds expansion; not promoted. |
| 6 | **Quiz clips** quiz-01 … quiz-10-c | **PASS** | 41 quiz mp3s: `quiz-choose.mp3` + 10 questions × (stem + a/b/c) = quiz-01 … quiz-10-c. All present in staging. |

---

## `build_lesson07_html.py` phrase map

`phrase_map` reuses story-line audio for Key Phrases screen:

| Phrase | Mapped file | Staging |
|--------|-------------|---------|
| Look into my eyes | `p09-01.mp3` | **PASS** (74 989 B) |
| First royal rule | `p14-01.mp3` | **PASS** (74 989 B) |
| I choose home | `p17-01.mp3` | **PASS** (74 989 B) |
| still hot | `p19-02.mp3` | **PASS** (21 024 B) |

(Also mapped but not rubric spot-check: `wild thing` → `p02-01.mp3`, `friendly bow` → `p14-02.mp3` — both present.)

---

## p13–p19 duration spot-check (plausible)

| Clip | Duration |
|------|----------|
| p13-01 … p13-04 | 2.95 – 5.33 s |
| p14-01 … p14-04 | 3.65 – 4.68 s |
| p15-01 … p15-04 | 4.06 – 5.58 s |
| p16-01 … p16-04 | 4.39 – 4.70 s |
| p17-01 … p17-04 | 3.20 – 5.04 s |
| p18-01 … p18-04 | 3.71 – 5.62 s |
| p19-01 … p19-04 | 3.50 – 5.30 s |

All within `check_lesson_audio.py` plausibility band; none under 1 KB.

---

## Staging boundary

- Reviewed **only** `lessons/assets/lesson-07/audio-sol/` (136 mp3s).
- **Did not** copy or overwrite `lessons/assets/lesson-07/audio/` (official 12-page set remains separate).

---

## Limits of this review

- File presence, size, duration plausibility, and voice-lock schema only — **no listening test** for emotional delivery or TTS quality.
- Player/HTML smoke with `audio-sol` path not run here (staging not wired into published `lesson-07.html`).

---

## VERDICT: **PASS**

All rubric items pass. `check_lesson_audio.py` reports 136/136 clips present with plausible durations and matching voice lock. p13–p19 expansion clips and phrase-map sources (`p09-01`, `p14-01`, `p17-01`, `p19-02`) exist in staging. Ready for promotion to official `audio/` when parent approves — **not done in this review**.
