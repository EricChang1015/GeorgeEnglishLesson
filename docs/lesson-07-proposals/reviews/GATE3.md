# Lesson 7 GATE 3 — 整課驗收

日期：2026-09-01  
課：**George and the Wild Parade**（`lessons/lesson-07.html`）

| 驗收面 | 結果 | 證據／備註 |
|--------|------|-----------|
| A 故事邏輯 | PASS | Grok 4.6 · `gate3-story-grok46.md` · 12 頁因果、道具、ORT、quiz、禁用句全過 |
| B 圖文契約 | PASS | Grok 4.5 · `gate3-art-grok45.md` · 封面＋p1–12 必見證據、頭套、Zone、三獸比例全過 |
| C 音檔 | PASS | `check_lesson_audio.py` 108/108 · voices 對齊 `voices.json`（Horn = `en-GB-ThomasNeural`，因 Noah 不存在） |
| D 走查 | PASS | Composer 2.5 · `gate3-player-composer.md`；本機 `localhost:4177` 封面／Story 1／7／12／Quiz，12 張 `.webp` 皆 200，console 無 JS error |
| 互檢 CP | PASS | 文 Grok 4.6、圖 Grok 4.5、player Composer 2.5 各自 PASS。逐頁圖另有 Grok 4.5／4.6／Composer／Luna 蓋章 |

## 瀏覽器抽查

- 封面：`cover.webp`、標題 *George and the Wild Parade*、Start／Go to／Auto read
- Story 1：`story-01.webp`、living room 對白；點播 `p01-02.mp3` → 206
- Story 7：`story-07.webp`；點播 Horn `p07-01.mp3`
- Story 12：`story-12.webp`、熱晚飯全家；點播 Mummy
- Quiz：A/B/C 未 Read 前 disabled；Read 後載入 `quiz-05*.mp3`

## 已知非阻擋

- Go to 下拉把 vocab 標成「Song words」（player 預設標籤）；頁面標題仍是 New Words
- `<title>` 為 *George's Wild Parade*，H1 為 *George and the Wild Parade*

## 逐頁四模型圖章

p1、p2b、p3b、p4、p5、p6、p7、p8、p9c、p10、p11、p12、cover 皆 Grok 4.5／Grok 4.6／Composer／Luna **OVERALL PASS**（中途 FAIL 已重畫後複審）。
