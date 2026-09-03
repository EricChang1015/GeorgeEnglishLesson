# Art review — Lesson 7 Sol p8 v7 / p9 v6 / p12 v12 (Grok 4.6, scale)

**Reviewer:** Cursor Grok 4.6 (independent continuity + scale; fresh context; no generation; no branch switch)  
**Date:** 2026-09-03  
**Locks:** `docs/lesson-07-proposals/reviews/ART-RUBRIC-p08-09-12.md`, `docs/lesson-07-proposals/bible-locked.md` (scale only), `docs/lesson-07-proposals/plot-working.md` pages 8, 9, 12  
**Images Read (real PNG, full frame, 1536×1024), then measured with labeled y-lines on character crops:**

| Page | Path |
|------|------|
| p8 | `docs/lesson-07-proposals/gen/l7-p08-three-warnings-v7.png` |
| p9 | `docs/lesson-07-proposals/gen/l7-p09-steady-stare-v6.png` |
| p12 | `docs/lesson-07-proposals/gen/l7-p12-stomping-parade-v12.png` |

Heights are vertical pixels on the shared raster: **(sole y) − (apex y)**. Body anchors use a horizontal line at George’s **hood / vine-crown top**. “Looks giant” is not a pass.

George height = **T-rex hood top** (p12: **vine-crown top**) → **navy sneaker sole**. Not the boat sail, not Horn’s shoulder, not the moon. If the span exceeds **300 px**, re-find the boy — on p12 the 315 px span *is* the boy (crown tips to planted white sole), not a wrong landmark.

Scale lock (same mud/sand line; soles in one y-band; no depth-shrink):

| Beast | Ratio vs George | Body anchor |
|-------|-----------------|-------------|
| Horn | ≥ 3.0× | hood/crown top ≈ Horn **knee** |
| Beak | ≥ 2.2× | hood/crown top ≈ Beak **waist** |
| Goat | ≥ 2.6× | hood/crown top ≈ Goat **mid-thigh** |

**p8 exception:** Goat may stand on sand at the bridge mouth; a low beach-level walkway is OK; a raised pier that shrinks Goat is FAIL.

**Not required (do not FAIL for absence):** p9 vine bridge / leaf chair; p12 leaf chair / boat / vine bridge.

Not copied into `lessons/assets/`.

---

## Shared hard fails (all three frames)

| Check | Result | Evidence |
|-------|--------|----------|
| T-rex hood off | **PASS** | p8–p9: tan/gold cracked-scale onesie, dinosaur hood up, bangs in the opening, dorsal plates onto a thick tail. p12: green vine crown sits **on** the still-worn hood (hood fabric under the leaves; no bare head). |
| Any beast &lt; 2× George on the same ground line | **FAIL (p12)** / **PASS (p8, p9)** | p12 Beak **1.63×** and Goat **1.90×** sit under the 2.0× hard floor; Horn **2.23×** clears 2.0× but not 3.0×. p8 lowest is Beak **2.95×**. p9 lowest is Beak **3.41×**. |
| 4th beast / 6th person | **PASS** | Roster is only George + Horn (bull horns, mane, horizontal stripes) + Beak (red comb, yellow-orange feathers, bird beak) + Goat (spiral ram horns, shaggy pale fur). A p9 mid-body crop can look like four masses because Horn’s two planted legs read as two torsos; the full frame is three beasts. |
| On-image English | **PASS** | Billy o' Tea sail is a green leaf emblem, not letters; no names, captions, or crown text. |
| Fighting, blood, weapons, wooden fork | **PASS** | Warnings, stare, and parade only. George’s hands are empty. No fork, no wounds. |
| Photoreal / 3D | **PASS** | Cream-paper watercolor with ink cross-hatching; Sendak-mood picture book, not CG. |

---

## Pixel scale sheet

