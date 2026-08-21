---
name: picture-book-consistency
description: Locks character look, dragon scale, and scene anchors before generating lesson illustrations. Use when creating or redrawing lesson art, covers, vocab pictures, character sheets, page prompts, or when the user mentions Pip, Ember, visual drift, 忽大忽小, or 角色一致性.
---

# Picture-book consistency

Do not generate lesson art from a one-line story beat. Lock the cast and places first.

## Read first

1. `docs/cast-bible.md` — scale, clothes, scene anchors, lock frames
2. `lessons/assets/refs/george/CATALOG.md` — then **Read** the photos named in the bible
3. `.cursor/rules/character-refs.mdc` — family photo rules

If the bible is missing a new character or place, **update the bible and get a sheet** before page images.

## Workflow

```
[ ] Bible fields filled (who / scale / clothes / cannot-change)
[ ] Character sheet exists or is generated (front + 3/4 + expressions)
[ ] Dragons: height vs George written on the sheet
[ ] Scene anchors listed (hill, path, cave…)
[ ] Page plan: one action or feeling per page
[ ] Each page prompt repeats bible cannot-change + scale lock
[ ] Generate one page; QA against bible; then the next page
```

## Prompt rules

- Repeat locked traits every page. Never write only “the same dragon”.
- Always state **Pip = waist-to-chest of George**, **Ember = knee-high, smaller than Pip**.
- One main action per page. Do not stack three props in six hands.
- No on-image story text. No photoreal faces. No style hop mid-lesson.
- After each image: check face, outfit, dragon size, cave/hill anchors. Reject and regenerate that page if any lock broke.

## New chapter

Before Lesson 4+ art: extend `docs/cast-bible.md` with any new role or place. Recurring cast keeps the same locks.

## Upstream patterns (do not vendor whole repos)

- [storybook-generator-skill](https://github.com/weaiw/storybook-generator-skill) — bible → page prompts → QA
- [tuzi-comic character-template](https://github.com/tuziapi/tuzi-skills/blob/main/skills/tuzi-comic/references/character-template.md) — sheet fields
