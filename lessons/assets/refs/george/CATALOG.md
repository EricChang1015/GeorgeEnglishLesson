# Character reference catalog — George family

Likeness refs for lesson illustration. Photos in this folder are **tracked in git**. Do not embed raw photos in published lesson HTML — generate picture-book art under `lessons/assets/lesson-XX/` instead.

## Naming

```
{subjects}-{setting}-{pose-or-mood}[-variant].jpg
```

- Subjects use role ids: `george`, `daddy`, `mummy`, `sylvia` (hyphen-joined, George first)
- Prefer lowercase kebab-case; no spaces

## Family cast (for story art)

| Id | Role | Appearance notes |
|----|------|------------------|
| `george` | Boy ~5, story hero | East Asian; short black hair with bangs; round face |
| `daddy` | Father | East Asian adult; short dark hair with volume on top; thin round/oval metal glasses; small mole on lower left chin — **solo refs:** `lessons/assets/refs/daddy/CATALOG.md` (group default: `george-daddy-outdoors-pavilion-neutral.jpg`)
| `mummy` | Mother | East Asian adult; long dark hair; thin round metal glasses — **solo refs:** `lessons/assets/refs/mummy/CATALOG.md`
| `sylvia` | Older sister | Dark hair (often ponytail); black rectangular glasses; often baseball cap outdoors — **solo refs:** `lessons/assets/refs/sylvia/CATALOG.md`

## How agents should pick refs

1. **George face / likeness (required for any George art):** start with `priority: primary` photos, especially `george-solo-bed-smile.jpg`.
2. **Daddy face / likeness:** prefer `george-daddy-outdoors-pavilion-neutral.jpg` (front-facing glasses + mole) for George scenes; solo Daddy refs in `lessons/assets/refs/daddy/CATALOG.md` (default: `daddy-solo-indoor-vehicle-neutral.png`).
3. **Family scenes:** match cast tags (`with:daddy`, `with:mummy`, `with:sylvia`). **Full family (all four):** see `george-daddy-mummy-sylvia-*` entries below; solo face refs in `refs/sylvia/`, `refs/mummy/`, `refs/daddy/`.
4. **Mood / setting:** use tags (`smile`, `outdoors`, `bed`, `play`) when generating matching story beats.
5. **George’s favorite doll (Mike Wazowski):** lime-green one-eyed *Monsters, Inc.* plush. Start with `mike-plush-indoor-closeup.jpg` for the toy look; use `george-solo-sofa-mike-plush-smile.jpg` when George is holding it. Sleeping-with-Mike refs are for bedtime / comfort beats only.
6. **Bedroom / bedtime scene:** use `mike-plush-bedroom-bed-scattered.jpg` for George's actual bed layout, cream blanket, far-wall grey curtains, and plush placement; use `george-daddy-bedtime-reading.jpg` for bedtime reading posture **and the left-of-bed wall** (plain cream wall + beige headboard, **no window/curtains** on that side).
7. Read the photo with the Read tool before generating art; keep likeness consistent across a lesson.
8. Never copy a photo into a published lesson page; generate new picture-book illustrations inspired by these refs.

## Photos

### Solo — face / likeness

#### george-solo-bed-smile.jpg
- **priority:** primary
- **people:** george
- **tags:** solo, face-closeup, smile, joyful, indoors, bed, home
- **use_for:** best default George face + body proportions; happy expression
- **notes:** Clear front-facing smile; grey raglan long sleeves; cream pants

#### george-solo-sofa-alphabet-smile.jpg
- **priority:** high
- **people:** george
- **tags:** solo, face-closeup, smile, indoors, sofa, home, learning, alphabet, front-facing
- **use_for:** strong George face likeness for covers / close portraits; Lesson 3 cover
- **notes:** Round face, short black bangs, large dark eyes, open-mouth smile showing teeth, prominent ears; white quilted top with tiny red/blue motifs; holding alphabet practice paper (A–N). Prefer face only — do not copy the alphabet paper into story art unless the scene needs it.

#### george-solo-home-wave-smile.jpg
- **priority:** high
- **people:** george
- **tags:** solo, smile, wave, greeting, indoors, home, pajamas, front-facing
- **use_for:** happy hello / wave pose; indoor home scenes; another clear front-facing smile
- **notes:** Chest-up, right hand waving; open-mouth toothy smile, large dark eyes, prominent ears. Pale patterned pajama henley. Fish-tank glow in the background — use face/pose only, do not copy the tank into story art unless the scene is at home.

