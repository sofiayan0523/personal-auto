# 《從碳客變捷客》亮點強化計畫 — Prototype 修改 + 簡報調整

_制定日期：2026-08-11 · 依據：`competitor-analysis-2026-08-11.md`（8 隊競品分析）_
_目標：冠軍 + 可行性滿分 + 北捷導入 + Numbers 合作切入_

---

## 零、策略總綱：一句話 hook

> **「每一次通勤，都是可驗證的減碳資產。」**

- 8 隊有 7 隊做點數閉環、7 隊做店家導客、6 隊做遊戲化 → 這些都不能當主打
- 全場沒有任何一隊把「減碳量化」做成核心機制，更沒有人能回答「數據可不可信」
- 我方獨家五件套：**碳×點雙向聯動、健康共享生活圈、站內招商加值、Numbers 可稽核資料層、IFRS 15 財務論述**
- 所有修改都為了讓評審在 10 秒內記住：別隊發點數，我們把通勤變成「可驗證的減碳資產」，而且**全部串既有系統、北捷明天就能開工**

---

## 一、Prototype 修改計畫（`demo/index.html`，DC bundle）

### 技術路徑（已驗證）

- App 原始碼在 `__bundler/template` JSON 內（約 545KB），工作副本已解包至 workspace `.omni/demo_template_extracted.html`
- 修改後重新 `json.dumps` 並將 literal `<` 序列化為 `\u003c` 塞回（既知 DC runtime regex 陷阱）
- 部署：Cloudflare Pages `from-carbon-metro-vote` + 重打離線 zip

### P1 — 視覺「搶眼化」：對齊投票頁 Neo-brutalism（優先度最高，Sofia 明確要求）

現況：demo 是沉穩墨綠米白（`#0C6B4F`/`#F4F2EC`/`#FCE2A6`）；投票頁是高飽和普普風。

- 導入投票頁色 token：`--metro #0b7a75`、`--leaf #38b86f`、`--sun #ffd34d`、`--coin #f5a524`、`--coral #ff6a3d`、`--ink #17231c`、`--cream #fff7df`
- 主按鈕/CTA/Tab bar 選中態：粗 ink 描邊（2.5–3px）+ 硬偏移陰影（4px 4px 0 ink）+ 按壓位移微動畫
- 點數徽章、乘數徽章改「貼紙風」：sun/coin 漸層 + ink 描邊 + 微旋轉
- 頂部 header 與關鍵數字改高對比大字；保留內容卡淺色底確保可讀性
- Level Up 乘數特效升級：彩帶 + 貼紙彈跳（比競品 confetti 更有記憶點）

### P2 — 亮點放大：首頁「減碳資產」Hero 卡

- 首頁頂部新增 hero 卡：本月減碳 g CO₂e 特大數字 + 換算意象（≈幾棵樹/幾杯咖啡）+ 乘數進度條
- 每筆任務完成 toast 顯示「+N 捷運點 ∕ −N g CO₂e」雙數字聯動動畫（強化「雙向聯動」感知）
- 新增「碳係數怎麼算」說明卡：104/75/29 g/人km，標註「北捷提供之參考值，正式導入前由北捷確認」+ 引臺北市開放資料（分時進出量）作為推播時段依據 → 學捷點快閃的 HONESTY 誠實標註（評審吃這套）

### P3 — 雙端聯動 LIVE 感（正面迎戰 Metro-Link 的殺手橋段）

- Dashboard 頁新增「即時事件流」：乘客端每完成任務/核銷，dashboard 對應數字跳動 + 事件 log 滾入 + 「LIVE」pulse 紅點（同一 React state，純前端即可）
- Demo 動線：乘客完成借傘任務 → 切到北捷 dashboard → 觸及/導客/減碳數字即時 +1 → 評審親眼看到閉環

### P4 — Numbers 可稽核資料層（合作切入點，全場唯一）

- 核銷條碼 modal 與減碳紀錄加「資料指紋已封存」provenance 標記：Nid 樣式 hash + 時間戳 + 「可稽核」badge
- Dashboard 新增「稽核就緒」統計卡：碳數據/核銷紀錄 100% 附數位指紋，ESG 報告可直接引用
- 標註「Provenance by Numbers Protocol」＋ tagline「Human Truth. Machine Proof.」（一字不改）
- 話術：燎原智庫的 AI 審核是假動畫；我們的差異是「北捷發出去的每一點、每一克減碳，都經得起審計」

