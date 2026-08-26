# George's Real Adventures — 篇章定稿 v0

新篇章：George 一家的**真實旅行故事**，不接 Pip and Ember，也不接 Mike Dreams。
狀態：2026-08-26 — **lesson-05 已交付**（GATE 3 PASS）。家長修訂：拿掉初稿「睡龍」意象（非真實行程）；p9／封面改鐘乳石「石頭森林」；p11 改洞內短程槳板（無洞口日光）。

---

## 系列核心

真實發生過的家庭冒險，改寫成 ORT LV6 溫暖繪本。
George 是好奇又調皮的小探險家；每個故事有一位「那天的重要朋友」。
本課的重要朋友：教練 **Jojo**。

**系列名：** George's Real Adventures
**第一課（lesson-05）標題：** George's Big Cave Adventure

## 本課真實素材

- 地點：貴州興義三生洞（Sansheng Cave）；旱洞＋暗河、飛拉達、洞內茶歇、槳板
- 參考照片：`ref/IMG_00` ～ `IMG_20`（**只作畫圖參考，絕不進發佈頁面**）
- 家人：George、Daddy、Mummy、Sylvia（**Mummy 於 p2、p12 開口**；Sylvia 入畫不開口）

---

## 語音定調（GATE 1 一起簽）


| Role key   | 角色      | 引擎      | Voice               | Rate   | Pitch  | 狀態                                                                                          |
| ---------- | ------- | ------- | ------------------- | ------ | ------ | ------------------------------------------------------------------------------------------- |
| `narrator` | 旁白      | Edge    | `en-GB-SoniaNeural` | `-10%` | `+0Hz` | 沿用鎖定                                                                                        |
| `george`   | George  | MiniMax | `cute_boy` F2       | `1.30` | `0`    | 沿用鎖定                                                                                        |
| `daddy`    | Daddy   | Edge    | `en-GB-RyanNeural`  | `-5%`  | `-5Hz` | 沿用鎖定                                                                                        |
| `mummy`    | Mummy   | Edge    | `en-US-AriaNeural`  | `+5%`  | `+5Hz` | **家長定案**（試聽 B，`tmp/jojo-audition/jojo-B-aria-*`）；p2、p12 使用                                      |
| `jojo`     | 教練 Jojo | Edge    | `en-US-AvaNeural`   | `-8%`  | `+5Hz` | **家長定案**（試聽 E，`tmp/jojo-audition-round2/jojo-E-ava-*`）；GATE 1 全文簽核後寫入 `scripts/voices.json` |


---



## 畫風定調（Stage 2 鎖定）

### 整體

| 項目 | 鎖定 |
|------|------|
| 風格 | 溫暖手繪／水彩童書（同前兩篇章）；洞穴黑暗但溫暖，不恐怖 |
| 光 | 洞內頁**唯一光源＝頭燈的暖白錐形光束**；岩壁可被光帶出形狀；洞口頁／飯店頁為自然光／室內暖光 |
| 比例尺 | `lessons/assets/refs/cast/real-adventures-sheet.png`（GATE 2 簽核後為主錨） |
| 禁止 | 寫實照片臉、3D 電影風、恐怖陰影、畫面英文正文、洞內人工彩色投射燈、**龍形／動物形鐘乳石**（真實旅行篇不接 Pip 龍線） |

### Scale lock（以站立的 George 為尺，群像頁必同時成立）

**身高順序（左到右 sheet 亦同）：Daddy 最高 → Sylvia → Mummy → George 最小。** Jojo 教練約與 Mummy 同高或略高。

| 角色 | 相對身高 | 不要變成 |
|------|----------|----------|
| George | 基準（~5 歲）；全家最矮 | 另一張臉、金髮 |
| Mummy | 比 Sylvia **矮**；比 George 高很多 | 比 Sylvia 高 |
| Sylvia | **比 Mummy 高**；George 頭頂約到她**胸口** | 和 George 同高、變成大人 |
| Daddy | **全家明顯最高**；比 Mummy 高出一截；George 約到他**腰** | 彎腰縮矮、和 Mummy 一樣高 |
| Jojo | 年輕女性教練；George 頭頂約到她**胸口** | 比 Daddy 高、長相不必像真人 |

