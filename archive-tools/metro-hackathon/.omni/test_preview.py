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
    page.screenshot(path=f'{OUT}/preview-home.png')
    # find hero CTA button and click
    btns = page.locator('button').all()
    print('button count:', len(btns))
    texts = [b.inner_text().strip().replace('\n',' ')[:30] for b in btns[:25]]
    print('buttons:', texts)
    clicked = False
    for b in btns:
        t = b.inner_text()
        if '完成' in t or '出站' in t or '通勤' in t:
            b.click(); clicked = True
            print('clicked:', t.strip()[:30]); break
    page.wait_for_timeout(700)
    page.screenshot(path=f'{OUT}/preview-after-cta.png')
    page.wait_for_timeout(1500)
    page.screenshot(path=f'{OUT}/preview-after-cta2.png')
    browser.close()

print('errors:', errors if errors else 'NONE')
