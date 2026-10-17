# -*- coding: utf-8 -*-
import zipfile, hashlib, os
z = zipfile.ZipFile('offline/from-carbon-to-metro-offline.zip')
mismatch = []
for n in z.namelist():
    rel = n.split('from-carbon-to-metro/', 1)[-1]
    if os.path.isfile(rel):
        a = hashlib.sha256(z.read(n)).hexdigest()
        b = hashlib.sha256(open(rel,'rb').read()).hexdigest()
        if a != b:
            mismatch.append(rel)
print('mismatched vs repo:', mismatch if mismatch else 'NONE')