### 外形鎖（探洞裝備版，**家人以 `ref/IMG_01` 為主**）

| 角色 | 鎖定 |
|------|------|
| George | **紅頭盔**＋頭燈；**深藍 raglan 長袖**（淺灰袖）；淺灰長褲；**黃雨鞋**＋黃手套；兒童 harness（p4 起鞋褲帶泥）；臉依 `george-solo-bed-smile.jpg` |
| Daddy | **細框圓金屬眼鏡（不可漏）**；**紅頭盔**＋頭燈；**淺橄欖卡其長袖戶外衫**；深橄欖 cargo 長褲；**黑雨鞋**；harness；臉依 `george-daddy-outdoors-pavilion-neutral.jpg` |
| Mummy | 細框眼鏡；**藍頭盔**＋頭燈；**藏青短袖運動衫**（腋下淺藍拼色）；橄欖棕長褲；**粉紅雨鞋**；harness |
| Sylvia | 細框眼鏡；**黃頭盔**＋頭燈；**淺藍白波浪紋長袖**；淺灰長褲；**粉紅雨鞋**（與 Mummy 同款）；harness |
| Jojo | 教練；外形不必像真人。**橘頭盔**＋頭燈；橘 T 罩深色長袖；深色長褲；黃雨鞋；harness（`IMG_03` 僅作動作參考） |
| p11 加穿 | George＋Daddy **亮橘救生衣**；紫白槳板（`IMG_18`） |
| p12 飯店 | George 灰色 raglan 睡衣（黑袖）；白色飯店大床（`IMG_20_Hotel_Bed.jpg`） |

頭盔辨識：**George 紅／Daddy 紅／Mummy 藍／Sylvia 黃／Jojo 橘**（George 與 Daddy 同紅盔，靠身高與衣著區分）。

### Prompt 重複句（洞內頁逐頁複製）

```text
Warm hand-drawn watercolor picture-book. Dark limestone cave; the ONLY light is the warm headlamp beams from the characters' helmets — no artificial lamps, dark but cozy, never scary. HEIGHT ORDER: Daddy tallest (clearly tallest adult) > Sylvia (teen girl, taller than Mummy) > Mummy > George (smallest child). George (East Asian boy ~5, short black bangs, round face, RED helmet with headlamp, navy raglan long-sleeve with light grey sleeves, light grey trousers, YELLOW rain boots and yellow gloves, child harness, muddy from page 4 on). Daddy (East Asian man, thin round metal glasses, RED helmet, light olive-khaki long-sleeve outdoor shirt, dark olive cargo trousers, BLACK rain boots, harness, clearly the tallest). Mummy (East Asian woman, thin round glasses, BLUE helmet, navy athletic shirt with light blue side panels, olive-brown trousers, PINK rain boots, shorter than Sylvia). Sylvia (East Asian teen girl, glasses, YELLOW helmet, light blue long-sleeve with white wave pattern, light grey trousers, PINK rain boots, taller than Mummy). Coach Jojo (young woman coach, ORANGE helmet, orange T-shirt over dark long sleeves, dark trousers, yellow rain boots, harness — likeness not important). Do not resize characters independently. No photoreal faces, no on-image story text, no horror.
```

### 場景 ref 對照（出圖前 Read）

