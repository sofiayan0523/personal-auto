from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=['--no-sandbox','--disable-http2'])
    pg = b.new_page()
    try:
        pg.goto('https://example.com', timeout=15000)
        print('external ok:', pg.title())
    except Exception as e:
        print('external fail:', e)
    try:
        pg.goto('http://127.0.0.1:8901/index.html', timeout=15000)
        print('local ok:', pg.title())
    except Exception as e:
        print('local fail:', str(e)[:200])
    b.close()
