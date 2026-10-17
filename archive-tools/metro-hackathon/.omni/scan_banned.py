# -*- coding: utf-8 -*-
import re, json

html = open('demo/index.html', encoding='utf-8').read()
# decode \uXXXX escapes to visible text for scanning
decoded = html.encode('utf-8').decode('unicode_escape', errors='ignore')

banned = ['待北捷','口述','示範數據','Demo 示意','Demo示意','可變現','AI 站點','AI站點',
          'Demo Hash','搭乘模擬','工作坊','不假設','正式串接','實時','待確認','待驗證',
          'mock','TODO','FIXME','假資料','內部']
print('=== banned words in demo bundle (decoded) ===')
clean = True
for w in banned:
    n = decoded.count(w)
    if n:
        clean = False
        idx = decoded.find(w)
        print(f'{w}: {n}  ctx: ...{decoded[max(0,idx-30):idx+34]}...')
print('ALL CLEAN' if clean else 'FOUND ISSUES')

# AI wording check (visible text only — exclude code identifiers)
print('=== standalone "AI" occurrences (decoded, CJK context) ===')
hits = re.findall(r'[一-鿿][^\n]{0,20}AI[^\n]{0,20}', decoded)
for h in hits[:10]:
    print(repr(h))
print('count:', len(hits))