| 用途 | 檔案 |
|------|------|
| George 臉 | `lessons/assets/refs/george/george-solo-bed-smile.jpg` |
| Daddy 臉 | `lessons/assets/refs/george/george-daddy-outdoors-pavilion-neutral.jpg` |
| **家人裝備主 ref** | `ref/IMG_01_Dady_George_Mummy_Sister_BeforeEnterTheCave.jpg` |
| 全員裝備＋洞穴群像 | `ref/IMG_11_Jojo_Sylvia_George_Mummy_Daddy.jpg` |
| Jojo＋George 尺 | `ref/IMG_03_George_And_Trainer_Jojo.jpg` |
| 洞內槳板（p11） | `ref/IMG_16`～`IMG_18`（全程在洞內，無洞口） |
| 各分鏡頁 | 見各頁 Refs 欄 |

---

## 故事主軸（12 頁）

調皮 George（跳泥坑兩次得逞）→ 飛拉達差點滑倒被 Jojo 拉住（緊張頂點）→
糖果約定學會當 careful explorer → 鐘乳石大廳、茶歇雙獎勵、槳板 → 飯店床上宣布要娶 Jojo。

## 空間區（Zone）


| Zone         | 頁    | 必須                    | 禁止            |
| ------------ | ---- | --------------------- | ------------- |
| CaveEntrance | p1–2 | 樹林裡的洞口、白日光、全員頭盔＋頭燈＋黃雨鞋 | 洞內景           |
| MudPassage   | p3–5 | 全黑背景＋頭燈光束、濕泥地反光、泥坑／水坑 | 人工燈光、平整地面     |
| RiverWall    | p6–8 | 岩壁鋼纜＋扶手＋安全鎖、下方暗河水面    | 樓梯、護欄步道       |
| CrystalHall  | p9   | 大量鐘乳石、頭燈光束向上；**不要**畫成龍或動物輪廓  | 彩色人工投射燈、龍形／動物形鐘乳石 |
| TeaBreak     | p10  | 綠色小摺椅＋小桌點心、洞內昏暗只有頭燈   | 餐廳裝潢          |
| DarkRiver    | p11  | 全程在洞內短程槳板：墨綠暗河、槳板、**亮橘救生衣**、頭燈光；岩壁包圍 | 洞口日光、藍天綠葉、龍形鐘乳石、白天湖面、沒有救生衣 |
| HotelRoom    | p12  | 飯店床上、夜間暖光、George 躺被窩、**全家四口都在房裡**；床與房間依 `ref/IMG_20_Hotel_Bed.jpg` | 洞穴內景、Jojo 在房內 |


**全課連續性鎖：**
- 黃雨鞋 p1 穿上；**p4 起**鞋與褲腳永遠帶泥（p5–p11 每頁可見）
- 頭盔＋頭燈 p1 穿上、出洞前不脫；安全帶／harness p1 穿上（飛拉達前已在身上）
- **牽手交接：** p1 Daddy 牽 George → p2 Jojo 接過手 → p3 Jojo 牽著走 → p4 George 掙開手跳泥坑 → p5 Jojo 再牽緊，George 把她拉到水坑**邊上**（Jojo 人不落水）
- 安全繩 p6 扣上鋼纜；p7 繩子拉住＋Jojo 扶穩（不是只靠徒手）
- 糖果 p8 出現在 Jojo 手心 → p10 才交給 George
- p11 槳板必見救生衣；**畫面全程在洞內**（划完還要再走才出洞；旁白「走出陽光」是時間跳躍，圖上不畫洞口）

---

## 封面（Cover）

**敘事功能：** 課名視覺錨：George 與 Jojo 在洞內抬頭看鐘乳石奇觀。
**圖上必見證據：** George（紅盔）＋ Jojo（橘盔）；滿頂細長鐘乳石像石頭森林；頭燈暖光向上。
**禁止：** 龍形／動物形鐘乳石、洞口日光、藍天綠葉、圖上英文正文。
**Refs:** `story-09` 風格鎖、`real-adventures-sheet.png`

---



## 分鏡（每頁：敘事功能／圖上必見證據／對白）



### Page 1 — Gear up（CaveEntrance）