#### george-solo-restaurant-bib-neutral.jpg
- **priority:** high
- **people:** george
- **tags:** solo, face-closeup, front-facing, focused, indoors, restaurant, eating, bib
- **use_for:** George face when not smiling; mealtime / sitting-at-table scenes
- **notes:** Seated at a bright restaurant table, fry near his mouth, calm focused look at camera. White tiger/cactus bib over grey striped-collar tee and navy dino-print pants. Prefer face + sitting pose — do not copy the bib or restaurant interior unless the scene needs them.

### Solo — outdoor play / full body

#### george-solo-park-dragon-sculpture-smile.jpg
- **priority:** high
- **people:** george
- **tags:** solo, smile, outdoors, park, play, dragon-sculpture, daytime, front-facing
- **use_for:** strong George face + full-body proportions; Lesson 3 Story 1 likeness
- **notes:** Round face, short black bangs, large dark eyes, bright toothy smile; grey graphic tee, blue camo pants, blue sneakers. Sitting on a red playground dragon. Use face/body only — do not copy the park sculpture or photo clothes into story art unless the scene needs them.

#### george-solo-park-balance-focused.jpg
- **priority:** high
- **people:** george
- **tags:** solo, full-body, standing, focused, outdoors, park, play, daytime
- **use_for:** full-body proportions; playground / balancing / active standing pose
- **notes:** Standing on a colorful wobble board, feet apart, looking right with a concentrated open-mouth expression. Green-white striped tee with monkey graphic, navy dinosaur-skeleton joggers, lime slides. Use body proportions and focused mood — do not copy the playground equipment unless the scene is a park.

### Solo — water / adventure

#### george-solo-lake-paddleboard-smile.jpg
- **priority:** medium
- **people:** george
- **tags:** solo, smile, outdoors, water, lake, paddleboard, lifevest, sunhat, daytime
- **use_for:** solo water adventure; George in life vest + sun hat (pairs with Daddy life-vest refs)
- **notes:** Sitting on a pink paddleboard; soft smile. White sun hat with neck flaps; black pirate-theme life vest (skull + red accents) over a dark long-sleeve rash guard. Face partly shaded by the hat — prefer other files for a clear face. Small source photo; do not copy the board or vest art unless the scene is on water.

### Solo — daily / eating

#### george-solo-restaurant-snack-neutral.jpg
- **priority:** low
- **people:** george
- **tags:** solo, indoors, restaurant, eating, snack, candid, raglan
- **use_for:** backup mealtime pose (holding food); casual raglan shirt colors
- **notes:** Slightly blurry, low-resolution candid. White tee, blue raglan sleeves, red collar, red vehicle graphic; holding a piece of grilled food. Neutral look off-camera. Prefer `george-solo-restaurant-bib-neutral.jpg` for face at a table.

### With Daddy

Solo Daddy face / body refs: `lessons/assets/refs/daddy/CATALOG.md` (default solo face: `daddy-solo-indoor-vehicle-neutral.png`).

#### george-daddy-outdoors-pavilion-neutral.jpg
- **priority:** primary
- **people:** george, daddy
- **tags:** outdoors, daytime, pavilion, travel, closeup, daddy-face, glasses, backpack, george-profile, neutral
- **use_for:** best default **Daddy face** likeness (front-facing); Lesson 3 ending / Daddy reunion scenes
- **notes:** Daddy: short thick black hair with volume on top; thin round dark-metal glasses; small mole on lower left chin; light grey athletic tee; black backpack straps. George in profile (navy tee) — prefer other refs for George face.

#### george-daddy-bed-selfie-smile.jpg
- **priority:** high
- **people:** george, daddy
- **tags:** smile, indoors, bed, selfie, closeup, affectionate
- **use_for:** George + Daddy warm indoor scenes; George face from slightly side/close angle
- **notes:** Daddy: grey tee, thin metal glasses; George leaning on Daddy

#### george-daddy-bedtime-reading.jpg
- **priority:** high
- **people:** george, daddy
- **tags:** indoors, bed, bedtime, reading, phone, cozy, daddy, blanket
- **use_for:** bedtime story / shared reading posture; Daddy and George tucked in together; **Lesson 4 p1 room layout** (left of bed)
- **notes:** Beige padded headboard with dark-wood curved trim against a **plain cream wall**. **No window and no curtains on the left of this camera** — that wall is solid. Daddy in glasses and blue-grey raglan sleep shirt; George beside him. Use posture, closeness, bed setup, and bedtime mood. Do not copy phone UI, timestamp, or exact blanket artwork into published story art. Grey curtains belong on the far wall only (see `mike-plush-bedroom-bed-scattered.jpg`), not beside the headboard.

