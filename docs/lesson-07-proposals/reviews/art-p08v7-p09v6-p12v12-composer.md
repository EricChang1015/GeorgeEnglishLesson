# Art review — Lesson 7 p8 v7 / p9 v6 / p12 v12 (Composer 2.5)

**Reviewer:** Composer 2.5 (independent structure + scale; fresh context; no generation; no branch switch)  
**Date:** 2026-09-03  
**Locks:** `docs/lesson-07-proposals/reviews/ART-RUBRIC-p08-09-12.md`, `docs/lesson-07-proposals/bible-locked.md`, `docs/lesson-07-proposals/plot-working.md` pages 8, 9, 12  
**Images Read (real PNG, full frame, 1536×1024), then measured with y-grid overlays and character crops:**

| Page | Path |
|------|------|
| p8 | `docs/lesson-07-proposals/gen/l7-p08-three-warnings-v7.png` |
| p9 | `docs/lesson-07-proposals/gen/l7-p09-steady-stare-v6.png` |
| p12 | `docs/lesson-07-proposals/gen/l7-p12-stomping-parade-v12.png` |

Heights are vertical pixels on the shared raster: **(sole y) − (hood/crown apex y)**. George = **T-rex hood top** (p8–p9) or **vine-crown leaf tips** (p12) → **navy sneaker sole** on the planted foot. Valid canvas y is **0–1023**; feet land ~**y810–860**, not y≈1017.  
Not copied into `lessons/assets/`.

---

## Shared hard fails (all three frames)

| Check | Result | Evidence |
|-------|--------|----------|
| T-rex hood off | **PASS** | p8–p9: tan cracked-scale onesie, dinosaur hood up, bangs visible. p12: green vine crown sits **on** the still-worn hood (leaves over fabric; no bare head). |
| Any beast &lt; 2× George on the same sole y-band | **FAIL (p12)** / **PASS (p8, p9)** | p12 Beak **1.68×** and Goat **1.82×** sit under the 2.0× hard floor; Horn **2.46×** also under 2.0× if measured to horn tips vs a 280 px George. p8 lowest is Beak **2.13×**. p9 lowest is Beak **2.80×**. |
| 4th beast / 6th person | **PASS** | Roster is only George + Horn (bull horns, mane, horizontal stripes) + Beak (red comb, yellow-orange feathers, bird beak) + Goat (spiral ram horns, shaggy pale fur). |
| On-image English | **PASS** | Billy o' Tea sail is a green leaf emblem, not letters; no names, captions, or crown text. |
| Fighting, blood, weapons, wooden fork | **PASS** | Warnings, stare, and parade only. George’s hands are empty. No fork, no wounds. |
| Photoreal / 3D | **PASS** | Cream-paper watercolor with ink cross-hatching; Sendak-mood picture book, not CG. |

---

## Pixel scale sheet

| Page | George (hood/crown → sole) | Horn | Beak | Goat | Sole y-band |
|------|----------------------------|------|------|------|-------------|
| **p8** | hood **y627** → sole **y857** = **230 px** | horn tips **y125**, planted claws **y815** = **690 px → 3.00×** | comb **y220**, talons on log **y710** = **490 px → 2.13×** | ram-horn peaks **y240**, plank claws **y800** = **560 px → 2.43×** | George sand **y857**; Horn plant **y815**; Goat plank **y800** (Δ **57 px**). Beak talons on dead log **y710** (plot perch). |
| **p9** | hood **y635** → sole **y860** = **225 px** | horn tips **y150**, sand **y850** = **700 px → 3.11×** | comb **y190**, sand **y820** = **630 px → 2.80×** | ram-horn top **y87**, sand **y860** = **773 px → 3.44×** | All four in one shore band **y820–860** (Δ **40 px**). |
| **p12** | vine-crown tips **y530** → planted sneaker **y810** = **280 px** (raised stomp foot **y740**) | horn tips **y120**, mud **y810** = **690 px → 2.46×** | comb **y340**, talons **y810** = **470 px → 1.68×** | ram-horn peaks **y320**, planted foot **y810** = **490 px → 1.75×** | Horn / George / Beak / Goat all **y810** — tight clearing band, but beasts undersized vs George. |

Body-anchor line (horizontal through George’s hood/crown top):

| Page | Line | Hits Horn | Hits Beak | Hits Goat |
|------|------|-----------|-----------|-----------|
| p8 | **y627** | **upper thigh / groin** of the stomping figure (readable knee ~y660–670) | feathered **tarsi / knee** on the log perch, not waist | **mid-thigh** (crotch above; knees below) |
| p9 | **y635** | **knee** of the hunched, lowered standing leg | **waist** / base of feathered torso | **mid-thigh** |
| p12 | **y530** | **waist / drum-head** (drum rim **y480–490**), far above knee | **chest / neck** of a short Beak, not waist | **chest / upper torso**, not mid-thigh |

---

## p8 — Three Wild Warnings (`l7-p08-three-warnings-v7.png`)

