from playwright.sync_api import sync_playwright

BASE = 'https://restyle-preview.from-carbon-metro-vote.pages.dev'
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
    page.locator('button', has_text='完成今天通勤').first.click()
    page.wait_for_timeout(500)
    page.screenshot(path=f'{OUT}/preview-float-fx2.png')
    browser.close()
print('errors:', errors if errors else 'NONE')
