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

    # scroll TODAY tab so scenario card centers; use partner chip as anchor
    chip = page.locator('text=既有廠商').first
    chip.scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.screenshot(path=f'{OUT}/p5-partner-chip.png')

    # go to ROUTE tab, find a redeem button
    page.locator('button', has_text='路線').last.click()
    page.wait_for_timeout(800)
    got = False
    for txt in ['兌換此券', '兌換', '使用捷運點']:
        loc = page.locator('button', has_text=txt)
        if loc.count() > 0:
            try:
                loc.first.scroll_into_view_if_needed()
                loc.first.click()
                got = True
                print('clicked redeem button:', txt)
                break
            except Exception as e:
                errors.append(f'redeem {txt}: {e}')
    page.wait_for_timeout(800)
    page.screenshot(path=f'{OUT}/p4-voucher-modal.png')
    if not got:
        texts = [b.inner_text().strip().replace(chr(10),' ')[:28] for b in page.locator('button').all()]
        print('route buttons:', texts[:40])
    browser.close()

print('errors:', errors if errors else 'NONE')
