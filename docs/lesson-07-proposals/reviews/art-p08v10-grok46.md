# Art review — Lesson 7 p8 v10 (Grok 4.6, scale)

**Reviewer:** Cursor Grok 4.6 (independent continuity + scale; fresh context; no generation; no branch switch)  
**Date:** 2026-09-03  
**Locks:** `docs/lesson-07-proposals/reviews/ART-RUBRIC-p08-09-12.md` (p8 section), `docs/lesson-07-proposals/bible-locked.md` (scale only), `docs/lesson-07-proposals/plot-working.md` page 8  
**Not reviewed:** p9, p12, any other v10-adjacent frame.  
**Image Read (real PNG, full 1536×1024), then measured on character strips, hood/sole overlays, joint-band crops, and dark-vs-sand y-profiles:**

| Page | Path |
|------|------|
| p8 | `docs/lesson-07-proposals/gen/l7-p08-three-warnings-v10.png` |

Heights are vertical pixels on the shared raster: **(sole y) − (apex y)**. Body anchors use a horizontal line at George’s **T-rex hood top**. “Looks giant” is not a pass.

George height = **T-rex hood top → navy sneaker sole** (white/cream outsole contact included). Not the boat sail, not Horn’s shoulder, not the moon. If a span exceeds **300 px**, re-find the boy.

**Scale rule:** body anchors are the **MINIMUM** size picture. If a beast is **taller** than the lock, the hood sitting **below** that joint is **PASS**. FAIL only when the beast is **too short** (ratio under the floor, **or** hood **above** the named joint).

| Beast | Ratio floor | Min landmark |
|-------|-------------|--------------|
| Horn | ≥ 3.0× | hood at or below Horn **knee** |
| Beak | ≥ 2.2× | hood at or below Beak **waist** |
| Goat | ≥ 2.6× | hood at or below Goat **mid-thigh** |

Same sole y-band. Canvas **1536×1024**. Valid y is **0–1023**.

**p8 exception:** Goat may stand on sand at the bridge mouth; a low beach-level walkway is OK; a raised pier that shrinks Goat is FAIL.

Not copied into `lessons/assets/`.

---

## Shared hard fails

| Check | Result | Evidence |
|-------|--------|----------|
| T-rex hood off | **PASS** | Tight head crop (`x250–380, y610–720`): tan/gold cracked-scale dinosaur hood is **on**; short black bangs in the opening; yellow hood-line at **y644** grazes the snout/crest. Not a bare head. No vine hoop. |
| Any beast &lt; 2× George on the same ground line | **PASS** | Lowest ratio this frame: Goat **3.09×** (conservative lit-fur/head **y199** → sand **y856**). Horn **3.75–3.78×**, Beak **3.56–3.58×**. All clear the 2.0× hard floor. |
| 4th beast / 6th person | **PASS** | Roster is only George + Horn (bull horns, mane, striped/chevron fur, yellow eyes) + Beak (red comb, yellow-orange feathers, hooked beak) + Goat (spiral ram horns, shaggy pale/tan fur, yellow eyes). |
| On-image English | **PASS** | Billy o' Tea sail is a green leaf emblem, not letters. No names, captions, or crown text. |
| Fighting, blood, weapons, wooden fork | **PASS** | Warnings only. George’s hands are empty at the sleeve cuffs. No wounds. Beak’s dead-wood trunk is a claw-mark prop, not a swung weapon. |
| Photoreal / 3D | **PASS** | Cream-paper watercolor with ink cross-hatching; Sendak-mood picture book, not CG. |

---

## Pixel scale sheet

George landmark hunt (left-shore boy, not the sail): first ochre snout pixels at **x300–301, y644**; navy uppers dense **y836–852**; last substantial dark at the planted sneaker **y856**; sand dominates from **y858**. Span **856 − 644 = 212 px**. Under 300.

| Page | George (hood → sole) | Horn | Beak | Goat | Sole y-band |
|------|----------------------|------|------|------|-------------|
| **p8** | hood-crest (first ochre x300–301) **y644** → planted navy/outsole **y856** = **212 px**. Navy uppers **y836–852**; sand from **y858**. | clustered horn-keratin tip **y55–61** (x618–624; overlay red **y61** sits on the visible tip), planted sand **y856** = **795–801 px → 3.75–3.78×** | comb-red tips **y98** (x909–910), talons/sand drop **y850–856** = **754–758 px → 3.56–3.58×** | ram-horn crest **y100** (Goat-strip orange line on the dark spiral tips); lit fur/head keratin **y199**; plank claws **y830–856** = **657–756 px → 3.09–3.57×** | George sand **y856**; Horn plant **y856** (Δ **0**); Beak talons **y850–856** (Δ **0–6 px**); Goat claws on the first planks **y830**, same plank continuing to **y856** (Δ **0–26 px**). Low beach mouth, not a high pier. |