| Page | George (hood/crown → sole) | Horn | Beak | Goat | Sole y-band |
|------|----------------------------|------|------|------|-------------|
| **p8** | hood **y648** → sole **y850** = **202 px** (hood-crest line y648 on the ochre snout peak; navy sneakers + white soles land y848–860, contact **y850**) | horn tips **y90**, planted claws **y850** = **760 px → 3.76×**; head-fur y135 = 715 px → 3.54× | comb tips **y219**, talons on log **y815** = **596 px → 2.95×** | ram-horn peaks **y264**, **plank** claws **y830** = **566 px → 2.80×** | George sand **y850**; Horn plant **y850**; Goat plank **y830**; sand under plank face **y850** (Δ **20 px**). Beak talons on log **y815** (plot perch, not a receded extra). |
| **p9** | hood **y648** → sand **y873** = **225 px** (hood-curve line y648; white soles on y873; y538 is foliage / not the boy) | horn tips **y85**, sand **y873** = **788 px → 3.50×**; head-fur y138 = 735 px → 3.27× | comb **y105**, sand **y873** = **768 px → 3.41×** | ram-horn top **y53**, sand **y873** = **820 px → 3.64×** | All four in one shore band at **y873** (George white-sole contact and beast claw tips on the same red sole-line). |
| **p12** | vine-crown leaf tips **y525** → planted sneaker **y840** = **315 px** (hood fabric **y540** → 300 px; raised stomp sneaker ~y760). 315 px is the **boy**, not sail/Horn/moon. | horn tips **y137**, mud **y840** = **703 px → 2.23×** (vs hood-only 300 px → 2.34×) | comb tips **y326**, talons **y840** = **514 px → 1.63×** (vs 300 px → 1.71×) | ram-horn peaks **y240**, mud **y840** = **600 px → 1.90×** (vs 300 px → 2.00×) | Horn / George / Beak share **~y840**; Goat plant in the same clearing dirt (spinning lift does not move him to a far plane). |

Body-anchor line (horizontal through George’s hood/crown top):

| Page | Line | Hits Horn | Hits Beak | Hits Goat |
|------|------|-----------|-----------|-----------|
| p8 | **y648** | planted-leg **knee** (28% proxy y637, Δ **11 px**). Raised stomp **thigh** also crosses the line. | **lower tarsus / just above scaly ankles** (talons y815; expected waist ~y565) — **not waist** | **hip / bottom of torso / top of legs** — **not mid-thigh** (35% proxy y632 is numerically close; the readable joint is the crotch, not the thigh) |
| p9 | **y648** | **knee** of the hunched standing legs (28% proxy y653, Δ **5 px**); hanging claws at the same band | **mid-torso / waist** of the feathered body (legs begin below the line) | **upper-to-mid thigh** (hanging claws; 3.64× goat puts true mid-thigh a little higher, but the line is in the thigh band) |
| p12 | **y525** (crown) | **lower chest / drum-head / mallet hand** — far above the knee | **upper chest / underside of raised wings** — not waist of a 2.2× bird | **chest** of the spinning goat — not mid-thigh |

---

## p8 — Three Wild Warnings (`l7-p08-three-warnings-v7.png`)