**敘事功能：** 開場定地點；George 其實有點怕，要爸爸牽手。鉤子：黑黑的洞口在等我們。
**圖上必見證據：** 全家四人＋裝備區；頭盔（George **紅**、Daddy **紅**、Mummy **藍**、Sylvia **黃**）＋亮著的頭燈＋**George 黃雨鞋**＋藍色安全帶；George 牽著 Daddy 的手；衣著依 `IMG_01`。
**Refs:** `IMG_01`, `IMG_00`


| Role     | Line                                                                    | Emotion |
| -------- | ----------------------------------------------------------------------- | ------- |
| narrator | One summer day, George and his family came to Sansheng Cave.            | calm    |
| narrator | Everyone put on a helmet, a bright little headlamp and yellow rain boots. | calm    |
| daddy    | "Look at the dark cave mouth, George. Are you ready?"                   | soft    |
| george   | "I'm scared. Hold my hand, Daddy!"                                      | worried |




### Page 2 — Same name!（CaveEntrance）

**敘事功能：** 名字梗：Mummy 喊「Jojo」叫 George 小心，教練 Jojo 誤以為在叫她；Mummy 解釋暱稱；之後教練 Jojo 一路照顧 George。
**圖上必見證據：** Mummy 大聲朝 George 喊話（擔心、揮手）；George 在洞口濕滑處、仍穿黃雨鞋；教練 Jojo（橘盔橘衣）轉頭驚訝；Mummy 轉向 Jojo 解釋；**本頁結尾 Jojo 接過 George 的手**（Daddy 放開）。
**Refs:** `IMG_03`


| Role     | Line                                                                 | Emotion   |
| -------- | -------------------------------------------------------------------- | --------- |
| mummy    | "Jojo! Look out! Be careful!"                                        | worried   |
| jojo     | "Oh! I thought you were calling me!"                                 | surprised |
| mummy    | "Our son is George. Sometimes we call him Jo or Jojo."               | calm      |
| narrator | Then Coach Jojo took George's hand and looked after him.             | calm      |




### Page 3 — Into the dark（MudPassage）

**敘事功能：** 進洞；Jojo 姊姊牽著 George 帶路（承接 p2）。建立黑暗＋濕滑的世界規則（只有頭燈）。
**圖上必見證據：** 全黑中幾道頭燈光束；**Jojo 牽 George 走在最前**；地面濕泥反光；家人剪影在後。
**Refs:** `IMG_02`, `IMG_04`


| Role     | Line                                                          | Emotion |
| -------- | ------------------------------------------------------------- | ------- |
| narrator | Inside, the cave was dark, wet and very slippery.             | calm    |
| narrator | Only their headlamps made little roads of light on the rocks. | wonder  |
| jojo     | "Hold my hand, George. The mud is very slippery here."        | calm    |
| george   | "Squish, squish! The mud is singing under my boots!"          | happy   |




### Page 4 — Muddy puddle!（MudPassage）

**敘事功能：** 調皮事件 #1：跳泥坑得逞。
**圖上必見證據：** George **掙開 Jojo 的手**跳進泥坑、泥花四濺；Jojo 伸手來不及；雨鞋褲腳沾泥（此後每頁保留）。
**Refs:** `IMG_05`


| Role     | Line                                                  | Emotion   |
| -------- | ----------------------------------------------------- | --------- |
| narrator | Then George saw a big brown puddle of mud.            | calm      |
| george   | "A muddy puddle! I love muddy puddles!"               | excited   |
| narrator | SPLASH! He jumped in before Jojo could pull him back. | surprised |
| jojo     | "Oh no, George! You are a naughty boy!"               | worried   |




### Page 5 — Quick little frog（MudPassage）

**敘事功能：** 調皮事件 #2 升級：牽更緊仍得逞，反拉 Jojo 跳水坑；鋪墊 p7 的危險。
**圖上必見證據：** George 拉著 Jojo 的手衝向亮亮的水坑並跳進去；**Jojo 停在坑邊、沒有落水**（被拉近一步但仍站穩）。
**Refs:** `IMG_06`


