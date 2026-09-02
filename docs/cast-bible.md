# Cast & scene bible — Pip and Ember chapter

出任何新插畫（含重畫 Lesson 1–3）**之前**先讀本檔，再讀 `.cursor/skills/picture-book-consistency/SKILL.md`。  
真人參考仍以 `lessons/assets/refs/george/CATALOG.md` 為準。本檔鎖定**故事角色比例、服裝、場景**，補照片沒有的部分。

狀態：2026-08-21。已有角色表 `lessons/assets/refs/cast/pip-ember-sheet.png`（Lesson 3 重畫用）。比例仍以下列鎖定頁為輔。

---

## Style (整篇章共用)

- 溫暖手繪／水彩童書；柔和邊緣、飽和但不過螢光
- 不要寫實照片、不要 3D 電影風、不要每頁換畫風
- 畫面不寫英文正文（文字留給播放器）

---

## Scale lock（最容易跑掉，每次都要寫進 prompt）

以站立的 George（約 5 歲）為尺：

| 角色 | 相對身高 | 不要變成 |
|------|----------|----------|
| George | 基準（站立約到成人腰） | 另一張臉、另一套日常衣服 |
| Pip | 站到 George **腰～胸口**；頭明顯小於 George | 和 George 一樣高、或像寵物一樣只有腳踝高 |
| Ember | 站到 George **膝蓋上下**；明顯比 Pip 小、剛孵出來的妹妹 | 和 Pip 一樣大、或比 George 還大 |
| Daddy | 成人；George 約到他腰／胸口 | 和 George 差不多高 |

群像頁必須同時看得到這組比例。遠景可縮小整組，但**彼此相對尺寸不變**。

---

## Characters — 不可變項

### George

- 東亞男孩約 5 歲；短黑髮含瀏海；圓臉；大眼
- 臉：先讀 `george-solo-bed-smile.jpg`；封面近臉可用 `george-solo-sofa-alphabet-smile.jpg`
- **出門預設服裝（山丘／洞穴故事）：** 亮藍拉鍊連帽外套、卡其／米色長褲、藍白運動鞋
- 可變：表情、姿勢、外套拉鍊開合；**不可變：** 另一個孩子的臉、金髮、完全不同的招牌衣服（除非故事明確换衣服）

### Pip（綠龍，哥哥）

- 友善的小綠龍；雙足可站；小蝙蝠翅
- 鎖定：翠綠身體、淺奶油／淡黃分節肚皮、淺棕／黃褐色一對角、背部一排較小的綠或黃綠刺
- 眼睛大、溫暖棕或琥珀，不是兇惡細長瞳
- 體型見上表。L2 孵蛋頁把 Pip 畫得過大，**不要再沿用那一頁的比例**
- 比例鎖定頁：`lessons/assets/lesson-01/story-03.webp`（Pip ≈ 腰／胸高）
- 群像鎖定頁：`lessons/assets/lesson-03/story-01.webp`（三人＋洞口）

### Ember（紅龍，妹妹，Lesson 2 出生）

- 幼龍；紅／橘紅；比 Pip 明顯更圓、更小
- 小翅、短角、大眼；剛出生可以帶一點蛋殼／草窩，之後仍保持「幼體」比例
- 不要畫成第二隻綠色龍，也不要畫成和 Pip 同體型的紅龍

### Daddy

- 東亞成人；短深色頭髮；細框圓／橢圓金屬眼鏡
- 臉：`george-daddy-outdoors-pavilion-neutral.jpg`
- 上山尋人：成人戶外衣著即可，但眼鏡與臉型要穩

### Mummy / Sylvia

**Sylvia** — older sister, East Asian teen (~12–14). Long straight black hair (side-swept bangs; ponytail or half-up in some refs); **black rectangular glasses** in most lesson art; taller than Mummy, shorter than Daddy.

- Solo refs + tags: `lessons/assets/refs/sylvia/CATALOG.md`
- Default face: `sylvia-solo-outdoors-graduation-smile.jpg`
- With George / family: `lessons/assets/refs/george/CATALOG.md` (e.g. `george-sylvia-arcade-play.jpg`)

**Mummy** — 尚未在本篇章對白中固定登場。若入畫：先問家長，再補聖經欄位。

---

## Scenes — 本篇章錨點

少而穩，每頁 prompt 重複關鍵錨點，不要每頁發明新地標。

| 錨點 | 鎖定 | 出現課次 |
|------|------|----------|
| 綠山丘 | 緩坡、草地、遠山；天氣可變（晴／陰／雨） | 1–3 |
| 莓果小徑 | 淺色土石路、兩旁矮叢與紅莓 | 3（2 有採莓） |
| Pip 的洞穴 | 山壁上的圓形／拱形洞口、外有苔蘚石；內暖黃岩壁 | 1–3 |
| 紅蛋／草窩 | 只在 L1 結尾與 L2 開頭；蛋紅、窩金黃草 | 1–2 |

**不要**每頁換一條河的位置、換一個完全不同的洞口形狀，除非故事走到新地點。

---

## Prompt 重複句（複製到每一頁）

```text
Same picture-book watercolor cast: George (East Asian boy ~5, short black bangs, round face, bright blue zip hoodie, tan trousers); Pip (small green dragon, cream segmented belly, tan horns, small bat wings, only waist-to-chest high next to George); Ember (tiny red baby dragon, knee-high to George, clearly smaller than Pip). Do not resize the dragons independently. Same green hill and mossy cave mouth unless the page is a new place.
```

---

## Approved lock frames（出圖前 Read）

| 用途 | 檔案 |
|------|------|
| 角色表（出圖主錨） | `lessons/assets/refs/cast/pip-ember-sheet.png` |
| George 臉 | `lessons/assets/refs/george/george-solo-bed-smile.jpg` |
| George 近臉／封面 | `lessons/assets/refs/george/george-solo-sofa-alphabet-smile.jpg` |
| Daddy 臉 | `lessons/assets/refs/george/george-daddy-outdoors-pavilion-neutral.jpg` |
| Pip 對 George 的身高 | `lessons/assets/lesson-01/story-03.webp` |
| 三人＋洞口群像 | `lessons/assets/lesson-03/story-01.webp` |

L1 封面（Pip 過小、George 衣服不同）與 L2 孵蛋（Pip 過大）**只當劇情參考，不當外形聖經**。
