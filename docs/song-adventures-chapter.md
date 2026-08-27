# George's Song Adventures — 篇章提案 v0

新篇章：George 在熟悉的歌曲中進入歷史與想像交織的冒險；本篇不接其他幻想篇章。
狀態：2026-08-27 — **精簡版**：封面 → Song Words → 一句一圖 slideshow → Full Song（YouTube）。  
12 頁故事繪本、故事 TTS、quiz、phrases、notes **暫緩**。

---

## 系列核心

George 在夜裡唱起一首歌，歌曲把房間變成一場完整冒險。故事保留原始歌詞中的歷史背景，同時以溫暖、非暴力的方式呈現海上追逐。

**系列名／Chapter name（提案）：** George's Song Adventures  
**第一課（lesson-06）標題（提案）：** George and the Wellerman

本課定位：
- George 從唱歌進入冒險，直到 p12 醒來才知道那是一場夢。
- 故事依 public-domain sea shanty〈Wellerman〉推進，課文以 ORT Level 6 方式重述，不整段傾倒歌詞。
- 捕鯨只作歷史背景：無血、無傷口、無死亡；鯨魚始終沒有被捉到。
- 精簡版 PLAYER：**先學歌詞難詞，再一句一圖跟唱，最後聽完整首歌**。故事頁暫不進 player。

---

## 語音定調（GATE 1 一起簽）

| Role key | 角色 | 引擎 | Voice | Rate | Pitch | 狀態 |
|---|---|---|---|---|---|---|
| `narrator` | 旁白 | Edge | `en-GB-SoniaNeural` | `-10%` | `+0Hz` | 沿用 `scripts/voices.json` 鎖定 |
| `george` | George | MiniMax | `cute_boy` F2 | `1.30` | `0` | Lesson 3+ 沿用鎖定 |
| `daddy` | Daddy | Edge | `en-GB-RyanNeural` | `-5%` | `-5Hz` | 沿用 `scripts/voices.json` 鎖定 |

Captain 與 crew 本課只作視覺角色，不開口，因此不用新增 voice。若 GATE 1 決定讓 Captain 開口，須另提 voice 試聽並標記「待 GATE 1 簽核」；在簽核前不設定 rate／pitch。

---

## 畫風定調（Stage 2 鎖定）

### 整體

| 項目 | 鎖定 |
|---|---|
| 風格 | 溫暖手繪水彩童書；帶有海風、木船與歌聲流動感 |
| 色調 | BedroomNight 深藍暖黃；海上以茶棕木色、海藍與柔和晨光為主 |
| 冒險感 | 刺激但安全；大浪與鯨尾有動勢，人物不陷入恐怖或絕望 |
| 歷史呈現 | 捕鯨是故事背景；harpoon 僅畫成連著繩索的長桿，不畫刺入身體 |
| 禁止 | 血、傷口、死鯨、被捕鯨魚、醉酒、恐怖陰影、寫實暴力、圖上英文正文 |
| 文字 | 圖像內不放課文、歌詞、船名或其他英文文字；船隻以造型與圖徽辨識 |

### 視覺與連續性鎖

- **George 水手裝 p2–p11 完全一致：** 白色長袖水手衫、海軍藍方領與袖口、海軍藍短褲、棕色短靴、白色小水手帽；保留 George 的短黑瀏海、圓臉與約五歲比例。
- **Billy o' Tea p3–p11 為同一艘船：** 中型木造帆船、茶棕色船身、暖米色偏茶色船帆；主帆有簡單茶葉圖徽，但不能出現英文船名。
- **同一條 right whale p5–p11：** 巨大、深灰褐色、寬背、V 字形噴氣；體型與疤痕／斑紋固定。牠有力量但不兇惡，始終自由、沒有受傷，也沒有被捕。
- **Wellerman 是另一艘船：** p9–p11 出現，較小、較整潔的補給帆船；淺色船身、單一高桅、綠色圓形圖徽，與 Billy o' Tea 明顯不同。
- **補給品：** sugar 為封好的木箱／麻袋、tea 為茶葉木箱、rum 為封口木桶；只表現物資運送，不飲酒、不醉酒。
- **Harpoon／line：** p6–p8 是連著粗繩的長桿與繩圈；不可刺中鯨魚，不得有血。
- p1 的奶油黃星星毯在 p2 變成茶色船帆；p12 回到同一張床、同一條毯子，完成夢境視覺閉環。

比例尺：`lessons/assets/refs/cast/song-adventures-sheet.png`  
船與鯨：`lessons/assets/refs/cast/song-adventures-ships.png`

### 角色表（2026-08-27 重繪鎖）

**sheet 上不出現 Daddy。** 篇章視覺以海上冒險為主；Daddy 僅保留在 pending 12 頁故事的 BedroomNight／BedroomWake 分鏡，不進角色比例尺。

| ID | 角色 | 外觀鎖 | 比例（相對 George 水手裝） |
|---|---|---|---|
| `george-pajamas` | George 睡衣版 | 灰／藍灰 raglan 長袖、米白長褲、赤腳；短黑瀏海、圓臉、大耳 | — |
| `george-sailor` | George 水手裝 | 白長袖水手衫、海軍藍方領與袖口、海軍藍短褲、棕短靴、白小水手帽；瀏海露出 | — |
| `captain` | Captain | **硬漢船長：** 四十多歲、風吹深皺紋、濃眉、短硬鬍或修剪短鬍渣；深藍厚呢大衣、金扣、船長帽；表情嚴肅果斷，不笑臉討好 | 腰高 ≈ George 的 1.8× |
| `crew-red` | Crew A（紅鬍） | 壯實、紅棕捲鬍、無帽或毛線帽、條紋海魂衫、棕靴；膚色偏白 | 腰高 ≈ George 的 1.7× |
| `crew-young` | Crew B（年輕） | 瘦高、黑短髮、無鬍、深藍上衣、米色褲；東亞或混血面孔，與 A 明顯不同臉型 | 腰高 ≈ George 的 1.75× |
| `crew-stocky` | Crew C（矮壯） | 矮壯、光頭或極短髮、大鬍子、深綠或褐色厚衫、吊帶；膚色深一階 | 腰高 ≈ George 的 1.55× |
| `supply-beard` | Wellerman 補給員 A | 中等身材、棕色全鬍、橄欖綠毛衣、卡其褲、無帽；**只站 Wellerman 甲板** | 腰高 ≈ George 的 1.65× |
| `supply-cap` | Wellerman 補給員 B | 瘦高、灰毛線帽、紅圍巾、米白衫＋棕背心、淺短髭；臉與 A 及 Billy crew 皆不同；**只站 Wellerman 甲板** | 腰高 ≈ George 的 1.7× |