### P5 — 可行性滿分細節

- 各情境任務卡加「既有系統」小標：raingo／ChargeSPOT／YouBike／U-Sport／亞尼克 YTM → 每個功能都有現成廠商，零新建
- Onboarding 完成頁加一行「本 Demo 依臺北市資料大平臺北捷分時進出量開放資料設計推播時段」

### 迭代排程

- 迭代 3：P1 視覺 + P2 hero 卡（template 改寫）
- 迭代 4：P3 LIVE 事件流 + P4 Numbers 層 + P5 標註
- 迭代 5：重新封裝 bundle、部署 Cloudflare Pages、browser smoke test、離線 zip 同步

---

## 二、決賽簡報調整計畫（Google Slides `1_MIRSbXIKBMvQkZTQPgr2GkFS6UrxYYh1440pvbjUEc`）

### 視覺 spec（與投票頁/Prototype 同語言）

- 配色：ink/teal/leaf/sun/coin/coral + cream 底；粗描邊 + 硬陰影 + 貼紙徽章；吉祥物（捷客松官方視覺）貫穿
- 每頁一個特大數字或一句話；Noto Sans TC 粗體標題
- 執行方式：以 python-pptx 重製搶眼版 .pptx（Slides API 難做 Neo-brutalism 細節），或以 HTML 簡報 + 匯出備援——迭代 6 開工時定案

### 頁面結構（15 頁重排）

| # | 頁面 | 重點 |
|---|---|---|
| 1 | 封面 | 吉祥物 + hook「每一次通勤，都是可驗證的減碳資產」 |
| 2 | 痛點 | 點數沉澱無感 ×通勤碳排未被資產化（引北捷 114 年日運量 207.4 萬官方數據） |
| 3 | **競爭定位（新增）** | 「10 強都在發點數，只有我們做可驗證的減碳資產」差異化矩陣一頁 |
| 4 | 核心機制 | 碳×點雙向聯動：104/75/29 係數 + 乘數 Level Up |
| 5 | 使用者旅程 | 進站→通勤→出站推播→花點核銷 4 格漫畫式 |
| 6 | 健康共享生活圈 | U-Sport/U-Walk/YouBike——串市府既有系統、零新建 |
| 7 | 站內招商加值 | 亞尼克 YTM/raingo/ChargeSPOT 既存廠商→北捷場站商業開發新營收線 |
| 8 | 雙端 Demo | 乘客端×北捷 dashboard LIVE 聯動截圖 + QR 掃碼現場玩 |
| 9 | Numbers 可稽核資料層 | 每一點、每一克減碳都經得起審計；ESG 揭露就緒 |
| 10 | 可行性對照表 | 每功能→既有系統/廠商→導入成本；「不是另一支 App，是 Go App 的加值模組」 |
| 11 | 財務試算 | 首年合作金流 2,270 萬/支出 1,525 萬/餘額 745 萬 + IFRS 15 點數負債與 breakage（全場唯一） |
| 12 | 三階段導入藍圖 | 試辦站點→擴大→全網 + KPI（核銷率/移轉成本/減碳量） |
| 13 | 誠實標註 | 模擬資料聲明、係數待北捷確認——風險透明化 |
| 14 | 團隊×技術 | Omni Edge / Numbers Protocol 技術支持 |
| 15 | 收尾 | hook 重述 + Demo QR + 投票資訊 |

### QA 備彈（附錄頁或口頭）

- 「跟 MetroPulse 的商家出資有何不同?」→ 我們對接的是北捷**既有招商業務**的加值，不需說服商家買新概念
- 「碳係數怎麼驗證?」→ Numbers 資料指紋 + 北捷正式值導入即換，架構不變
- 「點數會計怎麼處理?」→ IFRS 15 遞延收入 + breakage 估算（研究底稿：points-business-model-report.html）

### 迭代排程

- 迭代 6：讀取現有 15 頁 Slides 內容、產出新版簡報（含視覺模板）
- 迭代 7：完成全部頁面 + 匯出 .pptx + 截圖檢查
- 迭代 8：總驗證（prototype 部署 + 離線包 + 簡報 + 8/24 繳交清單對照）
