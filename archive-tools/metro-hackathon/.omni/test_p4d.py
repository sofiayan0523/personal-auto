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
    page.locator('button', has_text='路線').last.click()
    page.wait_for_timeout(600)
    # select use-type merchant 黑潮咖啡 from list, then redeem
    sel = page.evaluate("""() => {
      const els = [...document.querySelectorAll('button, div[onclick], [role=button]')];
      const card = els.find(x => x.textContent.includes('黑潮咖啡') && x.textContent.length < 400);
      if (card) { card.click(); return card.tagName + ':' + card.textContent.slice(0, 40); }
      return null;
    }""")
    print('selected merchant via:', sel)
    page.wait_for_timeout(600)
    ok = page.evaluate("""() => {
      const btns = [...document.querySelectorAll('button')];
      const b = btns.find(x => x.textContent.includes('使用捷運點兌換此券'));
      if (b) { b.click(); return true; }
      return false;
    }""")
    print('redeem clicked:', ok)
    page.wait_for_timeout(900)
    page.screenshot(path=f'{OUT}/p4-voucher-modal2.png')
    print('fingerprint visible:', page.evaluate("() => document.body.innerText.includes('資料指紋已封存')"))
    browser.close()

print('errors:', errors if errors else 'NONE')
