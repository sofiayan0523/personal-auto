import json
html = open('.omni/prod_demo.html', encoding='utf-8').read()
tag = '<script type="__bundler/template">'
ts = html.index(tag) + len(tag); te = html.index('</script>', ts)
t = json.loads(html[ts:te])
for kw in ['每一次通勤，都是可驗證的減碳資產', 'LIVE 即時事件流', '資料指紋已封存', 'Human Truth. Machine Proof.', '既有廠商 ·', '臺北捷運各站分時進出量', '#0B7A75', '#0C6B4F']:
    print(kw[:24], '=>', t.count(kw))
root = open('.omni/prod_root.html', encoding='utf-8').read()
print('root size:', len(root), '| android link ok:', 'tw.com.trtc.is.android05' in root)