| Role     | Line                                                                    | Emotion   |
| -------- | ----------------------------------------------------------------------- | --------- |
| narrator | Jojo held George's hand tight, but George was quick.                    | calm      |
| narrator | He tugged her to the puddle's edge and jumped again!                    | surprised |
| george   | "Ha ha! Muddy puddle. I wanna play!"                                | excited   |
| jojo     | "You are faster than a little frog! Slow down, the rocks are slippery!" | worried   |




### Page 6 — The rock wall（RiverWall）

**敘事功能：** 場景轉折：暗河擋路 → 開始飛拉達；建立安全規則。
**圖上必見證據：** Jojo 幫 George 把**安全繩的掛鉤扣上鋼纜**（特寫，對白與畫面同物件）；下方暗河水面；岩壁扶手腳踏。
**Refs:** `IMG_04`, `IMG_07`


| Role     | Line                                                               | Emotion |
| -------- | ------------------------------------------------------------------ | ------- |
| narrator | Soon a dark river blocked the path in the cave.                    | calm    |
| narrator | Now they had to climb along the rock wall, like real explorers.    | wonder  |
| jojo     | "Click! Your safety rope is clipped on. Stay close to me."         | calm    |
| george   | "I am a cave explorer!"                                            | proud   |




### Page 7 — The slip!（RiverWall）— 轉折頂點

**敘事功能：** 調皮的後果：爬太快滑倒；安全繩拉住、Jojo 扶穩。George 又一次心裡一跳。
**圖上必見證據：** George 一腳滑離腳踏、身體微傾；**安全繩繃緊把他留在岩壁上**；Jojo 一手扶他背後安全帶。**畫面不可像懸在深淵上**：腳踏點就在腳下、Jojo 緊靠身旁，刺激但安全。
**Refs:** `IMG_07_2`, `IMG_07_3`


| Role     | Line                                                                        | Emotion   |
| -------- | --------------------------------------------------------------------------- | --------- |
| narrator | George climbed faster and faster on the wet rock.                           | worried   |
| narrator | Then his boot slipped — "Whoa!" — but the rope held, and Jojo held his harness. | surprised |
| jojo     | "I've got you, George. Slow steps, one at a time."                          | calm      |
| george   | "My heart went bump! Thank you, Jojo."                                      | worried   |




### Page 8 — The candy deal（RiverWall 寬岩台）

**敘事功能：** 行為轉折：糖果約定，George 學會小心走。
**圖上必見證據：** Jojo 蹲下、手心一顆糖果；George 認真點頭；兩人頭燈互相照亮對方的臉。
**Refs:** `IMG_10`


| Role     | Line                                                            | Emotion |
| -------- | --------------------------------------------------------------- | ------- |
| narrator | On a wide rock ledge, Jojo took a little candy from her pocket. | calm    |
| jojo     | "Walk like a careful cave explorer, and this candy is yours."   | happy   |
| george   | "I promise! Careful steps, like a cave explorer."               | calm    |
| narrator | After that, George walked slowly and watched every step.        | calm    |




### Page 9 — The stone forest（CrystalHall）

**敘事功能：** 獎勵感官頁：鐘乳石奇觀；驗證他守約定。不接幻想龍線。
**圖上必見證據：** 滿頂鐘乳石、頭燈光束向上；鐘乳石就是細長石柱／石林，**不要**畫成龍、恐龍或任何動物；George 小步慢走。
**Refs:** `IMG_13`, `IMG_14`


| Role     | Line                                                        | Emotion |
| -------- | ----------------------------------------------------------- | ------- |
| narrator | Their lamps lit up a huge hall of strange, beautiful rocks. | wonder  |
| narrator | Stalactites hung from the roof like a stone forest.         | wonder  |
| george   | "Look! So many long rocks hang from the roof!"              | wonder  |
| jojo     | "Good eyes, George! And you are walking so carefully now."  | proud   |




