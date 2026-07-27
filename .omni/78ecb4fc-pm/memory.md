# Workspace Context

<!-- This file is auto-maintained. The Repositories section is refreshed -->
<!-- by the system. The AI should maintain Environment & Key Discoveries. -->

**Workspace root (absolute path):** `/home/workspaces/conversations/78ecb4fc-f4f7-400d-a996-e2454cc37674`

## Repositories

- **`from-carbon-to-metro/`** — Branch: `omni/78ecb4fc/from-carbon-to-metro`, Remote: `sofiayan0523/from-carbon-to-metro`
  - > 2026 捷運盃黑客松「玩點生活・智慧串聯」創新應用競賽 — App Mockup

- **`personal-auto/`** — Branch: `omni/78ecb4fc/personal-auto`, Remote: `sofiayan0523/personal-auto`

- **`sofia-s-blog/`** — Branch: `omni/78ecb4fc/sofia-s-blog`, Remote: `sofiayan0523/sofia-s-blog`
  - **URL**: https://lovable.dev/projects/REPLACE_WITH_PROJECT_ID

## Environment & Tools

- Prototype 專案 `from-carbon-to-metro/` 已複製並在 branch `omni/78ecb4fc/from-carbon-to-metro` 進行更新，無 build step；2026-07-27 起根目錄 `index.html` 是民眾投票展示頁，完整互動 prototype 保留於 `demo/index.html`，更新 prototype bundle 時需同步維護 `demo/assets/vendor/` 與離線備援 zip。
- `personal-auto/` 目前可直接放靜態 HTML；`workshop-presentation.html` 不需 build step，瀏覽器直接開啟即可播放。

## Key Discoveries

