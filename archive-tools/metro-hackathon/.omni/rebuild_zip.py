# -*- coding: utf-8 -*-
import zipfile, os, hashlib

src_root = '../temp_offline_build'
out = 'offline/from-carbon-to-metro-offline.zip'

# read existing zip entry list to reproduce same structure
old = zipfile.ZipFile(out)
names = old.namelist()
old.close()

with zipfile.ZipFile(out + '.new', 'w', zipfile.ZIP_DEFLATED) as z:
    for n in sorted(names):
        p = os.path.join(src_root, n)
        if os.path.isfile(p):
            z.write(p, n)
        else:
            print('MISSING:', n, p)

os.replace(out + '.new', out)
z = zipfile.ZipFile(out)
print('entries:', len(z.namelist()))
for n in z.namelist():
    if n.endswith('demo/index.html'):
        print('zip demo sha256:', hashlib.sha256(z.read(n)).hexdigest())
h = hashlib.sha256(open('demo/index.html','rb').read()).hexdigest()
print('repo demo sha256:', h)
