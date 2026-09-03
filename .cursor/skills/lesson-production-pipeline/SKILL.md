---
name: lesson-production-pipeline
description: Staged, gated pipeline for producing a new lesson (story, art, audio, HTML) or revising an existing one. Use when creating lesson 5+, rewriting a story, planning a new chapter, or when the user mentions 新課, 建課, 分鏡, 改劇情, rework, or 流程.
---

# Lesson production pipeline（分階段閘門）

Lesson 4 的教訓：**劇情沒簽核就出全套圖＋音，之後每次改文都連鎖重工**（61→35→39 句三次重錄、6～7 輪重繪、改文保舊圖造成圖文脫節）。本流程用「閘門」擋住這件事。

核心原則：**上游未凍結，下游不開工。** 圖與音是最貴的產物，永遠最後做。  
文件地圖：`docs/README.md`。`lessons/` 只放課件 HTML。

---

## 全流程與閘門

```
Stage 0 定調 ──► Stage 1 劇本＋分鏡 ──► GATE 1 家長簽核
                                            │
Stage 2 視覺鎖定（bible＋sheet）──► GATE 2 家長看角色表
                                            │
Stage 3 出圖（逐頁 QA）──► Stage 4 音檔 ──► Stage 5 組裝
                                            │
                     GATE 3 整課驗收（lesson-delivery-qa）──► 家長預覽 ──► 發佈
```

**一次交付原則：GATE 1 簽核後，Stage 2→5 ＋ GATE 3 一氣呵成，最後一次交付整課。**
中途只有 GATE 2（新角色／比例尺變動）需要回頭找家長；不准「圖出完先給看看」「音錄完先交卷」這種半成品交付。

## 開工素材（家長提供，Stage 0 一次收齊）

家長開新課時提供以下素材；缺哪項就在 **Stage 0 一次問完**，之後不再逐項回頭追問：

| 素材 | 說明 | 缺省時 |
|------|------|--------|
| 角色 | 出場人物／新角色名字與定位 | 沿用篇章既有 cast，不擅自加新角色 |
| 劇情大綱 | 幾句話的起承轉合，或想講的主題 | 必問，不可腦補 |
| 篇章歸屬 | 接哪個 chapter（Pip and Ember / Mike Dreams / 新篇章） | 必問 |
| 必含／禁止元素 | 一定要有的橋段、不想出現的東西 | 視為無特殊要求 |
| 詞彙方向 | 想練的字或短語（可空） | agent 依 ORT LV6 規則自選 |
| 頁數 | 故事頁數 | 預設 12 頁 |

### Stage 0 — 定調（半小時內完成，不出任何圖）

- 篇章前提、主題、與哪些舊課同篇章
- **角色名字在此定案**。改名 = JSON、HTML、voices、音檔、docs 全棧重做（Big Eye→Mike 的教訓），之後不再改
- 新角色：先查 `scripts/voices.json`；`reserved` 角色要先問家長（見 `.cursor/rules/character-voices.mdc`）

### Stage 1 — 劇本＋分鏡（只有文字，成本最低，改到滿意為止）

寫進 `docs/<chapter>.md`（格式參考 `docs/big-eye-chapter.md` 或 `docs/wild-things-storyboard.md`），每頁一張表：

| 欄位 | 內容 |
|------|------|
| Page / Zone | 頁碼＋空間區（房間／山丘／森林…） |
| 敘事功能 | 這頁推進什麼；翻頁鉤子是什麼 |
| 圖上必見證據 | 畫面必須看得到的物件與方向（腳印朝哪、誰牽誰） |
| 對白 | 完整台詞（role + line + emotion） |

交給家長前先自查（Lesson 4 全部踩過）：

- [ ] **因果順序**：逐頁講得出「因為上一頁…所以這一頁…」（p3/p4 順序反的教訓）
- [ ] **誰知道什麼**：角色不可說出他不該知道的事（「知道是夢」的教訓）
- [ ] **道具與方向連續**：腳印、燈、巢…每次出現位置與方向一致（腳印方向相反的教訓）
- [ ] **句長 ORT LV6**：每頁 3–4 句、8–16 字；不過度堆旁白也不縮成電報（61→35→39 的教訓）
- [ ] 每句有 `emotion`；驚喜／害怕／悄悄話要分得出來

