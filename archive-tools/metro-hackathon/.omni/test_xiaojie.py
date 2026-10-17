from playwright.sync_api import sync_playwright

BASE = 'https://fedc1d46.from-carbon-metro-vote.pages.dev'
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
    # text checks in rendered DOM
    body = page.evaluate("() => document.body.innerText")
    for bad in ['待北捷', '口述', '示範數據', 'Demo 示意', '可變現', 'AI 站點', 'Demo Hash', '搭乘模擬', '實時']:
        print(('LEAK ' if bad in body else 'clean'), bad)
    for good in ['小捷 · 出站小幫手', '你的通勤小夥伴', '以官方參考係數計算', '營運總覽']:
        print(('OK   ' if good in body else 'MISS '), good)
    # complete commute → exit push shows 小捷提醒 with mascot
    page.locator('button', has_text='完成今天通勤').first.click()
    page.wait_for_timeout(600)
    body2 = page.evaluate("() => document.body.innerText")
    print(('OK   ' if '小捷提醒' in body2 else 'MISS '), '小捷提醒 (exit push)')
    # scroll to scenario card and screenshot
    page.locator('text=小捷 · 出站小幫手').first.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    page.screenshot(path=f'{OUT}/xiaojie-scenario.png')
    browser.close()

print('errors:', errors if errors else 'NONE')