**Zone:** WildIsland (night shore). **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| Horn hoof makes a sand pit but does not touch George | **PASS** | Horn’s right plant is on the sand (claw band **y850**); the left foot is raised over a deep circular crater (rim ~y810, pit toward y900). George stands far left outside the pit — no contact. |
| Beak claws leave marks on dead wood only | **PASS** | Beak stands on a fallen weathered log; long dark talons press the dead wood at **y815**, not a living trunk being snapped. |
| Goat arms block a readable vine bridge into the island | **PASS** | Far right: log-plank walkway with twisted-vine / rope rails and vine-wrapped posts into the jungle; Goat stands in the mouth with both arms on the posts. Readable bridge, not hanging vines only. |
| George stands steady, empty-handed | **PASS** | Hooded T-rex boy in navy sneakers, profile facing the beasts, both hands empty at his sides (no fork). |
| Billy o' Tea behind George | **PASS** | Tea-brown hull and off-white sail with a green leaf emblem sit in the shallows immediately left/behind George; no crew, no letters. |
| Beasts ≥2×, same shore line | **PASS** (2.0× floor) | Horn **3.76×**, Beak **2.95×**, Goat **2.80×** — all over the 2.0× hard floor. George/Horn sand **y850**; Goat plank **y830** (see exception). Beak is on the plot log (**y815**), which raises him rather than shrinking him. |
| Horn ≥3.0×; hood ≈ knee | **PASS** | 760/202 = **3.76×** (head-fur **3.54×**), over **3.0×**. Hood **y648** vs planted-knee proxy **y637** (Δ 11 px). The raised stomp thigh also crosses y648; the locked joint of the planted giant hits. |
| Beak ≥2.2×; hood ≈ waist | **PASS** (ratio) / **FAIL** (waist) | 596/202 = **2.95×**, over **2.2×**. Hood y648 cuts **just above the scaly ankles / lower tarsus** (talons **y815**), not the waist of a standing 2.2× bird (expected waist ~y565). |
| Goat ≥2.6×; hood ≈ mid-thigh | **PASS** (ratio) / **FAIL** (mid-thigh) | Deck-height 566/202 = **2.80×**, over **2.6×**. Hood y648 hits **hip / bottom of torso**, not mid-thigh. |
| p8 Goat bridge exception | **PASS** | Soles on the plank **y830**; sand under the plank face **y850** (Δ **20 px**). That is a **low beach-level walkway**, not a high terrace used to shrink him. His own-sole ratio already meets 2.80×. |
| No crown yet | **PASS** | Nothing on the T-rex hood except the costume spikes; no vine hoop. |
| Identity / costume | **PASS** | Horn: bull horns, lion mane, horizontal stripes, claws. Beak: comb/wattle, yellow-orange feathers, hooked beak. Goat: ridged ram horns, pale shag, yellow eyes. Onesie + hood + thick tail + navy sneakers. |
| Shared hard fails | **PASS** | No beast under 2.0×. Hood on; no 4th beast; no English; no fight; not 3D. |

**Exact miss (cannot be majority-voted away):** On this shore George is **202 px** (hood y648 → soles y850). Horn is a true **3.76×** with the hood at the **planted knee**. Beak is **2.95×** on the log but the hood line hits **ankles / lower tarsus, not waist**. Goat is **2.80×** on a legal 20 px walkway but the hood line hits **hip, not mid-thigh**. Pit, dead-wood claws, vine-bridge block, boat, empty-handed stand, and no-crown all land.

**VERDICT: FAIL** — Beak waist anchor and Goat mid-thigh anchor miss. Ratio floors for all three beasts, Horn knee, warnings, bridge, and boat all land.

---

## p9 — The Steady Stare (`l7-p09-steady-stare-v6.png`)

