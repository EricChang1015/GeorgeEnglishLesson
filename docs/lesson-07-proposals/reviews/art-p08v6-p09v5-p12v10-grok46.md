# Art review — Lesson 7 Sol p8 v6 / p9 v5 / p12 v10 (Grok 4.6, scale)

**Reviewer:** Cursor Grok 4.6 (independent continuity + scale; fresh context; no generation; no branch switch)  
**Date:** 2026-09-02  
**Locks:** `docs/lesson-07-proposals/reviews/ART-RUBRIC-p08-09-12.md` (checklist only — files below are newer than the rubric table), `docs/lesson-07-proposals/bible-locked.md` (character + scale), `docs/lesson-07-proposals/plot-working.md` pages 8, 9, 12  
**Images Read (real PNG, full frame, 1536×1024), then measured with labeled y-lines on character crops:**

| Page | Path |
|------|------|
| p8 | `docs/lesson-07-proposals/gen/l7-p08-three-warnings-v6.png` |
| p9 | `docs/lesson-07-proposals/gen/l7-p09-steady-stare-v5.png` |
| p12 | `docs/lesson-07-proposals/gen/l7-p12-stomping-parade-v10.png` |

Heights are vertical pixels on the shared raster: **(sole y) − (apex y)**. Body anchors use a horizontal line at George’s **hood / vine-crown top**. “Looks giant” is not a pass.

Scale lock (same mud/sand line; soles in one y-band; no depth-shrink):

| Beast | Ratio vs George | Body anchor |
|-------|-----------------|-------------|
| Horn | ≥ 3.0× | hood/crown top ≈ Horn **knee** |
| Beak | ≥ 2.2× | hood/crown top ≈ Beak **waist** |
| Goat | ≥ 2.6× | hood/crown top ≈ Goat **mid-thigh** |

**p8 exception:** Goat may stand on sand at the bridge mouth; a low beach-level walkway is OK; a raised pier that shrinks Goat is FAIL.

Not copied into `lessons/assets/`.

---

## Shared hard fails (all three frames)

| Check | Result | Evidence |
|-------|--------|----------|
| T-rex hood off | **PASS** | p8–p9: tan cracked-scale onesie, dinosaur hood up, bangs in the opening. p12: green vine crown sits **on** the still-worn hood (hood fabric under the leaves; no bare head). |
| Any beast &lt; 2× George on the same ground line | **FAIL (p12)** / **PASS (p8, p9)** | p12 Beak **1.30×** and Goat **1.43×** (crown-top George) sit under the 2.0× hard floor; Horn **1.84×** also under 2.0×. p8 lowest is Beak **2.28×**. p9 lowest is Beak **3.11×**. |
| 4th beast / 6th person | **PASS** | Roster is only George + Horn (bull horns, mane, horizontal stripes) + Beak (red comb, yellow-orange feathers, bird beak) + Goat (spiral ram horns, shaggy pale fur). |
| On-image English | **PASS** | Billy o' Tea sail is a green leaf emblem, not letters; no names, captions, or crown text. |
| Fighting, blood, weapons, wooden fork | **PASS** | Warnings, stare, and parade only. George’s hands are empty. No fork, no wounds. |
| Photoreal / 3D | **PASS** | Cream-paper watercolor with ink cross-hatching; Sendak-mood picture book, not CG. |

---

## Pixel scale sheet

| Page | George (hood/crown → sole) | Horn | Beak | Goat | Sole y-band |
|------|----------------------------|------|------|------|-------------|
| **p8** | hood **y620** → sole **y835** = **215 px** (magenta hood-line skims the hood peak; navy sneakers + white soles land on y835) | horn tips **y125**, planted claws **y800** = **675 px → 3.14×**; head-fur y148 = 652 px → 3.03× | comb tips **y220**, talons on log **y710** = **490 px → 2.28×** | ram-horn peaks **y240**, **plank** claws **y800** = **560 px → 2.60×** | George sand **y835**; Horn plant **y800**; Goat plank **y800**; sand under plank face **y835** (Δ **35 px**). Beak talons on log **y710** (plot perch, not a receded extra). |
| **p9** | hood **y685** → sand **y920** = **235 px** (hood-curve line y685; spike tips ~y670; white soles in y910–920) | horn tips **y150**, sand **y920** = **770 px → 3.28×**; head-fur ~y201 = 719 px → 3.06× | comb **y190**, sand **y920** = **730 px → 3.11×** | ram-horn top **y87**, sand **y920** = **833 px → 3.54×** | All four in one shore band at **y920** (George white-sole contact ~y910–915; beast claw tips in the same sand). |
| **p12** | vine-crown leaf tips **y450** → planted sneaker **y820** = **370 px** (hood fabric **y490** → 330 px; raised stomp sneaker **y740**) | horn tips **y120**, mud **y800** = **680 px → 1.84×** (vs hood-only 330 px → 2.06×) | comb tips **y340**, talons **y820** = **480 px → 1.30×** (vs 330 px → 1.45×) | ram-horn peaks **y320**, mud **y850** = **530 px → 1.43×** (vs 330 px → 1.61×) | Horn **y800**, George/Beak **y820**, Goat **y850** — **50 px** spread, not one tight clearing band. |

