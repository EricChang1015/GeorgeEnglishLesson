#!/usr/bin/env python3
"""Build scripts/lesson07_story.json from frozen Sol 19-page plot (GATE 1 approved)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = [
    {
        "img": "story-01.png",
        "alt": "In the living room George in a T-rex onesie chases Sylvia with a wooden play fork; she laughs in green pajamas",
        "lines": [
            ("narrator", "After tea, George stomped through the living room in his T-rex suit.", "lively"),
            ("george", "Roar! I am the biggest dinosaur in this whole house!", "proud"),
            ("sylvia", "George, stop chasing me with that silly wooden fork!", "annoyed"),
            ("george", "Keep running, Sylvia! Wild T-rex George is coming closer!", "naughty"),
        ],
    },
    {
        "img": "story-02.png",
        "alt": "Mummy in dusty-pink pajamas points toward the bedroom; George holds the wooden fork; Sylvia watches",
        "lines": [
            ("mummy", "George, you are being wild, not being a kind brother.", "cross"),
            ("george", "Wild things never have to listen to anybody else!", "defiant"),
            ("mummy", "Then there is no supper. Go to your room now.", "firm"),
            ("sylvia", "Next time, please leave the wooden fork behind.", "gentle"),
        ],
    },
    {
        "img": "story-03.png",
        "alt": "George sits alone on his cream bed in T-rex suit; the wooden fork beside the bed; bird lamp glowing",
        "lines": [
            ("narrator", "George shut his bedroom door with one enormous thump.", "calm"),
            ("george", "Fine! I do not want any supper tonight anyway.", "sulky"),
            ("narrator", "He left the wooden fork beside his bed and listened.", "soft"),
            ("george", "Why does being wild suddenly feel so lonely?", "lonely"),
        ],
    },
    {
        "img": "story-04.png",
        "alt": "Green vines climb the cream bedroom walls; bed, bird lamp and grey curtains remain visible",
        "lines": [
            ("narrator", "A green vine curled around the beige headboard beside him.", "wonder"),
            ("george", "My bed is still here, but the walls are growing!", "amazed"),
            ("narrator", "The bird lamp glowed warmly between broad jungle leaves.", "calm"),
            ("george", "Something is pushing through the leaves near my curtains.", "curious"),
        ],
    },
    {
        "img": "story-05.png",
        "alt": "A small tea-brown boat with a tea-leaf sail waits beside George's bed; fork stays on the bed",
        "lines": [
            ("narrator", "A little tea-brown boat nosed through the leaves beside his bed.", "wonder"),
            ("george", "Billy o' Tea, you came here just for me!", "excited"),
            ("narrator", "George left the fork behind and climbed carefully aboard.", "calm"),
            ("george", "Take me somewhere every wild thing can be free!", "bold"),
        ],
    },
    {
        "img": "story-06.png",
        "alt": "George steers Billy o' Tea alone under a lavender sky; island silhouettes ahead; bird-lamp glow behind",
        "lines": [
            ("narrator", "Billy o' Tea sailed beyond fern waves under lavender skies.", "calm"),
            ("george", "The sea smells like rain, leaves, and something sweet.", "curious"),
            ("narrator", "The bird-lamp glow shrank as one long night rolled past.", "soft"),
            ("george", "An island! Three enormous shapes are waiting on the shore.", "alert"),
        ],
    },
    {
        "img": "story-07.png",
        "alt": "Horn, Beak and Goat block the sandy shore; George stands brave at the boat bow in blue shoes",
        "lines": [
            ("horn", "Who brings that tiny boat onto our enormous island?", "fierce"),
            ("beak", "Turn your leaf sail around before we show our claws!", "challenging"),
            ("goat", "The path ahead belongs to three very wild things.", "warning"),
            ("george", "I sailed too far to run away before meeting you.", "brave"),
        ],
    },
    {
        "img": "story-08.png",
        "alt": "Horn stamps the sand, Beak scratches dead wood, Goat blocks the vine bridge; George stands steady",
        "lines": [
            ("horn", "My hooves can make the whole sandy shoreline tremble!", "booming"),
            ("beak", "My claws can scratch deep lines into dead wood!", "showy"),
            ("goat", "My horns guard the only bridge into our jungle.", "firm"),
            ("george", "You are noisy, but I can still stand steady.", "composed"),
        ],
    },
    {
        "img": "story-09.png",
        "alt": "George stares into three pairs of yellow eyes; Horn lowers his head first; boat still on the shore",
        "lines": [
            ("george", "Look into my eyes. I will not hurt you or hide.", "steady"),
            ("narrator", "George held their yellow gaze without raising a single fist.", "calm"),
            ("horn", "His knees stayed still. Lower your claws, wild friends.", "awed"),
            ("goat", "Courage like that may cross our guarded bridge.", "respectful"),
        ],
    },
    {
        "img": "story-10.png",
        "alt": "Horn leads George across a vine bridge into a wide moonlit jungle; footprints point inland",
        "lines": [
            ("horn", "Follow my footprints; brave visitors may enter our island.", "welcoming"),
            ("narrator", "Beyond the bridge, the jungle opened wider than the shore.", "wonder"),
            ("beak", "Our moonlit clearing has waited for someone truly fearless.", "excited"),
            ("george", "Then show me what waits beyond those enormous trees.", "eager"),
        ],
    },
    {
        "img": "story-11.png",
        "alt": "Beak places a vine crown on George's T-rex hood in a moonlit clearing; leaf throne and wooden drum nearby",
        "lines": [
            ("beak", "Wear this vine crown, brave George, and lead us fairly.", "proud"),
            ("horn", "You faced our wildness without becoming cruel or afraid.", "loyal"),
            ("goat", "A good king listens before making the island roar.", "wise"),
            ("george", "I will be a wild king who keeps everyone safe.", "honoured"),
        ],
    },
    {
        "img": "story-12.png",
        "alt": "George with vine crown stomps in a wild parade with Horn, Beak and Goat in the clearing",
        "lines": [
            ("goat", "Our wild parade begins with four enormous stamping beats!", "joyful"),
            ("george", "Stomp together, then spin when Horn strikes the drum!", "gleeful"),
            ("narrator", "Four happy sets of feet thundered around the clearing.", "lively"),
            ("horn", "The silver seedpods are answering us from the trees!", "excited"),
        ],
    },
    {
        "img": "story-13.png",
        "alt": "Moonlit parade swirl in the clearing; Beak leads from a low stump; silver seedpods in the trees",
        "lines": [
            ("beak", "Follow my wings beneath the bright and bumpy moon!", "delighted"),
            ("george", "Swirl past the seedpods, then roar and bow together!", "playful"),
            ("narrator", "Their shadows wheeled around the trees for another merry round.", "warm"),
            ("horn", "Careful! Our happy feet are tangling into one furry heap!", "surprised"),
        ],
    },
    {
        "img": "story-14.png",
        "alt": "George with crown holds up two fingers announcing royal rules; beasts sit laughing on the ground",
        "lines": [
            ("george", "First royal rule: big feet wait for smaller feet.", "kindly"),
            ("george", "Second royal rule: every roar ends with a friendly bow.", "playful"),
            ("goat", "Those rules leave room for every wild thing.", "approving"),
            ("beak", "Line up again! This time, nobody tangles their tails.", "eager"),
        ],
    },
    {
        "img": "story-15.png",
        "alt": "George leads another parade round in the clearing; moon high; many footprint rings on the ground",
        "lines": [
            ("narrator", "The kinder parade rolled through three more moonlit rounds.", "warm"),
            ("horn", "King George, your rules make wild games last longer!", "delighted"),
            ("george", "One final march, then everyone takes a quiet rest.", "content"),
            ("narrator", "The last bow ended, and George's empty tummy growled.", "soft"),
        ],
    },
    {
        "img": "story-16.png",
        "alt": "Tired George sits on the leaf throne holding crown and tummy; distant bird-lamp glow over the sea",
        "lines": [
            ("narrator", "After so many rounds, the vine crown felt strangely heavy.", "soft"),
            ("george", "My tummy is louder than Horn's great wooden drum.", "hungry"),
            ("narrator", "A warm supper smell drifted from the distant bird-lamp glow.", "tender"),
            ("george", "I miss Mummy, Daddy, Sylvia, and our table.", "homesick"),
        ],
    },
    {
        "img": "story-17.png",
        "alt": "George gives the vine crown to Horn on the shore; Beak steadies Billy o' Tea; Goat waves goodbye",
        "lines": [
            ("george", "I choose home. Horn, please keep my crown here.", "resolved"),
            ("goat", "A true king may follow where his loving heart leads.", "gentle"),
            ("beak", "I will steady your boat while you climb aboard.", "helpful"),
            ("horn", "Sail safely, George. Your kind rules will stay here.", "warm"),
        ],
    },
    {
        "img": "story-18.png",
        "alt": "George sails Billy o' Tea homeward; Horn holds the crown on the shrinking island; bird-lamp glow ahead",
        "lines": [
            ("narrator", "Billy o' Tea turned from the island toward the warm glow.", "calm"),
            ("george", "Goodbye, wild friends! Keep bowing after every happy roar!", "wistful"),
            ("narrator", "The three beasts waved until moonlit waves hid the shore.", "tender"),
            ("george", "The bird lamp is brighter now. Home must be close.", "hopeful"),
        ],
    },
    {
        "img": "story-19.png",
        "alt": "Family in pajamas waits with steaming supper in George's bedroom; George still wears the T-rex hood",
        "lines": [
            ("george", "I came back because home is my favourite wild place.", "loving"),
            ("mummy", "Your supper is still hot, and we saved your seat.", "soft"),
            ("daddy", "Welcome back, George. We were waiting to eat together.", "warm"),
            ("sylvia", "After supper, chase me with hugs, not that fork!", "teasing"),
        ],
    },
]

def main():
    base = json.loads((ROOT / "scripts" / "lesson07_story.json").read_text(encoding="utf-8"))
    pages = []
    for i, pg in enumerate(PAGES, start=1):
        prefix = f"p{i:02d}"
        lines = []
        for j, (role, text, emotion) in enumerate(pg["lines"], start=1):
            lines.append({
                "role": role,
                "text": text,
                "audio": f"{prefix}-{j:02d}.mp3",
                "emotion": emotion,
            })
        pages.append({"img": pg["img"], "alt": pg["alt"], "lines": lines})

    base["learning"] = {
        "summary_zh": (
            "George 穿 T-rex 裝在客廳拿木叉追姐姐，被罰回房不准吃晚飯。房間長出叢林，"
            "Billy o' Tea 載他到野獸島。他拒退、對視馴服三獸，當王跳 wild parade、"
            "頒兩條王規後自願留冠回家，晚飯還熱。"
        ),
        "focus_en": [
            "Story words: wild thing, jungle, stare, crown, parade, rule",
            "Home words: wooden fork, living room, supper, homeward",
            "Feeling: lonely, homesick, still hot",
            "Key phrases: Look into my eyes. First royal rule. I choose home.",
        ],
        "tutor_prompts_zh": [
            "問：Mummy 為什麼罰 George？（客廳拿木叉追 Sylvia、太 wild）",
            "問：George 怎樣進入野獸國？（對視、不逃、過藤橋）",
            "問：George 當王時訂了什麼規矩？（大腳等小腳；吼完要鞠躬）",
            "問：他為什麼想回家？（冠變重、肚子餓、聞到家中暖香）",
            "問：王冠後來呢？（自願留給 Horn，沒帶回家）",
        ],
    }
    base["vocab"] = [
        {"word": "wild thing", "example": "Mummy said wild things still need kind brothers.", "img": "story-02.png", "alt": "Mummy calling George wild in the living room", "audio": "vocab-wild-thing.mp3", "example_audio": "vocab-wild-thing-ex.mp3"},
        {"word": "wooden fork", "example": "Sylvia asked George to leave the wooden fork behind.", "img": "story-01.png", "alt": "George chasing Sylvia with a wooden play fork", "audio": "vocab-wooden-fork.mp3", "example_audio": "vocab-wooden-fork-ex.mp3"},
        {"word": "jungle", "example": "Green vines turned his room into a jungle.", "img": "story-04.png", "alt": "vines growing in George's bedroom", "audio": "vocab-jungle.mp3", "example_audio": "vocab-jungle-ex.mp3"},
        {"word": "stare", "example": "George stared into their yellow eyes without fear.", "img": "story-09.png", "alt": "George staring into yellow wild-thing eyes", "audio": "vocab-stare.mp3", "example_audio": "vocab-stare-ex.mp3"},
        {"word": "crown", "example": "Beak placed a vine crown on George's dinosaur hood.", "img": "story-11.png", "alt": "a leafy vine crown on George's hood", "audio": "vocab-crown.mp3", "example_audio": "vocab-crown-ex.mp3"},
        {"word": "parade", "example": "Their wild parade began with four enormous stamping beats.", "img": "story-12.png", "alt": "George and wild things stomping in a parade", "audio": "vocab-parade.mp3", "example_audio": "vocab-parade-ex.mp3"},
        {"word": "rule", "example": "First royal rule: big feet wait for smaller feet.", "img": "story-14.png", "alt": "George announcing two royal rules", "audio": "vocab-rule.mp3", "example_audio": "vocab-rule-ex.mp3"},
        {"word": "still hot", "example": "His supper was still hot when he came home.", "img": "story-19.png", "alt": "steaming supper tray with the family", "audio": "vocab-still-hot.mp3", "example_audio": "vocab-still-hot-ex.mp3"},
    ]
    base["pages"] = pages
    base["quiz"] = [
        {"q": "Where did George chase Sylvia?", "options": ["In the living room", "On the island", "On the boat"], "answer": 0},
        {"q": "What did George leave beside his bed?", "options": ["His blue shoes", "The wooden fork", "The vine crown"], "answer": 1},
        {"q": "What grew in George's room?", "options": ["A jungle of vines", "A stone forest", "A muddy puddle"], "answer": 0},
        {"q": "What was the name of the little boat?", "options": ["Wellerman", "Billy o' Tea", "Wild Parade"], "answer": 1},
        {"q": "How did George tame the wild things?", "options": ["He hit them with the fork", "He stared into their yellow eyes", "He hid behind the boat"], "answer": 1},
        {"q": "Who put the vine crown on George?", "options": ["Beak", "Daddy", "Sylvia"], "answer": 0},
        {"q": "What was George's first royal rule?", "options": ["No more roaring ever", "Big feet wait for smaller feet", "Kings must sleep standing up"], "answer": 1},
        {"q": "What did George do with the crown?", "options": ["He took it home to bed", "He threw it in the sea", "He left it with Horn"], "answer": 2},
        {"q": "What was waiting in his room?", "options": ["A cold sandwich", "Supper that was still hot", "The three wild things"], "answer": 1},
        {"q": "Who was waiting at home?", "options": ["Only Mummy", "Mike and Nibble", "Mummy, Daddy and Sylvia"], "answer": 2},
    ]
    base["phrases"] = [
        "Look into my eyes",
        "wild thing",
        "First royal rule",
        "I choose home",
        "still hot",
        "friendly bow",
    ]

    out = ROOT / "scripts" / "lesson07_story.json"
    out.write_text(json.dumps(base, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out} — {len(pages)} pages, {sum(len(p['lines']) for p in pages)} lines")


if __name__ == "__main__":
    main()
