import zipfile, hashlib, sys
z = zipfile.ZipFile('offline/from-carbon-to-metro-offline.zip')
names = z.namelist()
print('zip entries:', len(names))
for n in names:
    if n.endswith('demo/index.html') or n.endswith('index.html') or n.endswith('TESTING_STEPS.md'):
        h = hashlib.sha256(z.read(n)).hexdigest()
        print(n, h)
