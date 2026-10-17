from playwright.sync_api import sync_playwright

BASE = 'https://from-carbon-metro-vote.pages.dev'
OUT = '/home/workspaces/conversations/78ecb4fc-f4f7-400d-a996-e2454cc37674/.omni/shots'
errors = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
    page = browser.new_page(viewport={'width': 1280, 'height': 950})
    page.on('console', lambda m: errors.append('console: ' + m.text) if m.type == 'error' else None)
    page.on('pageerror', lambda e: errors.append('pageerror: ' + str(e)))
    # root vote page
    page.goto(BASE + '/', timeout=60000)
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(2000)
    page.screenshot(path=f'{OUT}/prod-root.png')
    # demo
    page.goto(BASE + '/demo/', timeout=60000)
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(6000)
    page.locator('button', has_text='完成今天通勤').first.click()
    page.wait_for_timeout(500)
    page.screenshot(path=f'{OUT}/prod-demo.png')
    # mobile UA check
    ctx = browser.new_context(viewport={'width': 390, 'height': 844}, user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
    mp = ctx.new_page()
    mp.on('pageerror', lambda e: errors.append('mobile pageerror: ' + str(e)))
    mp.goto(BASE + '/demo/', timeout=60000)
    mp.wait_for_load_state('networkidle')
    mp.wait_for_timeout(6000)
    mp.screenshot(path=f'{OUT}/prod-demo-mobile.png')
    browser.close()

print('errors:', errors if errors else 'NONE')
