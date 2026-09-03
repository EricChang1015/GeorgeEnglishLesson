# Art review — Lesson 7 p8 v9 / p12 v15 (Composer 2.5)

**Reviewer:** Composer 2.5 (independent structure + scale; fresh context; no generation; no branch switch)  
**Date:** 2026-09-03  
**Locks:** `docs/lesson-07-proposals/reviews/ART-RUBRIC-p08-09-12.md`, `docs/lesson-07-proposals/bible-locked.md`, `docs/lesson-07-proposals/plot-working.md` pages 8, 12  
**Skipped:** p9 — out of scope.  
**Anchor rule (UPDATED):** body anchors are **minimums**; hood/crown **below** the joint (taller beast) = **PASS**. **FAIL** only when ratio is under the floor **or** hood/crown is **above** the joint (beast too short).  
**Images Read (real PNG, full frame, 1536×1024), then measured with y-grid overlays and character crops:**

| Page | Path |
|------|------|
| p8 | `docs/lesson-07-proposals/gen/l7-p08-three-warnings-v9.png` |
| p12 | `docs/lesson-07-proposals/gen/l7-p12-stomping-parade-v15.png` |

Heights are vertical pixels on the shared raster: **(sole y) − (hood/crown apex y)**. George = **T-rex hood top** (p8) or **vine-crown leaf tips** (p12) → **navy sneaker sole** on the planted foot. Valid canvas y is **0–1023**; feet land ~**y730–880**, not y≈1017.  
**p12 boat leftover is NOT a FAIL.**  
Not copied into `lessons/assets/`.

---

## Shared hard fails (both frames)

| Check | Result | Evidence |
|-------|--------|----------|
| T-rex hood off | **PASS** | p8: tan cracked-scale onesie, dinosaur hood up, bangs visible. p12: green vine crown sits **on** the still-worn hood (leaves over fabric; no bare head). |
| Any beast &lt; 2× George on the same sole y-band | **PASS** | p8 lowest beast ≈ **3.1×** (Goat). p12 lowest beast ≈ **3.4×** (Beak). All clear the 2.0× hard floor on the shared clearing/shore band. |
| 4th beast / 6th person | **PASS** | Roster is only George + Horn (bull horns, mane, horizontal stripes) + Beak (red comb, yellow-orange feathers, bird beak) + Goat (spiral ram horns, shaggy pale fur). |
| On-image English | **PASS** | Billy o' Tea sail is a green leaf emblem, not letters; no names, captions, or crown text. |
| Fighting, blood, weapons, wooden fork | **PASS** | Warnings and parade only. George’s hands are empty. No fork, no wounds. |
| Photoreal / 3D | **PASS** | Cream-paper watercolor with ink cross-hatching; Sendak-mood picture book, not CG. |

---

## Pixel scale sheet

| Page | George (hood/crown → sole) | Horn | Beak | Goat | Sole y-band |
|------|----------------------------|------|------|------|-------------|
| **p8** | hood **y640** → sole **y845** = **205 px** | horn tips **y110**, planted claws **y850** = **740 px → 3.61×** | comb **y180**, talons on log **y780** = **600 px → 2.93×** | ram-horn peaks **y190**, plank claws **y880** = **690 px → 3.37×** | George sand **y845**; Horn plant **y850** (Δ **5 px**); Goat plank **y880** (Δ **35 px**, low walkway OK). Beak talons on dead log **y780** (plot perch). |
| **p12** | vine-crown tips **y618** → planted sneaker **y800** = **182 px** (raised stomp foot **y760**) | horn tips **y100**, mud **y750** = **650 px → 3.57×** | comb **y110**, talons **y730** = **620 px → 3.41×** | ram-horn peaks **y110**, planted foot **y760** = **650 px → 3.57×** | Horn / George / Beak / Goat all **y730–800** — tight clearing band; no depth-shrink. |

Body-anchor line (horizontal through George’s hood/crown top) — **minimum-size check** (hood/crown **above** joint = too short):

| Page | Line | Hits Horn | Hits Beak | Hits Goat |
|------|------|-----------|-----------|-----------|
| p8 | **y640** | **knee band** (~y643; hood **at** knee — not above) | **below waist** (~y584) — taller bird OK | **at mid-thigh** (~y638) — not above |
| p12 | **y618** | **below knee** (~y568) — taller beast OK | **below waist** (~y470) | **below mid-thigh** (~y532) |

---

## p8 — Three Wild Warnings (`l7-p08-three-warnings-v9.png`)