### Page 10 — Two treats（TeaBreak）

**敘事功能：** 雙獎勵：兌現糖果＋自選巧克力；輕鬆回落。
**圖上必見證據：** 綠色小摺椅＋小桌點心；Jojo 遞糖給 George；George 另一手拿巧克力；鼻頭一點泥。
**Refs:** `IMG_15`


| Role     | Line                                                              | Emotion |
| -------- | ----------------------------------------------------------------- | ------- |
| narrator | They sat down on little chairs for a snack, deep inside the cave. | calm    |
| jojo     | "Here is your candy, my careful explorer."                        | soft    |
| george   | "And I choose chocolate too! Two treats in one day!"              | excited |
| narrator | George ate happily, with a little mud still on his nose.          | happy   |




### Page 11 — On the dark river（DarkRiver）

**敘事功能：** 洞內短程槳板體驗（划完還要再走一段才出洞）；鉤子：飯店床上還有一句話要說。
**圖上必見證據：** George 與 Daddy 同一塊槳板；**兩人都穿亮橘救生衣**（頭盔仍在）；墨綠鏡面水映出頭燈光；**四周都是岩壁，沒有洞口、沒有日光、沒有龍形石**。
**Refs:** `IMG_16`, `IMG_17`, `IMG_18`


| Role     | Line                                                        | Emotion |
| -------- | ----------------------------------------------------------- | ------- |
| narrator | Last of all, it was time to paddle on the dark green river. | calm    |
| narrator | George sat on a big board in a bright life vest.            | wonder  |
| george   | "Bye-bye, cave! Bye-bye, stone forest!"                     | happy   |
| narrator | Then the family walked out into the warm, bright sunshine.  | calm    |




### Page 12 — George's big news（HotelRoom）

**敘事功能：** 溫暖收尾＋笑點：Mummy 問喜不喜歡探洞、喜不喜歡 Jojo；George 宣布要娶她。
**圖上必見證據：** 飯店房間夜間暖光；George 躺在被窩裡；Mummy 坐在床邊俯身問話；**Daddy 與 Sylvia 也在房裡**（所以旁白的 Everyone 成立）；床邊可見探洞頭盔。Jojo 不在房內。
**Refs:** `ref/IMG_20_Hotel_Bed.jpg`


| Role     | Line                                                                 | Emotion |
| -------- | -------------------------------------------------------------------- | ------- |
| narrator | Back at the hotel that night, George was tucked up in bed.           | calm    |
| mummy    | "Did you like the cave, George? Do you like Jojo?"                   | soft    |
| george   | "Yes! I love Jojo! I want to marry her!"                             | happy   |
| narrator | Everyone laughed out loud, and George dreamed of the cave all night. | happy   |


---



## Vocab（8 個，story words＋slight step up）


| Word       | Example（取自課文或貼近課文）                                | 圖   |
| ---------- | ------------------------------------------------- | --- |
| cave       | Inside, the cave was dark, wet and very slippery. | p3  |
| helmet     | Everyone put on a helmet, a bright little headlamp and yellow rain boots. | p1  |
| slippery   | The mud is very slippery here.                    | p3  |
| puddle     | Then George saw a big brown puddle of mud.        | p4  |
| rope       | Click! Your safety rope is clipped on.            | p6  |
| harness    | The rope held, and Jojo held his harness.         | p7  |
| stalactite | Stalactites hung from the roof like a stone forest. | p9 |
| paddle     | It was time to paddle on the dark green river.    | p11 |


短語練習（sight words 區）："Hold my hand." / "I've got you." / "One step at a time."

## 家教提示（tutor prompts）

