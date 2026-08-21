# Big Eye Dreams — 篇章定稿 v0

獨立新篇章，**不**接 Lesson 1–3（Pip / Ember）。  
狀態：2026-08-21 — **Lesson 4 已出圖、已錄音、已上線**（George and the Dinosaur Under the Blanket）。

---

## 系列核心

George 每晚抱著膽小的獨眼布偶 **Big Eye**（大眼仔）睡覺。  
Big Eye 眨眼三下，房間就慢慢變成夢裡世界。  
Big Eye 看得很清楚，但很容易害怕；George 要觀察、推理、溫柔幫忙。  
每次醒來，床邊都會留下一個小小證據。

**系列名（暫定）：** Big Eye Dreams  
**第一課標題：** George and the Dinosaur Under the Blanket

---

## 畫風定調

### 整體

| 項目 | 鎖定 |
|------|------|
| 風格 | 溫暖手繪／水彩 bedtime picture-book |
| 色調 | 奶油白、淡藍、月光紫、柔綠；夜晚不恐怖 |
| 光 | 小夜燈暖光 + 月光；Big Eye 眨眼時有柔柔綠光 |
| 禁止 | 3D 電影風、寫實照片臉、恐怖陰影、畫面英文正文 |

### 夢境規則（每頁都要有一點「還是我的房間」）

| 現實（ref） | 夢裡變形 |
|-------------|----------|
| 奶油色棉被／床單 | 柔軟的 blanket mountain |
| 枕頭 | pillow cave |
| 灰色窗簾 | curtain forest（暗但不嚇人） |
| 星星小夜燈 | 指路的小星光 |
| 淺藍床單 | moonlit path |

### 角色外形鎖定

#### George（睡前篇）

- 東亞男孩約 5 歲；短黑髮、瀏海、圓臉、大眼
- **睡衣（本系列固定）：** 白色短袖睡衣 + 小彩色圓點／齒輪印花；淺藍床單
- 臉 ref：`george-solo-bed-smile.jpg`；睡姿 ref：`george-solo-bed-mike-plush-side-sleep.jpg`
- 不可變：另一張臉、白天出門外套

#### Big Eye（大眼仔）— 原創布偶，不是 Mike Wazowski

- 柔軟圓球身體；高度約 George 胸口（可抱）
- 一隻大圓眼：暖白眼白 + 藍綠虹膜
- 兩隻短短軟角（像布耳朵）；細長手腳，末端圓圓布手，**無尖爪**
- 縫線微笑；害怕時嘴變成小小一條線
- 靈感 ref：`mike-plush-indoor-closeup.jpg`（只借形狀比例，畫成原創、更圓更軟）
- 夢裡會動、會說話，但仍是布偶質感

#### Nibble（小恐龍）

- 幼龍；**膝蓋高**；圓頭、大眼、短手短尾
- 暖黃綠身體 + 背上幾個柔和小斑點；**不要**畫成暴龍
- 聲音是 soft peep，不是 roar
- 個性：害羞、迷路、想回家

#### Daddy

- 沿用 cast bible；睡前場景：細框眼鏡、藍灰 raglan 睡衣上衣
- 臉 ref：`george-daddy-outdoors-pavilion-neutral.jpg`；姿勢 ref：`george-daddy-bedtime-reading.jpg`

### 場景 ref（出圖前 Read）

| 用途 | 檔案 |
|------|------|
| George 臉 | `lessons/assets/refs/george/george-solo-bed-smile.jpg` |
| 房間布局／棉被 | `lessons/assets/refs/george/mike-plush-bedroom-bed-scattered.jpg` |
| Daddy 睡前閱讀 | `lessons/assets/refs/george/george-daddy-bedtime-reading.jpg` |
| George 抱玩偶側睡 | `lessons/assets/refs/george/george-solo-bed-mike-plush-side-sleep.jpg` |
| Big Eye 外形 | `lessons/assets/refs/george/mike-plush-indoor-closeup.jpg` |

### Prompt 重複句（每頁複製）

```text
Warm watercolor bedtime picture-book. George (East Asian boy ~5, short black bangs, round face, white short-sleeve pajamas with tiny colorful prints). Big Eye (original soft lime-green one-eyed plush, round body, one large blue-green eye, tiny soft fabric horns, thin floppy limbs, stitched smile — NOT Mike Wazowski). Nibble (tiny baby dinosaur, knee-high to George, warm yellow-green, round head, gentle eyes, small spots). Cozy bedroom: cream blanket, pale blue sheet, beige headboard, grey curtains, star night-light. Dream transforms the same room — blanket becomes a soft mountain, pillow a cave, curtains a gentle forest. No horror, no photorealism, no on-image text.
```

