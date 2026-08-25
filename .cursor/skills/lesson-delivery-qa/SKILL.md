---
name: lesson-delivery-qa
description: Whole-lesson acceptance gate (GATE 3) that must pass before reporting any lesson work as done. Use before delivering a new lesson or any change touching story text, art, audio, quiz, or player; or when the user mentions 交付, 驗收, 交卷, 完工, deliver, done, 發佈, publish, 圖文不符, 劇情不連貫, or 聲音異常.
---

# Lesson delivery QA（GATE 3 — 交付前整課驗收）

存在理由：過去每次交付都由家長人工抓出「劇情不合理／圖文不匹配／人物畫錯／聲音異常」。
這些缺陷全部可以在交付前被驗出來。**本閘門沒過，就不准說「做完了」。**

## 鐵律

1. **交付單位是整課，不是單一產物。** 就算只改了一張圖或一句話，也要把整課從封面走到 notes，確認改動沒有破壞連貫性。禁止「圖出完了」「音錄完了」就交卷。
2. **產生者不能自評。** 內容審查（故事邏輯、圖文契約）必須開 **fresh-context subagent** 執行：只給它最終成品與鎖定文件，不給它產生過程的上下文，讓它以「第一次看這課的讀者」身分挑毛病。
3. **逐項書面判定。** 每個檢查項寫 PASS / FAIL ＋ 一句證據。「看起來沒問題」＝沒有驗收。
4. **任一 FAIL → 修 → 重跑該驗收面。** 全部 PASS 才交付，交付訊息附上驗收報告。

## 四個驗收面

### A. 故事邏輯（subagent，只給文字）

開一個 subagent，**只提供**：定稿的逐頁課文（page / role / line / emotion）＋ quiz 題目。要求它逐頁回答：

- 因果：這頁為什麼接在上一頁後面？講不出來 = FAIL（p3/p4 順序反的教訓）
- 誰知道什麼：角色有沒有說出他不該知道的事（「知道是夢」的教訓）
- 道具與方向：腳印、燈、巢…每次出現位置與方向是否一致
- ORT LV6：每頁 2–4 句、句長 8–16 字、對白自然
- emotion 標籤是否符合該句情緒節拍
- quiz 每題能否只靠故事內容答出、正解無歧義

### B. 圖文契約（subagent，必須真的看圖）

開一個 subagent，給它：每頁的 webp/png 路徑、該頁課文、分鏡「圖上必見證據」、`docs/cast-bible.md` 鎖定項。要求它 **逐頁用 Read 開啟圖檔**（不准憑檔名猜），對每頁判定：

- 必見證據都在圖上，**方向**與文字一致（腳印朝向的教訓）
- George／家人像 ref、服裝 = bible 固定款；無多手多腳（Mike 三隻腳的教訓）
- 比例對 sheet（Pip waist-chest、Ember knee-high、Mike knee-high、Nibble mid-shin）
- Zone 錨點在、禁止元素不在；與相鄰同 Zone 頁的擺設／光源不跳動
- 無恐怖元素（發光眼、恐怖陰影）、無圖上故事文字

### C. 音檔（腳本 + 抽查）

```
python scripts/check_lesson_audio.py --story scripts/lessonXX_story.json --audio lessons/assets/lesson-XX/audio
```

- exit 0 才算過：驗每個 mp3 存在、非空、時長合理、voices 符合 `scripts/voices.json`
- 本次**重新生成過**的句子：在瀏覽器走查時實際點播，確認不是壞檔／錯角色（時長異常的檔案腳本會標出，必須處理）

### D. 整課瀏覽器走查（比 delivery.mdc 的 smoke 更完整）

1. `npx serve .`（或既有 server），開 `lessons/lesson-XX.html`
2. 封面 → vocab 每一張卡 → **每一頁 story**（不是只抽第 1 頁）→ quiz 完整答一輪 → sight words → notes
3. 每頁確認：正確的 `.webp` 載入、文字是定稿版本、console 零錯誤
4. 至少在 3 頁（不同角色）點播句子音檔，network 無 404
5. 若改過 player／hash／Auto read：照 `.cursor/rules/delivery.mdc` 補測

## 驗收報告格式（交付時必附）

| 驗收面 | 結果 | 證據／備註 |
|--------|------|-----------|
| A 故事邏輯 | PASS | subagent 逐頁過，無因果斷裂 |
| B 圖文契約 | PASS（p7 重畫 1 次） | p7 腳印方向修正後複驗過 |
| C 音檔 | PASS | check_lesson_audio 105/105 |
| D 走查 | PASS | 12 頁全走，console 乾淨 |

FAIL 過的項目要寫「修了什麼、複驗結果」，不是刪掉重寫成 PASS。

## 適用範圍

- 新課 Stage 5 之後、任何動到 story JSON／插圖／音檔／quiz／player 的改動之後：**必跑**
- 只動 `docs/`、rules、腳本註解等不影響成品的改動：可免，但要在交付訊息說明為何免跑