Body-anchor line (horizontal through George’s hood/crown top):

| Page | Line | Hits Horn | Hits Beak | Hits Goat |
|------|------|-----------|-----------|-----------|
| p8 | **y620** | **upper thigh / groin** of the stomping figure (groin ~y600, posed planted knee ~y660–670). Unbent size-proxy knee would be ~y611, but the readable joint is the posed knee — lock is visual. | feather/scale junction of the standing tarsi (**knee**, not waist); hanging claw tips also at this line | **mid-thigh** (crotch above the line; knees below) |
| p9 | **y685** | **knee** of the hunched standing leg | **waist** / base of the feathered torso on this tall drawing | **mid-thigh** |
| p12 | **y450** (crown) / **y490** (hood) | **waist / drum-head** (drum top **y490**), far above the knee | **chest / neck** of a short Beak, not waist of a 2.2× bird | **chest / upper torso**, not mid-thigh |

---

## p8 — Three Wild Warnings (`l7-p08-three-warnings-v6.png`)

**Zone:** WildIsland (night shore). **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| Horn hoof makes a sand pit but does not touch George | **PASS** | Horn’s left plant is on the sand (claw band **y800**, ~x480–650); the right foot is raised over a deep circular crater (rim ~y800, pit to ~y845). George stands far left (~x260–310) outside the pit — no contact. |
| Beak claws leave marks on dead wood only | **PASS** | Beak stands on a fallen weathered log (~x760–1050); long dark talons press the dead wood at **y710**, not a living trunk being snapped. |
| Goat arms block a readable vine bridge into the island | **PASS** | Far right: log-plank walkway with twisted-vine rails/pillars into the jungle; Goat stands in the mouth with both arms on the vine posts (~x1100–1460). Readable bridge, not hanging vines only. |
| George stands steady, empty-handed | **PASS** | Hooded T-rex boy in navy sneakers, profile facing the beasts, both hands empty (no fork). |
| Billy o' Tea behind George | **PASS** | Tea-brown hull and off-white sail with a green leaf emblem sit in the shallows immediately left/behind George; no crew, no letters. |
| Beasts ≥2×, same shore line | **PASS** (2.0× floor) / mixed line | Horn **3.14×**, Beak **2.28×**, Goat **2.60×** — all over the 2.0× hard floor. George/Horn sand **y800–835**; Goat plank **y800** (see exception). Beak is on the plot log (**y710**), which raises him rather than shrinking him. |
| Horn ≥3.0×; hood ≈ knee | **PASS** (ratio) / **FAIL** (knee) | 675/215 = **3.14×** (head-fur 3.03×), over **3.0×**. Hood **y620** sits at **upper thigh / groin** (groin ~y600; posed planted knee ~y660–670) — **~40–50 px above** the readable knee, so the knee picture misses. Height is in torso + horns on short legs. |
| Beak ≥2.2×; hood ≈ waist | **PASS** (ratio) / **FAIL** (waist) | 490/215 = **2.28×**, over **2.2×**. Hood y620 cuts the **feather/scale knee** of the tarsi (talons **y710**), not the waist of a standing 2.2× bird (expected waist ~y490–520). |
| Goat ≥2.6×; hood ≈ mid-thigh | **PASS** | Deck-height 560/215 = **2.60×** on the nose. Hood y620 hits Goat **mid-thigh**. |
| p8 Goat bridge exception | **PASS** | Soles on the plank **y800**; sand under the plank face **y835** (Δ **35 px**). That is a **low beach-level walkway**, not a high terrace used to shrink him. His own-sole ratio already meets 2.60×. |
| No crown yet | **PASS** | Nothing on the T-rex hood except the costume. |
| Identity / costume | **PASS** | Horn: bull horns, lion mane, horizontal stripes, claws. Beak: comb/wattle, yellow-orange feathers, hooked beak. Goat: ridged ram horns, pale shag, yellow eyes. Onesie + hood + thick tail + navy sneakers. |
| Shared hard fails | **PASS** | No beast under 2.0×. Hood on; no 4th beast; no English; no fight; not 3D. |

