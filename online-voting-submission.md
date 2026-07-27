# 從碳客變捷客｜線上投票提交素材

最後更新：2026-07-27

## 提交欄位

### 作品圖片

建議主投：A 版。三版皆已輸出為主辦方指定尺寸 `768x514px`。

| 版本 | 風格 | 檔案 | 適合用途 | 判斷 |
|---|---|---|---|---|
| A | 明亮插畫、生活情境 | `personal-auto/assets/voting/online-voting/vote-submit-A-illustration-768x514.png` | 公開投票主圖 | 最容易讓一般民眾一眼看懂「搭捷運、賺點、減碳」 |
| B | 深色 App UI、科技質感 | `personal-auto/assets/voting/online-voting/vote-submit-B-appui-768x514.png` | 若想強調作品成熟度 | 視覺最有產品感，但比 A 更偏 tech pitch |
| C | 路線圖資訊圖表 | `personal-auto/assets/voting/online-voting/vote-submit-C-routemap-768x514.png` | 補充說明或候選主圖 | 說明力強，但情緒吸引力低於 A / B |

### 作品介紹

建議提交版本，約 66 字：

> 《從碳客變捷客》把每趟捷運變成有感任務：出站收到沿線推薦，搭車累積減碳，還能用捷運點換生活優惠。讓通勤不只抵達，也替城市多做一點事。

備用短版，約 65 字：

> 每天搭捷運，也能讓城市變得更好。《從碳客變捷客》用出站推薦、捷運點回饋與減碳任務，把通勤變成省錢、順路、低碳又有成就感的生活選擇。

### 作品展示連結

建議提交連結：

```text
https://from-carbon-metro-vote.pages.dev/
```

目前狀態：

- 2026-07-27 loop iteration 3 已將最新版 prototype 部署到 Cloudflare Pages：`from-carbon-metro-vote.pages.dev`。
- 已驗證穩定 URL 可回應 `HTTP/2 200`，且必要 vendor assets 正確回傳 `application/javascript`。
- Browser fresh session 已通過互動 smoke test：首頁正常渲染，無 bundler error；可見 `104 g/km`、`75 g/km`、`每公里少排 29 g`、`3 題偏好 onboarding`、`U-Sport`、`YouBike`；點 `完成今天通勤` 後出現 `出站推播`，點 `打開推薦` 可進路線，點 `減碳` 可見 `北捷／合作方 dashboard`、`估算導客量`、`招商加值`。
- 舊詞 `綠點` / `綠章` 在公開頁可見文字中為 0。
- 原 GitHub Pages 連結 `https://sofiayan0523.github.io/from-carbon-to-metro/` 仍可回應 `HTTP 200`，但目前仍是舊版；`from-carbon-to-metro` 本地開發分支仍為 `ahead 6`，遠端分支停在 `4377d8b`，GitHub Pages `main` 停在 `54829e6`。2026-07-27 GitHub API 認證仍回 `401 Bad credentials`，因此暫不建議用 GitHub Pages 作送件連結。

## 圖片 Review

### A 版｜明亮插畫、生活情境

![A 版投票圖：通勤族在捷運站使用手機，主標從碳客變捷客](/home/workspaces/conversations/78ecb4fc-f4f7-400d-a996-e2454cc37674/personal-auto/assets/voting/online-voting/vote-submit-A-illustration-768x514.png)

### B 版｜深色 App UI、科技質感

![B 版投票圖：深色手機 App 介面，顯示路線與減碳加成](/home/workspaces/conversations/78ecb4fc-f4f7-400d-a996-e2454cc37674/personal-auto/assets/voting/online-voting/vote-submit-B-appui-768x514.png)

### C 版｜路線圖資訊圖表

![C 版投票圖：捷運路線圖串起賺點、用點、減碳與加成](/home/workspaces/conversations/78ecb4fc-f4f7-400d-a996-e2454cc37674/personal-auto/assets/voting/online-voting/vote-submit-C-routemap-768x514.png)

## 下一輪建議

- 若只選一張送件：建議選 A。
- 若希望更像科技產品：選 B，但建議把介紹文案用生活化版本搭配，避免太像評審簡報。
- 若主辦方頁面會把圖片縮很小：不要選 C 作主圖，因為 C 需要讀字，縮小後優勢會下降。
- GitHub Pages 可在認證恢復後再補推 / PR / merge；但目前送件展示連結已可先用 Cloudflare Pages 版本。

## 送件檢查狀態

| 欄位 | 狀態 | 備註 |
|---|---|---|
| 作品圖片 | 可送 review | A / B / C 三版皆為 `768x514px` RGB PNG；建議主投 A |
| 作品介紹 | 可提交 | 主推 66 字、備用 65 字，皆符合 50–120 字 |
| 作品展示連結 | 可提交 | 建議使用 `https://from-carbon-metro-vote.pages.dev/`；已部署最新版 prototype 並通過公開 URL browser smoke test |