**船員彼此禁止：** 同一張臉複製、同一髮型鬍型、同一套衣服換色。

補給員鎖定圖：`lessons/assets/refs/cast/song-adventures-supply.png`

### 船隻與鯨（2026-08-27 重繪鎖 — 更像真實船型）

| ID | 名稱 | 造型鎖（參考歷史木帆船／捕鯨船） |
|---|---|---|
| `billy-o-tea` | Billy o' Tea | **雙桅以上木造捕鯨帆船**（brig 或 bark 型）：深茶棕船身、多層橫帆＋船首斜帆；主帆有**茶葉圖徽**（無英文）。船首有雕飾、舷側可見吊艇架與索具；比例像真實 19 世紀遠洋帆船，不要玩具感 |
| `wellerman` | Wellerman 補給船 | **明顯較小的單桅／雙桅補給帆船**（schooner 型）：淺色上層船身、深褐水線、單方帆或縱帆；船尾小艙；甲板可見糖箱、茶葉箱、封口 rum 桶；帆上**綠色圓形圖徽**（無英文）。整體比 Billy o' Tea 短約 40–50% |
| `right-whale` | 同一條 right whale | **北露脊鯨（Eubalaena）**：無背鯨鰭、巨大圓頭、**吻部 callosities（灰白斑塊）**、V 形雙噴氣、寬大尾鰭；深灰褐至近黑；體長可與 Billy o' Tea 相當或略長。溫和眼神，**始終自由、無傷、無繩綁身** |

### Prompt 重複句（海上頁 p2–p11 逐頁複製）

```text
Warm hand-drawn watercolor children's picture book, grainy painterly texture. George is an East Asian boy ~5, short black bangs, round face, big dark eyes, toothy smile. SAILOR LOOK: white long-sleeve sailor shirt, navy square collar and cuffs, navy shorts, brown short boots, small white sailor hat with bangs visible. CAPTAIN: rugged weathered face, thick eyebrows, short scruffy beard, stern serious expression, dark navy peacoat, captain hat — NOT friendly soft smile. BILLY CREW: three distinct sailors — crew-red (stocky red-brown curly beard, striped shirt, knit cap), crew-young (tall lean East Asian, black short hair, clean-shaven, navy shirt, beige trousers), crew-stocky (short bald, big dark beard, olive shirt, suspenders). Never clone faces. SUPPLY CREW (Wellerman only): supply-beard (brown full beard, olive-green sweater, no hat) and supply-cap (grey knit cap, red scarf, cream shirt, brown vest). Billy o' Tea: realistic 19th-century wooden brig/bark whaler, tea-brown hull, tea-leaf emblem on main sail, no letters. Wellerman: smaller schooner supply ship (~half length), pale upper hull, green circle emblem, no letters. Cargo lock: 3 pale sugar crates PORT, 2 darker tea chests MID, 4 sealed rum barrels STARBOARD. Right whale: Eubalaena, no dorsal fin, three callosity patches (snout tip, above left eye, right jaw), V-shaped blow spray, kind eye, never harpooned, never bleeding. Whaleboat-1: clinker-built, dark-brown hull, cream interior; bow always crew-red, stern always crew-young. George never in the whaleboat. No on-image text, no photoreal faces, no horror, no blood, no drunkenness.
```

## GATE 2 凍結（2026-08-27 修訂）

角色表、船隻表已鎖定。睡衣版 George＝灰／藍灰 raglan＋米白褲；水手裝、硬漢 Captain、三名差異化 Billy crew、兩船／鯨依 **2026-08-27 重繪** `song-adventures-sheet.png`、`song-adventures-ships.png`。**Sheet 不含 Daddy。** Wellerman 兩名補給員與貨物堆依 `song-adventures-supply.png`。歌詞逐句圖另受下方 **Cast Continuity Lock** 約束。

---

## 空間區（Zone）

| Zone | 頁 | 必須 | 禁止 |
|---|---|---|---|
| BedroomNight | p1 | George 的床、奶油黃星星毯、月光、Daddy 在門邊；歌聲化成柔和旋線 | 船隻已完整出現、白日、圖上英文 |
| DreamDeck | p2 | **只做一件變形：**星星毯拉長成茶色船帆；床沿已是木甲板；房間牆已淡成夜海。George 已穿固定水手裝 | 多物件同時變形（燈塔／衣櫃）、George 說自己在做夢 |
| OpenSea | p3–4 | Billy o' Tea、茶葉圖徽帆、風浪、船首下沉再抬起 | Wellerman、鯨魚、現代船 |
| WhaleChase | p5–8 | 同一條 right whale、同一艘 Billy o' Tea、小艇、長桿與繩索；刺激但安全 | 血、傷口、死鯨、鯨魚被捕、恐怖表情、日曆／日月時間軸小圖 |
| SupplyShip | p9–11 | 不同且較小的 Wellerman、糖箱／茶箱／rum 木桶；p11 鯨魚仍在遠方游走 | 醉酒、把兩艘船畫成同一艘、鯨魚消失或被拖走、日月弧線時間軸 |
| BedroomWake | p12 | 同一睡房、床與星星毯；George 已穿回灰色 raglan 睡衣；Daddy 在床邊 | 水手裝仍穿在身上、海面與毯子在同一畫面裡「融化變形」 |

---

## 故事主軸（12 頁 — **pending，未進 player**）

George 夜裡突然唱起 Wellerman → 歌聲讓房間變成 Billy o' Tea → 風浪帶來 right whale → 船員展開漫長但不傷害鯨魚的追逐 → Wellerman 定期送來 sugar、tea、rum → 四十天後鯨魚仍自由游走，船員仍唱歌 → George 醒來才明白是夢，Daddy 說全家都聽見了歌聲。

---

## 封面（Cover）— 2026-08-27 重繪分鏡

**敘事功能：** 一眼看見鎖定後的 George 水手裝、Billy o' Tea、自由的 right whale、較小的 Wellerman；夜海夢境仍在。  
**Zone：** OpenSea + 遠景 SupplyShip（兩船可分）+ 鯨在水中自由。  
**在場：**
- **Billy 船首／甲板：** `george-sailor`（張口唱歌、開心）為最大前景；後方可辨 `captain`（嚴肅、呢大衣）、`crew-red`、`crew-young`、`crew-stocky`（臉小但服裝鎖可見，不是路人）。
- **Wellerman（明顯較小、遠處右側）：** `supply-beard`（橄欖綠毛衣、棕鬍、無帽）、`supply-cap`（灰毛線帽、紅圍巾、米衫棕背心）。貨物：port 3 淺箱、mid 2 深箱、starboard 4 桶。
- **鯨：** 同一條北露脊鯨，無背鰭、吻部 callosities、V 噴氣；靠近船但**未被捕、無繩、無傷**。
**動作：** George 在船首唱歌；鯨噴氣；Wellerman 朝 Billy 駛近。  
**道具／錨點：** Billy 茶棕船身、主帆**茶葉圖徽**；Wellerman 帆**空心綠圓（無茶葉）**；夜空滿月；可有淡淡星星毯旋線。  
**禁止：** 圖上英文、血、魚叉刺鯨、醉酒、Daddy、補給員站上 Billy、兩船畫成同一艘、Wellerman 用茶葉帆。  
**連續性：** 人物／船／鯨必須對 `song-adventures-sheet.png`、`song-adventures-ships.png`、`song-adventures-supply.png`。