---

## 語音定調

沿用已鎖角色；新角色需與 George / Pip / Ember **可分辨**。

| Role key | 角色 | 引擎 | Voice | Rate / Speed | Pitch | 聽感 |
|----------|------|------|-------|--------------|-------|------|
| `narrator` | 旁白 | Edge | `en-GB-SoniaNeural` | `-10%` | `+0Hz` | 平穩英國成人 |
| `george` | George | MiniMax | `cute_boy` F2 | `1.30` | `0` | 同 L3；逐句 emotion |
| `daddy` | Daddy | Edge | `en-GB-RyanNeural` | `-5%` | `-5Hz` | 溫暖父親 |
| `bigeye` | Big Eye | Edge | `en-US-AnaNeural` | `+5%` | `+20Hz` | **同 Pip**；緊張／開心靠逐句 `emotion` |
| `nibble` | Nibble | Edge | `en-GB-MaisieNeural` | `+12%` | `+8Hz` | 幼龍；軟、短、略尖 |

**分工：** Big Eye = 看見線索、容易怕；George = 冷靜推理；Nibble = 短句 + peep 感。

機器可讀：`scripts/voices.json`（`bigeye`, `nibble`）  
故事 draft：`scripts/lesson04_story.json`

---

## Lesson 4 — 故事全文（12 頁，每頁 3–4 句）

敘事規則：George 與 Big Eye **不知道這是夢境**。角色只描述眼前發生的事；直到早晨留下蕨葉，真實與夢境仍沒有答案。

### Page 1 — Bedtime reading

**Illustration:** Daddy 和 George 靠床頭；George 手邊放著 Big Eye。  
**Refs:** `george-daddy-bedtime-reading.jpg`

| Role | Line | Emotion |
|------|------|---------|
| narrator | It was late, and George was tucked under his warm blanket in the big bed. | calm |
| narrator | Daddy sat beside him and read one last story from the phone. | calm |
| daddy | "Just one more chapter, George. Then it is time to sleep." | soft |
| george | "Can Big Eye listen too? He likes adventures." | happy |

### Page 2 — Lights out

**Illustration:** 房間變暗；George 側躺，手臂環抱 Big Eye。  
**Refs:** `george-solo-bed-mike-plush-side-sleep.jpg`

| Role | Line | Emotion |
|------|------|---------|
| narrator | When the story ended, Daddy kissed George good night and turned off the main light. | calm |
| narrator | Only the little star lamp was left, glowing softly beside the bed. | calm |
| george | "Good night, Big Eye. Hold my hand until I fall asleep." | calm |

### Page 3 — Thump under the blanket

**Illustration:** 棉被下微微鼓起；Big Eye 睜眼。  
**Refs:** `mike-plush-bedroom-bed-scattered.jpg`

| Role | Line | Emotion |
|------|------|---------|
| narrator | George had almost closed his eyes when something under the blanket went thump, thump, thump. | surprised |
| bigeye | "George, did you hear that? Something is moving under the blanket!" | fearful |
| george | "My feet did not move. Let us look again, very carefully." | worried |

### Page 4 — Three blinks

**Illustration:** Big Eye 眨眼；窗簾泛銀光；棉被隆起。  
**Refs:** bedroom anchor + dream glow

| Role | Line | Emotion |
|------|------|---------|
| narrator | Big Eye blinked once, twice, then three times, and a soft green light filled the room. | wonder |
| narrator | The grey curtains shone like silver trees, and the blanket rose beneath them like a hill. | wonder |
| george | "Big Eye, what is happening to our room?" | surprised |

### Page 5 — Blanket mountain

**Illustration:** 棉被變山；枕頭變洞；蕨類從床單長出；仍看得見床頭。  
**Refs:** `mike-plush-bedroom-bed-scattered.jpg` → dream transform

| Role | Line | Emotion |
|------|------|---------|
| narrator | The blanket had become a soft green mountain, with a pillow cave at the very top. | wonder |
| narrator | Small green ferns grew beside the sheet, and tiny footprints led up the slope. | wonder |
| bigeye | "Look! I can see tiny footprints on the mountain!" | surprised |
| george | "We should follow them. Stay close to me, Big Eye." | calm |

### Page 6 — Behind the fold

**Illustration:** George 彎腰看棉被褶皺後；Big Eye 躲在他袖子後。  
**Refs:** blanket mountain close-up