- 線上投票提交草稿在 `personal-auto/online-voting-submission.md`；2026-07-27 依 Sofia 回饋「不夠吸睛」全面重製為 v2 三版：v2-A 3D 吉祥物、v2-B 普普爆點海報、v2-C 電影感實景（檔名 `vote-submit-v2-*-768x514.png`），底圖用 gpt-image-1 生成、繁中文字以 Noto Sans TC 程式合成避免 AI 錯字；建議主投 v2-A。2026-07-27 已將 Cloudflare Pages `https://from-carbon-metro-vote.pages.dev/` 改成 v2-A 風格民眾投票展示頁，互動 prototype 在同站內 `/demo/`；公開 URL、手機 UA、主圖 PNG、agent-readiness 檔與 demo smoke test 均通過。GitHub Pages production 仍是舊版，`from-carbon-to-metro` 本地分支 ahead，且 GitHub API 認證回 401。
- 2026-07-27 Prototype 已補齊決賽提案 v2 / 工作坊討論的五項核心缺口：104/75/29 可配置碳係數、3 題 opt-in 偏好 onboarding、完成通勤後出站推播、U-Sport/U-Walk/YouBike 健康共享生活圈任務，以及北捷/合作方 dashboard（觸及、導客、招商加值、換券、核銷、健康共享任務）；GitHub Pages production 仍因 GitHub API 401 未更新，但線上投票展示備援已部署至 Cloudflare Pages `https://from-carbon-metro-vote.pages.dev/` 並通過公開 URL browser smoke test。
- Prototype 核心與終端術語升級：地毯式清除「綠點／綠章」舊詞彙，全面統一為「捷運點／捷運章」與決賽提案一致。實作「捷運點與減碳排雙向聯動機制」，完成情境任務（如借傘、補電、時租會議亭、蛋糕補給）能同步累積減碳量並動態觸發乘數倍率 Level Up 特效；並針對花點（點數消耗）需求，全新實作「已選推薦店家詳情與花點兌換（App 換券）」與「我的票券夾（Me Tab Wallet）」，直接可在手機中模擬扣點換券、出示核銷條碼，展示 earn-to-spend 完整永續商業閉環。
- 決賽提案 v2 Google Doc：`1wIR6SyXYyqJVXteGhcC-kcH68appxkIu30gKcIYjg8g`（工作坊調整版，v1→v2 對照表在文件開頭）。決賽簡報初稿 Google Slides：`1_MIRSbXIKBMvQkZTQPgr2GkFS6UrxYYh1440pvbjUEc`（15 頁，以 GWS DWD 用 Sofia 身份建立，可由 Slides 直接下載 .pptx）。
- 點數商業模式研究報告已建立於 `personal-auto/points-business-model-report.html`：涵蓋 OPENPOINT、Hami Point、LINE POINTS、台灣星巴克、Rakuten、Marriott Bonvoy，以及 IFRS 15／點數負債與 breakage 風險；可作為捷運提案與 prototype 的研究底稿。
- 北捷站內即時補給與空間租賃公開案例可分為甜點／餐飲自助機（亞尼克 YTM、Yo-Kai）、補電（旅電、ChargeSPOT 及充電線）、共享傘（raingo）、香氛試香機（TRICENT）、客製悠遊卡、珠寶禮品、手機線材／配件、智慧生活站、快閃櫃、快剪與小樹屋電話亭等；可包成「租賃廠商可被 Go App 推播／Go!Map 標記／捷運點券導客」的招商加值，但租賃點位自有行銷與第三方廣告需依北捷審查邊界標示。
- 捷運盃黑客松工作坊簡報已建立於 `personal-auto/workshop-presentation.html`，內容依 Google Doc 提案「從碳客變捷客」整理；使用 `assets/fonts/NotoSansCJKtc-Workshop.woff2` 子集字型確保繁中離線顯示。
- 原版企劃書 `personal-auto/2026捷運盃黑客松_提案企劃書_綠點導航.docx` 的 ESG 內容集中在「綠點導航／碳足跡回饋／國泰世華 ESG 聯名／全市減碳量」；決賽口徑宜改掛到 AI 站點情境助理、捷運點減碳加成與北捷可衡量站點導客。
- `from-carbon-to-metro/index.html` 的 bundler template script 需將 raw JSON 內的 literal `<` 序列化為 `\u003c`；DC runtime 會 `fetch(location.href)` 並用 regex 搜 `<x-dc>`，若外層 bundle raw script 留有 literal `<x-dc>`，會誤解析 JSON 字串內的 template，導致 React `onClick` 收到 string 並在點擊時出現 `[bundle] Script error`。
- 共享經濟／健康減碳方向提案已整理為台北捷運審閱版 `personal-auto/metro-shared-health-proposal.html`；定位為「捷運健康共享生活圈」，以捷運點承接 U-Sport／U-Walk、YouBike、raingo、旅電／ChargeSPOT、亞尼克 YTM 與悠遊付第二階段合作場景，已新增 ESG 敘事與首年財務試算（基準：合作金流 2,270 萬、支出 1,525 萬、可支應營運餘額 745 萬，待北捷確認）；文案已移除 v3／新版比較語氣；同檔使用 `assets/fonts/NotoSansCJKtc-MetroShared-*.woff2` 子集字型避免繁中缺字。
- 捷運盃工作坊與後續點數討論整理於 `personal-auto/workshop-discussion-notes.md`；核心 pivot 是從「泛綠點」收斂為「捷運點減碳加成 + 精準推播導客 + 北捷可變現行銷方案」，並需改用北捷口述碳係數 104/75/29（待正式確認）。

## Installed Skills

- **`aeo-assessment`** (system)
- **`agent-readiness-generator`** (system)
- **`ai-bot-traffic`** (system)
- **`dev-monitor`** (system)
- **`doc-coauthoring`** (system)
- **`frontend-design`** (system)
- **`google-ads`** (system)
- **`google-workspace`** (system)
- **`gov-projects-search`** (space)
- **`harness-agent`** (system)
- **`harness-dev`** (system)
- **`harness-execution`** (system)
- **`harness-plan`** (system)
- **`harness-supervisor`** (system)
- **`image-generation`** (system)
- **`internal-comms`** (system)
- **`line-messaging`** (system)
- **`meta-ads`** (system)
- **`morning-brief`** (space)
- **`ms-office-suite`** (system)
- **`omni-help`** (system)
- **`pdf`** (system)
- **`short-video`** (system)
- **`skill-creator`** (system)
- **`theme-factory`** (system)
- **`webapp-testing`** (system)
- **`z-agent-ticket-creation`** (system)
- **`z-check-comment`** (system)
- **`z-report-status`** (system)
- **`z-sync`** (system)
- **`z-ticket-check`** (system)
- **`z-writing-rules`** (system)


---
_Last system refresh: 2026-07-27 07:40 UTC_
