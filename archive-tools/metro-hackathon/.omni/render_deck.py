# -*- coding: utf-8 -*-
"""Approximate PIL renderer for the generated pptx — QA for overflow/layout."""
from pptx import Presentation
from pptx.util import Emu
from PIL import Image, ImageDraw, ImageFont
import io, os

SCALE = 96  # px per inch
W, H = int(13.333*SCALE), int(7.5*SCALE)
FONT_PATH = 'from-carbon-to-metro/assets/fonts/NotoSansCJKtc-Regular.otf'
os.makedirs('.omni/deckqa', exist_ok=True)

_fonts = {}
def F(size_pt, bold=False):
    px = max(8, int(size_pt * 96 / 72))
    key = (px, bold)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(FONT_PATH, px)
    return _fonts[key]

def emu2px(v): return int(Emu(v).inches * SCALE)

def draw_text_frame(draw, shape, overflows, slide_no):
    tf = shape.text_frame
    x, y = emu2px(shape.left), emu2px(shape.top)
    w, h = emu2px(shape.width), emu2px(shape.height)
    # margins approx
    pad_x, pad_y = 8, 4
    # gather paragraph lines with wrapping
    lines = []  # (text, font, color, align, size_pt, space_after_px)
    for p in tf.paragraphs:
        if not p.runs:
            continue
        r = p.runs[0]
        size = r.font.size.pt if r.font.size else 14
        bold = bool(r.font.bold)
        try:
            color = tuple(r.font.color.rgb) if r.font.color and r.font.color.rgb else (23,35,28)
        except Exception:
            color = (23,35,28)
        align = str(p.alignment) if p.alignment else 'LEFT'
        text = ''.join(run.text for run in p.runs)
        f = F(size, bold)
        # wrap
        avail = w - 2*pad_x
        cur = ''
        for ch in text:
            if ch in ('\n', '\r'):
                lines.append((cur, f, color, align, size, bold, 0))
                cur = ''
                continue
            if draw.textlength(cur + ch, font=f) <= avail:
                cur += ch
            else:
                lines.append((cur, f, color, align, size, bold, 0))
                cur = ch
        sa = int((p.space_after.pt if p.space_after else 4) * 96/72)
        ls = p.line_spacing if p.line_spacing else 1.12
        lines.append((cur, f, color, align, size, bold, sa))
        # apply line spacing padding roughly by adding extra to sa
    # total height
    total = sum(int(f.size*1.18) + sa for (_,f,_,_,_,_,sa) in lines)
    anchor_mid = tf.vertical_anchor is not None and 'MIDDLE' in str(tf.vertical_anchor)
    ty = y + (h - total)//2 if anchor_mid else y + pad_y
    if total > h + 6:
        overflows.append((slide_no, shape.shape_id, round(total/SCALE,2), round(h/SCALE,2), lines[0][0][:30]))
    for (text, f, color, align, size, bold, sa) in lines:
        lw = draw.textlength(text, font=f)
        if 'CENTER' in align:
            tx = x + (w - lw)//2
        elif 'RIGHT' in align:
            tx = x + w - lw - pad_x
        else:
            tx = x + pad_x
        sw = 1 if bold else 0
        draw.text((tx, ty), text, font=f, fill=color, stroke_width=sw, stroke_fill=color)
        ty += int(f.size*1.18) + sa

def render(prs_path):
    prs = Presentation(prs_path)
    overflows = []
    for i, slide in enumerate(prs.slides, 1):
        img = Image.new('RGB', (W, H), (255,247,223))
        draw = ImageDraw.Draw(img)
        for shape in slide.shapes:
            try:
                x, y = emu2px(shape.left), emu2px(shape.top)
                w, h = emu2px(shape.width), emu2px(shape.height)
            except Exception:
                continue
            if shape.shape_type == 13:  # picture
                try:
                    pim = Image.open(io.BytesIO(shape.image.blob)).convert('RGB')
                    pim = pim.resize((max(w,1), max(h,1)))
                    img.paste(pim, (x, y))
                except Exception as e:
                    draw.rectangle([x,y,x+w,y+h], outline=(200,0,0))
                continue
            # autoshape / textbox fills
            fill_rgb = None
            try:
                if shape.fill.type is not None and int(shape.fill.type) == 1:
                    fill_rgb = tuple(shape.fill.fore_color.rgb)
            except Exception:
                pass
            line_rgb, line_w = None, 0
            try:
                if shape.line.color and shape.line.color.rgb:
                    line_rgb = tuple(shape.line.color.rgb)
                    line_w = int((shape.line.width.pt if shape.line.width else 1) * 96/72)
            except Exception:
                pass
            if fill_rgb or line_rgb:
                r = int(min(w,h)*0.12)
                draw.rounded_rectangle([x,y,x+w,y+h], radius=r, fill=fill_rgb, outline=line_rgb, width=max(line_w,0) or None)
            if shape.has_text_frame and shape.text_frame.text.strip():
                draw_text_frame(draw, shape, overflows, i)
        img.save(f'.omni/deckqa/slide-{i:02d}.png')
    return overflows

ov = render('personal-auto/final-deck/從碳客變捷客_決賽簡報_v3.pptx')
print('rendered 12 slides')
print('OVERFLOWS (slide, shape, need_in, box_in, first_text):')
for o in ov: print(' ', o)