#### george-daddy-outdoors-lifevest-smile.jpg
- **priority:** high
- **people:** george, daddy
- **tags:** smile, outdoors, forest, adventure, lifevest, bucket-hat, sunny
- **use_for:** outdoor adventure with Daddy; joyful George looking up
- **notes:** George white star bucket hat; both in life vests

#### george-daddy-outdoors-lifevest-hat.jpg
- **priority:** medium
- **people:** george, daddy
- **tags:** outdoors, forest, adventure, lifevest, bucket-hat, serious, selfie
- **use_for:** outdoor/water adventure; calmer George expression
- **notes:** Daddy yellow life vest + glasses; George black pirate-style life vest + white star hat

### With Sylvia

Solo Sylvia face / body refs: `lessons/assets/refs/sylvia/CATALOG.md` (default face: `sylvia-solo-outdoors-graduation-smile.jpg`).

#### george-sylvia-arcade-play.jpg
- **priority:** medium
- **people:** george, sylvia
- **tags:** play, indoors, arcade, excited, activity
- **use_for:** George + Sylvia play / fun indoor activity
- **notes:** George dark blue tee at game controls; Sylvia beige cap + glasses behind him

#### george-sylvia-park-dino-smile.jpg
- **priority:** medium
- **people:** george, sylvia
- **tags:** smile, outdoors, park, play, dinosaur-prop, daytime
- **use_for:** George + Sylvia outdoor play; light adventure / park scenes
- **notes:** George on blue dino sculpture; navy/grey raglan; Sylvia mint tee, white “GOOD” cap

### With Mummy

Solo Mummy face / body refs: `lessons/assets/refs/mummy/CATALOG.md` (default face: `mummy-solo-indoor-smile.png`).

#### george-mummy-indoor-reading-smile.jpg
- **priority:** high
- **people:** george, mummy
- **tags:** indoors, restaurant, reading, story-time, bedtime, books, affectionate, mummy-face, glasses
- **use_for:** Mummy reading to George; shared story-time / bedtime reading posture
- **notes:** Mummy: low ponytail, wispy bangs, thin round dark metal glasses, cream/beige knit sweater, gold necklace. George: grey sweatshirt, short black bangs, leaning in to look at the book (Sleeping Beauty). Use faces, closeness, and reading pose — do not copy restaurant booth or exact book cover into story art unless the scene needs them.

### Family group — full cast (George + Daddy + Mummy + Sylvia)

Height order in story art: **Daddy tallest → Sylvia → Mummy → George smallest.**

#### george-daddy-mummy-sylvia-indoor-sofa-selfie-smile.png
- **priority:** high
- **people:** george, daddy, mummy, sylvia
- **tags:** family, full-cast, indoors, home, sofa, selfie, smile, glasses
- **use_for:** warm home family group; all four faces + relative positions on a couch
- **notes:** Brown leather sofa; plain wall. Daddy far left: cream tee, round metal glasses. George center: green-white striped tee, drinking from grey water bottle. Mummy: white tee + pink fleece vest, round glasses, wide smile. Sylvia far right: white long-sleeve, rectangular black glasses, calm smile. Use faces and sofa grouping — do not copy exact pajama/stripe patterns unless the scene is at home.

#### george-daddy-mummy-sylvia-indoor-livingroom-play-selfie.jpg
- **priority:** high
- **people:** george, daddy, mummy, sylvia
- **tags:** family, full-cast, indoors, home, livingroom, play, selfie, matching-shirts
- **use_for:** indoor family play at home; George focused on activity while parents + Sylvia pose
- **notes:** Matching black "we are family" monster tees on all four. George foreground left playing purple kinetic sand in pink tray. Mummy center: long dark hair, round glasses, gentle smile. Sylvia center-back: rectangular glasses, playful tongue-out. Daddy right: selfie-taker, short dark hair. Use cast positions and play-at-home mood — do not copy monster-shirt graphic into story art unless needed.

#### george-daddy-mummy-sylvia-outdoors-park-bench-family-shirts.jpg
- **priority:** high
- **people:** george, daddy, mummy, sylvia
- **tags:** family, full-cast, outdoors, park, bench, travel, selfie, smile, matching-shirts
- **use_for:** outdoor family outing; park bench group pose
- **notes:** Green park bench; trees behind. Daddy left (selfie): round glasses, black family tee. George: pink sunglasses, family tee. Mummy: round sunglasses, blue lanyard, laughing. Sylvia far right: mint tee (not matching), rectangular glasses, blue backpack — **Sylvia often wears different outfit from rest**. Use relative seating and outing mood.