### vocab-wellerman 分鏡

| 欄 | 內容 |
|---|---|
| 用途 | 單字卡：Wellerman = 補給帆船 |
| Zone | SupplyShip 特寫（**不要** Billy、不要鯨） |
| 在場 | 僅 `supply-beard`、`supply-cap` 在較小單桅／雙桅補給船上 |
| 動作 | 船在開闊海上行駛；二人在甲板貨物旁（可扶箱或掌舵），不是空白無人船 |
| 道具 | 淺色船身、帆上**綠圓無茶葉**；貨物鎖 3／2／4 |
| 禁止 | 燈塔、海岸小鎮搶戲、茶葉帆、英文、飲酒 |

### vocab-tonguing 分鏡

| 欄 | 內容 |
|---|---|
| 用途 | 單字卡：tonguing = 辛苦剝鯨脂 |
| Zone | 甲板特寫（對齊 lyric-07，更近） |
| 在場 | 與 lyric-07 **同一五人、全部出力（不得寫成可選）**：`crew-red`、`crew-young`、`crew-stocky` 在剝開處用長柄鏟；`captain` 拉滑輪；`george-sailor` 拉細繩（不拿刀、不笑著玩）。近景可裁畫面邊緣，文字 roster 五人必須寫齊 |
| 動作 | 深色鯨身在甲板；淡色鯨脂毯被桅杆吊鉤從身上剝起；長柄鏟在剝開處；吃力 |
| 禁止 | 血、內臟、Wellerman、海中活鯨、英文、輕鬆切條的餐桌構圖 |

---

## 封面（Cover）— 舊稿（12 頁故事 pending 仍可參考）

**敘事功能：** 同時交代 George、歌曲、兩艘船與自由的鯨魚，讓讀者期待海上夢境。  
**圖上必見證據：** 固定水手裝的 George 站在 Billy o' Tea 船首，張口快樂唱歌；茶色帆上的茶葉圖徽清楚；同一條大 right whale 在船旁躍出水面但保持距離；較小的 Wellerman 帶著木箱和木桶從遠處駛來；月光旋線把畫面邊緣連回星星毯的圖案。  
**禁止：** harpoon 刺中鯨魚、血、捕獲、醉酒、恐怖海怪、圖上英文標題或歌詞。

---

## 分鏡（每頁：敘事功能／圖上必見證據／對白）

### Page 1 — The song begins（BedroomNight）

**敘事功能：** 夜裡 George 突然站起唱歌；Daddy 驚訝但溫柔。鉤子：歌聲開始把他帶離房間。  
**圖上必見證據：** George 穿固定灰色 raglan 睡衣，突然站在床旁、仰頭唱歌；床上奶油黃星星毯；Daddy 穿睡衣站在半開房門邊；金色歌聲旋線繞過床腳，朝窗外海藍月光延伸。  

| Role | Line | Emotion |
|---|---|---|
| narrator | Late one night, George suddenly stood up beside his warm little bed. | calm |
| george | "Soon may the Wellerman come!" | excited |
| daddy | "George, what a big song for such a quiet night!" | surprised |
| narrator | The song swirled around him and carried the bedroom far away. | wonder |

### Page 2 — The room becomes a ship（DreamDeck）

**敘事功能：** 承接歌聲旋線，完成房間到海上的連續變形；George 成為小水手，但不知道自己在夢中。  
**圖上必見證據：** **單一變形：**奶油黃星星毯正拉長成茶色船帆；George 已站在木甲板上，穿鎖定水手裝（白長袖水手衫、海軍藍方領與袖口、海軍藍短褲、棕色短靴、白色小水手帽）；房間牆已淡成開闊夜海。不要同時畫衣櫃、燈塔或其他變形物件。  

| Role | Line | Emotion |
|---|---|---|
| narrator | His blanket billowed upward and became a great tea-coloured sail. | wonder |
| george | "The floor is wood! Am I standing on a ship?" | surprised |
| narrator | He wore a white sailor shirt, blue shorts and brown boots. | calm |
| george | "A ship! I am a little sailor on the sea!" | excited |

### Page 3 — Billy o' Tea（OpenSea）

**敘事功能：** 建立歌曲中的船、船名與航程起點；因 p2 已在甲板，所以日出時正式啟航。  
**圖上必見證據：** Billy o' Tea 全船遠景；茶棕木船身、暖米色偏茶色船帆、茶葉圖徽；船員與 Captain 只作視覺角色；George 在繩索旁幫忙，晨光從夜藍轉金。  

| Role | Line | Emotion |
|---|---|---|
| narrator | At sunrise, the wooden sailing ship put out to sea. | calm |
| narrator | Her name was Billy o' Tea, with tea-coloured sails. | proud |
| narrator | George held a rope while the busy crew raised sail. | excited |
| george | "Billy o' Tea, take us over the bright waves!" | happy |

### Page 4 — Blow, boys, blow!（OpenSea）

**敘事功能：** 風勢升高，船首上下起伏；呼應 Verse 1，並以吹風口號把船推向下一頁的未知海域。  
**圖上必見證據：** 強風吹滿同一面茶葉圖徽帆；Billy o' Tea 船首先壓入浪谷、浪花飛起；George 與船員向後拉同一條繩保持平衡；所有人興奮而非恐慌。  

| Role | Line | Emotion |
|---|---|---|
| narrator | A strong wind filled the sails and pushed them onward. | excited |
| narrator | The wooden bow dipped down, then climbed another shining wave. | wonder |
| narrator | George and the crew leaned back and pulled together. | excited |
| george | "Hold tight, everyone! Blow, me bully boys, blow!" | proud |

### Page 5 — A whale beside the ship（WhaleChase）

**敘事功能：** 因風把船帶離岸邊兩週，right whale 出現；Captain 召集所有人，啟動追逐。  
**圖上必見證據：** 遠方只剩一條細細的海岸線（或空空的海平線），表示已離岸很遠；**不要日曆、不要日月小圖**。同一條大 right whale 從右舷平行浮起、V 字噴氣；Captain 以手勢召集 crew；George 緊握欄杆，驚訝但不害怕。  