**Zone:** WildIsland (night shore). **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| Horn hoof makes a sand pit but does not touch George | **PASS** | Horn’s right foot is raised over a deep circular crater (rim ~y800, pit to ~y845); left plant on sand ~y815. George stands far left (~x260) outside the pit — no contact. |
| Beak claws leave marks on dead wood only | **PASS** | Beak stands on a fallen weathered log (~x760–1050); long talons press dead wood at **y710**, not a living trunk. |
| Goat arms block a readable vine bridge into the island | **PASS** | Far right: log-plank walkway with twisted-vine rails/pillars into the jungle; Goat stands in the mouth gripping both vine-wrapped posts (~x1100–1460). |
| George stands steady, empty-handed | **PASS** | Hooded T-rex boy in navy sneakers, profile facing the beasts, both hands empty (no fork). |
| Billy o' Tea behind George | **PASS** | Tea-brown hull and off-white sail with green leaf emblem in the shallows left/behind George; no crew, no letters. |
| Beasts ≥2×, same shore line | **PASS** (2.0× floor) | Horn **3.00×**, Beak **2.13×**, Goat **2.43×** — all over the 2.0× hard floor. George/Horn sand **y815–857**; Goat plank **y800** (low walkway exception). |
| Horn ≥3.0×; hood ≈ knee | **PASS** (ratio) / **FAIL** (knee) | 690/230 = **3.00×** on the nose. Hood **y627** sits at **upper thigh / groin** (~y600), **~30–40 px above** the readable posed knee — knee lock misses. |
| Beak ≥2.2×; hood ≈ waist | **FAIL** | 490/230 = **2.13×**, under **2.2×**. Hood **y627** cuts the **tarsi / knee** on the log, not the waist of a standing 2.2× bird. |
| Goat ≥2.6×; hood ≈ mid-thigh | **FAIL** | 560/230 = **2.43×**, under **2.6×**. Hood **y627** does hit **mid-thigh** (anchor OK) but ratio undershoots. |
| p8 Goat bridge exception | **PASS** | Plank soles **y800**; sand under plank face **y835–857** (Δ **35–57 px**). Low beach-level walkway, not a high terrace. |
| No crown yet | **PASS** | Nothing on the T-rex hood except the costume. |
| Identity / costume | **PASS** | Horn: bull horns, mane, stripes, claws. Beak: comb/wattle, yellow-orange feathers, hooked beak. Goat: ridged ram horns, pale shag. Onesie + hood + tail + navy sneakers. |
| Shared hard fails | **PASS** | No beast under 2.0×. Hood on; no 4th beast; no English; no fight; not 3D. |

**Page verdict:** **FAIL** — story beats land, but Beak **2.13×** and Goat **2.43×** miss the **2.2× / 2.6×** locks; Horn knee anchor misses despite a bare **3.00×** ratio.

---

## p9 — The Steady Stare (`l7-p09-steady-stare-v6.png`)

**Zone:** WildIsland (night shore). **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| George stares into three yellow eyes | **PASS** | George in profile looks up; Horn, Beak, and Goat each show large yellow pupils aimed at him — readable three-way gaze. |
| Horn lowers face/claws first but stays giant | **PASS** | Horn is hunched forward, muzzle and tusks dropped toward George (~x300–650); claws visible but not striking; still tallest figure in frame. |
| Beak claws in (retracted, not striking) | **PASS** | Beak’s long talons hang at its sides / slightly curled inward; no swipe at George. |
| Goat arms down (not blocking) | **PASS** | Goat stands with arms at its sides; no bridge-block spread (correct for p9; bridge not required). |
| No contact | **PASS** | Clear air gap between George and all three beasts. |
| Moon + leaf-sail boat | **PASS** | Full moon upper left (~y100); Billy o' Tea with green leaf emblem in shallows behind George. |
| No crown | **PASS** | Hood only; no vine crown. |
| NOT required: vine bridge, leaf chair, drum | **PASS** | None present; not penalized. |
| Horn ≥3.0×; hood ≈ knee | **PASS** | 700/225 = **3.11×**. Hood **y635** aligns with Horn’s **knee** on the hunched standing leg. |
| Beak ≥2.2×; hood ≈ waist | **PASS** | 630/225 = **2.80×**. Hood **y635** hits Beak **waist** / lower torso. |
| Goat ≥2.6×; hood ≈ mid-thigh | **PASS** | 773/225 = **3.44×**. Hood **y635** hits Goat **mid-thigh**. |
| Sole y-band | **PASS** | George **y860**, Horn **y850**, Beak **y820**, Goat **y860** — one shore band (Δ **40 px**). |
| Identity / costume | **PASS** | Same locked cast + T-rex onesie + navy sneakers. |
| Shared hard fails | **PASS** | All beasts well over 2.0×; hood on; roster clean. |

**Page verdict:** **PASS** — stare beat, de-escalation poses, boat/moon, and all three scale locks meet rubric.

