# Lesson 7 劇本匿名投票結果

規則：四個模型各讀匿名 A–D，投第一、第二（可投別人）。計分：第一名 2 分、第二名 1 分。

揭曉（投票時評審看不到）：

| 匿名 | 原稿 |
|------|------|
| A | Composer — *George and the Wild Parade* |
| B | GPT sol — *George and the Moonlit Wild Things* |
| C | Grok — *George and the Still-Hot Supper* |
| D | Gemini — *George and the Island of Wild Things* |

## 各票

| 評審 | 第一 | 第二 | 有沒有投「自己那份」 |
|------|------|------|----------------------|
| Grok | C（Grok） | A（Composer） | 是（第一） |
| Composer | A（Composer） | B（Sol） | 是（第一） |
| Gemini | C（Grok） | A（Composer） | 否 |
| GPT sol | B（Sol） | A（Composer） | 是（第一） |

## Ranking（依分數）

| 名次 | 劇本 | 分數 | 第一名票 | 第二名票 |
|------|------|------|----------|----------|
| **1** | **Composer** *Wild Parade* | **5** | 1 | 3 |
| **2** | **Grok** *Still-Hot Supper* | **4** | **2** | 0 |
| **3** | **GPT sol** *Moonlit Wild Things* | **3** | 1 | 1 |
| **4** | **Gemini** *Island of Wild Things* | **0** | 0 | 0 |

兩種讀法：

- **共識第二名最多 → Composer 總分第一**（四票裡有三張第二＋一張第一）
- **第一名票最多 → Grok**（兩張第一：Grok 自己＋Gemini）

Gemini 是唯一沒投自己的評審；D 被四處點名：對白偏長、p12 脫頭套、近原句、Mummy 沒收尾。

評審理由摘要見 `ballot/vote-*.md`。
