# Tools（不發佈）

`lessons/` 只放正式課件 HTML。聲線試聽、抽樣腳本寫到 **gitignored** 目錄，不要再加 `lessons/*.html` 測試頁。

## 聲線試聽

| 腳本 | 輸出（gitignored） |
|------|---------------------|
| `scripts/sample_boy_voice.py` | `lessons/assets/lesson-02/voice-tests/` |
| `scripts/sample_minimax_speech.py` | `lessons/assets/lesson-03/voice-tests/` |
| `scripts/sample_george_f2_speed.py` | 同上（F2 語速） |
| `scripts/sample_l7_voices.py` | `lessons/assets/lesson-07/voice-tests/` |

跑完後用本機 server 開該資料夾的 `index.html`。家長選定後改 `scripts/voices.json`＋`docs/character-voices.md`＋`.cursor/rules/character-voices.mdc`，再重錄該角色出現的課。

現有角色已鎖定，平常不必重跑。
