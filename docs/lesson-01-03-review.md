# Lesson 1–3 家長回饋（2026-08-21）

教學理由（詞彙半級、逐句 emotion、篇章不分三張平鋪卡、quiz 抽 5 題）。player／bible／抽題已依此實作；改 L1–3 或新課時仍以此為準。

三課是同一條故事線，主頁應收成**一個篇章**，不要三張平鋪卡片。

| Lesson | 標題 | 在篇章裡的角色 |
|--------|------|----------------|
| 1 | George and the Little Dragon | 認識 Pip、發現紅蛋 |
| 2 | The Red Egg Hatches | Ember 出生、第一次飛 |
| 3 | George and the Storm on the Hill | 採莓、暴風雨、熊、Daddy 上山 |

建議篇章名（暫定，實作時可再定）：**Pip and Ember** 或 **The Hill and the Cave**。

---

## 現況對照

| 項目 | 現況 | 家長判斷 |
|------|------|----------|
| 單字 | L1: 8 個（dragon, cave, hill, egg…）；L2: 8 個；L3: 10 個。聽讀都偏短、偏具體 | 聽對 George 太容易，缺一點挑戰 |
| 語音 | 每角色固定 Edge TTS `voice` / `rate` / `pitch`；整課同一語調 | 音色語速語調常與情節不合，童書情緒不夠 |
| 插畫 | 有真人參考（George / Daddy）；**沒有** Pip / Ember / 場景聖經；每頁獨立出圖 | 人物臉與服裝漂移；Pip、Ember 忽大忽小 |
| Quiz | 每課 4 題，進入後全做完 | 題庫可以多；**每次只抽 5 題**。孩子很享受作答 |

---

## 1. 單字：稍微加強，不要大跳級

- 目標仍是 ORT Level / Stage 6，**不要**突然跳到遠高於 LV6。
- 聽力已強：單字預覽不要只停在 `hill` / `egg` / `friend` 這種一聽就會的詞。
- 每課仍約 8–12 個新詞，但應混入：
  - 1–3 個**故事裡真正要學**的詞（例：shelter, thunder, hatch, brave）
  - 1–2 個**短語／搭配**（例：stay close, wait quietly），不只單詞
  - 例句要比單字本身難半級（完整句、一點對話感）
- 舊篇章若重做單字：保留故事核心詞，替換最容易的 2–3 個。

---

## 2. 語音：先鎖角色，再鎖「這一句的情緒」

現在的問題不是「誰在說話」，而是「這句該用什麼情緒說」。童書需要誇張一點：驚喜、擔心、小聲、開心、勇敢。

| 限制 | 說明 |
|------|------|
| Edge TTS | 角色音色仍以 `scripts/voices.json` 為準；**沒有**可用的逐句 `express-as` / 自訂 SSML |
| MiniMax Speech 2.8 | 已有試聽腳本 `scripts/sample_minimax_speech.py`（emotion + speed）。尚未成為正式課語音 |

**之後每句對白要帶情緒標籤**（寫在 story JSON，例如 `emotion`），產生音檔時必須對上情節：

| 標籤 | 用在 |
|------|------|
| `wonder` / `surprised` | 發現蛋、第一次看見龍 |
| `worried` / `fearful` | 暴風雨、熊、走散 |
| `soft` / `whisper` | 「Keep quiet」「Stay close」 |
| `happy` / `proud` | 成為朋友、Ember 飛起來、Daddy 找到他們 |
| `calm` | 旁白說明、收尾 |

實作順序（尚未做）：story JSON 加 `emotion` → 試 MiniMax 或「固定角色 + 逐句微調 rate/volume」→ 家長聽過再批次重產。

---

## 3. 插畫：故事開畫前先定調（角色 + 場景）

這是三課裡最需要改流程的一項。George 有照片參考；Pip / Ember / 山丘洞穴**沒有**鎖定稿，所以每頁獨立出圖就會跑樣、跑比例。

### 之後強制流程（bible-first）

