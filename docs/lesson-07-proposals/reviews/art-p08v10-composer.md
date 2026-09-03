# Art review — Lesson 7 p8 v10 (Composer 2.5)

**Reviewer:** Composer 2.5 (independent structure + scale; fresh context; no generation; no branch switch)  
**Date:** 2026-09-03  
**Locks:** `docs/lesson-07-proposals/reviews/ART-RUBRIC-p08-09-12.md`, `docs/lesson-07-proposals/bible-locked.md`, `docs/lesson-07-proposals/plot-working.md` page 8  
**Anchor rule:** body anchors are **minimums**; hood/crown **below** the joint (taller beast) = **PASS**. **FAIL** only when ratio is under the floor **or** hood/crown is **above** the joint (beast too short).  
**Image Read (real PNG, full frame, 1536×1024), then measured with y-grid overlays and character crops:**

| Page | Path |
|------|------|
| p8 | `docs/lesson-07-proposals/gen/l7-p08-three-warnings-v10.png` |

Heights are vertical pixels on the shared raster: **(sole y) − (hood apex y)**. George = **T-rex hood top** → **navy sneaker sole** on the planted foot. Valid canvas y is **0–1023**; feet land ~**y730–880**, not y≈1017.  
Not copied into `lessons/assets/`.

---

## Shared hard fails

| Check | Result | Evidence |
|-------|--------|----------|
| T-rex hood off | **PASS** | Tan cracked-scale onesie, dinosaur hood up, bangs visible. |
| Any beast &lt; 2× George on the same sole y-band | **PASS** | Lowest beast = Goat **2.73×**; all clear the 2.0× hard floor. |
| 4th beast / 6th person | **PASS** | Roster is only George + Horn (bull horns, mane, horizontal stripes) + Beak (red comb, yellow-orange feathers, bird beak) + Goat (spiral ram horns, shaggy pale fur). |
| On-image English | **PASS** | Billy o' Tea sail is a green leaf emblem, not letters; no names, captions, or crown text. |
| Fighting, blood, weapons, wooden fork | **PASS** | Warnings only. George’s hands are empty. No fork, no wounds. |
| Photoreal / 3D | **PASS** | Cream-paper watercolor with ink cross-hatching; Sendak-mood picture book, not CG. |

---

## Pixel scale sheet

| Page | George (hood → sole) | Horn | Beak | Goat | Sole y-band |
|------|----------------------------|------|------|------|-------------|
| **p8** | hood **y628** → sole **y842** = **214 px** | horn tips **y48**, planted claws **y852** = **804 px → 3.76×** | crest **y98**, talons on log **y752** = **654 px → 3.06×** | ram-horn peaks **y188**, plank claws **y772** = **584 px → 2.73×** | George sand **y842**; Horn plant **y852** (Δ **10 px**); Goat plank **y772** (Δ **70 px**, low sloped walkway OK). Beak talons on dead log **y752** (plot perch). |

Body-anchor line (horizontal through George’s hood top) — **minimum-size check** (hood **above** joint = too short):

| Page | Line | Hits Horn | Hits Beak | Hits Goat |
|------|------|-----------|-----------|-----------|
| p8 | **y628** | **knee band** (~y627; hood **at** knee — not above) | **below waist** (~y477) — taller bird OK | **below mid-thigh** (~y568) — taller beast OK |

---

## p8 — Three Wild Warnings (`l7-p08-three-warnings-v10.png`)

**Zone:** WildIsland (night shore). **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| Horn hoof makes a sand pit but does not touch George | **PASS** | Horn’s right foot is raised over a deep circular crater (rim ~y790, pit to ~y835); left plant on sand ~y852. George stands far left (~x175) outside the pit — no contact. |
| Beak claws leave marks on dead wood only | **PASS** | Beak grips a grey weathered dead log/stump (~x700–900); long talons press dead wood at **y752**, not a living trunk. |
| Goat arms block a readable vine bridge into the island | **PASS** | Far right: **horizontal plank deck** (readable board path) with twisted-vine rails/pillars angling into the jungle; Goat stands in the mouth gripping both vine-wrapped posts (~x1050–1380). Reads as a **walkable 藤橋**, not a post-and-rail fence. |
| George stands steady, empty-handed | **PASS** | Hooded T-rex boy in navy sneakers, profile facing the beasts, both hands empty (no fork). |
| Billy o' Tea behind George | **PASS** | Tea-brown hull and off-white sail with green leaf emblem in the shallows left/behind George; no crew, no letters. |
| Beasts ≥2×, same shore line | **PASS** | All three beasts **≥2.73×** on the shared shore band; no perspective shrink below floors. |
| Horn ≥3.0×; hood ≈ knee (minimum) | **PASS** | 804/214 = **3.76×**. Hood **y628** meets Horn knee band **~y627** — not above the joint. |
| Beak ≥2.2×; hood ≈ waist (minimum) | **PASS** | 654/214 = **3.06×**. Hood **y628** sits **below** Beak waist **~y477** (taller beast). |
| Goat ≥2.6×; hood ≈ mid-thigh (minimum) | **PASS** | 584/214 = **2.73×**. Hood **y628** sits **below** Goat mid-thigh **~y568** — not above the joint. |
| p8 Goat bridge exception | **PASS** | Plank soles **y772**; sand under George **y842** (Δ **70 px**). Low sloped beach-level walkway at bridge mouth, not a high terrace used to shrink Goat below the floor. |
| No crown yet | **PASS** | Nothing on the T-rex hood except the costume. |
| Identity / costume | **PASS** | Horn: bull horns, mane, stripes, claws. Beak: comb/wattle, yellow-orange feathers, hooked beak. Goat: ridged ram horns, pale shag. Onesie + hood + tail + navy sneakers. |
| George height sanity | **PASS** | Hood **y628** → sole **y842** = **214 px** — inside typical **180–260** band; correct boy landmark (not sail or beast shoulder). |
| Shared hard fails | **PASS** | All beasts **≥2.73×**; hood up; roster clean. |

**Page verdict:** **PASS** — story beats land; scale floors and minimum body anchors all clear; readable vine plank bridge (not fence).

---

## Revision delta (vs prior reviewed builds)

| Page | Prior | This build | Scale trend |
|------|-------|------------|-------------|
| p8 | v9 — George **205 px**; Horn **3.61×**; Beak **2.93×**; Goat **3.37×**; Grok 4.5 flagged bridge as fence | v10 — George **214 px**; Horn **3.76×**; Beak **3.06×**; Goat **2.73×** | George still in **180–260** band; Horn/Beak ratios hold or improve; Goat tightens to **2.73×** but still clears **2.6×** floor; plank deck now readable as bridge path. |

---

## Summary table

| Page | File | Verdict | Primary evidence |
|------|------|---------|------------------|
| p8 | `l7-p08-three-warnings-v10.png` | **PASS** | George **214 px**; Horn **3.76×** at knee; Beak **3.06×** below waist; Goat **2.73×** below mid-thigh; pit / dead-wood log / **readable plank vine bridge** / boat / empty hands land. |

## VERDICT: PASS

p8 v10 clears the written scale gate (ratio floors + minimum body anchors on the shared sole band), shared hard fails, and plot must-haves including a readable vine plank bridge. No images copied into `lessons/assets/`.
