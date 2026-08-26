#!/usr/bin/env python3
"""Cut per-line Wellerman clips from timeline JSON via ffmpeg (no full-song copy)."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TIMELINE = REPO_ROOT / "scripts" / "wellerman_timeline.json"
DEFAULT_OUT = REPO_ROOT / "lessons" / "assets" / "lesson-06" / "audio"
SAMPLES_OUT = REPO_ROOT / "tmp" / "wellerman-samples"
FADE_SEC = 0.05

GATE1_SAMPLE_IDS = ("chorus-01", "chorus-02", "v1-01")


def load_timeline(path: Path) -> dict:
    with path.open(encoding="utf-8-sig") as f:
        return json.load(f)


def resolve_source(timeline: dict) -> Path:
    rel = timeline["source_file"]
    src = (REPO_ROOT / rel).resolve()
    if not src.is_file():
        raise SystemExit(f"Source audio not found: {src}")
    return src


def cut_line(src: Path, line: dict, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / line["file"]
    start = float(line["start"])
    end = float(line["end"])
    duration = max(end - start, FADE_SEC * 2 + 0.01)
    fade_out_start = max(duration - FADE_SEC, 0.0)
    af = f"afade=t=in:st=0:d={FADE_SEC},afade=t=out:st={fade_out_start}:d={FADE_SEC}"
    cmd = [
        "ffmpeg",
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-ss",
        f"{start:.3f}",
        "-to",
        f"{end:.3f}",
        "-i",
        str(src),
        "-af",
        af,
        "-c:a",
        "libmp3lame",
        "-q:a",
        "2",
        str(out_path),
    ]
    subprocess.run(cmd, check=True)
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Cut Wellerman line clips from timeline JSON.")
    parser.add_argument(
        "--timeline",
        type=Path,
        default=DEFAULT_TIMELINE,
        help="Path to wellerman_timeline.json",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_OUT,
        help="Output directory for clips (default: lesson-06 audio)",
    )
    parser.add_argument(
        "--ids",
        type=str,
        default="",
        help="Comma-separated line ids to cut (default: all lines)",
    )
    parser.add_argument(
        "--samples",
        action="store_true",
        help=f"GATE 1 samples only -> {SAMPLES_OUT.relative_to(REPO_ROOT)}",
    )
    args = parser.parse_args()

    timeline = load_timeline(args.timeline.resolve())
    src = resolve_source(timeline)
    lines = timeline["lines"]

    if args.samples:
        out_dir = SAMPLES_OUT
        want = set(GATE1_SAMPLE_IDS)
    elif args.ids.strip():
        out_dir = args.out.resolve()
        want = {x.strip() for x in args.ids.split(",") if x.strip()}
    else:
        out_dir = args.out.resolve()
        want = None

    selected = []
    for line in lines:
        lid = line["id"]
        if want is not None and lid not in want:
            continue
        selected.append(line)

    if want is not None:
        missing = want - {line["id"] for line in selected}
        if missing:
            raise SystemExit(f"Unknown or missing timeline ids: {', '.join(sorted(missing))}")

    if not selected:
        print("No lines selected.", file=sys.stderr)
        return 1

    for line in selected:
        out_path = cut_line(src, line, out_dir)
        print(f"Wrote {out_path.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