| Role | Line | Emotion |
|---|---|---|
| narrator | Billy o' Tea had not been two weeks away from shore. | calm |
| george | "Look! A huge right whale beside our ship!" | surprised |
| narrator | The captain called all hands to take the whale in tow. | excited |
| george | "That whale is bigger than our whole wooden ship!" | wonder |

### Page 6 — Ropes and a little boat（WhaleChase）

**敘事功能：** 承接 Captain 的召集，crew 準備小艇、長桿與 line；明示目的但維持溫和歷史呈現。  
**圖上必見證據：** 小木艇正從 Billy o' Tea 船側緩緩放下；粗繩整齊盤成圈；harpoon 是未接觸鯨魚的長桿連粗繩；George 在大船甲板協助遞繩，不坐進小艇；鯨魚仍在前方自由游。  

| Role | Line | Emotion |
|---|---|---|
| narrator | The crew lowered a little boat beside Billy o' Tea. | calm |
| narrator | They carried long poles and strong lines for the chase. | worried |
| narrator | George passed down a rope and watched the whale swim. | wonder |
| george | "Keep the line tidy, and keep everyone safe today!" | worried |

### Page 7 — The mighty tail（WhaleChase）

**敘事功能：** 小艇才碰水，鯨尾帶起浪花並碰撞小艇；刺激點來自水勢，不是傷害。  
**圖上必見證據：** 小艇剛接觸海面；同一鯨魚的巨大尾巴在前方拍水，浪花推到小艇側面；小艇傾斜但未翻覆，crew 抓穩船邊；長桿仍在艇內或上舉，沒有刺入鯨魚；George 從母船安全位置看見。  

| Role | Line | Emotion |
|---|---|---|
| narrator | Before the little boat had settled, the whale turned around. | worried |
| narrator | Its mighty tail struck the water and bumped the boat. | surprised |
| narrator | The crew grabbed the sides as white water splashed everywhere. | excited |
| george | "Whoa! That tail can make a mountain of water!" | surprised |

### Page 8 — Down below（WhaleChase）

**敘事功能：** 鯨魚潛下、line 快速滑動；明示沒有人傷到鯨魚，追逐未完。  
**圖上必見證據：** 同一鯨魚完整身影向深藍水下潛，身上無桿、無傷口；粗繩從小艇邊快速滑過但沒有綁住鯨身；crew 收回長桿並控制繩圈；George 指向水下氣泡路徑。  

| Role | Line | Emotion |
|---|---|---|
| narrator | The whale dived deep below the bright and foamy water. | excited |
| narrator | A strong line raced past while everyone held on tightly. | worried |
| narrator | They held the line, but the whale swam free. | calm |
| george | "There it goes, diving down below the waves!" | happy |

### Page 9 — The Wellerman arrives（SupplyShip）

**敘事功能：** 因追逐拖長、船上物資變少，另一艘補給船抵達；清楚區分兩艘船。  
**圖上必見證據：** Billy o' Tea **大、在前景左側**；Wellerman **明顯較小、在右遠方駛近**（兩船不要畫成一樣大，避免外形互混）。Wellerman：淺色船身、單一高桅、綠色圓形圖徽。遠處同一鯨魚噴氣，沒有被拖行。  

| Role | Line | Emotion |
|---|---|---|
| narrator | The chase went on, and their supplies began running low. | calm |
| narrator | Then a smaller supply ship appeared across the sparkling sea. | wonder |
| narrator | It carried sugar boxes, tea chests and sealed rum barrels. | happy |
| george | "Look! The Wellerman has found us at last!" | excited |

### Page 10 — Sugar, tea and rum（SupplyShip）

**敘事功能：** 兩船並行交接補給；George 與 crew 以口說／歡呼方式加入副歌，形成情緒高點。  
**圖上必見證據：** **特寫 Billy o' Tea 甲板**：sugar 木箱、tea 木箱、封口 rum 木桶已放到甲板上；Wellerman 只露出右側船頭／船舷一角（綠色圓形圖徽可見），不要兩艘完整大船對開。George 張手歡呼。無人喝 rum，無醉態。  

| Role | Line | Emotion |
|---|---|---|
| narrator | The Wellerman drew alongside, bringing supplies for everyone aboard. | happy |
| narrator | The crew passed over sugar, tea and sealed rum barrels. | calm |
| george | "Soon may the Wellerman come!" | excited |
| narrator | Everyone answered, "To bring us sugar and tea and rum!" | proud |

### Page 11 — Forty days and still singing（SupplyShip）

**敘事功能：** 四十天後，追逐仍沒成功；用幽默明確交代鯨魚沒被捕、補給船定期來、大家仍唱。  
**圖上必見證據：** 同一鯨魚在遠處快樂噴氣並游離，無繩、無傷；Billy o' Tea 上 crew 疲倦但笑著唱歌；較小 Wellerman 再次從遠方載補給來。**不要日月弧線、不要日曆、不要數字。** 用疲憊笑容＋遠方鯨魚表達「追了很久還沒捉到」。  

| Role | Line | Emotion |
|---|---|---|
| narrator | Forty days passed, but the strong whale still swam onward. | calm |
| george | "They did not catch it, and that whale is still going!" | surprised |
| narrator | George and the crew kept singing across the rolling sea. | proud |
| george | "One day we'll take our leave and go!" | happy |

### Page 12 — Everyone heard（BedroomWake）

**敘事功能：** 最後一個音符把海面變回星星毯；George 醒來才知道是夢。Daddy 溫暖回應，歌曲留在現實房間。  
**圖上必見證據：** George 已穿回灰色 raglan 睡衣、坐在同一張床、同一條奶油黃星星毯上剛醒；Daddy 坐床邊微笑；窗外只剩普通夜空（可有一點淡淡海光，但**不要**畫海面融化成毯子）。床邊沒有水手帽或海上實物。  

| Role | Line | Emotion |
|---|---|---|
| narrator | With one final note, the rolling sea became his blanket. | soft |
| george | "What a dream! Soon may the Wellerman come!" | surprised |
| daddy | "We all heard you singing from your warm little room." | happy |
| narrator | George laughed softly, with the sea song still inside him. | happy |

---

## Song Words（精簡版 9 個 — 2026-08-26）

家長否決太簡單的名詞（sail / whale / captain / sugar / tea）。改教歌詞裡需要解釋的詞與短語。例句一律取自 Nathan Evans VEVO 用字；單字卡為**專用圖**（不用故事內頁）。跟唱改走一句一圖 slideshow。