**>300 px trap:** 212 px. Wrong-landmark objects (moon upper-left, Horn shoulder, leaf-sail) are not in play.

Body-anchor line (horizontal through George’s hood top **y644**). Floor-not-ceiling: at-or-below the joint is PASS; above the joint is FAIL.

| Page | Line | Hits Horn | Hits Beak | Hits Goat |
|------|------|-----------|-----------|-----------|
| p8 | **y644** | **knee of the striding/raised leg; shin of the raised foot** (raised claws hang ~y720–780 over the pit; yellow line sits **above that foot**, i.e. **at or below the knee**, not at the thigh/hip) | **mid-thigh / mid-log** — yellow line crosses the gripped grey trunk and Beak’s lower torso, **below** chest and **below** the waist lock | **knee / mid-thigh** of the standing goat — at or **below** the mid-thigh lock, not at the waist/chest |

---

## p8 — Three Wild Warnings (`l7-p08-three-warnings-v10.png`)

**Zone:** WildIsland (night shore). **Roster:** george, horn, beak, goat.

| Check | Result | Evidence |
|-------|--------|----------|
| Horn hoof makes a sand pit but does not touch George | **PASS** | Deep circular crater between George and Horn (pit crop + `y720–920` feet band). Raised clawed foot hangs over the hole; it does **not** sit in the pit or on George. Planted foot stays on sand in the **y856** band. George stands left of the rim — no contact. |
| Beak claws leave marks on dead wood only | **PASS** | Both clawed hands grip a thick grey weathered trunk with broken branch stubs (Beak strip + claws/wood crop). Bird talons also plant on sand/log at **y850–856**. Dead wood, not a living trunk being snapped. |
| Goat arms block a readable vine bridge into the island | **PASS** | Far right: **horizontal wooden plank path** with vine-wrapped posts and vine railings, receding up into the jungle. Goat stands in the mouth, clawed hand on the vine rail. Walkable 藤橋 / plank deck, **not** a post-and-rail fence. |
| George stands steady, empty-handed | **PASS** | Hooded T-rex boy in navy sneakers, profile facing the beasts; bare hands at sleeve cuffs, no fork. |
| Billy o' Tea behind George | **PASS** | Tea-brown hull and off-white sail with a green leaf emblem sit in the shallows immediately left/behind George; no crew, no letters. |
| Beasts ≥2×, same shore line | **PASS** | Horn **3.75–3.78×**, Beak **3.56–3.58×**, Goat **3.09–3.57×**. George/Horn/Beak sand **y850–856**; Goat in the same **y830–856** mouth band (max Δ **26 px**). |
| Horn ≥3.0×; hood at or below knee | **PASS** | 795–801 / 212 = **3.75–3.78×**, over **3.0×**. Hood **y644** sits at the striding knee / raised-leg shin — not above the joint. |
| Beak ≥2.2×; hood at or below waist | **PASS** | 754–758 / 212 = **3.56–3.58×**, over **2.2×** and over **2.0×**. Hood y644 cuts **mid-thigh / mid-log**, below chest — taller than the waist lock. |
| Goat ≥2.6×; hood at or below mid-thigh | **PASS** | Conservative (lit head **y199** → **y856**) **3.09×**; horn-crest (**y100**) **3.57×**. Both over **2.6×**. Hood y644 hits **knee / mid-thigh**, not hip/waist. |
| p8 Goat bridge exception | **PASS** | Claw tops on the first planks **y830**; same plank / sand band **y856**; George sand **y856** (Δ **0–26 px**). Low beach-level mouth, not a high terrace used to shrink him. Own-sole ratio still **≥3.09×**. |
| No crown yet | **PASS** | Nothing on the T-rex hood except costume spikes / snout; no vine hoop. |
| Identity / costume | **PASS** | Horn: bull horns, mane, striped body, claws. Beak: comb/wattle, yellow-orange feathers, hooked beak. Goat: ridged ram horns, pale shag, yellow eyes. Onesie + hood + thick tail + navy sneakers. |
| Shared hard fails | **PASS** | All three ≥2.0×. Hood on; no 4th beast; no English; no fight; not 3D. |

**Exact hit:** On this shore George is **212 px** (hood y644 → soles y856). Horn is **3.75–3.78×** with the hood **at or below the knee**. Beak is **3.56–3.58×** with the hood **below the waist**. Goat is **3.09–3.57×** with the hood **at or below mid-thigh**. Pit, dead-wood claws, vine-bridge block (plank path, not a fence), boat, empty-handed stand, no-crown, and the 0–26 px low mouth all land.

## VERDICT: PASS

Locked WildIsland scale and the warning beats of pit / log / readable vine bridge / boat all hold on `l7-p08-three-warnings-v10.png`. Do not copy into `lessons/assets/` from this review alone.