**Exact miss (cannot be majority-voted away):** On this shore George is **215 px** (hood y620 → soles y835). Horn is a true **3.14×** by horn-tip height, but the hood line hits **upper thigh, not knee**. Beak is **2.28×** on the log but the hood line hits **knee, not waist**. Goat **2.60×** with hood at mid-thigh, and the 35 px plank is a legal low walkway. Pit, dead-wood claws, vine-bridge block, boat, and empty-handed stand all land.

**VERDICT: FAIL** — Horn knee anchor and Beak waist anchor miss. Ratio floors for all three beasts, Goat mid-thigh, warnings, bridge, and boat all land.

---

## p9 — The Steady Stare (`l7-p09-steady-stare-v5.png`)

**Zone:** WildIsland (night shore). **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| George looks into the three yellow eyes (stare) | **PASS** | George at the waterline, head tipped up toward Horn. Horn, Beak, and Goat all show large yellow irises with pupils in the same frame; no fist is raised. |
| Horn lowers first (head/claws) but body stays giant (hood at knee, ≥3×) | **PASS** | Horn is slightly hunched, face turned down toward George (horn tips still **y150**). Beak and Goat stay upright behind him. Near arm hangs; claws are not in a strike. Standing height **770/235 = 3.28×**; hood **y685** sits on Horn’s **knee**. |
| Beak claws in; Goat arms no longer blocking as the threat | **PASS** | Beak’s feathered arms/claws hang beside the body (not on the p8 log). Goat stands on the open sand with arms at the torso — no vine-bridge block remains in this frame. |
| No crown; no contact / no magic glow | **PASS** | T-rex hood only; a gap of sand between boy and beasts; no sparkle, beam, or touch. |
| Moonlit night; leaf-sail boat still at shore | **PASS** | Full moon upper-left, dark blue sky, palm wall. Billy o' Tea with the green-leaf sail remains in the left shallows beside George. |
| Horn ≥3.0×; hood ≈ knee; same ground line | **PASS** | George **235 px** (hood y685 → sand y920). Horn **770 px → 3.28×** (head-fur **3.06×**). Hood y685 ≈ knee. One shore band at **y920**. |
| Beak ≥2.2×; hood ≈ waist | **PASS** | 730/235 = **3.11×**, well over **2.2×**. Hood y685 cuts the **waist** of this tall drawing. |
| Goat ≥2.6×; hood ≈ mid-thigh | **PASS** | 833/235 = **3.54×**. Hood y685 sits in the goat-body **mid-thigh**. |
| Identity / costume | **PASS** | Same three-beast locks; hood on; navy sneakers, white soles into the y910–920 sand. |
| Shared hard fails | **PASS** | No hood-off, no 4th beast, no English, no fight, not 3D. Every beast ≥ 3.1×. |

**Soft (not FAIL):** Type ladder is inverted — Goat **3.54×** &gt; Horn **3.28×** &gt; Beak **3.11×** (bible wants Horn &gt; Goat &gt; Beak). All three still clear their numeric floors, and the hood line hits the locked joints. Do not shrink George to “fix” this; he is already 235 px.

**Note vs a prior p9 v5 remeasure that used George hood y538 / height 358 px:** y538 is in the **monster-shoulder / sail** band, not George’s hood. Overlay on the boy puts hood-curve at **y685** and sand contact at **y920**. That 538/358 reading is a wrong landmark, not a second scale on this file.

**VERDICT: PASS**

---

## p12 — Stomping Parade (`l7-p12-stomping-parade-v10.png`)