| Role | Line | Emotion |
|------|------|---------|
| narrator | They climbed a little way when another thump came from behind a fold in the blanket. | worried |
| george | "Hold my hand, Big Eye. I will look first, and you can stay right behind me." | calm |
| bigeye | "All right, but please do not let go of my hand." | whisper |

### Page 7 — Not a monster

**Illustration:** 小恐龍 Nibble 探頭；圓眼、短尾、發抖。  
**Refs:** Nibble scale lock (knee-high)

| Role | Line | Emotion |
|------|------|---------|
| narrator | George lifted the fold gently, and a tiny dinosaur peeked out with round, worried eyes. | surprised |
| bigeye | "A dinosaur! George, it might be a monster!" | fearful |
| george | "Look carefully, Big Eye. It is little, and it looks frightened, not fierce." | calm |

### Page 8 — The lost little dinosaur

**Illustration:** Nibble 從棉被後走出；留下小腳印。  
**Refs:** footprint trail on blanket

| Role | Line | Emotion |
|------|------|---------|
| nibble | "Peep! Peep! I cannot find my nest anywhere!" | worried |
| george | "Do not worry, little one. We will help you. Which way is home?" | calm |
| nibble | "My nest smells like warm leaves, near a pale cave at the top of the hill." | soft |

### Page 9 — Footprints and star light

**Illustration:** George 舉星星夜燈；Big Eye 指腳印；窗簾森林在遠處。  
**Refs:** star night-light as compass

| Role | Line | Emotion |
|------|------|---------|
| bigeye | "The footprints go towards the curtain forest! I can see them clearly." | excited |
| narrator | George raised the star lamp high, and its warm beam lit a narrow path between the curtains. | wonder |
| george | "One step at a time. Nibble, follow the footprints with us." | calm |

### Page 10 — Brave whisper

**Illustration:** 窗簾森林較暗；Big Eye 發抖；George 牽著他。  
**Refs:** grey curtains → gentle forest

| Role | Line | Emotion |
|------|------|---------|
| narrator | Beneath the tall curtains, the path grew darker, and Big Eye began to tremble. | worried |
| bigeye | "It is too dark in here! What if something big is hiding in the curtain forest?" | fearful |
| george | "We can be quiet, but we can still be brave. I am right beside you." | whisper |

### Page 11 — The warm nest

**Illustration:** 枕頭洞旁軟葉巢；Nibble 蜷進去；Big Eye 微笑。  
**Refs:** pillow cave + nest

| Role | Line | Emotion |
|------|------|---------|
| narrator | At last they reached the pillow cave, where a nest of warm leaves waited in the moonlight. | wonder |
| nibble | "My nest! We found it! Peep, peep!" | happy |
| george | "You are home now, Nibble. Sleep well in your warm nest." | calm |
| bigeye | "I was scared, but I kept looking, and we found the way." | happy |

### Page 12 — Morning proof

**Illustration:** 早晨 George 醒來；Big Eye 在下巴下；枕邊一片小蕨葉；Daddy 在門口。  
**Refs:** `george-solo-bed-mike-plush-side-sleep.jpg` → morning

| Role | Line | Emotion |
|------|------|---------|
| narrator | In the morning, George woke beside Big Eye and found a tiny green fern leaf on the blanket. | wonder |
| george | "Daddy, look! Where did this leaf come from? It was not here last night." | surprised |
| daddy | "I do not know, George. It looks very strange. Do you know where it came from?" | wonder |

---

## 單字方向（Lesson 4 草案）

約 10 個；例句比單字難半級：

| Word | Example |
|------|---------|
| blanket | Something moved under the blanket. |
| whisper | Big Eye spoke in a soft whisper. |
| tremble | Big Eye began to tremble in the dark. |
| footprint | I can see tiny footprints on the mountain. |
| fern | A green fern grew beside the sheet. |
| nest | Nibble could not find her warm nest. |
| brave | We can be quiet, but we can still be brave. |
| lost | The little dinosaur was lost under the blanket. |
| glow | The star night-light glowed softly. |
| adventure | I think I had an adventure last night. |

**Key phrases:** `Hold my hand.` · `Look carefully.` · `Stay close to me.` · `Let us look again.` · `You are home now.`

---

## 下一步（尚未做）

1. 家長確認 Big Eye / Nibble 語音試聽  
2. 產 Big Eye + Nibble character sheet  
3. 依本檔 + `scripts/lesson04_story.json` 出 cover + 12 story pages  
4. 錄音 → `lessons/lesson-04.html`
