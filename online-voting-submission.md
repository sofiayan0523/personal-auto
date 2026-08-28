# 從碳客變捷客｜線上投票提交素材

最後更新：2026-07-27

## 提交欄位

### 作品圖片（v2 重製版，2026-07-27 依 Sofia 回饋「不夠吸睛」全面重做）

建議主投：v2-A 吉祥物版。三版皆為主辦方指定尺寸 `768x514px` RGB PNG，繁中文字全部以 Noto Sans TC 程式合成，無 AI 錯字。

| 版本 | 風格 | 檔案 | 吸睛策略 |
|---|---|---|---|
| v2-A | 3D 可愛吉祥物（盲盒公仔質感捷運列車） | `personal-auto/assets/voting/online-voting/vote-submit-v2-A-mascot-768x514.png` | 可愛角色是大眾投票場景中點擊率最高的類型；金幣+葉子直覺傳達「賺點+減碳」 |
| v2-B | 復古普普爆點海報（高彩度、漫畫爆炸） | `personal-auto/assets/voting/online-voting/vote-submit-v2-B-pop-768x514.png` | 高對比色塊在縮圖牆中最搶眼；優惠券+金幣從手機炸出，主打「賺回饋」 |
| v2-C | 電影感實景（月台光影+綠色光流） | `personal-auto/assets/voting/online-voting/vote-submit-v2-C-cinematic-768x514.png` | 情感共鳴路線；真實通勤場景+魔幻綠光，適合喜歡質感的投票者 |

舊版三張（v1 A/B/C）保留於同目錄供對照，不再建議主投。

### 作品介紹（民眾投票版，搭配 v2-A 吉祥物與展示頁）

主推版本，73 字（搭 v2-A 吉祥物與民眾展示頁）：

> 搭捷運也能賺好康！《從碳客變捷客》把日常通勤變成小任務：出站領沿線優惠、集捷運點換咖啡甜點，還能累積減碳加成。投我們一票，讓臺北的捷運生活更好玩！

備用口語版，73 字（搭 v2-A / v2-B）：

> 搭捷運還能賺？《從碳客變捷客》讓每趟通勤都有回饋：出站秒收沿線好康、集捷運點換咖啡甜點，順手減碳還能升級加成。你的日常通勤，就是讓臺北更綠的一票！

備用情感版，76 字（搭 v2-C）：

> 原來每天搭捷運，就是在為城市投票。《從碳客變捷客》把通勤變成小遊戲：出站領好康、集點換優惠、減碳拿加成，省錢又有成就感。投我們一票，一起把臺北變得更綠！

備用短版，73 字：

> 搭捷運賺點數、換好康、還能減碳！《從碳客變捷客》讓你每次出站都收到沿線優惠，集點兌換、加成升級，通勤秒變日常小確幸。投我們一票，讓好康跟著捷運跑！

（v1 文案 66/65 字版本移至文末封存。）

### 作品展示連結

建議提交連結：

```text
https://from-carbon-metro-vote.pages.dev/
```

目前狀態：

- 2026-07-27 已將展示策略改為「民眾版展示頁 + 同站內 prototype demo」：根目錄 `https://from-carbon-metro-vote.pages.dev/` 是 v2-A 吉祥物風格公開投票入口，互動 prototype 保留於 `https://from-carbon-metro-vote.pages.dev/demo/`。
- 展示頁文案與 v2-A 圖一致，主打 `搭捷運，也能賺好康`、出站領沿線優惠、集捷運點換咖啡甜點與減碳加成。
- 2026-07-27 已重新部署 Cloudflare Pages production；根目錄、`/demo/`、v2-A PNG、vendor JS、`llms.txt`、`agent.json` 均回 `HTTP 200`，手機 UA 檢查也通過。
- Browser public smoke test 通過：根目錄可見 v2-A 展示頁與 `立即體驗 Demo`；`/demo/` 可完成 `完成今天通勤` -> `出站推播` -> `打開推薦` -> `路線` -> `減碳` dashboard。
- `/demo/` 仍保留最新版 prototype：可見 `104 g/km`、`75 g/km`、`每公里少排 29 g`、`3 題偏好 onboarding`、`U-Sport`、`YouBike`；點 `完成今天通勤` 後出現 `出站推播`，點 `打開推薦` 可進路線，點 `減碳` 可見 `北捷／合作方 dashboard`、`估算導客量`、`招商加值`。
- 舊詞 `綠點` / `綠章` 在公開頁可見文字中為 0。
- 原 GitHub Pages 連結 `https://sofiayan0523.github.io/from-carbon-to-metro/` 仍可回應 `HTTP 200`，但目前仍是舊版；`from-carbon-to-metro` 本地開發分支仍為 `ahead 6`，遠端分支停在 `4377d8b`，GitHub Pages `main` 停在 `54829e6`。2026-07-27 GitHub API 認證仍回 `401 Bad credentials`，因此暫不建議用 GitHub Pages 作送件連結。

## 圖片 Review（v2 重製版）

### v2-A｜3D 可愛吉祥物

![v2-A 投票圖：3D 可愛捷運列車吉祥物，金幣與葉子環繞，標語從碳客變捷客](/home/workspaces/conversations/78ecb4fc-f4f7-400d-a996-e2454cc37674/personal-auto/assets/voting/online-voting/vote-submit-v2-A-mascot-768x514.png)

### v2-B｜復古普普爆點海報

![v2-B 投票圖：手持手機炸出金幣與優惠券的普普風海報](/home/workspaces/conversations/78ecb4fc-f4f7-400d-a996-e2454cc37674/personal-auto/assets/voting/online-voting/vote-submit-v2-B-pop-768x514.png)

### v2-C｜電影感實景

![v2-C 投票圖：捷運月台上微笑看手機的乘客，綠色光流飛向手機](/home/workspaces/conversations/78ecb4fc-f4f7-400d-a996-e2454cc37674/personal-auto/assets/voting/online-voting/vote-submit-v2-C-cinematic-768x514.png)

## 圖片 Review（v1 舊版，封存）

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
| 作品圖片 | 可送 review | v2-A / v2-B / v2-C 三版皆為 `768x514px` RGB PNG；建議主投 v2-A 吉祥物版 |
| 作品介紹 | 可提交 | 民眾投票主推 73 字、口語版 73 字、情感版 76 字、短版 73 字，皆符合 50–120 字 |
| 作品展示連結 | 可提交 | 建議使用 `https://from-carbon-metro-vote.pages.dev/`；根目錄為民眾版展示頁，`/demo/` 為同站內互動 prototype |

## v1 文案封存

- v1 主推（66 字）：《從碳客變捷客》把每趟捷運變成有感任務：出站收到沿線推薦，搭車累積減碳，還能用捷運點換生活優惠。讓通勤不只抵達，也替城市多做一點事。
- v1 備用（65 字）：每天搭捷運，也能讓城市變得更好。《從碳客變捷客》用出站推薦、捷運點回饋與減碳任務，把通勤變成省錢、順路、低碳又有成就感的生活選擇。
