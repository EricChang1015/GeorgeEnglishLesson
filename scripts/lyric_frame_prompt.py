#!/usr/bin/env python3
"""Print an image prompt for one lyric frame (or all)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "scripts" / "lesson06_lyric_frames.json").read_text(encoding="utf-8"))

LOCK = (
    "Warm hand-drawn watercolor children's picture book, grainy painterly texture. "
    "George is an East Asian boy ~5, short black bangs, round face, big dark eyes, toothy smile. "
    "SAILOR LOOK: white long-sleeve sailor shirt, navy square collar and cuffs, navy shorts, brown short boots, small white sailor hat with bangs visible. "
    "CAPTAIN: rugged weathered face, thick eyebrows, short scruffy beard, stern serious expression, dark navy peacoat, captain hat, NOT a friendly soft smile. "
    "crew-red: stocky, red-brown curly beard, blue-white striped shirt, knit cap. "
    "crew-young: tall lean East Asian man, black short hair, clean-shaven, navy shirt, beige trousers. "
    "crew-stocky: short bald man, big dark beard, olive shirt, brown suspenders. Never clone crew faces. "
    "supply-beard: brown full beard, olive-green sweater, khaki trousers, no hat. "
    "supply-cap: grey knit cap, red scarf, cream shirt, brown vest, small mustache. "
    "Billy o' Tea: realistic 19th-century wooden brig/bark whaler, tea-brown hull, green tea-leaf emblem on mainsail, no letters. "
    "Wellerman: smaller schooner, pale upper hull, green circle emblem, no letters. "
    "Cargo lock: THREE pale sugar crates PORT, TWO darker tea chests MID, FOUR sealed rum barrels STARBOARD. "
    "Right whale: Eubalaena, no dorsal fin, callosities on snout tip, above left eye, and right jaw, V-shaped blow, kind eye, never harpooned, never bleeding. "
    "Whaleboat-1: clinker-built dark-brown hull, cream interior; bow ALWAYS crew-red, stern ALWAYS crew-young. "
    "George never sits in the whaleboat. Daddy is not in this picture. "
    "No on-image text, no letters, no photoreal faces, no horror, no blood, no drunkenness."
)

LOOK = {
    "george-sailor": "small East Asian boy sailor (George)",
    "captain": "stern hard-boiled captain in navy peacoat",
    "crew-red": "stocky red-bearded sailor in striped shirt",
    "crew-young": "tall lean clean-shaven East Asian sailor",
    "crew-stocky": "short bald sailor with big dark beard and suspenders",
    "supply-beard": "Wellerman man with brown beard and olive sweater",
    "supply-cap": "Wellerman man with grey cap and red scarf",
}


def prompt_for(frame: dict) -> str:
    deck = ", ".join(LOOK[i] for i in frame["cast"]["deck"]) or "nobody"
    boat = ", ".join(LOOK[i] for i in frame["cast"]["whaleboat"]) or "empty"
    well = ", ".join(LOOK[i] for i in frame["cast"]["wellerman"]) or "nobody"
    evidence = "; ".join(frame["evidence"])
    return (
        f"{LOCK}\n\n"
        f"ONE SCENE for lyric line {frame['index']}: \"{frame['text']}\". "
        f"Zone {frame['zone']}. "
        f"ON BILLY DECK: {deck}. "
        f"IN WHALEBOAT: {boat}. "
        f"ON WELLERMAN: {well}. "
        f"Action: {frame['action']} "
        f"Must show: {evidence}. "
        f"{frame['continuity_note']}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=int, default=0, help="1-24, or 0 for all")
    args = parser.parse_args()
    frames = DATA["frames"]
    chosen = frames if args.index == 0 else [f for f in frames if f["index"] == args.index]
    if not chosen:
        raise SystemExit(f"No frame {args.index}")
    for frame in chosen:
        print(f"===== lyric-{frame['index']:02d} {frame['id']} =====")
        print(prompt_for(frame))
        print()


if __name__ == "__main__":
    main()