1. 寫／更新 [`docs/cast-bible.md`](cast-bible.md)（角色、體型比例、服裝、場景錨點）
2. 產出或沿用 **character sheet**（正視＋側視＋表情；龍要標相對 George 的身高）
3. 再寫逐頁分鏡與提示詞；**每一頁都重複聖經裡的不可變項**
4. 出圖後對照聖經 QA；跑樣就重出該頁，不要「將就用」

專案 skill：`.cursor/skills/picture-book-consistency/SKILL.md`  
出圖或新開故事時先讀它。

### 網上可用的做法／skills（2026-08 查過）

| 來源 | 用途 | 本專案怎麼用 |
|------|------|----------------|
| [weaiw/storybook-generator-skill](https://github.com/weaiw/storybook-generator-skill) | 先寫角色／風格聖經、再逐頁 prompt、最後 QA | **最接近**。已把核心收進本專案 skill，不整包複製（它偏中文繪本／KDP） |
| [tuzi-comic character-template](https://github.com/tuziapi/tuzi-skills/blob/main/skills/tuzi-comic/references/character-template.md) | 角色定義＋reference sheet 提示詞模板 | 做 Pip／Ember sheet 時當欄位清單 |
| [baoyu-comic character-template](https://github.com/NousResearch/hermes-agent/blob/HEAD/optional-skills/creative/baoyu-comic/references/character-template.md) | 同上（漫畫向） | 同上 |
| [StoryState](https://github.com/YuZhenyuLindy/StoryState)（論文／程式） | 用結構化 story state 管角色與場景 | 研究向；我們用 markdown 聖經即可 |
| BookAgent（多 agent 繪本） | 規劃→出圖→全本一致性檢查 | 流程概念可參考；不必上整套框架 |

**不要**依賴「同一個小龍」這種短提示。要鎖定：體色、角、肚皮、翅膀、**相對身高**、固定服裝。

### 已觀察到的漂移（當作反面教材）

- **Pip 體型**：L1 見面約到 George 腰／胸；L2 孵蛋時頭幾乎和 George 一樣大；L3 又變小。
- **Pip 長相**：角、眼睛顏色、背刺、翅膀大小頁與頁不同。
- **George 服裝**：封面有時是藍灰插肩衣，故事頁常是藍連帽外套；沒有「出門預設服裝」。
- **場景**：綠山、河、洞穴入口每課都重畫，石頭形狀與洞口方向不固定。

鎖定稿與「以哪一頁為準」見 [`docs/cast-bible.md`](cast-bible.md)。

---

## 4. Quiz：題庫加厚，每次只抽 5 題

- 孩子喜歡即時對錯與語音 A/B/C，**保留這個節奏**。
- 每課題庫目標：**至少 8–12 題**（理解、細節、詞義、一句話推理）。
- 每次進入 Quiz：**隨機抽 5 題**（不足 5 題就全出）。
- 同一瀏覽器再開一次可以換題；不必記住上次抽過哪些（先做簡單隨機即可）。
- 抽中的題仍走現有流程：先 Read（題幹＋A/B/C），選項在讀完前停用。

播放器尚未實作抽題；現在是題庫有幾題就做幾題（目前每課 4 題）。

---

## 建議實作順序（尚未開始）

1. 定稿 [`docs/cast-bible.md`](cast-bible.md)，必要時補 Pip／Ember character sheet 圖  
2. 主頁把 L1–L3 收成一個篇章  
3. 播放器：題庫抽 5 題  
4. story JSON 加 `emotion`，試聽後再決定是否換引擎  
5. 新課（或重畫舊課）一律 bible-first；單字略為加難  

## Lesson 3 試作（2026-08-21）

已試做，尚未發佈：

- 先出角色表 `lessons/assets/refs/cast/pip-ember-sheet.png`，再重畫封面與 Story 1–8
- George 對白改 MiniMax `cute_boy` F2，並依情節加 `emotion`
- Quiz 題庫 10 題，每次隨機 5 題（`quizPick: 5`）

仍待家長看：龍比例是否夠穩、George 臉是否夠像、MiniMax 情緒是否夠童書。
