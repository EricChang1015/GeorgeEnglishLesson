#!/usr/bin/env bash
# Idempotent Cloud Agent setup for the George English Lessons repo.
# Installs the Python tooling used by the lesson pipeline (audio, image, QA).
set -euo pipefail

cd "$(dirname "$0")/.."

# Python packages for scripts/: edge-tts (TTS), Pillow (WebP), mutagen (MP3 QA).
# The base image is externally managed, so --break-system-packages is required.
python3 -m pip install --break-system-packages --no-warn-script-location -r requirements.txt

python3 - <<'PY'
import edge_tts, PIL, mutagen
from PIL import Image
from mutagen.mp3 import MP3
print("tooling ok: edge-tts", edge_tts.__version__, "| Pillow", PIL.__version__, "| mutagen", mutagen.version)
PY
