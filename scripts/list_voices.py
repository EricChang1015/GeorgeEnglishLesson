import asyncio
import edge_tts


async def main() -> None:
    vs = await edge_tts.list_voices()
    for v in sorted(vs, key=lambda x: x["ShortName"]):
        if not v["Locale"].startswith("en"):
            continue
        name = v["ShortName"]
        blob = f"{v.get('FriendlyName', '')} {name}".lower()
        keys = ("ana", "maisie", "noah", "child", "guy", "eric", "davis", "andrew", "ryan", "thomas", "sonia", "aria", "jenny", "christopher", "brian", "jason", "tony")
        if any(k in blob for k in keys):
            print(f"{name}\t{v['Gender']}\t{v['Locale']}")


if __name__ == "__main__":
    asyncio.run(main())