#### george-daddy-mummy-sylvia-outdoors-dino-selfie-smile.jpg
- **priority:** high
- **people:** george, daddy, mummy, sylvia
- **tags:** family, full-cast, outdoors, zoo, dinosaur, adventure, selfie, smile, travel
- **use_for:** family adventure / dinosaur park; full cast with prop
- **notes:** Triceratops statue in lush greenery. Daddy left: navy tee, rectangular glasses, bag strap. George front center: blue long-sleeve with Mickey graphic. Mummy: blue hooded windbreaker (lime hood lining), hands on George's shoulders. Sylvia right: black Mickey-pattern sweatshirt, rectangular glasses. Pairs with `george-sylvia-park-dino-smile.jpg` (George+Sylvia only) for dino-play chapters.

#### george-daddy-mummy-sylvia-outdoors-plaza-pigeons-smile.jpg
- **priority:** medium
- **people:** george, daddy, mummy, sylvia
- **tags:** family, full-cast, outdoors, urban, plaza, pigeons, travel, smile, winter-coats
- **use_for:** city travel; feeding birds; winter outdoor family
- **notes:** Urban plaza with blue skyscraper behind. Daddy far left: grey GAP hoodie, round tinted glasses. Sylvia crouching: black hoodie, sunglasses, interacting with pigeons. Mummy holding George on lap: bronze puffer, sunglasses. George: bright red puffer, blue pants, happy. Use winter-coat grouping and city outing — do not copy GAP logo unless needed.

#### george-daddy-mummy-sylvia-outdoors-tower-selfie-smile.jpg
- **priority:** medium
- **people:** george, daddy, mummy, sylvia
- **tags:** family, full-cast, outdoors, travel, landmark, tower, selfie, smile, winter-coats
- **use_for:** family sightseeing; landmark travel group
- **notes:** Eiffel-tower replica; clear blue sky; low-angle selfie. Daddy foreground left: black puffer, round sunglasses. George center: green/beige camo puffer, looking sideways. Sylvia center: rectangular glasses, pink face mask. Mummy right: bronze puffer, round sunglasses, blue crossbody bag. Use travel landmark mood — masks/sunglasses are trip-only, not default lesson look.

#### george-daddy-mummy-sylvia-indoor-airport-selfie-smile.jpg
- **priority:** medium
- **people:** george, daddy, mummy, sylvia
- **tags:** family, full-cast, indoors, airport, travel, selfie, smile
- **use_for:** family travel departure; airport terminal group
- **notes:** Airport terminal floor + queue stanchions. Daddy left: beige tee, round glasses, wide smile. Sylvia behind: long hair + bangs, rectangular glasses, navy graphic tee. Mummy right holding George: short layered hair, round glasses, navy tee. George: white patterned long-sleeve, leaning on Mummy. **Extra person in background (grandmother, peace sign) — NOT in cast bible; do not draw in lesson art.** Use four core family faces only.

#### george-mummy-daddy-sylvia-halloween-trex-play.jpg
- **priority:** high
- **people:** george, mummy, daddy, sylvia
- **tags:** family, full-cast, halloween, costume, trex, indoors, smile, play
- **use_for:** Lesson 7 family likeness + George in T-rex hood with family; home-clothes hints (not cave gear)
- **notes:** George center in orange-brown dino hood, excited hands. Sylvia (teen, long dark wavy hair, gold headband, dark dress with gold trim) making a playful face. Mummy behind George, glasses, dark long sleeves, smile. Daddy far left, glasses, navy tee with colorful animal icons. Use faces and George costume; do not copy the lobby sign or exact party clothes into every page.

### Family group — partial (3 or fewer)

#### george-daddy-mummy-indoor-closeup.jpg
- **priority:** medium
- **people:** george, daddy, mummy
- **tags:** family, indoors, closeup, parents
- **use_for:** full parents cast; Daddy + Mummy likeness
- **notes:** Compact family selfie; George center (open-mouth expression — prefer other files for calm smile)