| Word | Example（歌詞） | 圖 |
|---|---|---|
| Wellerman | Soon may the Wellerman come, to bring us sugar and tea and rum. | `vocab-wellerman` |
| bow | The winds blew hard, her bow dipped down. | `vocab-bow` |
| bully boys | Blow, me bully boys, blow! | `vocab-bully-boys` |
| rum | To bring us sugar and tea and rum. | `vocab-rum`（木桶＋深色飲料；無酒醉、圖上無英文字） |
| tonguing | One day, when the tonguing's done. | `vocab-tonguing`（甲板剝脂：淡色鯨脂毯＋滑輪；無血。意思見家教提示） |
| harpoon | All hands to the side, harpooned and fought her. | `vocab-harpoon`（甲板上的魚叉＋繩，不刺入鯨魚） |
| in tow | He'd take that whale in tow. | `vocab-in-tow` |
| all hands | The Captain called all hands and swore. | `vocab-all-hands` |
| take our leave | We'll take our leave and go. | `vocab-leave` |

## Key phrases

- "Soon may the Wellerman come."
- "Blow, me bully boys, blow."
- "Take our leave and go."

---

## Cast Continuity Lock（歌詞 24 句 — 2026-08-27）

機器可讀來源：`scripts/lesson06_lyric_frames.json`。出圖與 slideshow **禁止**手改人物位置；改連續性只改 bible + JSON，再重跑 `scripts/check_lyric_frames.py`。

### 固定群組

| 群組 | 鎖定 ID | 規則 |
|---|---|---|
| Billy o' Tea 甲板 | `george-sailor`, `captain`, `crew-red`, `crew-young`, `crew-stocky` | 五人同船；Captain **永遠**在船尾指揮位或中甲板高處，不進小艇、不上 Wellerman |
| 捕鯨小艇 Whaleboat-1 | bow = `crew-red`，stern = `crew-young` | **全課唯一乘員組合**。只在 lyric-13…16 有人在艇內。`crew-stocky`、George、Captain **永不**進小艇 |
| Wellerman 甲板 | `supply-beard`, `supply-cap` | **只出現在 Wellerman**；從第一次副歌起造型不變；不上 Billy o' Tea、不進小艇 |
| 貨物 | `cargo-sugar`×3、`cargo-tea`×2、`cargo-rum`×4 | Wellerman 甲板永遠：左舷（port）三箱糖、中間兩箱茶、右舷（starboard）四桶 rum。交接時只搬運，不改箱桶款式與堆法 |
| 鯨魚 | `right-whale` | 同一條北露脊鯨。Callosities：**吻尖一塊、左眼上方一塊、右下頷一塊**。無背鰭、V 噴氣、無傷無繩 |

### 硬禁止（連續性）

- 同一句或相鄰句不得把小艇上的 A 換成 B。
- `supply-*` 不得出現在 Billy 甲板或小艇。
- George 24 句皆水手裝；Daddy 不進歌詞圖。
- 副歌 #5≡#21、#6≡#22、#7≡#23、#8≡#24：**同一批人、同一批貨**；只許鏡頭角度不同。
- 圖上無英文、無血、無魚叉刺入鯨身、無日曆／數字。

### 歌詞 Zone

| Zone | Frames | 必須 | 禁止 |
|---|---|---|---|
| OpenSea | 1–4, **7–9**, **17**, **23–24** | Billy o' Tea | Wellerman、海中游動的近景鯨（#7／#23 甲板上是淡色鯨脂作業，不是活鯨） |
| SupplyShip | **5–6, 21–22** | 兩船外形可分；補給員只在 Wellerman | 補給員站上 Billy；貨物款式改款 |
| WhaleChase | 10–16, 18–**20** | 同一條鯨、同一艘 Billy；13–16 小艇乘員鎖定 | 小艇換人、George 下艇、血、刺中 |

---

## Lyric frames（一句歌詞一圖 — roster）

**目標：** `lesson-06.html` 流程為封面 → Song Words → **一句一圖 slideshow** → Full Song。Sing 1–3 已撤下。

來源：Nathan Evans VEVO 用字；時間軸 `scripts/wellerman_timeline.json`；音檔 `song-*.mp3`。

### lyric-01 `v1-01` — There once was a ship that put to sea

| 欄 | 內容 |
|---|---|
| Zone | OpenSea |
| 敘事功能 | 開場：主船啟航 |
| 在場 | **甲板（遠景剪影）：** 五人皆在船上但臉可很小。**小艇：** 空（收在吊架）。**Wellerman：** 無 |
| 動作 | Billy o' Tea 正離開港口／入開闊海；晨光 |
| 道具 | `billy-o-tea`；茶葉圖徽可小但可辨 |
| 連續性 | 開場。無鯨、無補給船 |

### lyric-02 `v1-02` — The name of that ship was the Billy o' Tea

| 欄 | 內容 |
|---|---|
| Zone | OpenSea |
| 敘事功能 | 點名主船 |
| 在場 | **甲板：** George 在船中靠近桅；Captain 船尾；三名 crew 在索具旁。**小艇／Wellerman：** 無 |
| 動作 | 中景展示全船；主帆茶葉圖徽清楚 |
| 道具 | 同一艘 Billy o' Tea |
| 連續性 | 承接 #1 的同一艘船、同一五人；鏡頭靠近 |

### lyric-03 `v1-03` — The winds blew hard, her bow dipped down

| 欄 | 內容 |
|---|---|
| Zone | OpenSea |
| 敘事功能 | 強風、船首入浪 |
| 在場 | **船首：** George + `crew-stocky` 抓欄杆。**中／船尾：** Captain 站穩；`crew-red`、`crew-young` 在甲板後方抓索。**小艇／Wellerman：** 無 |
| 動作 | 船首壓入浪谷、浪花飛濺、帆鼓滿 |
| 道具 | 船首（bow）為畫面主體 |
| 連續性 | 五人仍全在母船；George 與 crew-stocky 在船首，為後面拉繩做鋪墊 |

### lyric-04 `v1-04` — Blow, my bully boys, blow (huh)

| 欄 | 內容 |
|---|---|
| Zone | OpenSea |
| 敘事功能 | 水手齊力迎風 |
| 在場 | **甲板中：** George + `crew-red` + `crew-young` + `crew-stocky` 同拉一條粗繩。**船尾：** Captain 看著他們。**小艇／Wellerman：** 無 |
| 動作 | 四人向後傾拉繩、張口歡呼；興奮不驚恐 |
| 道具 | 一條主帆控繩 |
| 連續性 | 三名 Billy crew 首次同時近景；臉必須可辨且互不相同 |

### lyric-05 `chorus-01` — Soon may the Wellerman come

