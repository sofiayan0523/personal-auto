from playwright.sync_api import sync_playwright

BASE = 'https://98f4b517.from-carbon-metro-vote.pages.dev'
OUT = '/home/workspaces/conversations/78ecb4fc-f4f7-400d-a996-e2454cc37674/.omni/shots'
errors = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
    page = browser.new_page(viewport={'width': 1280, 'height': 950})
    page.on('pageerror', lambda e: errors.append('pageerror: ' + str(e)))
    page.goto(BASE + '/demo/', timeout=60000)
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(6000)
    page.locator('button', has_text='路線').last.click()
    page.wait_for_timeout(600)
    info = page.evaluate("""() => {
      const txt = document.body.innerText;
      const has = ['黑潮咖啡','美廉社','誠品生活','QB HOUSE'].map(n => n + ':' + txt.includes(n));
      const clickables = [...document.querySelectorAll('[onclick], button')].filter(x => /美廉社|黑潮|誠品|QB/.test(x.textContent) && x.textContent.length < 600).map(x => x.tagName + '|' + x.textContent.replace(/\\s+/g,' ').slice(0,60));
      return { has, clickables: clickables.slice(0,10) };
    }""")
    print(info)
    # click via dispatch on the smallest element containing 美廉社
    ok = page.evaluate("""() => {
      const all = [...document.querySelectorAll('div')].filter(x => x.textContent.includes('美廉社'));
      if (!all.length) return 'none';
      let smallest = all.reduce((a, b) => a.textContent.length <= b.textContent.length ? a : b);
      // climb up to nearest element with onclick handler (React synthetic: just click)
      smallest.click();
      return 'clicked:' + smallest.textContent.replace(/\\s+/g,' ').slice(0,40);
    }""")
    print(ok)
    page.wait_for_timeout(700)
    ok2 = page.evaluate("""() => {
      const b = [...document.querySelectorAll('button')].find(x => x.textContent.includes('使用捷運點兌換此券'));
      if (b) { b.click(); return true; } return false;
    }""")
    print('redeem clicked:', ok2)
    page.wait_for_timeout(900)
    print('fingerprint visible:', page.evaluate("() => document.body.innerText.includes('資料指紋已封存')"))
    page.screenshot(path=f'{OUT}/p4-voucher-modal3.png')
    browser.close()

print('errors:', errors if errors else 'NONE')
