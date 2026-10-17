from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    pg = b.new_page()
    pg.goto('http://127.0.0.1:8901/index.html')
    pg.wait_for_timeout(1000)
    print('root title:', pg.title())
    r = pg.request.get('http://127.0.0.1:8901/demo/index.html')
    print('demo via request:', r.status, len(r.body()))
    b.close()