#### george-daddy-sylvia-arcade-selfie.jpg
- **priority:** high
- **people:** george, daddy, sylvia
- **tags:** daddy Sylvia George in Arcade, arcade, indoors, play, selfie, family, daddy-face, glasses, nighttime
- **use_for:** George + Daddy + Sylvia indoor play; extra Daddy face (glasses + mole, three-quarter)
- **notes:** Arcade racing cabinet; Daddy holds a takeaway cup; Sylvia white cap + glasses at the controls; George focused on the game. Use faces/poses — do not copy neon arcade interior into story art unless the scene is an arcade.

#### george-daddy-sylvia-overlook-selfie.jpg
- **priority:** medium
- **people:** george, daddy, sylvia
- **tags:** outdoors, travel, mountains, bridge, selfie, daytime
- **use_for:** George + Daddy + Sylvia outing / travel
- **notes:** Overlook with green suspension bridge; Sylvia light cap + sunglasses

### Daddy + Sylvia / Daddy + Mummy

#### daddy-sylvia-outdoors-selfie.jpg
- **priority:** high
- **people:** daddy, sylvia
- **tags:** daddy Sylvia outdoor, outdoors, travel, mountains, selfie, daytime, daddy-face, glasses
- **use_for:** Daddy + Sylvia outdoor travel; Daddy face (glasses + mole)
- **notes:** Karst hills overlook; Daddy blue tee + bag strap; Sylvia pale cap, dark rectangular glasses, white tee with pink collar trim. No George in frame.

#### daddy-sylvia-indoor-selfie.jpg
- **priority:** high
- **people:** daddy, sylvia
- **tags:** daddy sylvia, indoors, home, selfie, closeup, daddy-face, glasses, front-facing
- **use_for:** strong extra **Daddy face** likeness (front-facing glasses + mole); Sylvia without cap
- **notes:** Living-room selfie; Daddy navy tee, thin round glasses, mole on lower jaw; Sylvia long dark hair, school uniform (white shirt + teal tie). Prefer faces — do not copy the room clutter or uniform into story art unless the scene needs them.

#### daddy-mummy-indoor-smile.jpg
- **priority:** high
- **people:** daddy, mummy
- **tags:** daddy mummy, indoors, family, parents, smile, closeup, daddy-face, mummy-face, glasses
- **use_for:** Daddy + Mummy likeness together; Daddy slight smile with round glasses
- **notes:** Indoor pet-cafe selfie; Daddy charcoal tee, holding a small banded snake; Mummy long black hair, round glasses, floral tee. Use faces — do not copy the snake or cafe interior into story art unless the scene needs them.

### Favorite toy — Mike Wazowski

George’s favorite doll: a lime-green, one-eyed Mike Wazowski plush (*Monsters, Inc.*). He often sleeps hugging one (sometimes several). Draw the toy as a soft spherical green monster with one large eye, two small grey horns, a simple smile, and long thin limbs — not a dragon, and not a new character unless the lesson is about him.

#### mike-plush-indoor-closeup.jpg
- **priority:** primary
- **people:** none
- **tags:** mike-wazowski, plush, favorite-toy, doll, green, one-eye, horns, closeup, indoors
- **use_for:** default Mike doll look (shape, eye, horns, smile, thin arms/legs)
- **notes:** Seated lime-green sphere; large white eye with teal-blue iris; thin stitched smile; two small grey horns; grey claw tips. Cropped from a phone screenshot — use the toy only, ignore any leftover background clutter.

#### mike-plush-bed-collection.jpg
- **priority:** high
- **people:** none
- **tags:** mike-wazowski, plush, favorite-toy, doll, collection, bed, indoors
- **use_for:** size/texture variants of the same doll (he owns more than one)
- **notes:** Three lime-green Mike plushes on a car-print pillow. Top: shaggy/open-mouth. Middle + bottom: smoother fabric, stitched smile. Bottom has a Tokyo Disney Resort tag and a tiny brown teddy on its belly. Do not copy the pillow pattern into story art.

#### george-solo-sofa-mike-plush-smile.jpg
- **priority:** high
- **people:** george
- **tags:** solo, smile, indoors, sofa, home, mike-wazowski, plush, favorite-toy, drawing, front-facing
- **use_for:** George holding his Mike doll; toy scale vs George; a calm front-facing face
- **notes:** Dark green padded vest; holds a lime-green Mike plush in one hand and a hand-drawn Mike on paper. Prefer face + doll — do not copy the paper drawing into story art unless the scene is about his picture.