**Zone:** WildClearing. **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| Vine crown **on** the T-rex hood (hood stays on) | **PASS** | Green pointed-leaf hoop sits on the still-worn hood (leaf tips **y450**, hood fabric **y490**); bangs in the opening; dorsal plates run onto the thick tail. No bare head. |
| George center stomping; four happy figures | **PASS** | George is the mid-foreground stomp (planted navy sneaker **y820**, raised sneaker **y740**). Horn, Beak, and Goat close a four-figure line, grinning / singing — happy, not horror. |
| Horn plays the wooden drum | **PASS** | Upright hollow wooden drum with rope lattice sits between Horn’s feet (drum head **y490**, at Horn’s waist); two round-headed sticks in clawed hands. |
| Goat spinning; Beak wings/beat | **PASS** | White motion arc across Goat’s torso; Goat is on one planted leg (sole **y850**) with the other lifted. Beak’s wings are spread and the beak is open on the beat. |
| Real footprint rings (pressed prints, not zen-raked grooves) | **PASS** | Clearing floor shows **dark depressed footprints** packed into a large curving / circular track — impressions in mud (claw, talon, hoof, and sneaker stamps), not smooth zen-raked grooves. |
| Horn ≥3.0× / Beak ≥2.2× / Goat ≥2.6× on **one** clearing mud line | **FAIL** | Crown-top George **370 px**. Horn **680/370 = 1.84×** — under **3.0×** and under the **2.0×** hard floor. Beak **480/370 = 1.30×**. Goat **530/370 = 1.43×**. Even the generous hood-only George (**330 px**) still leaves Horn **2.06×**, Beak **1.45×**, Goat **1.61×**. Crown y450 / hood y490 hit Horn **waist/drum-head**, Beak **chest**, Goat **chest** — not knee / waist / mid-thigh. Soles span **y800–850** (50 px), not one tight mud band. |
| Horn hood/crown ≈ knee | **FAIL** | Crown y450 and hood y490 sit at the **drum head (y490) / Horn waist**, well above the standing knee. |
| Roster = George + Horn + Beak + Goat only | **PASS** | No fourth beast, no family. |
| Happy; claws visible; no harm | **PASS** | Talons/claws readable on all three beasts; no blood, no blow. |
| Silver seedpods + moon | **PASS** | Ribbed pale/grey pods hang in the canopy and sit in the foreground plants; full moon centered in the night sky. |
| Shared hard fails | **FAIL** | All three beasts &lt; 2.0× vs crown-top George. Hood on; no English; not 3D. |

**Exact miss (cannot be majority-voted away):** Same clearing as George, but Horn is **1.84× not ≥3.0×**, Beak is **1.30× not ≥2.2×**, and Goat is **1.43× not ≥2.6×** (crown-top George **370 px**). Crown/hood at Horn **waist**, Beak **chest**, Goat **chest**. Drum, stomp, spin, wings, crown-on-hood, seedpods, moon, and pressed footprint rings all land.

**VERDICT: FAIL** — locked WildClearing scale does not. Story beats of the parade do.

---

## Adjacent continuity (p8 → p9, same WildIsland shore)

| Check | Result | Evidence |
|-------|--------|----------|
| Night / boat / cast | **PASS** | Same moonlit palm shore, leaf-sail Billy o' Tea at left, same three beasts in Horn–Beak–Goat order. |
| Beat change | **PASS** | p8 = three separate warnings (pit / dead wood / blocked bridge). p9 = Horn bowed in, claws in, Goat off the bridge. Causal turn is readable. |
| Scale continuity | **SOFT** | George is **215 px** on p8 and **235 px** on p9 (close). Horn stays giant (3.14× → 3.28×). Beak jumps from a 2.28× log-perch to a 3.11× standing bird; Goat from 2.60× to 3.54×. p8’s missing knee/waist pictures become p9 hits mainly because p9 draws longer beast legs, not because George shrank. |

p12 is a new Zone (WildClearing); moon + three-beast identities + T-rex + (new) vine crown match the crown track. Scale undershoots all three beasts under the 2.0× hard floor.

---

## Summary

| Page | File | VERDICT | Exact miss if FAIL |
|------|------|---------|--------------------|
| p8 | `l7-p08-three-warnings-v6.png` | **FAIL** | Horn **3.14×** but hood at **upper thigh, not knee**; Beak **2.28×** but hood at **knee, not waist**. Goat **2.60×** / mid-thigh / 35 px low walkway all land. |
| p9 | `l7-p09-steady-stare-v5.png` | **PASS** | — |
| p12 | `l7-p12-stomping-parade-v10.png` | **FAIL** | Crown-top George **370 px**: Horn **1.84×**, Beak **1.30×**, Goat **1.43×** (all &lt; 2.0×). Crown at Horn waist / Beak chest / Goat chest. Drum, stomp, spin, wings, crown-on-hood, and pressed rings land. |

Passing page: **p9**.  
Failing pages: **p8, p12**.

Written FAILs (p8 Horn knee + Beak waist; p12 all three beasts under 2.0×) cannot be majority-voted away.

Redraw note (locks only, not a producer prompt): keep p8’s pit / dead-wood claws / vine-bridge block / boat, and p12’s crown/drum/stomp/spin/pressed rings. Restore **Horn ≥3.0× with hood/crown at the knee** (p8 needs longer standing legs, not just longer horns), **Beak ≥2.2× with hood/crown at the waist** (p8 needs a standing waist at y620, not a tarsus knee), and **Goat ≥2.6× with hood/crown at mid-thigh** on the **same sole y-band** as George. On p12, shrink George in frame or raise all three beasts so crown-top George is not 370 px against a 680 px Horn.
