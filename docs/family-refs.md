# Family likeness refs — 選圖地圖

**為什麼有這批素材：** Lesson 7 出圖時 George 像本人，但 Daddy／Mummy／Sylvia 不像。原因是家人幾乎只靠一張萬聖節合照（`george-mummy-daddy-sylvia-halloween-trex-play.jpg`）當臉，合照臉小、服裝是派對衣，模型容易發明另一張成人／少女臉。

之後凡畫家人：**必須先 Read 各角色 solo `priority: primary` 臉**，合照只當「誰在哪／身高／姿勢」，不當唯一臉。

不要把真人照片嵌進課文 HTML。只畫繪本插圖到 `lessons/assets/lesson-XX/`。

## 資料夾

| 誰 | 路徑 | 目錄 |
|----|------|------|
| George + **合照** | `lessons/assets/refs/george/` | `CATALOG.md` |
| Sylvia 獨照 | `lessons/assets/refs/sylvia/` | `CATALOG.md` |
| Mummy 獨照 | `lessons/assets/refs/mummy/` | `CATALOG.md` |
| Daddy 獨照 | `lessons/assets/refs/daddy/` | `CATALOG.md` |

規則：`.cursor/rules/character-refs.mdc`

## 預設臉（出圖先 Read 這張）

| 角色 | 檔案 | 鎖定特徵 |
|------|------|----------|
| George | `george/george-solo-bed-smile.jpg` | 短黑瀏海、圓臉、門牙笑 |
| Sylvia | `sylvia/sylvia-solo-outdoors-graduation-smile.jpg` | 長黑髮側瀏海、**黑方框眼鏡**、溫和微笑；比 Mummy 高 |
| Mummy | `mummy/mummy-solo-indoor-smile.png` | 長深色髮＋空氣瀏海、**細圓金屬眼鏡**、溫暖露齒笑；比 Sylvia 矮 |
| Daddy | `daddy/daddy-solo-indoor-vehicle-neutral.png` | 短黑髮頭頂略蓬、**細圓金屬眼鏡**、**左下顎小痣**；全家最高 |

與 George 同框的 Daddy 臉仍可用：`george/george-daddy-outdoors-pavilion-neutral.jpg`

## 全家同框（比例／站位）

身高：**Daddy > Sylvia > Mummy > George**

優先用沙發合照看四人相對位置：

`george/george-daddy-mummy-sylvia-indoor-sofa-selfie-smile.png`

其他 `george-daddy-mummy-sylvia-*` 見 `george/CATALOG.md` → Family group — full cast。

**萬聖節合照**只鎖 Lesson 7「T-rex＋家人同框」姿勢與居家比例，**不要當 Sylvia／Mummy／Daddy 的主臉**。

## 命名

```
{subjects}-{setting}-{pose-or-mood}[-variant].jpg
```

- 獨照：`sylvia-solo-...`、`mummy-solo-...`、`daddy-solo-...`
- 有 George：放 `refs/george/`，George 寫在檔名最前
- 全家四人：`george-daddy-mummy-sylvia-...`

## Lesson 7 必讀（家人頁）

服裝跟 `docs/lesson-07-proposals/bible-locked.md`：**居家睡衣、不穿鞋**（不是洞穴裝備、不是外出便服）。全身鎖：`lessons/assets/refs/cast/wild-things-family-sheet.png`。

| 頁 | 誰在場 | 必 Read 臉 | 腳 |
|----|--------|------------|----|
| p1 | George、Sylvia | Sylvia graduation smile | 室內：George **赤腳或襪子** |
| p2 | George、Mummy、Sylvia | Mummy indoor smile + Sylvia graduation | 同上 |
| p3–p5 | 僅 George | George bed-smile + T-rex 正面 | **床上／室內不准運動鞋** |
| p12 | 全家四人 | 上列三張 + Daddy vehicle neutral + sofa group | 室內赤腳／襪子 |

島上／海上（p6–p11）才可深藍運動鞋。Horn 不再提 blue shoes。
