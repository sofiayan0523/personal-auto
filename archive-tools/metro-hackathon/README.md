# 捷運黑客松製作與驗證腳本歸檔

這些腳本於 2026-10-17 從對話工作區 `.omni/*.py` 原樣保存。

- `build_deck*.py`、`render*.py`：簡報生成與渲染。
- `package_demo.py`、`rebuild_zip.py`：Demo 與離線 ZIP 封裝。
- `test_*.py`、`verify*.py`：歷史驗證腳本。
- 其餘腳本：素材準備、文字與 ZIP 檢查。

原始腳本依賴工作區相對路徑 `personal-auto/`、`from-carbon-to-metro/` 和 `.omni/`；還原時先將本目錄 `.omni/` 的內容複製回工作區 `.omni/`，在工作區根目錄執行。原始截圖與擷取資料請由工作區歸檔索引連結至 Drive 下載並依 ZIP 原始路徑還原。

此處保留歷史腳本原貌，未重新執行部署、瀏覽器自動化或舊版 patch。部分腳本含舊預覽網址及工作區絕對路徑，使用前請檢查。Python 依賴依腳本包含 `python-pptx`、`Pillow`、`qrcode`。
