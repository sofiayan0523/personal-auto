import subprocess, zipfile, hashlib, json, os

def curl(url):
    r = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code} %{size_download}', url], capture_output=True, text=True)
    return r.stdout

checks = []
# 1. production URLs
for url in ['https://from-carbon-metro-vote.pages.dev/',
            'https://from-carbon-metro-vote.pages.dev/demo/',
            'https://from-carbon-metro-vote.pages.dev/offline/from-carbon-to-metro-offline.zip',
            'https://from-carbon-metro-vote.pages.dev/assets/voting/vote-submit-ig-story-1080x1920.png']:
    checks.append((url.split('.dev')[1] or '/', curl(url)))

# 2. online TESTING_STEPS contains new features
r = subprocess.run(['curl', '-s', 'https://from-carbon-metro-vote.pages.dev/TESTING_STEPS.md'], capture_output=True, text=True)
online_ts = r.stdout
for kw in ['LIVE 即時事件流', '資料指紋已封存', '既有廠商', '2026-08-11']:
    checks.append((f'TESTING_STEPS online has "{kw}"', kw in online_ts))

# 3. online demo bundle markers
r = subprocess.run(['curl', '-s', 'https://from-carbon-metro-vote.pages.dev/demo/'], capture_output=True, text=True)
demo = r.stdout
for kw in ['LIVE 即時事件流', '每一次通勤，都是可驗證的減碳資產', 'Human Truth. Machine Proof.']:
    checks.append((f'demo online has "{kw[:18]}"', kw in demo))
checks.append(('demo old color gone', '#0C6B4F' not in demo and '#0c6b4f' not in demo))

# 4. offline zip integrity
z = zipfile.ZipFile('from-carbon-to-metro/offline/from-carbon-to-metro-offline.zip')
for name in ['demo/index.html', 'TESTING_STEPS.md', 'index.html']:
    inzip = hashlib.sha256(z.read(name)).hexdigest()
    repo = hashlib.sha256(open('from-carbon-to-metro/' + name, 'rb').read()).hexdigest()
    checks.append((f'zip {name} == repo', inzip == repo))
checks.append(('zip has LIVE feature in TESTING_STEPS', 'LIVE 即時事件流' in z.read('TESTING_STEPS.md').decode('utf-8')))

# 5. deck file
checks.append(('deck pptx exists', os.path.getsize('personal-auto/final-deck/從碳客變捷客_決賽簡報_v2.pptx')))

for k, v in checks:
    print(f'{"OK " if v else "FAIL"} | {k} | {v}')
