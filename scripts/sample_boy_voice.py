"""Generate short boy-voice samples for George."""
import asyncio
from pathlib import Path
import edge_tts

OUT = Path(__file__).resolve().parents[1] / "lessons" / "assets" / "lesson-02" / "voice-tests"
TEXT = "Pip! I'm here! How is the red egg today?"

CANDIDATES = [
    ("liam_p32", "en-CA-LiamNeural", "+12%", "+32Hz"),
    ("thomas_p35", "en-GB-ThomasNeural", "+12%", "+35Hz"),
    ("brian_p28", "en-US-BrianNeural", "+15%", "+28Hz"),
    ("eric_p30", "en-US-EricNeural", "+15%", "+30Hz"),
]


async def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, voice, rate, pitch in CANDIDATES:
        path = OUT / f"{name}.mp3"
        await edge_tts.Communicate(TEXT, voice=voice, rate=rate, pitch=pitch).save(str(path))
        print("OK", path.name)


if __name__ == "__main__":
    asyncio.run(main())
