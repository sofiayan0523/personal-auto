# -*- coding: utf-8 -*-
"""Render v6 deck for QA via the shared render_deck renderer."""
import re, types

src = open('.omni/render_deck.py', encoding='utf-8').read()
# strip the module-level invocation at the bottom
src = src.split("ov = render(")[0]
mod = types.ModuleType('rd')
exec(compile(src, 'render_deck', 'exec'), mod.__dict__)
ov = mod.render('personal-auto/final-deck/從碳客變捷客_決賽簡報_v6_精髓版.pptx')
print('rendered slides to .omni/deckqa/')
print('OVERFLOWS:', len(ov))
for o in ov:
    print(' ', o)