| 欄 | 內容 |
|---|---|
| Zone | SupplyShip |
| 敘事功能 | 盼望補給船駛來 |
| 在場 | **Billy 甲板眺望：** 五人**引頸期盼、雀躍**，不是事不關己。`crew-stocky`／`crew-red` **放下粗繩**給靠近的補給船。George 揮手；Captain 指向 Wellerman。**Wellerman：** 正在**划／駛向** Billy（船首浪），`supply-beard`、`supply-cap` 出力划或收帆，對準母船。貨物堆鎖定。**小艇／鯨：** 無 |
| 動作 | 補給船朝捕鯨船靠近；母船準備接繩 |
| 道具 | 兩船、接舷繩；Wellerman 貨物堆已是鎖定布局 |
| 連續性 | 補給二人**首次**定裝；之後只在 #6、#21、#22 再出現。無近景鯨 |

### lyric-06 `chorus-02` — To bring us sugar and tea and rum

| 欄 | 內容 |
|---|---|
| Zone | SupplyShip |
| 敘事功能 | 看見補給內容並開始交接 |
| 在場 | **Wellerman：** `supply-beard` 遞茶箱、`supply-cap` 扶 rum 桶。**Billy 接貨：** George 拍手、`crew-stocky` 伸手接箱；Captain 在船尾監督；`crew-red`、`crew-young` 在 Billy 欄杆幫忙拉繩對齊兩船。**小艇：** 空 |
| 動作 | 箱桶從 Wellerman 遞向 Billy；無人飲酒 |
| 道具 | port 三糖箱、mid 兩茶箱、starboard 四 rum 桶（部分可在半空，款式不變） |
| 連續性 | 同一補給二人、同一貨物款；只許搬運 |

### lyric-07 `chorus-03` — One day, when the tonguing's done

| 欄 | 內容 |
|---|---|
| Zone | OpenSea |
| 敘事功能 | 齊心做非常辛苦的 tonguing（歷史剝脂：滑輪吊起大塊淡色鯨脂） |
| 在場 | **僅 Billy 五人全部出力**。**無 Wellerman、海中無活鯨、無小艇乘員** |
| 動作 | 甲板上有深色鯨身；淡色鯨脂毯正從身上被桅杆繩索吊起剝開；三人在剝開處用長柄鏟全力前傾；船長拉滑輪；George 拉細繩、認真不是笑著玩 |
| 道具 | 鯨脂毯、滑輪組、長柄鏟；參考 `lessons/assets/refs/cast/tonguing-flensing-ref.webp`。**無血、無內臟、無紅色組織** |
| 連續性 | 與 #23 同一批人同一工作。補給船此句不入鏡 |

### lyric-08 `chorus-04` — We'll take our leave and go

| 欄 | 內容 |
|---|---|
| Zone | OpenSea |
| 敘事功能 | 告別、船駛向地平線 |
| 在場 | **Billy 船尾甲板全五人揮手。** 小艇空、**無 Wellerman** |
| 動作 | 揮手告別；船尾浪跡 |
| 道具 | 只有 Billy o' Tea |
| 連續性 | 補給船已離開畫面；五人全回 Billy。#24 必須同一批人、可改夕陽 |

### lyric-09 `v2-01` — She had not been two weeks from shore

| 欄 | 內容 |
|---|---|
| Zone | OpenSea |
| 敘事功能 | 離岸未久（畫面與 #17 相同：漫長海上日子） |
| 在場 | **僅 Billy 五人**（同 lyric-17）。無 Wellerman、無鯨 |
| 動作 | 船長憂心掌舵；望遠鏡找鯨；掃／擦甲板；George 小掃把、愁眉 |
| 道具 | 同 #17；**不要日曆、不要第二艘船** |
| 連續性 | 家長指定重用 #17 圖 |

### lyric-10 `v2-02` — When down on her a right whale bore

| 欄 | 內容 |
|---|---|
| Zone | WhaleChase |
| 敘事功能 | 露脊鯨逼近主船 |
| 在場 | **右舷欄杆：** George（驚訝抓欄）、Captain、`crew-stocky`。**中甲板跑近：** `crew-red`、`crew-young`（仍在母船，尚未登艇） |
| 動作 | 同一條 right whale 從右舷浮起、V 噴氣 |
| 道具 | 鯨的三塊 callosities 必須可見 |
| 連續性 | 鯨首次近景；五人全在母船 |

### lyric-11 `v2-03` — The Captain called all hands and swore

| 欄 | 內容 |
|---|---|
| Zone | WhaleChase |
| 敘事功能 | 硬漢船長召集全員 |
| 在場 | **中甲板：** Captain 居中揮手／吹哨。`crew-red`、`crew-young`、`crew-stocky` 從三個方向跑向他。George 在側邊看 |
| 動作 | 嚴肅果斷，不是笑臉 |
| 道具 | 鯨可在畫面邊緣 |
| 連續性 | 三人跑向船長＝即將分工：紅鬍＋年輕去小艇，矮壯留母船 |

### lyric-12 `v2-04` — He'd take that whale in tow (huh)

| 欄 | 內容 |
|---|---|
| Zone | WhaleChase |
| 敘事功能 | 打算用繩拖鯨（尚未拖到） |
| 在場 | **甲板：** George 遞繩圈、Captain 指向鯨、`crew-stocky` 在吊架旁準備放艇。`crew-red`、`crew-young` **站在尚未放下的 Whaleboat-1 旁邊（仍在母船，未入座）** |
| 動作 | 粗繩朝鯨延伸但**未綁住**；鯨自由游 |
| 道具 | Whaleboat-1 掛在吊架上；拖纜 |
| 連續性 | 為 #13 登艇鋪墊；此幀小艇陣列仍為空 |

### lyric-13 `v3-01` — Before the boat had hit the water

| 欄 | 內容 |
|---|---|
| Zone | WhaleChase |
| 敘事功能 | 小艇離開甲板、尚未觸水 |
| 在場 | **Whaleboat-1：** `crew-red` 在船首、`crew-young` 在船尾。**母船甲板：** George、Captain、`crew-stocky` 在吊架邊放繩 |
| 動作 | 小艇吊在半空，艇底未碰海 |
| 道具 | 吊架、繩圈 |
| 連續性 | **乘員從此鎖定到 #16。** 與 #12 是同一對人登入同一艘艇 |

### lyric-14 `v3-02` — The whale's tail came up and caught her

| 欄 | 內容 |
|---|---|
| Zone | WhaleChase |
| 敘事功能 | 鯨尾拍水波及小艇 |
| 在場 | **小艇（同 #13）：** `crew-red` 船首、`crew-young` 船尾，抓艇舷。**母船：** George、Captain、`crew-stocky` 在右舷觀看 |
| 動作 | 巨大尾鰭拍浪；小艇傾斜**未翻** |
| 道具 | 魚叉桿仍在艇內或上舉，**不刺鯨** |
| 連續性 | 乘員不得換；母船三人不得突然出現在艇上 |

