# George's Song Adventures — 篇章提案 v0

新篇章：George 在熟悉的歌曲中進入歷史與想像交織的冒險；本篇不接其他幻想篇章。
狀態：2026-08-26 — **本課先發精簡版**：封面 → Song Words → Sing along 1–3（原曲逐句）→ Full Song（YouTube）。  
12 頁故事繪本、故事 TTS、quiz、phrases、notes **暫緩**（家長：畫面連貫與 TTS 唱歌都不夠好）。分鏡仍保留在下文，供之後改寫。

---

## 系列核心

George 在夜裡唱起一首歌，歌曲把房間變成一場完整冒險。故事保留原始歌詞中的歷史背景，同時以溫暖、非暴力的方式呈現海上追逐。

**系列名／Chapter name（提案）：** George's Song Adventures  
**第一課（lesson-06）標題（提案）：** George and the Wellerman

本課定位：
- George 從唱歌進入冒險，直到 p12 醒來才知道那是一場夢。
- 故事依 public-domain sea shanty〈Wellerman〉推進，課文以 ORT Level 6 方式重述，不整段傾倒歌詞。
- 捕鯨只作歷史背景：無血、無傷口、無死亡；鯨魚始終沒有被捉到。
- 精簡版 PLAYER：**先學歌詞難詞，再跟唱，最後聽完整首歌**。故事頁暫不進 player。

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

### Prompt 重複句（海上頁 p2–p11 逐頁複製）

```text
Warm hand-drawn watercolor children's picture book, grainy painterly texture. George is an East Asian boy ~5, short black bangs, round face, big dark eyes, toothy smile. SAILOR LOOK: white long-sleeve sailor shirt, navy square collar and cuffs, navy shorts, brown short boots, small white sailor hat with bangs visible. Billy o' Tea: tea-brown wooden hull, tea-cream sails, green tea-leaf emblem on the main sail, no letters. Wellerman (only p9–p11): smaller pale-hull supply ship, one mast, green circle emblem, no letters. Right whale (p5–p11): huge dark grey-brown, V-shaped blow spray, kind eye, never harpooned, never bleeding. No on-image text, no photoreal faces, no horror, no blood, no drunkenness.
```

## GATE 2 凍結（2026-08-26）

角色表、船隻表已鎖定，可畫內頁。睡衣版 George＝灰／藍灰 raglan＋米白褲（sheet）；水手裝與兩船／鯨依 sheet。

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

## 封面（Cover）

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

家長否決太簡單的名詞（sail / whale / captain / sugar / tea）。改教歌詞裡需要解釋的詞與短語。例句一律取自 Nathan Evans VEVO 用字；單字卡為**專用圖**（不用故事內頁）。Sing 1–3 則沿用故事內頁當跟唱插圖。

| Word | Example（歌詞） | 圖 |
|---|---|---|
| Wellerman | Soon may the Wellerman come, to bring us sugar and tea and rum. | `vocab-wellerman` |
| bow | The winds blew hard, her bow dipped down. | `vocab-bow` |
| bully boys | Blow, me bully boys, blow! | `vocab-bully-boys` |
| rum | To bring us sugar and tea and rum. | `vocab-rum`（木桶＋深色飲料；無酒醉、圖上無英文字） |
| tonguing | One day, when the tonguing's done. | `vocab-tonguing`（鯨脂切條；無血。意思見家教提示） |
| harpoon | All hands to the side, harpooned and fought her. | `vocab-harpoon`（甲板上的魚叉＋繩，不刺入鯨魚） |
| in tow | He'd take that whale in tow. | `vocab-in-tow` |
| all hands | The Captain called all hands and swore. | `vocab-all-hands` |
| take our leave | We'll take our leave and go. | `vocab-leave` |

## Key phrases

- "Soon may the Wellerman come."
- "Blow, me bully boys, blow."
- "Take our leave and go."

---

## Song-along page plan（獨立於 12 頁故事）

來源：Nathan Evans 官方版（VEVO 字幕用字）<https://www.youtube.com/watch?v=qP-7GNoDJ5c>。時間軸見 `scripts/wellerman_timeline.json`。重複副歌去重。跟唱頁插圖沿用故事內頁：Sing 1 = `story-04`、Sing 2 = `story-05`、Sing 3 = `story-11`。

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