**GATE 1（硬閘）：家長逐頁看過分鏡與對白、說 OK 之前，不准產生任何課文插圖或整包 TTS。** 這一輪家長改十次都便宜。

### Stage 2 — 視覺鎖定

1. 更新 `docs/cast-bible.md` 或篇章 bible：新角色外形、**相對 George 的身高**、固定服裝、場景錨點、空間區（Zone）表
2. 產出／沿用 character sheet（含比例尺，全員同框）
3. 寫好「每頁複製」的 prompt 重複句
4. 詳細規則照 `.cursor/skills/picture-book-consistency/SKILL.md` 執行

**GATE 2（軟閘）：新角色或比例尺有變時，先給家長看 sheet 再開內頁。**（Mike 從胸口高改到膝蓋高，內頁全部白畫的教訓。）

### Stage 3 — 出圖

- 逐頁出、逐頁對 bible QA（臉、服裝、比例、Zone 錨點、圖上必見證據），過了才下一頁
- 封面最後畫（等內頁風格穩定）
- PNG → `python scripts/optimize_lesson_images.py --lesson lesson-XX`

### Stage 4 — 音檔（文字凍結之後才錄）

- `python scripts/generate_lesson_audio.py --story scripts/lessonXX_story.json --out lessons/assets/lesson-XX/audio`
- 角色 voice 必須等於 `scripts/voices.json`；逐句 `emotion` 要對上分鏡表

### Stage 5 — 組裝

- 建 HTML、進 index 篇章卡；browser smoke（`.cursor/rules/delivery.mdc`）

### GATE 3 — 整課驗收（硬閘，交付前必過）

- 照 `.cursor/skills/lesson-delivery-qa/SKILL.md` 跑完四個驗收面。
- **模型輪替與放行**照 `.cursor/rules/checkpoint-review.mdc`：CP1–CP5 用不同 model；整包須三個 Cursor model 都 PASS；換檔先 A/B。
- 全部 PASS 才向家長交付，交付訊息附驗收報告
- 家長預覽 → 說「發佈」才 commit + push

---

## 改動守則（發佈後或 Stage 3 之後要改東西時）

1. **先做影響表再動手**。任何一句改文，先列出：這句的 mp3？這頁的圖？quiz 有沒有引用？篇章 doc？全列完再一次做完。
2. **改文動到畫面節拍 → 預設重畫受影響頁。** 「保留舊圖省成本」是 Lesson 4 最貴的錯誤，禁止。真要保圖，只能反向：改文遷就現有畫面。
3. **家長回饋收集成批**，一輪改完（文＋圖＋音＋doc 同一批、同一個 commit），不要一句一個 session 急救。
4. **篇章 doc 與成品同步**：改了故事就同 commit 改 `docs/<chapter>.md`，bible 永遠反映目前定稿，不留舊設定（綠光／pillow cave 誤導出圖的教訓）。
5. 單頁修圖也要**先讀 bible 的鎖定項再出圖**，不要憑上一張圖腦補。
6. **任何改動（哪怕只有一張圖、一句話）交付前都要重過 GATE 3**（`.cursor/skills/lesson-delivery-qa/SKILL.md`）——改動最容易破壞的就是「整課連貫性」，而那正是單點自查看不到的。

---

## 參考做法（不整包搬）

- [weaiw/storybook-generator-skill](https://github.com/weaiw/storybook-generator-skill) — story architecture before image generation；圖文契約
- [kart-io/picture-skills](https://github.com/kart-io/picture-skills)（CCLP 4.0）— 每頁 prompt 帶 signature 特徵＋LOCK/REFERENCE 聲明
- [danjdewhurst/story-skills](https://github.com/danjdewhurst/story-skills) — story bible 連續性檢查（角色狀態、伏筆回收）
