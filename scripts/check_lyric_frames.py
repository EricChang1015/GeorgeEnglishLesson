#!/usr/bin/env python3
"""Continuity + file checks for Lesson 6 lyric slideshow frames.

Usage:
    python scripts/check_lyric_frames.py
    python scripts/check_lyric_frames.py --require-art

Exit 0 = all pass; 1 = at least one FAIL.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRAMES_PATH = ROOT / "scripts" / "lesson06_lyric_frames.json"
TIMELINE_PATH = ROOT / "scripts" / "wellerman_timeline.json"
AUDIO_DIR = ROOT / "lessons" / "assets" / "lesson-06" / "audio"
IMG_DIR = ROOT / "lessons" / "assets" / "lesson-06"

DECK_OK = {
    "george-sailor",
    "captain",
    "crew-red",
    "crew-young",
    "crew-stocky",
}
WHALEBOAT_OK = {"crew-red", "crew-young"}
WELLERMAN_OK = {"supply-beard", "supply-cap"}
NEVER_BOAT = {
    "george-sailor",
    "captain",
    "crew-stocky",
    "supply-beard",
    "supply-cap",
}
REQUIRED_FIELDS = {
    "id",
    "index",
    "section",
    "text",
    "audio",
    "img",
    "zone",
    "cast",
    "action",
    "props",
    "evidence",
    "continuity_note",
}


def fail(rows: list[str], msg: str) -> None:
    rows.append(f"FAIL  {msg}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--require-art",
        action="store_true",
        help="Also require lyric-NN.png and .webp on disk.",
    )
    args = parser.parse_args()

    rows: list[str] = []
    data = json.loads(FRAMES_PATH.read_text(encoding="utf-8"))
    timeline = json.loads(TIMELINE_PATH.read_text(encoding="utf-8"))
    frames = data["frames"]
    locks = data["locks"]

    if len(frames) != 24:
        fail(rows, f"expected 24 frames, got {len(frames)}")

    indexes = [f["index"] for f in frames]
    if indexes != list(range(1, 25)):
        fail(rows, f"indexes must be 1..24 in order, got {indexes}")

    by_index = {f["index"]: f for f in frames}
    tl_by_id = {line["id"]: line for line in timeline["lines"]}

    occupied = set(locks["whaleboat_occupied_frames"])
    if occupied != {13, 14, 15, 16}:
        fail(rows, "locks.whaleboat_occupied_frames must be [13,14,15,16]")

    for frame in frames:
        missing = REQUIRED_FIELDS - set(frame)
        if missing:
            fail(rows, f"{frame.get('id')}: missing fields {sorted(missing)}")
            continue

        idx = frame["index"]
        fid = frame["id"]
        prefix = f"{idx:02d} {fid}"
        cast = frame["cast"]
        deck = list(cast.get("deck") or [])
        boat = list(cast.get("whaleboat") or [])
        well = list(cast.get("wellerman") or [])

        if not set(deck).issubset(DECK_OK):
            fail(rows, f"{prefix}: illegal deck ids {set(deck) - DECK_OK}")
        if not set(boat).issubset(WHALEBOAT_OK):
            fail(rows, f"{prefix}: illegal whaleboat ids {set(boat) - WHALEBOAT_OK}")
        if not set(well).issubset(WELLERMAN_OK):
            fail(rows, f"{prefix}: illegal wellerman ids {set(well) - WELLERMAN_OK}")

        if set(boat) & NEVER_BOAT:
            fail(rows, f"{prefix}: forbidden person in whaleboat {set(boat) & NEVER_BOAT}")
        if "crew-stocky" in boat:
            fail(rows, f"{prefix}: crew-stocky must never enter the whaleboat")
        if "george-sailor" in boat:
            fail(rows, f"{prefix}: George must never enter the whaleboat")

        overlap = set(deck) & set(boat)
        if overlap:
            fail(rows, f"{prefix}: person on deck AND in whaleboat: {overlap}")

        if idx in occupied:
            if boat != ["crew-red", "crew-young"]:
                fail(
                    rows,
                    f"{prefix}: whaleboat must be [crew-red, crew-young], got {boat}",
                )
            if set(deck) != {"george-sailor", "captain", "crew-stocky"}:
                fail(
                    rows,
                    f"{prefix}: deck during boat sequence must be George+Captain+crew-stocky, got {deck}",
                )
        else:
            if boat:
                fail(rows, f"{prefix}: whaleboat must be empty outside 13-16, got {boat}")

        if well and frame["zone"] != "SupplyShip":
            fail(rows, f"{prefix}: supply crew only allowed in SupplyShip zone")
        if frame["zone"] == "SupplyShip":
            if well != ["supply-beard", "supply-cap"]:
                fail(
                    rows,
                    f"{prefix}: SupplyShip must have [supply-beard, supply-cap], got {well}",
                )
            cargo = frame.get("cargo") or {}
            if cargo.get("sugar") != 3 or cargo.get("tea") != 2 or cargo.get("rum") != 4:
                fail(rows, f"{prefix}: cargo counts must be sugar3 tea2 rum4")
            if cargo.get("layout") != "port-sugar, mid-tea, starboard-rum":
                fail(rows, f"{prefix}: cargo layout lock broken")
        else:
            if well:
                fail(rows, f"{prefix}: wellerman crew must be empty outside SupplyShip")
            if frame.get("cargo"):
                fail(rows, f"{prefix}: cargo only on SupplyShip frames")

        if frame["zone"] == "OpenSea" and frame.get("whale"):
            fail(rows, f"{prefix}: OpenSea frames must not show a close/present whale flag")

        tl = tl_by_id.get(fid)
        if not tl:
            fail(rows, f"{prefix}: id not in wellerman_timeline.json")
        else:
            if frame["text"] != tl["text"]:
                fail(rows, f"{prefix}: text != timeline ({frame['text']!r} vs {tl['text']!r})")
            if frame["audio"] != tl["file"]:
                fail(rows, f"{prefix}: audio != timeline file {tl['file']}")
            if frame["section"] != tl["section"]:
                fail(rows, f"{prefix}: section != timeline {tl['section']}")

        want_img = f"lyric-{idx:02d}.png"
        if frame["img"] != want_img:
            fail(rows, f"{prefix}: img must be {want_img}")

        audio_path = AUDIO_DIR / frame["audio"]
        if not audio_path.is_file() or audio_path.stat().st_size < 1024:
            fail(rows, f"{prefix}: missing/empty audio {audio_path}")

        if args.require_art:
            png = IMG_DIR / frame["img"]
            webp = png.with_suffix(".webp")
            if not png.is_file() or png.stat().st_size < 1024:
                fail(rows, f"{prefix}: missing PNG {png}")
            if not webp.is_file() or webp.stat().st_size < 1024:
                fail(rows, f"{prefix}: missing WebP {webp}")

    for a, b in locks["chorus_pairs"]:
        fa, fb = by_index[a], by_index[b]
        if fa["cast"] != fb["cast"]:
            fail(rows, f"chorus pair {a}/{b}: cast mismatch")
        if fa["zone"] != fb["zone"]:
            fail(rows, f"chorus pair {a}/{b}: zone mismatch")
        if fa.get("cargo") != fb.get("cargo"):
            fail(rows, f"chorus pair {a}/{b}: cargo mismatch")
        if fa["cast"]["wellerman"] != fb["cast"]["wellerman"]:
            fail(rows, f"chorus pair {a}/{b}: wellerman crew mismatch")

    boat_ids = {f["index"]: f["cast"]["whaleboat"] for f in frames if f["index"] in occupied}
    if len({tuple(v) for v in boat_ids.values()}) != 1:
        fail(rows, f"whaleboat occupancy not identical across 13-16: {boat_ids}")

    if rows:
        print("\n".join(rows))
        print(f"\n{len(rows)} FAIL")
        return 1

    art = "art required" if args.require_art else "art not required yet"
    print(f"PASS  24 lyric frames, timeline/audio aligned, continuity locks held ({art})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