#### george-solo-bed-mike-plush-sleep.jpg
- **priority:** medium
- **people:** george
- **tags:** solo, sleep, bedtime, indoors, bed, home, mike-wazowski, plush, favorite-toy, hug
- **use_for:** bedtime / comfort; George asleep surrounded by Mike dolls
- **notes:** Side-sleeping, hugging one Mike to his face, another on his shoulder, a larger green plush along his torso. Eyes closed — do not use for George face likeness.

#### george-solo-bed-mike-plush-sleep-chin.jpg
- **priority:** medium
- **people:** george
- **tags:** solo, sleep, bedtime, indoors, bed, home, mike-wazowski, plush, favorite-toy, pajamas
- **use_for:** one well-loved Mike tucked under George’s chin
- **notes:** Light blue/white pajamas; cream quilt; Mike’s eye and grey horns clear beside his face. Eyes closed — do not use for George face likeness.

#### george-solo-bed-mike-plush-sleep-chest.jpg
- **priority:** medium
- **people:** george
- **tags:** solo, sleep, bedtime, indoors, bed, home, mike-wazowski, plush, favorite-toy, pajamas
- **use_for:** Mike resting on George’s chest while he sleeps
- **notes:** On his back, arms up; white pajamas with light-blue cuffs; Mike on chest near the neck. Eyes closed — do not use for George face likeness.

#### george-solo-bed-mike-plush-side-sleep.jpg
- **priority:** high
- **people:** george
- **tags:** solo, sleep, bedtime, indoors, bed, home, mike-wazowski, plush, favorite-toy, hug, pajamas, side-sleep
- **use_for:** strongest bedtime sleeping pose with George's Mike plush; George hugging the toy against his face; blanket partly covering him
- **notes:** Side-sleeping on pale blue sheet with car-print pillow; white short-sleeve pajamas with tiny colorful prints; green blanket and cream quilt nearby. Use pose, bedding palette, and plush-hugging comfort beat. Eyes closed — do not use for George face likeness.

### Bedroom / bedtime scene anchors

#### mike-plush-bedroom-bed-scattered.jpg
- **priority:** high
- **people:** none
- **tags:** bedroom, bed, bedtime, home, mike-wazowski, plush, favorite-toy, cream-blanket, grey-curtains, scene-anchor
- **use_for:** George bedroom layout; cream bedsheet / blanket texture; grey curtains; bed surface for "blanket hill" dream transition; multiple Mike plush placement
- **notes:** Wide bed view with beige padded headboard, cream sheet/blanket, grey curtains, and two lime-green one-eyed plush toys lying apart. Use as the real bedroom anchor before the room transforms. Do not copy clutter literally; simplify into a cozy picture-book bedroom.

#### george-bedroom-bird-lamp-product.jpg
- **priority:** high
- **people:** none
- **tags:** bedroom, lamp, night-light, bird-lamp, alarm-clock, prop, scene-anchor
- **use_for:** George's little lamp in RealBedroom and dream scenes; replace star night-light
- **notes:** Chubby glowing bird body, tiny black dot eyes, small yellow-orange beak, three-prong fan tail, white clock panel on lower belly. Scale lock: fist-sized / ankle-high vs standing George (see `lessons/assets/refs/cast/mike-nibble-sheet.png`). In Hill/Forest dream art: keep fist-sized, hide clock digits. No bedside table lamp in story art.

### Costume — T-rex onesie (Lesson 7)

#### george-solo-halloween-trex-bucket.jpg
- **priority:** primary
- **people:** george
- **tags:** solo, halloween, costume, trex, dinosaur, indoors, full-body, front-facing
- **use_for:** Lesson 7 George costume lock — front of T-rex onesie + face
- **notes:** Full-body tan/beige/light-orange cracked-scale T-rex jumpsuit with matching hood (dino head); front zipper; navy sneakers with white soles and green Nike swoosh. Orange pumpkin candy bucket is Halloween-only — do not copy into Lesson 7 unless the beat needs it. Face: short black bangs, East Asian boy ~5.

#### george-solo-halloween-trex-night-side.png
- **priority:** high
- **people:** george
- **tags:** solo, halloween, costume, trex, dinosaur, night, side, full-body, tail
- **use_for:** Lesson 7 costume lock — hood side eye, back plates, thick tapered tail
- **notes:** Side/rear view of the same mottled brown-orange scale onesie; dark triangular plates down the spine continuing onto the tail; blue sneakers; yellow pumpkin bucket (Halloween-only, do not copy unless needed).

#### george-mummy-daddy-sylvia-halloween-trex-play.jpg
- **See:** full-cast entry under **Family group — full cast** above (Lesson 7 family + T-rex costume).