### lyric-15 `v3-03` — All hands to the side, harpooned and fought her

| 欄 | 內容 |
|---|---|
| Zone | WhaleChase |
| 敘事功能 | 全員就位、溫和「作戰」（桿不刺入） |
| 在場 | **小艇仍是紅鬍船首 + 年輕船尾**，舉起帶繩魚叉桿。**母船右舷探身：** George、Captain、`crew-stocky` |
| 動作 | 小艇靠鯨側；桿指向鯨但**離開皮膚** |
| 道具 | 帶繩長桿、右舷 |
| 連續性 | 「all hands」＝母船三人到右舷 **加上** 艇上原班人馬，不是把艇上的人瞬移回甲板 |

### lyric-16 `v3-04` — When she dived down low (huh)

| 欄 | 內容 |
|---|---|
| Zone | WhaleChase |
| 敘事功能 | 鯨魚下潛、繩未拴住 |
| 在場 | 小艇乘員同 #13–15；母船三人同前，George 指向水下氣泡 |
| 動作 | 鯨完整下潛；繩從小艇邊滑過、未綁鯨身 |
| 道具 | 氣泡尾跡；鯨無傷 |
| 連續性 | 小艇序列結束。下一句已過四十天，二人回到母船 |

### lyric-17 `v4-01` — For forty days or even more

| 欄 | 內容 |
|---|---|
| Zone | OpenSea |
| 敘事功能 | 捕鯨已四十天仍無收穫；漫長空等 |
| 在場 | **僅 Billy 五人**（`crew-red`、`crew-young` 已回母船）。**無 Wellerman、無補給員、無貨物堆。小艇：** 空（可掛吊架） |
| 動作 | 全員愁眉／憂心（不笑）：Captain **掌舵**；`crew-young` **望遠鏡**掃空地平線找鯨；`crew-stocky` 跪擦甲板；`crew-red` 掃甲板；George 拿小掃把幫忙、擔心不是咧嘴笑 |
| 道具 | 舵輪、銅望遠鏡、掃把／擦甲板石；空曠海面；**不要寫 40、不要日曆、不要鯨、不要第二艘船** |
| 連續性 | 時間跳過後全員回母船合法。此幀補給船尚未入鏡（與副歌 5–7、20–23 分開） |

### lyric-18 `v4-02` — The line went slack then tight once more

| 欄 | 內容 |
|---|---|
| Zone | WhaleChase |
| 敘事功能 | 繩索鬆了又緊 |
| 在場 | **甲板：** `crew-stocky` 在絞盤／欄杆管繩；George 看著繩圈；Captain 船尾；`crew-red`、`crew-young` 在旁幫忙拉。**小艇空。Wellerman 不在此幀** |
| 動作 | 同一畫面裡繩圈明顯「一鬆一緊」（誇張弧線） |
| 道具 | 粗繩、絞盤 |
| 連續性 | 管繩的是留在母船的 `crew-stocky`，不是換一個新臉 |

### lyric-19 `v4-03` — All boats were lost, there were only four

| 欄 | 內容 |
|---|---|
| Zone | WhaleChase |
| 敘事功能 | 只剩四艘小艇 |
| 在場 | 五人全在 Billy 甲板清點／看吊架。Whaleboat-1 是四艘裡可辨的那艘（無人在艇內） |
| 動作 | **左舷兩艘、右舷（或船尾）兩艘**吊在吊艇架上，**禁止**同一側排四個吊鉤。另有兩側空吊架表示損失。五人清點剩下的艇 |
| 道具 | 四艇分兩舷 + 空吊架；**圖上不寫數字 4** |
| 連續性 | 小艇造型與 Whaleboat-1 一致；無人坐進艇裡 |

### lyric-20 `v4-04` — And still that whale did go (huh)

| 欄 | 內容 |
|---|---|
| Zone | WhaleChase |
| 敘事功能 | 鯨仍自由離去 |
| 在場 | **僅 Billy 五人**望向遠方。**無 Wellerman**。小艇空 |
| 動作 | 鯨擺尾游離、無繩 |
| 道具 | 遠鯨 + 只有 Billy |
| 連續性 | 幽默無奈，不是憤怒獵殺；補給船不入此幀 |

### lyric-21 `chorus2-01` — Soon may the Wellerman come

同 #5：**同一批人、同一貨物堆、同樣雀躍放繩、補給船划來**；鏡頭可略低。

### lyric-22 `chorus2-02` — To bring us sugar and tea and rum

同 #6：`supply-beard` 仍遞茶箱、`supply-cap` 仍扶 rum 桶；Billy 仍是 George 拍手 + `crew-stocky` 接箱。

### lyric-23 `chorus2-03` — One day, when the tonguing's done

同 #7：歷史剝脂姿勢（大塊淡色鯨脂＋桅杆滑輪），無血、無 Wellerman、海中無活鯨。

### lyric-24 `chorus2-04` — We'll take our leave and go

同 #8：Billy 五人揮手；無 Wellerman。可加夕陽，不可換人。

**檔名：** `lessons/assets/lesson-06/lyric-01.png` … `lyric-24.png`（頁面載入 `.webp`）。

**Slideshow 頁：** `lessons/lesson-06-slideshow.html`。`lesson-06.html`：封面 → Song Words → slideshow → YouTube。

### CP0 家長簽核

2026-08-27：家長指示實作「一句一圖 slideshow」完整計畫（含 roster 鎖、出圖與新頁）。本 roster 為 GATE 1b 凍結稿；改人物位置須先改本節與 JSON。

### GATE 3／互檢紀錄（2026-08-27）

| 關卡 | 執行 | 結果 |
|---|---|---|
| CP1 | Grok 4.6 分鏡連續性 | 歌詞 24 句 PASS。封面／vocab 初審 **FAIL**（tonguing 可選三人）→ 已改為 lyric-07 同一五人 |
| CP2 | Composer 2.5 schema／timeline／audio | PASS |
| CP3 | Grok 4.5 逐張圖文 | 歌詞圖複審 PASS。封面／vocab-wellerman／vocab-tonguing 安裝檔 **PASS** |
| CP4 | Grok 4.6 相鄰連續 | 歌詞圖 PASS（後續家長改 17／07／23 另記） |
| CP5 | Composer 2.5 player／走查 | **PASS**：無 Sing 1–3；cover → words → slideshow → `#listen` |
| C 音檔 | `check_lyric_frames.py --require-art`、`check_lesson_audio.py` | PASS（JSON 未引用的 p01–quiz mp3 未進本包） |

