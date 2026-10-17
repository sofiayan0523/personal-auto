# -*- coding: utf-8 -*-
import zipfile
z = zipfile.ZipFile('offline/from-carbon-to-metro-offline.zip')
banned = ['待北捷','口述','示範數據','Demo 示意','可變現','AI 站點','Demo Hash','demo hash','搭乘模擬','工作坊']
bad = []
for n in z.namelist():
    if n.endswith(('.md','.txt','.html','.json')):
        try:
            t = z.read(n).decode('utf-8', errors='ignore')
        except Exception:
            continue
        d = t.encode().decode('unicode_escape', errors='ignore') if 'demo/index' in n else t
        for w in banned:
            if w in d:
                bad.append((n, w))
print('zip banned scan:', bad if bad else 'ALL CLEAN')
