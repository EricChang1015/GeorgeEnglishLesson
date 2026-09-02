---
name: picture-book-consistency
description: Locks character look, scale, scene anchors, and page-to-page continuity before generating lesson illustrations. Use when creating or redrawing lesson art, covers, vocab pictures, character sheets, page prompts, or when the user mentions Pip, Ember, Mike, Nibble, visual drift, 忽大忽小, 角色一致性, or 畫面連貫.
---

# Picture-book consistency

Do not generate lesson art from a one-line story beat. Lock the cast and places first.
整課流程與閘門見 `.cursor/skills/lesson-production-pipeline/SKILL.md` — **分鏡未經家長簽核（GATE 1）前不出課文插圖**。

## Read first

1. `docs/cast-bible.md` — 全專案角色鎖；篇章 bible（如 `docs/big-eye-chapter.md`）— 該章比例、服裝、場景、Zone
2. `lessons/assets/refs/george/CATALOG.md` and `lessons/assets/refs/sylvia/CATALOG.md` — then **Read** the photos named in the bible
3. `.cursor/rules/character-refs.mdc` — family photo rules

If the bible is missing a new character or place, **update the bible and get a sheet** before page images.

## Workflow

```
[ ] Bible fields filled（who / scale / clothes / cannot-change / 禁止項）
[ ] Character sheet exists（全員同框比例尺；new scale → sheet 先給家長看）
[ ] Zone 表：每頁屬於哪個空間區；區內必見錨點、禁止元素
[ ] 分鏡的「圖上必見證據」逐頁抄進 prompt（腳印方向、誰牽誰、道具位置）
[ ] Page plan: one action or feeling per page
[ ] Each page prompt = bible 重複句 + 該頁證據 + Zone 錨點
[ ] Generate one page → QA（下表）→ 過了才下一頁；封面最後畫
```

## Prompt rules

- Repeat locked traits every page. Never write only "the same dragon" / "the same plush".
- 比例永遠寫絕對錨（相對 George 的身體部位）：Pip = waist-to-chest、Ember = knee-high、Mike = knee-high、Nibble = mid-shin、光鳥燈 = fist-sized。
- 同一 Zone 的頁共用同一組錨點描述（同一張床、同一個丘、同一片窗簾林），prompt 原句複製，不要每頁重新措辭。
- One main action per page. Do not stack three props in six hands.
- No on-image story text. No photoreal faces. No style hop mid-lesson. No horror（發光眼、恐怖陰影）。

## Per-page QA（出一張檢一張，任一項破鎖 → 重出該頁，不將就）

執行紀律（沒做到 = 沒 QA）：

1. **必須用 Read 真的打開生成的圖檔**再判定，不准憑 prompt 內容或縮圖印象打分。
2. 每頁**逐項寫下 PASS / FAIL ＋ 一句證據**（例：「腳印朝畫面右、與 p6 文字一致 → PASS」）。只說「看起來沒問題」視同未檢查。
3. 自己畫的圖自己容易看順眼——出圖後必須用**另一個 model** 的 fresh subagent 審圖文契約（`.cursor/rules/checkpoint-review.mdc` CP3／CP4）。**新檔未通過 A/B（比舊檔更好且無新硬傷）不准覆寫課件目錄。**

| 檢查 | 內容 |
|------|------|
| 臉與服裝 | George 像 ref、睡衣／外套 = bible 固定款 |
| 解剖 | 手腳數量正確（Mike 三隻腳的教訓）、無尖爪 |
| 比例 | 對 sheet：誰到誰的哪裡 |
| Zone | 錨點在、禁止元素不在（窗戶、星燈、pillow cave 的教訓） |
| 圖文契約 | 分鏡「必見證據」都看得到；**方向**與文字一致（腳印朝向的教訓） |
| 相鄰連續 | 和前一頁同 Zone 時，擺設／光源／天氣不跳動 |

## Story changes after art exists

改文動到畫面節拍 → **預設重畫受影響頁**，不准「保舊圖」讓文字與畫面脫節（Lesson 4 最貴的錯誤）。單頁修圖也要先重讀 bible，不要只看上一張圖腦補。

## New chapter

新篇章開畫前：先在篇章 doc 補齊角色、Zone、禁止項；bible 一旦更新，**同 commit** 作廢舊設定，不留兩套說法（綠光／pillow cave 誤導出圖的教訓）。

## Upstream patterns (do not vendor whole repos)

- [storybook-generator-skill](https://github.com/weaiw/storybook-generator-skill) — bible → page prompts → QA
- [kart-io/picture-skills](https://github.com/kart-io/picture-skills) — CCLP 4.0：每頁 prompt 帶 2–3 個 signature 特徵 + Page 1 LOCK / 後頁 REFERENCE 聲明
- [tuzi-comic character-template](https://github.com/tuziapi/tuzi-skills/blob/main/skills/tuzi-comic/references/character-template.md) — sheet fields
- [danjdewhurst/story-skills](https://github.com/danjdewhurst/story-skills) — story bible 連續性／狀態檢查