Slideshow：`lessons/lesson-06-slideshow.html`。封面 **Start** 進單字；單字後 **Picture song** 進 slideshow。

---

## Song-along page plan（獨立於 12 頁故事 — 過渡中）

來源：Nathan Evans 官方版（VEVO 字幕用字）<https://www.youtube.com/watch?v=qP-7GNoDJ5c>。時間軸見 `scripts/wellerman_timeline.json`。  
**現況：** 一句一圖 slideshow 已進 player 主線（封面 → 單字 → slideshow → YouTube）。

1. **Verse 1**
   - There once was a ship that put to sea
   - The name of that ship was the Billy o' Tea
   - The winds blew hard, her bow dipped down
   - Blow, me bully boys, blow (huh)
2. **Chorus（第一次，完整 block）**
   - Soon may the Wellerman come
   - To bring us sugar and tea and rum
   - One day, when the tonguing is done
   - We'll take our leave and go
3. **Verse 2**
   - She had not been two weeks from shore
   - When down on her a right whale bore
   - The captain called all hands and swore
   - He'd take that whale in tow
4. **Verse 3**
   - Before the boat had hit the water
   - The whale's tail came up and caught her
   - All hands to the side, harpooned and fought her
   - When she dived down low (huh)
5. **Later verse（四十天仍未結束）**
   - For forty days or even more
   - The line went slack, then tight once more
   - All boats were lost, there were only four
   - But still that whale did go
6. **Chorus（結尾再次完整播放）**
   - Soon may the Wellerman come
   - To bring us sugar and tea and rum
   - One day, when the tonguing is done
   - We'll take our leave and go

---

## 家教提示（tutor prompts）

精簡版（現在上課用）：
- 問：Wellerman 是什麼？（送來補給的船，不是人的名字）
- 問：bow 是船的哪裡？（船頭，不是蝴蝶結、也不是鞠躬）
- 問：bully boys 是欺負人嗎？（不是；歌裡指強壯開心的水手夥伴）
- 問：rum 是什麼？（以前水手在船上喝的一種深色飲料；歌詞裡跟 sugar、tea 一起送來）
- 問：tonguing 是什麼？（舊時把鯨脂切成長條；歌詞 One day, when the tonguing's done）
- 問：harpoon 是什麼？（帶繩的長魚叉；圖上只放在甲板，不刺鯨魚）
- 問：in tow 是什麼意思？（用繩子拖在後面）
- 問：all hands 是什麼意思？（船上所有人一起過來幫忙）
- 問：take our leave 是什麼意思？（告別離開／回家）

故事頁恢復後再用（pending）：
- 問：Billy o' Tea 與 Wellerman 有什麼不同？（前者是追逐鯨魚的木帆船；後者是較小的補給船）
- 問：鯨尾碰到小艇後發生什麼事？（浪花推動小艇，crew 抓穩，鯨魚潛下）
- 問：Wellerman 帶來哪些補給？（sugar、tea、rum）
- 問：四十天後 crew 捉到鯨魚了嗎？（沒有；鯨魚仍自由游走）
- 問：George 什麼時候才知道那是一場夢？（p12 醒回房間時）

## Quiz 草案（10 題，全部只靠故事可答）

正確答案 index 採 0-based，供後續 JSON 組裝。

| # | Question | Option 0 | Option 1 | Option 2 | Correct index |
|---|---|---|---|---|---|
| 1 | What carried George away from his bedroom? | His song | A toy train | A strong bird | 0 |
| 2 | What did George's blanket become? | A little boat | A tea-coloured sail | A fishing net | 1 |
| 3 | What was George's ship called? | The Wellerman | Billy o' Tea | The Moonlight | 1 |
| 4 | What appeared beside Billy o' Tea? | A right whale | A sea dragon | A blue car | 0 |
| 5 | What bumped the little boat? | A tea chest | The whale's tail | George's boot | 1 |
| 6 | What did the whale do after the big splash? | It climbed aboard | It dived below | It went to sleep | 1 |
| 7 | What kind of ship was the Wellerman? | A supply ship | A racing ship | A pirate ship | 0 |
| 8 | What did the Wellerman bring? | Sugar, tea and rum | Apples, milk and bread | Hats, boots and coats | 0 |
| 9 | Did the crew catch the whale after forty days? | Yes, at sunrise | No, it still swam onward | The story never says | 1 |
| 10 | When did George know the adventure was a dream? | On the first ship page | When the whale appeared | When he woke in his room | 2 |

---

## Stage 1 自查（pipeline 檢查表）

- [x] **12 頁 exactly：** Page 1–12 各一頁，Song-along plan 明確標為獨立頁型，不計入故事頁。
- [x] **因果順序：** p1 歌聲捲起 → p2 房間變船 → p3 出海 → p4 風推離岸 → p5 兩週後遇鯨 → p6 Captain 召集後放艇 → p7 鯨尾碰艇 → p8 鯨魚潛下使追逐延長 → p9 補給不足所以 Wellerman 到來 → p10 交接補給並歡呼 → p11 四十天仍未捕獲 → p12 最後音符把海變回毯子。
- [x] **誰知道什麼：** p2–p11 George 把海上經歷當真，沒有說出「dream」；只在 p12 醒來後說 "What a dream!"
- [x] **道具與方向連續：** 星星毯 p1→茶色帆 p2→星星毯 p12；水手裝 p2–p11；Billy o' Tea、Wellerman、right whale 各自造型固定；harpoon 不接觸鯨魚。
- [x] **ORT LV6：** 每頁 4 句；大多為 8–16 words。短 authentic chorus snippets（含 p11 "take our leave and go"）是刻意保留的歌曲口號。
- [x] **Emotion：** 每句均使用 `calm / wonder / excited / happy / surprised / worried / proud / soft` 之一。
- [x] **角色限制：** 開口者只有 narrator、George、Daddy；Captain／crew 只作視覺角色；沒有新增具名兒童角色。
- [x] **安全與結局：** 無血、無死鯨、無醉酒；歌詞保留原句 harpooned；故事結局鯨魚仍自由游走。

---

## GATE 1 凍結（2026-08-26）

家長指示執行完整計畫（含後續出圖／音檔／組裝）。下列項目凍結，之後不改故事結構：

- Chapter：**George's Song Adventures**
- Title：**George and the Wellerman**
- 12 頁分鏡（互審修訂版）
- Captain／crew 不開口；p12 只有 Daddy 開口
- 水手裝／兩艘船／鯨魚造型鎖見上文
- Song-along 用 Nathan Evans VEVO 字幕用字；時間軸 `scripts/wellerman_timeline.json`

**可進 Stage 2。**
