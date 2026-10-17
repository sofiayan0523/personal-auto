from playwright.sync_api import sync_playwright

BASE = 'https://629ce757.from-carbon-metro-vote.pages.dev'
OUT = '/home/workspaces/conversations/78ecb4fc-f4f7-400d-a996-e2454cc37674/.omni/shots'
errors = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
    page = browser.new_page(viewport={'width': 1280, 'height': 950})
    page.on('console', lambda m: errors.append('console: ' + m.text) if m.type == 'error' else None)
    page.on('pageerror', lambda e: errors.append('pageerror: ' + str(e)))
    page.goto(BASE + '/demo/', timeout=60000)
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(6000)
    page.locator('button', has_text='路線').last.click()
    page.wait_for_timeout(700)
    page.locator('text=板南線').first.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    page.screenshot(path=f'{OUT}/supply-schematic.png')
    page.locator('text=站內補給站').first.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    page.screenshot(path=f'{OUT}/supply-legend.png')
    body = page.evaluate("() => document.body.innerText")
    for kw in ['站內補給站 · 出站不用繞路', 'raingo 共享傘', '旅電 ChargeSPOT', '亞尼克 YTM', 'Happ. 小樹屋', '捷運點可折抵']:
        print(('OK  ' if kw in body else 'MISS'), kw)
    browser.close()
print('errors:', errors if errors else 'NONE')