---

## p12 — Stomping Parade (`l7-p12-stomping-parade-v12.png`)

**Zone:** WildClearing (moonlit jungle clearing). **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| Vine crown on hood | **PASS** | Green leaf/vine wreath sits on top of the still-worn T-rex hood; bangs visible beneath. |
| George stomping | **PASS** | Mid-stride march: right knee raised (~y740), left navy sneaker planted **y810**; happy open-mouth expression. |
| Horn wooden drum | **PASS** | Horn beats a barrel drum with rope bindings and two padded mallets (~x80–420). |
| Goat spinning | **PASS** | Goat on one leg, arms out, motion line at waist — dance/spin readable. |
| Beak wings | **PASS** | Beak holds wings spread wide on both sides for rhythm. |
| Pressed footprint rings | **PASS** | Concentric circular stomp tracks pressed into the clearing dirt behind the line (~y650–780). |
| Four figures, happy, claws visible but harmless | **PASS** | All four smiling / gleeful; teeth and claws show without injury. |
| Moon / seedpods OK | **PASS** | Full moon centered top (~y80–150); round spiky seedpod plants along foreground edge. |
| NOT required: leaf chair, boat, vine bridge | **PASS** | None present; not penalized. |
| Horn ≥3.0×; crown ≈ knee | **FAIL** | 690/280 = **2.46×** (under **3.0×**). Crown **y530** lines up with **drum-head / waist** (drum rim **y480–490**), not Horn knee. |
| Beak ≥2.2×; crown ≈ waist | **FAIL** | 470/280 = **1.68×** (under **2.2×** and under **2.0×** hard floor). Crown **y530** hits Beak **chest / neck**. |
| Goat ≥2.6×; crown ≈ mid-thigh | **FAIL** | 490/280 = **1.75×** (under **2.6×** and under **2.0×** hard floor). Crown **y530** hits Goat **chest**, not mid-thigh. |
| George height sanity | **PASS** (measurement) | Crown **y530** → sole **y810** = **280 px** — above typical 180–260 but under the 300 px wrong-landmark ceiling; planted sneaker sole is the correct anchor, not sail or beast shoulder. |
| Shared hard fails | **FAIL** | Beak **1.68×** and Goat **1.75×** under the **2.0×** hard floor on the shared **y810** band. |

**Page verdict:** **FAIL** — parade props and crown track land, but all three beasts undershoot scale locks; Beak and Goat also trip the **&lt;2×** hard fail.

---

## Cross-page continuity

| Item | Result | Evidence |
|------|--------|----------|
| Costume lock p8 → p9 → p12 | **PASS** | Same tan/khaki cracked-scale T-rex onesie, hood, thick tail, navy sneakers; p12 adds vine crown only. |
| Beast identity | **PASS** | Horn stripes + bull horns; Beak comb + bird beak; Goat ram horns + shag — consistent across all three. |
| Zone transition p9 → p12 | **PASS** | p9 shore confrontation → p12 WildClearing parade is a valid beat jump once crowned (crown on in p12). |
| George scale drift | **FAIL** | George **225–230 px** on shore (p8–p9) vs **280 px** in clearing (p12) while beasts shrink relative to him — p12 reads as “big George, small parade partners.” |

---

## Summary table

| Page | File | Verdict | Primary written FAIL |
|------|------|---------|-------------------|
| p8 | `l7-p08-three-warnings-v7.png` | **FAIL** | Beak **2.13×** (&lt;2.2×); Goat **2.43×** (&lt;2.6×); Horn knee anchor miss at **3.00×**. |
| p9 | `l7-p09-steady-stare-v6.png` | **PASS** | — |
| p12 | `l7-p12-stomping-parade-v12.png` | **FAIL** | Beak **1.68×**, Goat **1.75×**, Horn **2.46×** — all under ratio locks; Beak/Goat under **2.0×** hard floor; crown line at Horn waist / Beak chest / Goat chest. |

## VERDICT: FAIL

Failing pages: **p8, p12**. Passing page: **p9**.

Written FAILs (p8 Beak/Goat ratios + Horn knee; p12 all three beasts under scale locks with Beak/Goat under 2.0×) cannot be majority-voted away.

**Redraw note (locks only):** Keep p8’s pit / dead-wood claws / vine-bridge block / boat, and p12’s crown/drum/stomp/spin/wings/pressed rings. On p8, grow Beak and Goat (or shrink George) so Beak ≥**2.2×** with hood at **waist** and Goat ≥**2.6×** with hood at **mid-thigh** on the same sole band; lengthen Horn’s standing leg so hood hits **knee** at ≥**3.0×**. On p12, shrink George toward the **~225 px** shore height **or** enlarge all three beasts so crown-top George is not **280 px** against a **690 px** Horn — target Horn ≥**3.0×**, Beak ≥**2.2×**, Goat ≥**2.6×** with correct body anchors on the **y810** clearing band.
