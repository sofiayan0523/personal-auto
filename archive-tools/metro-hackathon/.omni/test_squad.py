from playwright.sync_api import sync_playwright

BASE = 'https://710c8f7b.from-carbon-metro-vote.pages.dev'
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

    # scroll to squad scene
    page.locator('text=今日健康共享生活圈').first.scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.screenshot(path=f'{OUT}/squad-eggs.png')

    # complete two tasks
    for txt in ['U-Walk 補 2,000 步', 'YouBike 接駁 10 分鐘']:
        page.locator('button', has_text=txt).first.click()
        page.wait_for_timeout(500)
        try: page.locator('button', has_text='稍後').first.click(timeout=1500)
        except Exception: pass
    page.locator('text=今日健康共享生活圈').first.scroll_into_view_if_needed()
    page.wait_for_timeout(600)
    page.screenshot(path=f'{OUT}/squad-two.png')

    # complete third
    page.locator('button', has_text='U-Sport 入場運動').first.click()
    page.wait_for_timeout(500)
    try: page.locator('button', has_text='稍後').first.click(timeout=1500)
    except Exception: pass
    page.locator('text=今日健康共享生活圈').first.scroll_into_view_if_needed()
    page.wait_for_timeout(700)
    page.screenshot(path=f'{OUT}/squad-full.png')
    body = page.evaluate("() => document.body.innerText")
    for kw in ['3 / 3 夥伴', '小隊到齊', '步步', '輪輪', '汗汗']:
        print(('OK  ' if kw in body else 'MISS'), kw)

    # ME tab squad collection
    page.locator('button', has_text='我的').last.click()
    page.wait_for_timeout(600)
    page.locator('text=我的小隊').first.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    page.screenshot(path=f'{OUT}/squad-me.png')
    browser.close()

print('errors:', errors if errors else 'NONE')
