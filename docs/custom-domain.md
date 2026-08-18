# Custom domain — george.macau-tech.com

George 的英語教材透過 **GitHub Pages** 託管，並以 Cloudflare 管理的子網域對外提供。

| 項目 | 值 |
|------|-----|
| 自訂網域 | `george.macau-tech.com` |
| DNS 供應商 | Cloudflare（`macau-tech.com`） |
| 託管 | GitHub Pages — [EricChang1015/GeorgeEnglishLesson](https://github.com/EricChang1015/GeorgeEnglishLesson) |
| Repo 根目錄 | `CNAME` 檔（內容為自訂網域） |

## 架構

```
瀏覽器 → george.macau-tech.com
       → Cloudflare DNS（CNAME）
       → ericchang1015.github.io（GitHub Pages）
       → 本 repo 根目錄的靜態檔
```

綁定自訂網域後，路徑**不含** `/GeorgeEnglishLesson/` 前綴，例如：

- 首頁：`https://george.macau-tech.com/`
- 第 1 課：`https://george.macau-tech.com/lessons/lesson-01.html`

舊的 GitHub Pages 網址（`ericchang1015.github.io/GeorgeEnglishLesson/`）通常仍可使用，但對外請以自訂網域為準。

---

## Cloudflare DNS（一次性設定）

1. 登入 [Cloudflare Dashboard](https://dash.cloudflare.com/) → 選 **`macau-tech.com`**
2. **DNS** → **Records** → **Add record**
3. 填入：

| 欄位 | 值 |
|------|-----|
| Type | `CNAME` |
| Name | `george` |
| Target | `ericchang1015.github.io` |
| Proxy status | **DNS only（灰雲）** |

> GitHub 建議指向 Pages 的 CNAME **不要**走 Cloudflare Proxy（橘雲），否則 HTTPS 憑證驗證可能失敗。靜態教材站用 GitHub 自帶 HTTPS 即可。

4. 儲存後，可用 [dnschecker.org](https://dnschecker.org/#CNAME/george.macau-tech.com) 確認 CNAME 已指向 `ericchang1015.github.io`。

---

## GitHub Pages（一次性設定）

1. Repo → **Settings** → **Pages**
2. **Custom domain** 填入 `george.macau-tech.com` → **Save**
3. 等待 DNS 檢查通過（數分鐘至約 1 小時）
4. 出現 **Enforce HTTPS** 後勾選啟用

Repo 根目錄的 `CNAME` 檔應與 Settings 中的自訂網域一致；若 GitHub 自動改寫，pull 後以遠端為準。

**Source：** `main` 分支、根目錄（`/ (root)`）。

---

## 日常發佈

內容更新與自訂網域無關：push 到 `main` 即可，GitHub Pages 會自動重建。

```bash
git push origin main
```

發佈後在 `https://george.macau-tech.com/` 硬重新整理（Ctrl+Shift+R）確認。詳見 `.cursor/rules/delivery.mdc`。

---

## 疑難排解

| 症狀 | 可能原因 | 處理 |
|------|----------|------|
| DNS 檢查失敗 | CNAME 未生效或 Target 錯誤 | 確認 Cloudflare 記錄為 `george` → `ericchang1015.github.io`（灰雲） |
| HTTPS 無法啟用 | Proxy 開啟或 DNS 剛生效 | 改灰雲；等 24h 後再試 Enforce HTTPS |
| 404 / 錯誤 repo | Custom domain 綁錯 repo | 確認 Settings → Pages 為本 repo |
| 混合內容警告 | 硬編碼 `http://` 資源 | 教材資源應為相對路徑或 `https://` |

---

## 變更子網域

若日後改用其他子網域（例如 `learn.macau-tech.com`）：

1. Cloudflare 新增或修改 CNAME
2. GitHub Pages → Custom domain 更新
3. 更新 repo 根目錄 `CNAME` 檔
4. 更新 `README.md` 與本文件
