"""Generate short boy-voice samples for George.

Chosen voice (parent-approved): en-US-AnaNeural, +12%, -10Hz — see lesson-design.mdc.
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
    for label, slug, voice, rate, pitch in CANDIDATES:
        path = OUT / f"{slug}.mp3"
        await edge_tts.Communicate(TEXT, voice=voice, rate=rate, pitch=pitch).save(str(path))
        print(f"OK  {slug}.mp3  —  {label}")


if __name__ == "__main__":
    asyncio.run(main())
