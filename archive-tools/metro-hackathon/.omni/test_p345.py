from playwright.sync_api import sync_playwright

BASE = 'https://98f4b517.from-carbon-metro-vote.pages.dev'
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

    # 1. complete commute
    page.locator('button', has_text='完成今天通勤').first.click()
    page.wait_for_timeout(400)
    # close exit push if a 稍後 button exists
    try:
        page.locator('button', has_text='稍後').first.click(timeout=2000)
    except Exception:
        pass
    # 2. scenario: 租借共享傘 (partner chip visible)
    page.locator('button', has_text='租借共享傘').first.click()
    page.wait_for_timeout(600)
    try:
        page.locator('button', has_text='稍後').first.click(timeout=2000)
    except Exception:
        pass
    page.screenshot(path=f'{OUT}/p5-scenario-chip.png')

    # 3. switch to 減碳 tab and scroll to dashboard
    page.locator('button', has_text='減碳').last.click()
    page.wait_for_timeout(800)
    # scroll inner containers to bottom to reveal dashboard
    page.evaluate("""() => { document.querySelectorAll('.ctm-scroll').forEach(el => { el.scrollTop = el.scrollHeight; }); }""")
    page.wait_for_timeout(800)
    page.screenshot(path=f'{OUT}/p3-dashboard-live.png')
    browser.close()

print('errors:', errors if errors else 'NONE')