**Zone:** WildIsland (night shore). **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| George looks into the three yellow eyes (stare) | **PASS** | George at the waterline, head tipped up toward Horn. Horn, Beak, and Goat all show large yellow irises with pupils in the same frame; no fist is raised. |
| Horn lowers first (head/claws) but body stays giant (hood at knee, ≥3×) | **PASS** | Horn leans in, yellow eyes aimed **down** at George; near arms hang with claws not in a strike. Beak and Goat stay upright behind him. Standing height **788/225 = 3.50×**; hood **y648** sits on Horn’s **knee** (proxy y653). |
| Beak claws in; Goat arms no longer blocking as the threat | **PASS** | Beak’s feathered arms/claws hang beside the body (not on the p8 log). Goat stands on the open sand with arms **down** at the torso — no vine-bridge block in this frame. |
| No crown; no contact / no magic glow | **PASS** | T-rex hood only; a gap of sand between boy and beasts; no sparkle, beam, or touch. |
| Moonlit night; leaf-sail boat still at shore | **PASS** | Full moon upper-left, dark blue sky, palm wall. Billy o' Tea with the green-leaf sail remains in the left shallows beside George. |
| Horn ≥3.0×; hood ≈ knee; same ground line | **PASS** | George **225 px** (hood y648 → sand y873). Horn **788 px → 3.50×** (head-fur **3.27×**). Hood y648 ≈ knee. One shore band at **y873**. |
| Beak ≥2.2×; hood ≈ waist | **PASS** | 768/225 = **3.41×**, well over **2.2×**. Hood y648 cuts the **mid-torso / waist** of the feathered body. |
| Goat ≥2.6×; hood ≈ mid-thigh | **PASS** | 820/225 = **3.64×**. Hood y648 sits in the goat-body **thigh** band with arms hanging. |
| Vine bridge / leaf chair | **n/a — not required** | Neither is in frame. Do not FAIL for that. |
| Identity / costume | **PASS** | Same three-beast locks; hood on; navy sneakers, white soles on the y873 sand. |
| Shared hard fails | **PASS** | No hood-off, no 4th beast, no English, no fight, not 3D. Every beast ≥ 3.4×. |

**Soft (not FAIL):** Type ladder is inverted — Goat **3.64×** &gt; Horn **3.50×** &gt; Beak **3.41×** (bible wants Horn &gt; Goat &gt; Beak). All three still clear their numeric floors, and the hood line hits the locked joints. Do not shrink George to “fix” this; he is already 225 px.

**Note on the &gt;300 px trap:** A hood reading near **y538** is **foliage behind the boy**, not the T-rex hood. Overlay on the boy puts hood-curve at **y648** and sand contact at **y873** (225 px).

**VERDICT: PASS**

---

## p12 — Stomping Parade (`l7-p12-stomping-parade-v12.png`)

**Zone:** WildClearing. **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| Vine crown **on** the T-rex hood (hood stays on) | **PASS** | Green pointed-leaf hoop sits on the still-worn hood (leaf tips **y525**, hood fabric **y540**); bangs in the opening; dorsal plates run onto the thick tail. No bare head. |
| George center stomping; four happy figures | **PASS** | George is the mid-foreground stomp (planted navy sneaker **y840**, raised sneaker ~y760). Horn, Beak, and Goat close a four-figure line, grinning / singing — happy, not horror. |
| Horn plays the wooden drum | **PASS** | Upright hollow wooden drum with rope lattice sits between Horn’s feet; two round-headed mallets in clawed hands (drum-head band at the crown line). |
| Goat spinning; Beak wings/beat | **PASS** | White motion rings around Goat’s torso; Goat is in a twist with claws out. Beak’s wings are spread high and the beak is open on the beat. |
| Real footprint rings (pressed prints, not zen-raked grooves) | **PASS** | Clearing floor shows **dark depressed footprints** (three-toed / diamond stamps) packed into a curving / circular track behind George — impressions in mud, not a smooth zen garden. Ribbed seedpods sit in the foreground. |
| Horn ≥3.0× / Beak ≥2.2× / Goat ≥2.6× on **one** clearing mud line | **FAIL** | Crown-top George **315 px**. Horn **703/315 = 2.23×** — under **3.0×** (clears 2.0×). Beak **514/315 = 1.63×**. Goat **600/315 = 1.90×**. Even the generous hood-only George (**300 px**) still leaves Horn **2.34×**, Beak **1.71×**, Goat **2.00×**. Crown y525 hits Horn **chest/drum**, Beak **upper chest**, Goat **chest** — not knee / waist / mid-thigh. |
| Horn hood/crown ≈ knee | **FAIL** | Crown y525 sits at the **drum head / Horn lower chest / mallet**, well above the standing knee. |
| Roster = George + Horn + Beak + Goat only | **PASS** | No fourth beast, no family. |
| Happy; claws visible; no harm | **PASS** | Talons/claws readable on all three beasts; no blood, no blow. |
| Silver seedpods + moon | **PASS** | Ribbed pale/grey pods in the foreground plants; full moon centered in the night sky. |
| Leaf chair / boat / vine bridge | **n/a — not required** | None in frame. Do not FAIL for that. |
| Shared hard fails | **FAIL** | Beak **1.63×** and Goat **1.90×** &lt; 2.0× vs crown-top George. Hood on; no English; not 3D. |