- 問：教練 Jojo 為什麼回頭？（Mummy 喊 George 的暱稱 Jojo，教練以為在叫她）
- 問：George 在岩壁上發生什麼事？（爬太快滑倒，安全繩拉住、Jojo 抓住 harness）
- 問：Jojo 的糖果約定是什麼？（像 careful cave explorer 一樣小心走就給糖）
- 問：洞頂掛著什麼？（鐘乳石，像石頭森林）
- 問：回飯店後 George 宣布什麼？（他愛 Jojo，長大要娶她）

## Quiz 草案（10 題，全部只靠故事可答）

1. Where did George's family go? — **A. Sansheng Cave** / B. the beach / C. the zoo
2. Why did Coach Jojo turn around? — **A. Mummy called "Jojo" and the coach thought she meant her** / B. She heard a noise in the cave / C. George waved at her
3. What was the cave like inside? — **A. Dark, wet and slippery** / B. Bright and dry / C. Full of pretty lamps
4. What did George jump into first? — **A. A big muddy puddle** / B. The dark river / C. A deep hole
5. What happened on the wet rock wall? — **A. George's boot slipped, but the rope held** / B. George fell into the water / C. George lost his headlamp
6. What was Jojo's candy deal? — **A. Walk carefully and the candy is yours** / B. Sing a song for the candy / C. Jump into one more puddle
7. What hung from the roof like a stone forest? — **A. Stalactites** / B. Pretty lamps / C. Yellow boots
8. What snack did George choose at the tea break? — **A. Chocolate** / B. Ice cream / C. An apple
9. What did they do on the dark green river? — **A. Paddled on a board** / B. Swam across / C. Caught a fish
10. What did George say about Jojo at the hotel? — **A. He loves Jojo and wants to marry her** / B. He never wants to see caves again / C. He lost his yellow boots

---



## Stage 1 自查（pipeline 檢查表）

- [x] 因果順序：p1 害怕牽爸爸 → p2 名字梗 Jojo 接手 → p4 跳泥坑 → p5 再得逞 → p6–p7 飛拉達滑倒 → p8 糖果約定 → p9–p11 乖乖走完 → p12 飯店床上收尾
- [x] 誰知道什麼：p2 教練聽見 Mummy 喊「Jojo」而轉頭；p12 Mummy 問當日經歷
- [x] 道具連續：黃雨鞋 p1、泥 p4 起；牽手交接已封閉；安全繩 p6 扣上、p7 繩子拉住；糖果 p8→p10；p11 救生衣；p12 全家四口對齊 Everyone
- [x] 句長：旁白維持 ORT LV6；小孩短句（I'm scared / Ha ha / Bye-bye）為家長鎖定的童語，不硬湊字數
- [x] 每句有 emotion，且僅使用音檔管線支援的標籤
- [x] **GATE 1 家長簽核**（2026-08-26）：p1/p2/p4/p5/p12 對白依家長定稿；Jojo=Ava、Mummy=Aria
- [x] 簽核後 fresh-context 再審（GPT-5.6 Sol）：阻擋項已修（牽手、p7 繩子、p11 救生衣、p12 Everyone、p5 不落水）；**未改**家長鎖定句：p4 *naughty boy*、p5 *I wanna play*、p12 *Everyone laughed out loud*
- [x] **交付後修訂**（2026-08-26）：初稿「睡龍」非真實素材 → p9 改石頭森林、封面重畫、p11 改洞內槳板（對照 `IMG_16`～`IMG_18`，禁止洞口日光）；quiz 7 改 stalactites；GATE 3 複驗 PASS

## 修訂紀錄

| 日期 | 變更 | 影響 |
|------|------|------|
| 2026-08-26 | 拿掉 sleeping dragon（初稿誤植，非家長口述行程） | 文 p9/p11、quiz 7、Notes；圖 cover／p9；音 p09-03、p11-03、quiz-07 |
| 2026-08-26 | p11 背景改洞內短程槳板 | 圖 story-11；分鏡 Zone DarkRiver 禁止洞口日光 |