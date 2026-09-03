# Art review — Lesson 7 Sol p8 v8 / p12 v14 (Grok 4.6, scale)

**Reviewer:** Cursor Grok 4.6 (independent continuity + scale; fresh context; no generation; no branch switch)  
**Date:** 2026-09-03  
**Locks:** `docs/lesson-07-proposals/reviews/ART-RUBRIC-p08-09-12.md` (p8 and p12 sections only), `docs/lesson-07-proposals/bible-locked.md` (scale only), `docs/lesson-07-proposals/plot-working.md` pages 8 and 12  
**Not reviewed:** p9 v6 (already four-PASS).  
**Images Read (real PNG, full 1536×1024), then measured on labeled y-line crops:**

| Page | Path |
|------|------|
| p8 | `docs/lesson-07-proposals/gen/l7-p08-three-warnings-v8.png` |
| p12 | `docs/lesson-07-proposals/gen/l7-p12-stomping-parade-v14.png` |

Heights are vertical pixels on the shared raster: **(sole y) − (apex y)**. Body anchors use a horizontal line at George’s **hood / vine-crown top**. “Looks giant” is not a pass.

George height = **T-rex hood top** (p12: **vine-crown top**) → **navy sneaker sole**. Not the boat sail, not Horn’s shoulder, not the moon. If a span exceeds **300 px**, re-find the boy — on p12 the **303 px** span *is* the boy (leaf-tip crown to planted white sole), not a wrong object.

Scale lock (same mud/sand line; soles in one y-band; no depth-shrink):

| Beast | Ratio vs George | Body anchor |
|-------|-----------------|-------------|
| Horn | ≥ 3.0× | hood/crown top ≈ Horn **knee** |
| Beak | ≥ 2.2× | hood/crown top ≈ Beak **waist** |
| Goat | ≥ 2.6× | hood/crown top ≈ Goat **mid-thigh** |

**p8 exception:** Goat may stand on sand at the bridge mouth; a low beach-level walkway is OK; a raised pier that shrinks Goat is FAIL.

**Not required (do not FAIL for absence):** p12 leaf chair / boat / vine bridge.

Not copied into `lessons/assets/`.

---

## Shared hard fails (both frames)

| Check | Result | Evidence |
|-------|--------|----------|
| T-rex hood off | **PASS** | p8: tan/gold cracked-scale onesie, dinosaur hood up, bangs in the opening, dorsal plates onto a thick tail. p12: green vine-leaf hoop sits **on** the still-worn hood (leaf tips y505, hood fabric ~y525); no bare head. |
| Any beast &lt; 2× George on the same ground line | **FAIL (both)** | p8 Beak **1.93×** (comb y253 → log talons y815) sits under the 2.0× hard floor. p12 Beak **1.41×** and Goat **1.68×** sit under 2.0×; Horn **2.17×** clears 2.0× but not 3.0×. |
| 4th beast / 6th person | **PASS** | Roster is only George + Horn (bull horns, mane, horizontal stripes) + Beak (red comb, yellow-orange feathers, bird beak) + Goat (spiral ram horns, shaggy pale fur). p12 Beak’s two bird legs can look like two masses in a feet crop; the full frame is three beasts. |
| On-image English | **PASS** | p8 Billy o' Tea sail is a green leaf emblem, not letters. p12 has no sail. No names, captions, or crown text. |
| Fighting, blood, weapons, wooden fork | **PASS** | Warnings and parade only. George’s hands are empty (p8: bare hands at sleeve cuffs, no fork). No wounds. |
| Photoreal / 3D | **PASS** | Cream-paper watercolor with ink cross-hatching; Sendak-mood picture book, not CG. |

---

## Pixel scale sheet

| Page | George (hood/crown → sole) | Horn | Beak | Goat | Sole y-band |
|------|----------------------------|------|------|------|-------------|
| **p8** | hood-crest (ochre snout peak) **y594** → planted white sole **y885** = **291 px** (navy uppers y863–881; first warm hood pixels x294–324 at y594–596; y578 is jungle, not ears). Under 300. | horn tips **y135**, planted claws **y885** = **750 px → 2.58×**; head-fur ~y150 = 735 px → 2.53× | comb tips **y253**, talons on log **y815** = **562 px → 1.93×** | ram-horn peaks **y245**, **plank** claw tips **y860** = **615 px → 2.11×** | George sand **y885**; Horn plant **y885**; Goat plank claws **y860**; sand under plank **y885** (Δ **25 px**). Beak talons on log **y815** (plot perch, not a receded extra). |
| **p12** | vine-crown leaf tips **y505** → planted sneaker **y808** = **303 px** (hood fabric **y525** → 283 px; raised stomp sneaker navy ~y717–742). 303 px is the **boy**, not sail/Horn/moon. | horn tips **y150**, mud **y808** = **658 px → 2.17×** (vs hood-only 283 px → 2.33×) | comb tips **y380**, talons **y808** = **428 px → 1.41×** (vs 283 px → 1.51×) | ram-horn / head-tuft apex **y300**, mud **y808** = **508 px → 1.68×** (vs 283 px → 1.80×) | Horn / George / Beak / Goat share **~y808** (Goat spinning lift does not move him to a far plane). |

