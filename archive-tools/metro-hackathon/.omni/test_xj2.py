from playwright.sync_api import sync_playwright
BASE = 'https://fedc1d46.from-carbon-metro-vote.pages.dev'
OUT = '/home/workspaces/conversations/78ecb4fc-f4f7-400d-a996-e2454cc37674/.omni/shots'
errors = []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
    page = browser.new_page(viewport={'width': 1280, 'height': 950})
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.goto(BASE + '/demo/', timeout=60000)
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(6000)
    html = page.evaluate("() => document.body.innerHTML")
    for kw in ['營運總覽', '待北捷', '示範', '可變現']:
        print(kw, '→ in DOM:', kw in html)
    page.locator('button', has_text='減碳').last.click()
    page.wait_for_timeout(600)
    body = page.evaluate("() => document.body.innerText")
    print('營運總覽 visible in carbon tab:', '營運總覽' in body)
    browser.close()
print('errors:', errors if errors else 'NONE')