**Zone:** WildIsland (night shore). **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| Horn hoof makes a sand pit but does not touch George | **PASS** | Horn’s right foot is raised over a deep circular crater (rim ~y800, pit to ~y845); left plant on sand ~y850. George stands far left (~x120) outside the pit — no contact. |
| Beak claws leave marks on dead wood only | **PASS** | Beak stands on a fallen weathered log (~x720–980); long talons press dead wood at **y780**, not a living trunk. |
| Goat arms block a readable vine bridge into the island | **PASS** | Far right: log-plank walkway with twisted-vine rails/pillars into the jungle; Goat stands in the mouth gripping both vine-wrapped posts (~x1050–1380). |
| George stands steady, empty-handed | **PASS** | Hooded T-rex boy in navy sneakers, profile facing the beasts, both hands empty (no fork). |
| Billy o' Tea behind George | **PASS** | Tea-brown hull and off-white sail with green leaf emblem in the shallows left/behind George; no crew, no letters. |
| Beasts ≥2×, same shore line | **PASS** | All three beasts **≥2.93×** on the shared shore band; no perspective shrink. |
| Horn ≥3.0×; hood ≈ knee (minimum) | **PASS** | 740/205 = **3.61×**. Hood **y640** meets Horn knee band **~y643** — not above the joint. |
| Beak ≥2.2×; hood ≈ waist (minimum) | **PASS** | 600/205 = **2.93×**. Hood **y640** sits **below** Beak waist **~y584** (taller beast). |
| Goat ≥2.6×; hood ≈ mid-thigh (minimum) | **PASS** | 690/205 = **3.37×**. Hood **y640** meets Goat mid-thigh **~y638** — not above the joint. |
| p8 Goat bridge exception | **PASS** | Plank soles **y880**; sand under plank face **y835–860** (Δ **20–45 px**). Low beach-level walkway, not a high terrace. |
| No crown yet | **PASS** | Nothing on the T-rex hood except the costume. |
| Identity / costume | **PASS** | Horn: bull horns, mane, stripes, claws. Beak: comb/wattle, yellow-orange feathers, hooked beak. Goat: ridged ram horns, pale shag. Onesie + hood + tail + navy sneakers. |
| George height sanity | **PASS** | Hood **y640** → sole **y845** = **205 px** — inside typical **180–260** band; correct boy landmark (not sail or beast shoulder). |
| Shared hard fails | **PASS** | All beasts **≥2.93×**; hood up; roster clean. |

**Page verdict:** **PASS** — story beats land; scale floors and minimum body anchors all clear.

---

## p12 — Stomping Parade (`l7-p12-stomping-parade-v15.png`)

**Zone:** WildClearing (moonlit jungle clearing). **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| Vine crown on hood | **PASS** | Green leaf/vine wreath sits on top of the still-worn T-rex hood; bangs visible beneath. |
| George stomping | **PASS** | Mid-stride march: right knee raised (~y760), left navy sneaker planted **y800**; happy open-mouth expression. |
| Horn wooden drum | **PASS** | Horn beats a barrel drum with rope bindings and two padded mallets (~x280–520). |
| Goat spinning | **PASS** | Goat on one leg, arms out, motion lines at waist — dance/spin readable. |
| Beak wings | **PASS** | Beak holds wings spread wide on both sides for rhythm. |
| Pressed footprint rings | **PASS** | Concentric circular stomp tracks pressed into the clearing dirt behind the line (~y650–780). |
| Four figures, happy, claws visible but harmless | **PASS** | All four smiling / gleeful; teeth and claws show without injury. |
| Moon / seedpods OK | **PASS** | Full moon upper-left (~y70); round spiky seedpod plants along foreground edge. |
| NOT required: leaf chair, boat, vine bridge | **PASS** | Leaf chair / vine bridge absent — not penalized. Small Billy o' Tea in far-left water is a **boat leftover** — **not scored as FAIL**. |
| Horn ≥3.0×; crown ≈ knee (minimum) | **PASS** | 650/182 = **3.57×**. Crown **y618** sits **below** Horn knee **~y568** — taller beast OK. |
| Beak ≥2.2×; crown ≈ waist (minimum) | **PASS** | 620/182 = **3.41×**. Crown **y618** sits **below** Beak waist **~y470**. |
| Goat ≥2.6×; crown ≈ mid-thigh (minimum) | **PASS** | 650/182 = **3.57×**. Crown **y618** sits **below** Goat mid-thigh **~y532**. |
| George height sanity | **PASS** | Crown **y618** → sole **y800** = **182 px** — inside **180–260** band and well under the **300 px** wrong-landmark ceiling. |
| Shared hard fails | **PASS** | All beasts **≥3.41×**; crown-on-hood; roster clean. |

**Page verdict:** **PASS** — parade props and crown track land; all three beasts clear scale floors with hood/crown below minimum joints.

---

## Revision delta (vs prior reviewed builds)

| Page | Prior | This build | Scale trend |
|------|-------|------------|-------------|
| p8 | v8 — George **260 px**; Horn **2.65×**; Beak **1.96×** (hard &lt;2×); Goat **2.15×** | v9 — George **205 px**; Horn **3.61×**; Beak **2.93×**; Goat **3.37×** | George back in **180–260** band; all three ratios **above** locked floors; Beak clears hard **2×** floor. |
| p12 | v14 — George **295 px**; Horn **2.32×**; Beak **1.66×**; Goat **1.83×** | v15 — George **182 px**; Horn **3.57×**; Beak **3.41×**; Goat **3.57×** | George shrunk to band; all beasts **≥3.4×**; crown line below all minimum joints. |

---

## Summary table

| Page | File | Verdict | Primary evidence |
|------|------|---------|------------------|
| p8 | `l7-p08-three-warnings-v9.png` | **PASS** | George **205 px**; Horn **3.61×** at knee; Beak **2.93×** below waist; Goat **3.37×** at mid-thigh; pit / log / bridge / boat / empty hands land. |
| p12 | `l7-p12-stomping-parade-v15.png` | **PASS** | George **182 px**; Horn **3.57×**, Beak **3.41×**, Goat **3.57×**; crown-on-hood; drum / stomp / spin / wings / pressed rings land; boat leftover ignored. |

## VERDICT: PASS

Both pages clear the written scale gate (ratio floors + minimum body anchors on the shared sole band), shared hard fails, and plot must-haves. p9 skipped. No images copied into `lessons/assets/`.