**>300 px trap (p12):** 303 px is 3 px over the heuristic because the **vine leaves** sit above the hood. Hood-only is **283 px**. Wrong-landmark objects (moon, Horn shoulder, sail) are not in play — p12 has no boat; Horn tips are y150; moon is centered in the sky. Even the generous hood-only George still leaves Beak and Goat under 2.0×.

Body-anchor line (horizontal through George’s hood/crown top):

| Page | Line | Hits Horn | Hits Beak | Hits Goat |
|------|------|-----------|-----------|-----------|
| p8 | **y594** | **mid-thigh / crotch** of the planted striped leg (not knee). Raised stomp thigh is above the line. | **mid-section / hanging-hand band** of this too-short bird — not the waist of a 2.2× Beak (expected waist ~y506 on this comb–talon span is close; the ratio still fails) | **hip / lower torso** — not mid-thigh (35% proxy y645; Δ **51 px**) |
| p12 | **y505** (crown) | **chest / drum-upper** — far above the knee | **upper chest / neck** under the comb (comb itself is y380) — not waist | **chest** of the spinning goat — not mid-thigh |

---

## p8 — Three Wild Warnings (`l7-p08-three-warnings-v8.png`)

**Zone:** WildIsland (night shore). **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| Horn hoof makes a sand pit but does not touch George | **PASS** | Horn’s planted claws sit on sand at **y885**; the other foot is raised over a deep circular crater (between George and the plant). George stands left of the pit — no contact. |
| Beak claws leave marks on dead wood only | **PASS** | Beak stands on a fallen weathered log; long dark talons grip the dead wood at **y815**, not a living trunk being snapped. |
| Goat arms block a readable vine bridge into the island | **PASS** | Far right: plank walkway with braided-rope rails and vine-wrapped posts into the jungle; Goat’s clawed hands rest on the railings / posts at the bridge mouth. Readable bridge, not hanging vines only. |
| George stands steady, empty-handed | **PASS** | Hooded T-rex boy in navy sneakers, three-quarter view facing the beasts; bare hands at sleeve cuffs, no fork. |
| Billy o' Tea behind George | **PASS** | Tea-brown hull and off-white sail with a green leaf emblem sit in the shallows immediately left/behind George; no crew, no letters. |
| Beasts ≥2×, same shore line | **FAIL** | Horn **2.58×**, Goat **2.11×** clear 2.0×. Beak **1.93×** on the log is under the 2.0× hard floor. George/Horn sand **y885**; Goat plank **y860** (see exception). |
| Horn ≥3.0×; hood ≈ knee | **FAIL** | 750/291 = **2.58×**, under **3.0×**. Hood **y594** hits **mid-thigh / crotch**, not the planted knee. |
| Beak ≥2.2×; hood ≈ waist | **FAIL** | 562/291 = **1.93×**, under **2.2×** and under **2.0×**. Hood y594 cuts the **hanging-hand / lower torso** of a bird whose comb is only 562 px above its talons. |
| Goat ≥2.6×; hood ≈ mid-thigh | **FAIL** (ratio / thigh) | Deck-height 615/291 = **2.11×**, under **2.6×** (clears 2.0×). Hood y594 hits **hip / lower torso**, not mid-thigh (proxy y645). |
| p8 Goat bridge exception | **PASS** | Claw tips on the plank **y860**; sand under the plank **y885** (Δ **25 px**). That is a **low beach-level walkway**, not a high terrace used to shrink him. His own-sole ratio still fails 2.6× on size, not on the pier cheat. |
| No crown yet | **PASS** | Nothing on the T-rex hood except costume spikes / snout; no vine hoop. |
| Identity / costume | **PASS** | Horn: bull horns, lion mane, horizontal stripes, claws. Beak: comb/wattle, yellow-orange feathers, hooked beak. Goat: ridged ram horns, pale shag, yellow eyes. Onesie + hood + thick tail + navy sneakers. |
| Shared hard fails | **FAIL** | Beak **1.93×** &lt; 2.0×. Hood on; no 4th beast; no English; no fight; not 3D. |

**Exact miss (cannot be majority-voted away):** On this shore George is **291 px** (hood y594 → soles y885). Horn is **2.58× not ≥3.0×**, with the hood at **crotch / mid-thigh, not knee**. Beak is **1.93× not ≥2.2×** (under the 2.0× hard floor). Goat is **2.11× not ≥2.6×**, with the hood at **hip, not mid-thigh**. Pit, dead-wood claws, vine-bridge block, boat, empty-handed stand, no-crown, and the 25 px low walkway all land.

**VERDICT: FAIL** — locked WildIsland scale does not. Warning beats of pit / log / bridge / boat do.

