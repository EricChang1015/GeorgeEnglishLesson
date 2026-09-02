# Lesson 7 擴寫影響表（12 → 19 頁，Sol 定稿）

**GATE 1：** 2026-09-02 家長選定 [`plot-expand-sol.md`](plot-expand-sol.md) → 凍結為 [`plot-working.md`](plot-working.md)  
**總頁數：** 19 故事頁 + cover + vocab + quiz + phrases + notes  
**對白：** 76 句（原 48 句）

---

## 頁碼對照（舊 12 → 新 19）

| 舊頁 | 新頁 | 節拍 | 圖 |
|------|------|------|-----|
| p1 | p1 | 客廳追叉 | **改對白**；圖可沿用 story-01（睡衣版已畫） |
| p2 | p2 | Mummy 罰晚餐 | **改對白**；圖可沿用 story-02 |
| p3 | p3 | 關房孤單 | **改對白**（去掉「偏心 Sylvia」句） |
| p4 | p4 | 叢林房 | **改對白** |
| p5 | p5 | 上船 | **改對白**（木叉留床） |
| p6 | p6 | 長航 | **改對白** |
| p7 | **p7–8** | 抵岸＋三獸示威 | **拆兩頁**；舊 story-07 僅參考，需重畫 |
| p8 | **p9–11** | 對視→入島→加冕 | **拆三頁**；舊 story-08 僅參考 stare／crown 各一幀 |
| p9 | **p12–15** | parade＋王規＋再玩 | **拆四頁**；舊 story-09 僅參考一幀 parade |
| p10 | **p16** | 冠重想家 | 舊 story-10 參考；需重畫（鳥燈暖香） |
| p11 | **p17–18** | 道別＋回航 | **拆兩頁**；舊 story-11 參考 |
| p12 | **p19** | 熱晚餐 | 圖可沿用 story-12 → 更名 story-19 |

---

## 插圖（19 內頁 + cover）

| 檔名 | 狀態 | 動作 |
|------|------|------|
| story-01.webp | 已有（睡衣版 p1） | 對白改 → **保留圖**，僅重錄音 |
| story-02.webp | 已有（睡衣版 p2） | 對白改 → **保留圖**，僅重錄音 |
| story-03.webp | 已有 | 對白改 → **保留圖**，僅重錄音 |
| story-04.webp | 已有 | 對白改 → **保留圖**，僅重錄音 |
| story-05.webp | 已有 | 對白改 → **保留圖**，僅重錄音 |
| story-06.webp | 已有 | 對白改 → **保留圖**，僅重錄音 |
| story-07.webp | 已有（舊單頁抵岸） | **重畫** → Blocked Shore |
| story-08.webp | — | **新畫** Three Wild Warnings |
| story-09.webp | 已有（舊對視+冠） | **重畫** → Steady Stare only |
| story-10.webp | — | **新畫** Into the Island（藤橋） |
| story-11.webp | — | **新畫** Crown of Vines |
| story-12.webp | 已有（舊 parade） | **重畫** → Stomping Parade |
| story-13.webp | — | **新畫** Moonlit Swirls |
| story-14.webp | — | **新畫** King's Rules |
| story-15.webp | — | **新畫** King for a While |
| story-16.webp | 已有（舊 hungry） | **重畫** → Heavy Crown |
| story-17.webp | — | **新畫** A King Chooses Home |
| story-18.webp | 已有（舊 homeward） | **重畫** → Homeward Light |
| story-19.webp | 已有（舊 p12 熱晚餐） | **複製/更名** story-12 → story-19；必要時微調 |
| cover.webp | 已有 | 可暫留；全課齊後可選更新 |

**小計：** 保留圖 6（p1–6）｜更名/複製 1（p19）｜重畫 7｜新畫 5 ｜cover 待定

---

## 音檔

| 類別 | 舊 | 新 | 動作 |
|------|----|----|------|
| 故事句 | p01-01 … p12-04（48） | p01-01 … p19-04（76） | **整包重錄**（`generate_lesson_audio.py`） |
| 詞彙 | 8 詞 × 2 | 8 詞 × 2（新增 `rule`，移除 `lonely` 卡） | 重錄 `vocab-rule*`；其餘例句更新 |
| title | 1 | 1 | 可保留 |
| quiz / phrases | — | 引用新 pXX | 隨故事音一併 |

---

## Player / HTML

| 檔案 | 動作 |
|------|------|
| `scripts/lesson07_story.json` | ✅ 已更新 19 頁 |
| `lessons/lesson-07.html` | ✅ `build_lesson07_html.py` 重建（19 story screens） |
| `lessons/js/lesson-player.js` | 無需改（動態頁數） |
| `index.html` | 確認 L7 連結仍有效 |

---

## Quiz / 教學

| 項目 | 動作 |
|------|------|
| quiz 10 題 | ✅ 已更新（加「第一條王規」「木叉留床」） |
| key phrases | ✅ 改為 Sol 句（Look into my eyes / First royal rule / I choose home） |
| tutor prompts | ✅ 已更新 summary |
| `docs/wild-things-chapter.md` | 改選案紀錄為 Sol + 19 頁 |

---

## Docs 同步（本 commit）

- [x] `plot-working.md` ← Sol 定稿 + GATE 1
- [x] `expansion-impact.md`（本檔）
- [x] `lesson07_story.json` + `lesson-07.html`
- [ ] `docs/wild-things-chapter.md` — 選案與頁數
- [ ] 出圖後：`optimize_lesson_images.py`、GATE 3 整課驗收

---

## 下一階段（Stage 2→5，GATE 1 後）

1. **不重畫 p1–6**（對白已變，先重錄音；圖文大方向仍合）
2. **優先出島段 p7–18**（12 張需新畫/重畫）
3. **p19** 由 story-12 複製為 story-19.webp 作暫用
4. 全圖齊 → 整包 TTS → CP3/CP4/CP5 → GATE 3
