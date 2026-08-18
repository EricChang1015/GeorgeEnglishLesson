# AI video lessons learned (Lesson 2 pilot)

This document records what failed in the first **Poe Veo-3.1-Fast** image-to-video pilot so we do not repeat the same mistakes.

## Verdict

The pilot videos are **not usable** for teaching. Failures came from **both** our pipeline design and model limits. Raw files are archived locally only:

`_local/failed-assets/lesson-02-veo-fast-pilot/` (gitignored)

## What failed

| Issue | Cause | Owner |
|-------|--------|--------|
| Wrong character speaks a line (e.g. Pip says Ember’s line) | Story **dialogue text** was pasted into the video prompt; Veo has native speech and assigns speakers randomly | **Pipeline** |
| Dialogue cut off before end of page | Fixed **6s** clip + model trying to speak full page text | **Pipeline** |
| Bird / wrong creature instead of Pip | Single `input_image` only; small/distant characters reinterpreted | **Model + pipeline** |
| Style / face drift | Fast tier + no multi-image character refs on `/v1/videos` | **Model** |
| Egg “sinks” mid-hatch (story-02) | Physics inconsistency on Fast tier | **Model** |

## Pipeline rules (must follow next time)

1. **Never put story dialogue in the video prompt.** Audio is already Edge TTS MP3s. Prompt must say: `silent, no speech, no dialogue, no talking, ambient motion only`.
2. **One subject, one gentle motion** per clip (e.g. “egg shakes, crack widens slowly”) — not three characters doing three actions in 6s.
3. **Static or very slow camera** — `static camera` or `very slow push-in`. Moving the camera forces the model to invent off-frame content.
4. **Large, clear subjects in the first frame** — tiny background characters get replaced (bird vs dragon).
5. **Pilot one clip, watch the whole file, then batch** — not just “file exists”.
6. **Poe `/v1/videos`**: only one reference image; no character ref pack. For consistency, evaluate **Veo reference mode** (Poe bot) before batching.
7. **Loop intent**: ask for `seamless loop, end pose similar to start` if the player loops the clip.

## Poe API scope for this project

- **Use:** `POST /v1/videos` for **Veo-3.1-Fast** (or Veo-3.1) image-to-video — default for any new clips.
- **Do not use:** Poe image generation (Nano-Banana / chat image bots) for lesson art — lesson illustrations stay as existing PNG/WebP assets.
- **Do not use: Kling API (retired for this project).** Lesson 3 story-02 was a one-off pilot. Quality was unsatisfactory and Poe point cost was very high vs Veo Fast. Keep the committed MP4 for reference only; do not regenerate via Kling.

## Cost note

- 8 × 6s Veo-3.1-Fast ≈ **$4.8** equivalent (order of ~16k points at typical Poe pricing).
- **Kling-O3 (Lesson 3 story-02 pilot, ~5s, one-time):** very high point cost vs Veo Fast; **parent decision: no further Kling use.**
- Poe video responses often return `usage: null` — reconcile points in the Poe account UI, not only from `scripts/poe_usage.jsonl`.

## Lesson 3 hybrid pilot (kept, not approved)

- `lessons/assets/lesson-03/video/story-02.mp4` — Kling-O3, Story 2 only in `videoPages`.
- Quality not satisfactory; retained for comparison. Other story pages stay static WebP.
- Approved lesson videos live under `lessons/assets/lesson-NN/video/` and **are tracked in git** (not gitignored).

## Local archive (this machine only)

`_local/failed-assets/lesson-02-veo-fast-pilot/` contains:

- `story-01.mp4` … `story-08.mp4` — failed Veo clips
- `lesson-02-video.html` — demo page (moved out of git with the clips)

Open locally after `npx serve .` from repo root:

`http://localhost:3000/_local/failed-assets/lesson-02-veo-fast-pilot/lesson-02-video.html`

## Player support (in repo)

`lessons/js/lesson-player.js` keeps optional `videoPages` / `videoDir` for a future successful pilot. Standard lessons are unchanged.

## Regenerate (Veo only)

```bash
python scripts/generate_lesson_video.py --lesson 3 --page 2 --model Veo-3.1-Fast
# or batch Lesson 2:
python scripts/generate_lesson02_videos.py --page 3 --out-dir _local/pending-videos/lesson-02
```

Output for lesson clips: `lessons/assets/lesson-NN/video/story-PP.mp4` (tracked in git).