---

## p12 — Stomping Parade (`l7-p12-stomping-parade-v14.png`)

**Zone:** WildClearing. **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| Vine crown **on** the T-rex hood (hood stays on) | **PASS** | Green pointed-leaf hoop sits on the still-worn hood (leaf tips **y505**, hood fabric **y525**); bangs in the opening; dorsal plates run onto the thick tail. No bare head. |
| George center stomping; four happy figures | **PASS** | George is the mid-line stomp (planted navy sneaker **y808**, raised sneaker ~y717–742). Horn, Beak, and Goat close a four-figure line, grinning / crowing / smiling — happy, not horror. |
| Horn plays the wooden drum | **PASS** | Upright stave drum with rope lattice stands between Horn’s feet; two round-headed mallets in clawed hands. |
| Goat spinning; Beak wings/beat | **PASS** | White concentric motion rings around Goat’s midsection; Goat balances on one leg with the other lifted. Beak’s wings are spread wide and the beak is open on the beat. |
| Real footprint rings (pressed prints, not zen-raked grooves) | **PASS** | Clearing dirt shows a **circular trail of dark depressed footprints** (visible in the Goat-side ground and as a concentric track around the group) plus shadows under planted feet — impressions in mud, not a blank floor. Ribbed seedpods sit in the foreground. |
| Horn ≥3.0× / Beak ≥2.2× / Goat ≥2.6× on **one** clearing mud line | **FAIL** | Crown-top George **303 px**. Horn **658/303 = 2.17×** — under **3.0×** (clears 2.0×). Beak **428/303 = 1.41×**. Goat **508/303 = 1.68×**. Even hood-only George (**283 px**) still leaves Horn **2.33×**, Beak **1.51×**, Goat **1.80×**. Crown y505 hits Horn **chest/drum**, Beak **upper chest**, Goat **chest** — not knee / waist / mid-thigh. |
| Horn hood/crown ≈ knee | **FAIL** | Crown y505 sits at Horn’s **chest / upper drum**, well above the standing knee. |
| Roster = George + Horn + Beak + Goat only | **PASS** | No fourth beast, no family. |
| Happy; claws visible; no harm | **PASS** | Talons/claws readable on all three beasts; no blood, no blow. |
| Silver seedpods + moon | **PASS** | Ribbed pale/grey pods in the foreground plants; full moon centered in the night sky (stars + palm wall). |
| Leaf chair / boat / vine bridge | **n/a — not required** | None in frame. Do not FAIL for that. |
| Shared hard fails | **FAIL** | Beak **1.41×** and Goat **1.68×** &lt; 2.0× vs crown-top George. Hood on; no English; not 3D. |

**Exact miss (cannot be majority-voted away):** Same clearing as George, but Horn is **2.17× not ≥3.0×**, Beak is **1.41× not ≥2.2×**, and Goat is **1.68× not ≥2.6×** (crown-top George **303 px**). Crown at Horn **chest/drum**, Beak **chest**, Goat **chest**. Drum, stomp, spin, wings, crown-on-hood, seedpods, moon, and pressed circular footprints all land.

**VERDICT: FAIL** — locked WildClearing scale does not. Story beats of the parade do.

---

## Summary

| Page | File | VERDICT | Exact miss if FAIL |
|------|------|---------|--------------------|
| p8 | `l7-p08-three-warnings-v8.png` | **FAIL** | George **291 px**. Horn **2.58×** with hood at **crotch / mid-thigh, not knee**. Beak **1.93×** (under 2.0×) with hood at **hands / lower torso, not a 2.2× waist**. Goat **2.11×** / 25 px low walkway land on the pier exception, but hood at **hip, not mid-thigh**. Pit, log, bridge, boat, empty hands, no-crown land. |
| p12 | `l7-p12-stomping-parade-v14.png` | **FAIL** | Crown-top George **303 px**: Horn **2.17×**, Beak **1.41×**, Goat **1.68×**. Crown at Horn chest/drum / Beak chest / Goat chest. Drum, stomp, spin, wings, crown-on-hood, seedpods, moon, and pressed rings land. |

Passing pages: **none**.  
Failing pages: **p8, p12**.

Written FAILs (p8 Beak under 2.0× plus all three under locked ratios/anchors; p12 Beak/Goat under 2.0× and all three under locked ratios) cannot be majority-voted away.

Redraw note (locks only, not a producer prompt): keep p8’s pit / dead-wood claws / vine-bridge block / boat, and p12’s crown/drum/stomp/spin/pressed rings. Restore **Beak ≥2.2× with hood at the waist**, **Goat ≥2.6× with hood at mid-thigh**, **Horn ≥3.0× with hood/crown at the knee**, on the **same sole y-band** as George. On both pages George is already ~290–303 px in frame — do not grow him; raise the beasts (or shrink George in frame) so a 291/303 px boy hits knee / waist / mid-thigh.
