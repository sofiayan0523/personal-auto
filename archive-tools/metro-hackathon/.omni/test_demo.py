from playwright.sync_api import sync_playwright

BASE = 'http://127.0.0.1:8901'
OUT = '/home/workspaces/conversations/78ecb4fc-f4f7-400d-a996-e2454cc37674/.omni/shots'
errors = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 900})
    page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.goto(BASE + '/demo/index.html')
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(4000)
    page.screenshot(path=f'{OUT}/demo-home.png')
    # click hero CTA (complete commute) to trigger dual-number float
    try:
        btn = page.locator('button', has_text='完成').first
        if btn.count() == 0:
            btn = page.locator('button').filter(has_text='通勤').first
        btn.click()
        page.wait_for_timeout(600)
        page.screenshot(path=f'{OUT}/demo-after-commute.png')
    except Exception as e:
        errors.append('CTA click: ' + str(e))
    browser.close()

print('console/page errors:', errors if errors else 'NONE')