**Exact miss (cannot be majority-voted away):** Same clearing as George, but Horn is **2.23× not ≥3.0×**, Beak is **1.63× not ≥2.2×**, and Goat is **1.90× not ≥2.6×** (crown-top George **315 px**). Crown at Horn **chest/drum**, Beak **chest**, Goat **chest**. Drum, stomp, spin, wings, crown-on-hood, seedpods, moon, and pressed footprint rings all land.

**VERDICT: FAIL** — locked WildClearing scale does not. Story beats of the parade do.

---

## Adjacent continuity (p8 → p9, same WildIsland shore)

| Check | Result | Evidence |
|-------|--------|----------|
| Night / boat / cast | **PASS** | Same moonlit palm shore, leaf-sail Billy o' Tea at left, same three beasts in Horn–Beak–Goat order. |
| Beat change | **PASS** | p8 = three separate warnings (pit / dead wood / blocked bridge). p9 = Horn bowed in, claws in, Goat off the bridge with arms down. Causal turn is readable. |
| Scale continuity | **SOFT** | George is **202 px** on p8 and **225 px** on p9 (close). Horn stays giant (3.76× → 3.50×). Beak 2.95× log-perch → 3.41× standing bird; Goat 2.80× → 3.64×. p8’s missing waist/mid-thigh pictures become p9 hits mainly because p9 draws longer beast legs, not because George shrank. |

p12 is a new Zone (WildClearing); moon + three-beast identities + T-rex + (new) vine crown match the crown track. Scale undershoots Beak and Goat under the 2.0× hard floor and Horn under 3.0×.

---

## Summary

| Page | File | VERDICT | Exact miss if FAIL |
|------|------|---------|--------------------|
| p8 | `l7-p08-three-warnings-v7.png` | **FAIL** | Horn **3.76×** with hood at **planted knee** (lands). Beak **2.95×** but hood at **ankles / lower tarsus, not waist**. Goat **2.80×** / 20 px low walkway land on ratio, but hood at **hip, not mid-thigh**. |
| p9 | `l7-p09-steady-stare-v6.png` | **PASS** | — |
| p12 | `l7-p12-stomping-parade-v12.png` | **FAIL** | Crown-top George **315 px**: Horn **2.23×**, Beak **1.63×**, Goat **1.90×**. Crown at Horn chest/drum / Beak chest / Goat chest. Drum, stomp, spin, wings, crown-on-hood, and pressed rings land. |

Passing page: **p9**.  
Failing pages: **p8, p12**.

Written FAILs (p8 Beak waist + Goat mid-thigh; p12 Beak/Goat under 2.0× and all three under locked ratios) cannot be majority-voted away.

Redraw note (locks only, not a producer prompt): keep p8’s pit / dead-wood claws / vine-bridge block / boat, and p12’s crown/drum/stomp/spin/pressed rings. Restore **Beak ≥2.2× with hood at the waist** (p8 needs a standing waist at y648, not a tarsus ankle), **Goat ≥2.6× with hood at mid-thigh**, and on p12 **Horn ≥3.0× with crown at the knee**, **Beak ≥2.2× with crown at the waist**, **Goat ≥2.6× with crown at mid-thigh** on the **same sole y-band** as George. On p12, shrink George in frame (he is 315 px) or raise all three beasts so crown-top George is not 315 px against a 703 px Horn.
