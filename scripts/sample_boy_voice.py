"""Generate short boy-voice samples for George.

Chosen voice (parent-approved): en-US-AnaNeural, +12%, -10Hz — see scripts/voices.json.
Outputs stay under lessons/assets/lesson-02/voice-tests/ (gitignored). See tools/README.md.
"""
import asyncio
from pathlib import Path
import edge_tts

OUT = Path(__file__).resolve().parents[1] / "lessons" / "assets" / "lesson-02" / "voice-tests"
TEXT = "Pip! I'm here! How is the red egg today?"

# Round 2: much higher pitch — target ~5-year-old boy (not teen/adult)
# (label, file slug, voice, rate, pitch)
CANDIDATES = [
    ("A · Ana — child voice (native)", "a_ana_child", "en-US-AnaNeural", "+10%", "+0Hz"),
    ("B · Liam — high pitch", "b_liam_high", "en-CA-LiamNeural", "+18%", "+58Hz"),
    ("C · Thomas — high pitch", "c_thomas_high", "en-GB-ThomasNeural", "+18%", "+62Hz"),
    ("D · Liam — extra high", "d_liam_xhigh", "en-CA-LiamNeural", "+22%", "+75Hz"),
    ("E · Ana — child, slightly lower", "e_ana_boyish", "en-US-AnaNeural", "+12%", "-10Hz"),
]


async def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    cards = []
    for label, slug, voice, rate, pitch in CANDIDATES:
        path = OUT / f"{slug}.mp3"
        await edge_tts.Communicate(TEXT, voice=voice, rate=rate, pitch=pitch).save(str(path))
        print(f"OK  {slug}.mp3  —  {label}")
        cards.append(
            f"<section><strong>{label}</strong>"
            f"<audio controls src='{slug}.mp3'></audio></section>"
        )
    html = f"""<!DOCTYPE html>
<html lang="zh-Hant"><head><meta charset="utf-8"/>
<title>Voice listen · George</title>
<style>
body {{ font-family: system-ui, sans-serif; max-width: 36rem; margin: 2rem auto; padding: 0 1rem; background: #fff9f0; }}
section {{ background: #fff; border-radius: 12px; padding: 0.8rem 1rem; margin: 0.6rem 0; }}
audio {{ width: 100%; display: block; margin-top: 0.4rem; }}
</style></head><body>
<h1>George 聲線試聽（未發佈）</h1>
<p>「{TEXT}」</p>
{''.join(cards)}
</body></html>
"""
    (OUT / "index.html").write_text(html, encoding="utf-8")
    print(f"Listen: {OUT / 'index.html'}")


if __name__ == "__main__":
    asyncio.run(main())
