#!/usr/bin/env python3
"""Poe API client for video generation only (George English Lesson pipeline).

Image generation via Poe is intentionally not supported — lesson art uses existing PNG/WebP assets.
"""

from __future__ import annotations

import argparse
import base64
import json
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = ROOT / ".env.local"
USAGE_LOG = ROOT / "scripts" / "poe_usage.jsonl"

POE_BASE = "https://api.poe.com/v1"
DEFAULT_VIDEO_MODEL = "Veo-3.1-Fast"


@dataclass
class UsageRecord:
    kind: str
    model: str
    prompt_preview: str
    usage: dict | None
    output: str | None = None


def load_api_key() -> str:
    key = None
    if ENV_FILE.is_file():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("POE_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
                break
    if not key:
        import os
        key = os.environ.get("POE_API_KEY", "").strip()
    if not key:
        raise RuntimeError(f"POE_API_KEY not found in {ENV_FILE} or environment")
    return key


def log_usage(record: UsageRecord) -> None:
    USAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "kind": record.kind,
        "model": record.model,
        "prompt_preview": record.prompt_preview[:160],
        "usage": record.usage,
        "output": record.output,
    }
    with USAGE_LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    if record.usage:
        print(f"  usage: {record.usage}")


class PoeClient:
    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or load_api_key()

    def _request(
        self,
        method: str,
        path: str,
        *,
        json_body: dict | None = None,
        accept: str = "application/json",
        timeout: int = 300,
    ) -> tuple[int, bytes, dict | None]:
        url = f"{POE_BASE}{path}"
        headers = {"Authorization": f"Bearer {self.api_key}", "Accept": accept}
        data = None
        if json_body is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(json_body).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
                parsed = None
                if "application/json" in resp.headers.get("Content-Type", ""):
                    parsed = json.loads(raw.decode("utf-8"))
                return resp.status, raw, parsed
        except urllib.error.HTTPError as exc:
            body = exc.read()
            detail = body.decode("utf-8", errors="replace")
            raise RuntimeError(f"Poe API {method} {path} failed ({exc.code}): {detail}") from exc

    def create_video(
        self,
        prompt: str,
        *,
        model: str = DEFAULT_VIDEO_MODEL,
        seconds: int = 6,
        size: str = "1280x720",
        input_image: Path | None = None,
    ) -> str:
        body: dict = {
            "model": model,
            "prompt": prompt,
            "seconds": seconds,
            "size": size,
        }
        if input_image:
            body["input_image"] = base64.b64encode(input_image.read_bytes()).decode("ascii")
        _, _, data = self._request("POST", "/videos", json_body=body, timeout=120)
        if not data or not data.get("id"):
            raise RuntimeError(f"Unexpected /videos response: {data}")
        return data["id"]

    def wait_for_video(
        self,
        video_id: str,
        *,
        poll_seconds: float = 5.0,
        timeout_seconds: float = 900.0,
    ) -> dict:
        deadline = time.time() + timeout_seconds
        while time.time() < deadline:
            _, _, data = self._request("GET", f"/videos/{video_id}", timeout=60)
            if not data:
                raise RuntimeError("Empty video status response")
            status = data.get("status")
            progress = data.get("progress")
            print(f"  video {video_id}: {status} {progress or ''}%")
            if status == "completed":
                log_usage(UsageRecord(
                    "video", data.get("model", DEFAULT_VIDEO_MODEL), video_id, data.get("usage"), video_id
                ))
                return data
            if status == "failed":
                raise RuntimeError(f"Video failed: {data.get('error')}")
            time.sleep(poll_seconds)
        raise TimeoutError(f"Video {video_id} not ready after {timeout_seconds}s")

    def download_video(self, video_id: str, out_path: Path) -> Path:
        url = f"{POE_BASE}/videos/{video_id}/content"
        req = urllib.request.Request(
            url,
            headers={"Authorization": f"Bearer {self.api_key}", "Accept": "video/mp4"},
            method="GET",
        )
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(req, timeout=300) as resp:
            out_path.write_bytes(resp.read())
        print(f"  saved video -> {out_path}")
        return out_path

    def generate_video(
        self,
        prompt: str,
        out_path: Path,
        *,
        input_image: Path | None = None,
        model: str = DEFAULT_VIDEO_MODEL,
        seconds: int = 6,
        size: str = "1280x720",
    ) -> Path:
        print(f"Creating video ({model}, {seconds}s)...")
        vid = self.create_video(
            prompt,
            model=model,
            seconds=seconds,
            size=size,
            input_image=input_image,
        )
        self.wait_for_video(vid)
        return self.download_video(vid, out_path)


def cmd_test(_: argparse.Namespace) -> int:
    key = load_api_key()
    masked = key[:6] + "…" + key[-4:] if len(key) > 12 else "(set)"
    print(f"POE_API_KEY loaded: {masked}")
    print("Video-only mode — use scripts/generate_lesson02_videos.py for image-to-video.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Poe video API utilities")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("test", help="Verify POE_API_KEY is configured")
    args = parser.parse_args()
    if args.cmd == "test":
        return cmd_test(args)
    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
