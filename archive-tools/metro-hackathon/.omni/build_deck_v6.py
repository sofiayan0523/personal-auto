# -*- coding: utf-8 -*-
"""決賽簡報 v6「提案精髓版」
設計原則：
1. 敘事骨架 = proposal 自己的三句話：站點即場景 / 任務即誘因 / 成效即產品
2. 主頁 11 頁全部口語化：IFRS15/Breakage/B2B/opt-in/Ledger 等術語全數下放附錄
3. 每頁一個「大白話標題」= 講者這 35 秒要說的那句話
4. 每頁內嵌講稿備忘稿（speaker notes），總計約 6.5 分鐘
5. 附錄 3 頁（財務會計 / 四場景 / 點數機制表）供 QA 備詢，不佔 7 分鐘
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

INK   = RGBColor(0x17,0x23,0x1C)
TEAL  = RGBColor(0x0B,0x7A,0x75)
DEEP  = RGBColor(0x08,0x3C,0x37)
LEAF  = RGBColor(0x38,0xB8,0x6F)
MINT  = RGBColor(0xC8,0xF3,0xDF)
SUN   = RGBColor(0xFF,0xD3,0x4D)
COIN  = RGBColor(0xF5,0xA5,0x24)
CORAL = RGBColor(0xFF,0x6A,0x3D)
CREAM = RGBColor(0xFF,0xF7,0xDF)
PAPER = RGBColor(0xFF,0xFD,0xF2)
GREY  = RGBColor(0x6E,0x77,0x6F)
WHITE = RGBColor(0xFF,0xFF,0xFF)
FONT  = '微軟正黑體'

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
A  = 'personal-auto/final-deck/assets'
V3 = 'personal-auto/final-deck/assets/v3'

def slide_bg(s, color=CREAM):
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = color

def set_text(tf, lines, default_size=14, default_color=INK, align=PP_ALIGN.LEFT, bold=False, font=FONT, line_spacing=1.12):
    tf.word_wrap = True
    first = True
    for line in lines:
        if isinstance(line, str): line = {'t': line}
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = line.get('align', align)
        p.line_spacing = line.get('ls', line_spacing)
        p.space_after = Pt(line.get('sa', 4))
        r = p.add_run(); r.text = line['t']
        r.font.name = line.get('font', font)
        r.font.size = Pt(line.get('size', default_size))
        r.font.bold = line.get('bold', bold)
        r.font.color.rgb = line.get('color', default_color)
        rPr = r._r.get_or_add_rPr()
        ea = rPr.find(qn('a:ea'))
        if ea is None:
            ea = rPr.makeelement(qn('a:ea'), {}); rPr.append(ea)
        ea.set('typeface', line.get('font', font))

def card(s, x, y, w, h, fill=PAPER, line_color=INK, line_w=2.5, shadow=0.09, radius=0.12, shadow_color=INK):
    if shadow:
        sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x+shadow), Inches(y+shadow), Inches(w), Inches(h))
        sh.fill.solid(); sh.fill.fore_color.rgb = shadow_color
        sh.line.fill.background(); sh.shadow.inherit = False
        try: sh.adjustments[0] = radius
        except Exception: pass
    c = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    c.fill.solid(); c.fill.fore_color.rgb = fill
    c.line.color.rgb = line_color; c.line.width = Pt(line_w)
    c.shadow.inherit = False
    try: c.adjustments[0] = radius
    except Exception: pass
    return c

def chip(s, x, y, w, h, text, fill=SUN, tcolor=INK, size=12, rot=0, bold=True, line_w=2.0):
    c = card(s, x, y, w, h, fill=fill, line_w=line_w, shadow=0.05, radius=0.5)
    if rot: c.rotation = rot
    tf = c.text_frame; tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.02); tf.margin_bottom = Inches(0.02)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    set_text(tf, [{'t': text, 'size': size, 'bold': bold, 'color': tcolor, 'align': PP_ALIGN.CENTER, 'sa': 0}])
    return c

def txt(s, x, y, w, h, lines, **kw):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    set_text(tb.text_frame, lines, **kw)
    return tb

def header(s, num, title, tag=None):
    bar = card(s, 0.55, 0.42, 0.62, 0.62, fill=SUN, line_w=2.5, shadow=0.07, radius=0.25)
    tfb = bar.text_frame; tfb.vertical_anchor = MSO_ANCHOR.MIDDLE
    set_text(tfb, [{'t': str(num), 'size': 22, 'bold': True, 'align': PP_ALIGN.CENTER, 'sa': 0, 'font': 'Arial Black'}])
    txt(s, 1.4, 0.42, 9.3, 0.8, [{'t': title, 'size': 26, 'bold': True}])
    if tag:
        chip(s, 10.75, 0.5, 2.1, 0.5, tag, fill=MINT, size=12)

def footer(s, page):
    txt(s, 0.55, 7.08, 9.0, 0.35, [{'t': '從碳客變捷客 · 2026 捷運盃黑客松決賽簡報 · 想領獎金的捷客', 'size': 9, 'color': GREY}])
    txt(s, 12.2, 7.08, 0.7, 0.35, [{'t': str(page), 'size': 10, 'color': GREY, 'align': PP_ALIGN.RIGHT, 'font': 'Arial'}])

def notes(s, script):
    s.notes_slide.notes_text_frame.text = script

# ============ SLIDE 1 — 封面：提案一句話 ============
s = prs.slides.add_slide(BLANK); slide_bg(s)
card(s, 0.55, 0.55, 7.4, 6.4, fill=TEAL, line_w=3, shadow=0.12, radius=0.06)
txt(s, 1.1, 1.0, 6.4, 0.5, [{'t': '2026 捷運盃黑客松 · 決賽提案', 'size': 15, 'bold': True, 'color': MINT}])
txt(s, 1.05, 1.5, 6.6, 2.6, [
    {'t': '從碳客', 'size': 76, 'bold': True, 'color': WHITE, 'sa': 0, 'ls': 1.0},
    {'t': '變捷客', 'size': 76, 'bold': True, 'color': SUN, 'ls': 1.0},
])
hook = card(s, 1.1, 4.5, 6.1, 0.82, fill=SUN, line_w=2.5, shadow=0.08, radius=0.3)
hook.rotation = -1.5
hook.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
set_text(hook.text_frame, [{'t': '把捷運點，變成健康生活圈的入口', 'size': 20, 'bold': True, 'align': PP_ALIGN.CENTER, 'sa': 0}])
txt(s, 1.1, 5.65, 6.2, 1.1, [
    {'t': '團隊：想領獎金的捷客', 'size': 15, 'bold': True, 'color': WHITE, 'sa': 3},
    {'t': '每一次通勤，都是可驗證的減碳資產', 'size': 12.5, 'color': MINT},
])
card(s, 8.35, 1.15, 4.4, 3.5, fill=PAPER, line_w=3, shadow=0.12, radius=0.08)
s.shapes.add_picture(f'{A}/mascot.png', Inches(8.55), Inches(1.4), width=Inches(4.0))
chip(s, 8.6, 4.35, 1.7, 0.5, '決賽 10 強', fill=CORAL, tcolor=WHITE, size=13, rot=-2)
chip(s, 10.45, 4.35, 2.2, 0.5, '互動原型可玩', fill=MINT, size=13, rot=1.5)
txt(s, 8.35, 5.35, 4.5, 1.2, [
    {'t': '線上互動原型', 'size': 12, 'bold': True, 'color': GREY, 'sa': 2},
    {'t': 'from-carbon-metro-vote.pages.dev/demo/', 'size': 13, 'bold': True, 'color': TEAL, 'font': 'Consolas'},
])
footer(s, 1)
notes(s, '（30 秒）評審好，我們是「想領獎金的捷客」。我們的提案一句話：把捷運點，變成健康生活圈的入口。'
         '接下來 7 分鐘，我會講三件事：市民為什麼無感、我們怎麼讓他有感、以及北捷為什麼划算。'
         '右邊這個原型現在就在線上，掃 QR 就能玩。')

# ============ SLIDE 2 — 痛點（口語版） ============
s = prs.slides.add_slide(BLANK); slide_bg(s)
header(s, 2, '每天 207 萬人搭捷運，但 Go App 只在查路線時被想起')
stat = card(s, 0.55, 1.45, 12.2, 1.0, fill=DEEP, line_w=3, shadow=0.1, radius=0.1)
stat.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
set_text(stat.text_frame, [
    {'t': '臺北捷運平均日運量 207.4 萬人次（114 年公開營運統計）— 每一趟，其實都是一筆沒被看見的減碳貢獻', 'size': 16.5, 'bold': True, 'color': WHITE, 'align': PP_ALIGN.CENTER, 'sa': 0},
])
pains = [
    ('打開沒事做', '現在的 Go App 偏「查資訊」：查完時刻表、看完路線，就關掉了。日常通勤沒有理由再打開它。', SUN),
    ('點數放到過期', '搭車有累點，但賺了不知道去哪花、花了也沒感覺。很多捷運點就這樣安靜地過期。', COIN),
    ('減碳只是口號', '大家都知道搭捷運環保，但「我今天這趟省了多少碳」從來沒人告訴你。沒被看見，就不會變成習慣。', MINT),
]
for i, (t, d, cl) in enumerate(pains):
    x = 0.55 + i * 4.18
    card(s, x, 2.9, 3.85, 2.5, fill=PAPER, line_w=2.5, shadow=0.09)
    chip(s, x + 0.25, 3.15, 2.1, 0.55, t, fill=cl, size=15)
    txt(s, x + 0.25, 3.9, 3.4, 1.4, [{'t': d, 'size': 13, 'ls': 1.3}])
bot = card(s, 0.55, 5.75, 12.2, 1.0, fill=SUN, line_w=2.5, shadow=0.09)
bot.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
set_text(bot.text_frame, [
    {'t': '三個問題其實是同一個問題：App 沒有走進市民的日常生活。我們的答案，就從「出站的那一刻」開始。', 'size': 15.5, 'bold': True, 'align': PP_ALIGN.CENTER, 'sa': 0},
])
footer(s, 2)
notes(s, '（40 秒）台北捷運每天有 207 萬人次在搭，但 Go App 大多只在查路線的時候被打開。'
         '這帶出三個連鎖問題：第一，App 打開沒事做，查完就關；第二，點數賺了不知道去哪花，很多就放到過期；'
         '第三，減碳只是口號——沒有人告訴市民「你今天這趟省了多少碳」。'
         '這三個問題其實是同一個：App 沒有走進日常生活。我們的答案，從出站的那一刻開始。')

# ============ SLIDE 3 — 解方骨架：站點即場景 / 任務即誘因 / 成效即產品 ============
s = prs.slides.add_slide(BLANK); slide_bg(s)
header(s, 3, '我們的解法：出站那一刻，App 說一句剛好有用的話')
lead = card(s, 0.55, 1.45, 12.2, 1.0, fill=TEAL, line_w=3, shadow=0.1)
lead.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
set_text(lead.text_frame, [
    {'t': '你搭捷運出站 → App 依「這一站、這個時間、這個天氣」給一個建議 → 照著做，拿捷運點 → 北捷看得到成效', 'size': 16, 'bold': True, 'color': WHITE, 'align': PP_ALIGN.CENTER, 'sa': 0},
])
cols = [
    ('站點即場景', '推薦不是亂槍打鳥，而是回到「此站、此時、此需求」：下雨就是傘、沒電就是充電、下班時段就是運動中心。', '市民視角', MINT),
    ('任務即誘因', '走一段路、騎一段 YouBike、借一把傘，都是任務。完成就有捷運點加成或換券——點數第一次有了明確的「賺法」和「花法」。', '點數視角', SUN),
    ('成效即產品', '多少人看到、多少人走過去、多少張券被用掉——北捷全部看得到，還能把這些成效包裝成方案，賣給站內店家與合作場館。', '北捷視角', COIN),
]
for i, (t, d, tag, cl) in enumerate(cols):
    x = 0.55 + i * 4.18
    card(s, x, 2.85, 3.85, 3.35, fill=PAPER, line_w=2.5, shadow=0.09)
    chip(s, x + 0.25, 3.1, 2.3, 0.6, t, fill=cl, size=16)
    chip(s, x + 2.75, 3.15, 0.95, 0.48, tag, fill=DEEP, tcolor=WHITE, size=10.5)
    txt(s, x + 0.25, 3.95, 3.4, 2.1, [{'t': d, 'size': 13, 'ls': 1.32}])
bar = card(s, 0.55, 6.45, 12.2, 0.65, fill=PAPER, line_w=2.5, shadow=0.07)
bar.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
set_text(bar.text_frame, [{'t': '這三句話，就是整份提案的骨架。後面每一頁，都是這三句話的展開。', 'size': 13.5, 'bold': True, 'align': PP_ALIGN.CENTER, 'sa': 0}])
footer(s, 3)
notes(s, '（40 秒）我們的解法一句話：出站那一刻，App 說一句剛好有用的話。'
         '整份提案就三句骨架。第一「站點即場景」：推薦回到此站、此時、此需求——下雨給傘、沒電給充電。'
         '第二「任務即誘因」：走一段路、借一把傘都是任務，完成就有捷運點，點數第一次有了明確的賺法和花法。'
         '第三「成效即產品」：多少人來、多少券被用掉，北捷看得到，還能把成效賣給合作店家。'
         '後面每一頁，都是這三句話的展開。')

# ============ SLIDE 4 — 生態圈：全部都已經在站裡了（零新建） ============
s = prs.slides.add_slide(BLANK); slide_bg(s)
header(s, 4, '這些服務，其實都已經在捷運站裡了', tag='零新建成本')
left = card(s, 0.55, 1.5, 6.0, 4.5, fill=TEAL, line_w=3, shadow=0.1)
txt(s, 0.9, 1.75, 5.3, 4.1, [
    {'t': '市府已經在推的健康政策', 'size': 18, 'bold': True, 'color': SUN, 'sa': 8},
    {'t': '不用新談、不用新建，直接對接：', 'size': 13.5, 'bold': True, 'color': WHITE, 'sa': 8},
    {'t': '· U-Sport：進運動中心運動就集點（體育局）', 'size': 13.5, 'color': MINT, 'sa': 5},
    {'t': '· U-Walk：健康萬步走（衛生局）', 'size': 13.5, 'color': MINT, 'sa': 5},
    {'t': '· YouBike：前 30 分鐘補助的綠色接駁（交通局）', 'size': 13.5, 'color': MINT, 'sa': 10},
    {'t': '捷運點的加成，就綁在「搭捷運去運動、走路、騎車」上——這比單純折扣，更像一座城市在鼓勵你健康生活。', 'size': 13, 'color': WHITE, 'ls': 1.3},
])
right = card(s, 6.85, 1.5, 5.9, 4.5, fill=PAPER, line_w=2.5, shadow=0.1)
txt(s, 7.2, 1.75, 5.2, 4.1, [
    {'t': '站裡已經在營業的店家', 'size': 18, 'bold': True, 'color': TEAL, 'sa': 8},
    {'t': '它們本來就付租金、也本來就需要人流：', 'size': 13.5, 'bold': True, 'sa': 8},
    {'t': '· 下雨 → rainGo 共享傘（甲站借、乙站還）', 'size': 13.5, 'color': GREY, 'sa': 5},
    {'t': '· 沒電 → 旅電 / ChargeSPOT 行動電源', 'size': 13.5, 'color': GREY, 'sa': 5},
    {'t': '· 嘴饞 → 亞尼克 YTM 蛋糕機、全家、黑潮咖啡', 'size': 13.5, 'color': GREY, 'sa': 5},
    {'t': '· 空檔 → 小樹屋電話亭、快剪、快閃櫃', 'size': 13.5, 'color': GREY, 'sa': 10},
    {'t': '我們幫北捷做的，是把「租位子給它們」升級成「帶客人給它們」——這就是招商的新賣點。', 'size': 13, 'ls': 1.3},
])
bar = card(s, 0.55, 6.25, 12.2, 0.75, fill=SUN, line_w=2.5, shadow=0.08)
bar.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
set_text(bar.text_frame, [{'t': '我們不新建任何東西——只是把已經存在的政策和店家，串在市民回家的那條路上。', 'size': 15, 'bold': True, 'align': PP_ALIGN.CENTER, 'sa': 0}])
footer(s, 4)
notes(s, '（40 秒）很多提案要蓋新東西，我們相反——這些服務全部已經在站裡了。'
         '左邊是市府已經在推的健康政策：U-Sport 運動集點、U-Walk 萬步走、YouBike 接駁補助，直接對接，不用新建。'
         '右邊是站裡已經在營業的店家：共享傘、行動電源、蛋糕機、電話亭，它們本來就付租金、本來就需要人流。'
         '我們做的，是把「租位子」升級成「帶客人」。一句話：不新建任何東西，只是把它們串在市民回家的那條路上。')

# ============ SLIDE 5 — 一天的場景故事 ============
s = prs.slides.add_slide(BLANK); slide_bg(s)
header(s, 5, '一個下班的傍晚，App 只說了三句話')
steps = [
    ('17:52 · 出站，下雨了', '「4 號出口就有 rainGo 共享傘，甲站借、乙站還。順手完成今天的共享任務。」', '☔', MINT),
    ('18:05 · 走在路上', '「今天離萬步還差 2,000 步——走 8 分鐘到運動中心，這個月的減碳加成就解鎖了。」', '👟', SUN),
    ('18:40 · 準備回家', '「騎 YouBike 接駁 10 分鐘可再加成；回程站內的亞尼克蛋糕機，捷運點可以折抵。」', '🚲', COIN),
]
for i, (t, d, emo, cl) in enumerate(steps):
    y = 1.55 + i * 1.55
    card(s, 0.55, y, 8.1, 1.35, fill=PAPER, line_w=2.5, shadow=0.08)
    chip(s, 0.8, y + 0.18, 2.35, 0.5, t, fill=cl, size=13)
    txt(s, 0.85, y + 0.75, 7.0, 0.55, [{'t': d, 'size': 13.5, 'ls': 1.2}])
    txt(s, 7.85, y + 0.3, 0.7, 0.7, [{'t': emo, 'size': 26, 'align': PP_ALIGN.CENTER}])
right = card(s, 9.0, 1.55, 3.8, 4.55, fill=DEEP, line_w=3, shadow=0.1)
txt(s, 9.3, 1.8, 3.2, 4.15, [
    {'t': '每一句話背後', 'size': 16, 'bold': True, 'color': SUN, 'sa': 8},
    {'t': '用的都只是：', 'size': 13, 'bold': True, 'color': WHITE, 'sa': 6},
    {'t': '· 這一站（出站紀錄）', 'size': 13, 'color': MINT, 'sa': 4},
    {'t': '· 這個時間（下班時段）', 'size': 13, 'color': MINT, 'sa': 4},
    {'t': '· 這個天氣（正在下雨）', 'size': 13, 'color': MINT, 'sa': 4},
    {'t': '· 你自己勾選的偏好', 'size': 13, 'color': MINT, 'sa': 10},
    {'t': '不追蹤行蹤、不看消費紀錄。提醒有用，是因為時機剛好。', 'size': 12.5, 'color': WHITE, 'ls': 1.3},
])
bar = card(s, 0.55, 6.35, 12.2, 0.65, fill=SUN, line_w=2.5, shadow=0.07)
bar.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
set_text(bar.text_frame, [{'t': '雨天借傘、轉乘空檔訂電話亭、週末親子行程——同一套邏輯，可以長出幾十種站點情境。', 'size': 13.5, 'bold': True, 'align': PP_ALIGN.CENTER, 'sa': 0}])
footer(s, 5)
notes(s, '（40 秒）讓我用一個下班的傍晚說明。17:52 出站，下雨了，App 說：4 號出口有共享傘。'
         '18:05，App 說：離萬步還差兩千步，走 8 分鐘到運動中心，這個月加成就解鎖。'
         '18:40 回家前：騎 YouBike 接駁可以再加成，站內蛋糕機捷運點可折抵。'
         '重點是右邊——每句話背後用的只有：這一站、這個時間、這個天氣、加上使用者自己勾選的偏好。'
         '不追蹤行蹤、不看消費紀錄。提醒有用，是因為時機剛好。')

# ============ SLIDE 6 — 遊戲化：為什麼每天想打開 ============
s = prs.slides.add_slide(BLANK); slide_bg(s)
header(s, 6, '為什麼會每天想打開？因為有一座森林在等你', tag='內容創新')
shots = [
    (f'{V3}/story-modal-1.png', '開場故事：你的碳森林需要幫忙', 2.55, 2.56),
    (f'{V3}/phone-hatch-modal.png', '做健康任務 → 孵出夥伴', 1.90, 3.94),
    (f'{V3}/phone-forest.png', '夥伴住進森林，週日回來收成', 1.90, 3.94),
]
xs = [0.55, 3.45, 5.7]
for (img, cap, w, h), x in zip(shots, xs):
    ytop = 1.55 + (4.1 - h) / 2
    card(s, x, ytop - 0.12, w + 0.24, h + 0.24, fill=PAPER, line_w=2.5, shadow=0.09, radius=0.07)
    s.shapes.add_picture(img, Inches(x + 0.12), Inches(ytop), width=Inches(w))
    txt(s, x - 0.05, 5.85, w + 0.35, 0.6, [{'t': cap, 'size': 11, 'bold': True, 'align': PP_ALIGN.CENTER}])
panel = card(s, 8.0, 1.55, 4.8, 4.35, fill=TEAL, line_w=3, shadow=0.1)
txt(s, 8.35, 1.78, 4.15, 4.0, [
    {'t': '把減碳數字，變成養得大的東西', 'size': 16.5, 'bold': True, 'color': SUN, 'sa': 8},
    {'t': '🌲 你省下的碳，會養大一座森林', 'size': 13.5, 'bold': True, 'color': MINT, 'sa': 2},
    {'t': '每趟通勤的減碳量不再是數字，而是眼前長出來的樹。', 'size': 12, 'color': WHITE, 'sa': 7},
    {'t': '🐣 做健康任務，會孵出小夥伴', 'size': 13.5, 'bold': True, 'color': MINT, 'sa': 2},
    {'t': '騎 YouBike 孵出「輪輪」、走萬步孵出「步步」——還有各站限定的裝扮可以收集（靈感來自皮克敏）。', 'size': 12, 'color': WHITE, 'sa': 7},
    {'t': '🌱 每週日，回來收成', 'size': 13.5, 'bold': True, 'color': MINT, 'sa': 2},
    {'t': '收成種子、培育神木。一週一個小儀式，讓人固定回訪。', 'size': 12, 'color': WHITE},
])
bar = card(s, 8.0, 6.05, 4.8, 0.75, fill=SUN, line_w=2.5, shadow=0.08)
bar.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
set_text(bar.text_frame, [{'t': '點數給人「該用」的理由，森林給人「想回來」的理由。', 'size': 13, 'bold': True, 'align': PP_ALIGN.CENTER, 'sa': 0}])
footer(s, 6)
notes(s, '（40 秒）光有用還不夠，要讓人每天想打開。我們的答案是一座森林。'
         '你省下的碳會養大一座森林——減碳量不再是數字，是眼前長出來的樹。'
         '做健康任務會孵出小夥伴：騎 YouBike 孵出輪輪、走萬步孵出步步，各站還有限定裝扮可以收集，靈感來自皮克敏。'
         '每週日回來收成種子、培育神木，一週一個小儀式。'
         '一句話：點數給人「該用」的理由，森林給人「想回來」的理由。')

# ============ SLIDE 7 — Demo：不是概念，現在就能玩 ============
s = prs.slides.add_slide(BLANK); slide_bg(s)
header(s, 7, '這不是概念圖——現在手機掃了就能玩')
journey = [
    ('① 開場故事', '3 頁世界觀＋\n選常用路線', MINT),
    ('② 出站結算', '+15 點 / +0.23 kg\n雙數字動畫', SUN),
    ('③ 任務孵蛋', '健康任務充能\n夥伴孵化', COIN),
    ('④ 森林收成', '夥伴入住棲地\n週日收成種子', MINT),
    ('⑤ 花點換券', '100 點換全家券\n出示條碼核銷', SUN),
]
for i, (t, d, cl) in enumerate(journey):
    x = 0.55 + i * 1.86
    card(s, x, 1.6, 1.72, 2.5, fill=PAPER, line_w=2.5, shadow=0.09)
    chip(s, x + 0.12, 1.82, 1.48, 0.5, t, fill=cl, size=12)
    txt(s, x + 0.14, 2.5, 1.48, 1.5, [{'t': line, 'size': 11, 'ls': 1.25, 'sa': 3} for line in d.split('\n')])
qr = card(s, 10.05, 1.6, 2.75, 2.5, fill=PAPER, line_w=3, shadow=0.1, radius=0.08)
s.shapes.add_picture(f'{A}/qr-demo.png', Inches(10.35), Inches(1.78), width=Inches(2.1))
txt(s, 10.05, 3.75, 2.75, 0.4, [{'t': '掃了就能玩（免安裝）', 'size': 11, 'bold': True, 'align': PP_ALIGN.CENTER}])
b = card(s, 0.55, 4.45, 12.2, 1.35, fill=DEEP, line_w=3, shadow=0.1)
txt(s, 0.95, 4.65, 11.5, 1.0, [
    {'t': '最後一步（評審高光）：切到「北捷營運後台」——剛才在乘客端做的每個動作，即時出現在後台事件流。', 'size': 15, 'bold': True, 'color': WHITE, 'sa': 3},
    {'t': '乘客端玩到的每件事，北捷端都看得到成效——這就是「成效即產品」的實際畫面。', 'size': 13, 'color': MINT},
])
bar = card(s, 0.55, 6.1, 12.2, 0.75, fill=PAPER, line_w=2.5, shadow=0.08)
bar.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
set_text(bar.text_frame, [{'t': '3 分鐘可以走完全部動線：故事 → 出站 → 孵蛋 → 森林 → 換券 → 營運後台。備有離線版，現場網路斷了也能演示。', 'size': 13, 'bold': True, 'align': PP_ALIGN.CENTER, 'sa': 0}])
footer(s, 7)
notes(s, '（35 秒）這些不是概念圖。掃這個 QR，手機上現在就能玩，免安裝。'
         '3 分鐘走完全部：開場故事、出站結算、任務孵蛋、森林收成、花點換券。'
         '最後一步是評審高光：切到北捷營運後台，剛才在乘客端做的每個動作，即時出現在後台的事件流——'
         '這就是「成效即產品」的實際畫面。我們也準備了離線版，現場網路斷了照樣能演。')

# ============ SLIDE 8 — 北捷為什麼要做：三方各拿所需 ============
s = prs.slides.add_slide(BLANK); slide_bg(s)
header(s, 8, '北捷為什麼要做？因為三方各拿到自己要的')
wins = [
    ('市民', '在對的時機收到有用的提醒；點數有地方賺、有地方花；自己的減碳第一次被看見。', '「原來我省了這麼多碳」', MINT),
    ('北捷', 'App 從查詢工具變成天天打開的生活入口；點數活起來；招商時多了「帶客人」這個新賣點。', '「租位子」升級成「帶客人」', SUN),
    ('店家與場館', '客人剛好在最需要的時刻走到門口；花的每一筆行銷費，都看得到多少人來、多少券被用掉。', '看得到成效，才願意付費', COIN),
]
for i, (t, d, q, cl) in enumerate(wins):
    x = 0.55 + i * 4.18
    card(s, x, 1.55, 3.85, 3.3, fill=PAPER, line_w=2.5, shadow=0.09)
    chip(s, x + 0.25, 1.8, 1.6, 0.6, t, fill=cl, size=16)
    txt(s, x + 0.25, 2.6, 3.4, 1.6, [{'t': d, 'size': 13, 'ls': 1.3}])
    chip(s, x + 0.25, 4.15, 3.35, 0.5, q, fill=DEEP, tcolor=WHITE, size=11.5)
sell = card(s, 0.55, 5.2, 12.2, 1.55, fill=TEAL, line_w=3, shadow=0.1)
txt(s, 0.95, 5.4, 11.5, 1.2, [
    {'t': '北捷因此多了四種可以「賣」的方案：', 'size': 14.5, 'bold': True, 'color': SUN, 'sa': 4},
    {'t': '① 站內店家推播導客包　② 租賃空間導客包（電話亭/快閃櫃/快剪）　③ 健康任務共創包（與市府場館）　④ 悠遊付生活圈擴充包（第二階段）', 'size': 13, 'color': WHITE, 'ls': 1.3},
])
footer(s, 8)
notes(s, '（40 秒）北捷為什麼要做？因為三方各拿到自己要的。'
         '市民：提醒有用、點數有地方花、減碳第一次被看見。'
         '北捷：App 變成天天打開的生活入口，招商多了「帶客人」這個新賣點。'
         '店家與場館：客人剛好走到門口，行銷費看得到成效。'
         '也因為成效看得到，北捷多了四種可以賣的方案：店家推播包、租賃導客包、健康共創包，以及第二階段的悠遊付擴充包。')

# ============ SLIDE 9 — 錢算得過來 ============
s = prs.slides.add_slide(BLANK); slide_bg(s)
header(s, 9, '錢，算得過來', tag='首年試算')
nums = [('合作方付的錢（收入）', 'NT$ 2,270 萬', TEAL), ('點數回饋＋維運（支出）', 'NT$ 1,525 萬', COIN), ('可支應營運餘額', 'NT$ 745 萬', LEAF)]
for i, (label, val, cl) in enumerate(nums):
    x = 0.55 + i * 4.18
    card(s, x, 1.55, 3.85, 1.7, fill=PAPER, line_w=2.5, shadow=0.1)
    txt(s, x + 0.3, 1.75, 3.3, 0.45, [{'t': label, 'size': 13.5, 'bold': True, 'color': GREY}])
    txt(s, x + 0.3, 2.2, 3.3, 0.9, [{'t': val, 'size': 28, 'bold': True, 'color': cl, 'font': 'Arial Black'}])
box = card(s, 0.55, 3.5, 7.9, 3.2, fill=DEEP, line_w=3, shadow=0.1)
txt(s, 0.95, 3.75, 7.2, 2.8, [
    {'t': '三個讓財務放心的設計', 'size': 16.5, 'bold': True, 'color': SUN, 'sa': 8},
    {'t': '① 點數的錢主要不是北捷出：由受惠的店家與場館共同出資，北捷自己的補貼一年上限 600 萬。', 'size': 13.5, 'color': WHITE, 'sa': 6, 'ls': 1.25},
    {'t': '② 每月 5 萬的合作包，賣出 8 個就損益兩平——這是很務實的門檻。', 'size': 13.5, 'color': WHITE, 'sa': 6, 'ls': 1.25},
    {'t': '③ 任務有名額、券有張數、活動有預算上限——成本從第一天就是可控的。', 'size': 13.5, 'color': WHITE, 'sa': 6, 'ls': 1.25},
    {'t': '點數的會計處理依國際準則規劃（細節在附錄，歡迎備詢）；試算數字待北捷確認。', 'size': 11.5, 'color': MINT},
])
src = card(s, 8.75, 3.5, 4.0, 3.2, fill=PAPER, line_w=2.5, shadow=0.1)
txt(s, 9.05, 3.75, 3.5, 2.8, [
    {'t': '收入從哪裡來', 'size': 15, 'bold': True, 'color': TEAL, 'sa': 6},
    {'t': '· 20 個店家合作包：1,200 萬', 'size': 12.5, 'sa': 3},
    {'t': '· 任務回饋池合作：270 萬', 'size': 12.5, 'sa': 3},
    {'t': '· 企業永續共創案：500 萬', 'size': 12.5, 'sa': 3},
    {'t': '· App 版位與租賃加值：300 萬', 'size': 12.5, 'sa': 8},
    {'t': '合作包內容＝站點曝光＋推播＋任務設計＋核銷＋成效報表', 'size': 11.5, 'color': GREY, 'ls': 1.25},
])
footer(s, 9)
notes(s, '（40 秒）錢算得過來。首年試算：合作方付 2,270 萬，點數回饋加維運 1,525 萬，剩 745 萬營運餘額。'
         '三個讓財務放心的設計：第一，點數的錢主要不是北捷出，是受惠店家共同出資，北捷補貼一年上限 600 萬；'
         '第二，每月五萬的合作包賣出 8 個就損益兩平，門檻很務實；'
         '第三，任務有名額、券有張數，成本第一天就可控。'
         '點數會計依國際準則規劃，細節在附錄，歡迎備詢。')

# ============ SLIDE 10 — 信任與隱私 ============
s = prs.slides.add_slide(BLANK); slide_bg(s)
header(s, 10, '每一筆減碳，都經得起查')
big = card(s, 0.55, 1.5, 7.6, 3.35, fill=DEEP, line_w=3, shadow=0.1)
txt(s, 0.95, 1.75, 6.9, 2.95, [
    {'t': '就像雲端發票：', 'size': 21, 'bold': True, 'color': WHITE, 'sa': 0, 'ls': 1.15},
    {'t': '每一筆減碳與兌換，都有存證。', 'size': 21, 'bold': True, 'color': SUN, 'sa': 10, 'ls': 1.15},
    {'t': '· 個人的減碳紀錄自動封存成「自己的資產」：換手機不會丟、拿去企業或學校做永續證明也查得到。', 'size': 13.5, 'color': WHITE, 'sa': 6, 'ls': 1.28},
    {'t': '· 對北捷：點數不會重複發、減碳量不會灌水，外部稽核隨時查得動——這是全場唯一做到可查證的方案。', 'size': 13.5, 'color': MINT, 'ls': 1.28},
])
tagc = card(s, 0.55, 5.1, 7.6, 0.8, fill=PAPER, line_w=2.5, shadow=0.08)
tagc.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
set_text(tagc.text_frame, [{'t': 'Human Truth. Machine Proof. — Numbers Protocol 官方技術支持', 'size': 15, 'bold': True, 'align': PP_ALIGN.CENTER, 'sa': 0, 'font': 'Consolas'}])
ph = card(s, 8.45, 1.5, 3.0, 5.1, fill=PAPER, line_w=3, shadow=0.1, radius=0.07)
s.shapes.add_picture(f'{V3}/phone-voucher-proof.png', Inches(8.9), Inches(1.68), height=Inches(4.35))
txt(s, 8.45, 6.15, 3.0, 0.45, [{'t': '兌換券內嵌「已存證」憑證', 'size': 11, 'bold': True, 'align': PP_ALIGN.CENTER}])
pts = card(s, 0.55, 6.1, 7.6, 0.8, fill=MINT, line_w=2.5, shadow=0.07)
pts.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
set_text(pts.text_frame, [{'t': '隱私三原則：自己同意才開啟 · 只留統計不留個資 · 隨時可一鍵關閉', 'size': 13.5, 'bold': True, 'align': PP_ALIGN.CENTER, 'sa': 0}])
footer(s, 10)
notes(s, '（30 秒）最後是信任。打個比方：就像雲端發票，每一筆減碳與兌換都有存證。'
         '對市民，減碳紀錄變成自己的資產，換手機不會丟；'
         '對北捷，點數不會重複發、減碳量不會灌水，外部稽核隨時查得動——這是全場唯一做到可查證的方案，由 Numbers Protocol 提供技術支持。'
         '隱私三原則：自己同意才開啟、只留統計不留個資、隨時可關閉。')

# ============ SLIDE 11 — 落地：小步驗證，一站一站放大 ============
s = prs.slides.add_slide(BLANK); slide_bg(s)
header(s, 11, '小步驗證，一站一站放大')
phases = [
    ('第一步 · 現在', '大家看到的原型：任務、推播、換券、營運後台，全流程可演示。', '驗收點：動線 3 分鐘走完，可離線演示。', MINT),
    ('第二步 · 試辦半年', '選 2–3 個示範站點，串既有店家與市府健康政策，實測真實導客。', '驗收點：推播開啟率、到店導客數、券核銷率。', SUN),
    ('第三步 · 擴大一年', '接入悠遊付生活圈與更多場館，開放企業永續合作。', '驗收點：合作包續約率、非票務收入成長。', COIN),
]
for i, (t, d, kpi, cl) in enumerate(phases):
    x = 0.55 + i * 4.18
    card(s, x, 1.7, 3.85, 3.6, fill=PAPER, line_w=2.5, shadow=0.09)
    chip(s, x + 0.25, 1.95, 2.35, 0.58, t, fill=cl, size=14.5)
    txt(s, x + 0.28, 2.75, 3.3, 1.35, [{'t': d, 'size': 13, 'ls': 1.3}])
    kbar = card(s, x + 0.25, 4.35, 3.35, 0.72, fill=DEEP, line_w=1.8, shadow=0.05, radius=0.15)
    kbar.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    kbar.text_frame.margin_left = Inches(0.1); kbar.text_frame.margin_right = Inches(0.1)
    set_text(kbar.text_frame, [{'t': kpi, 'size': 10.5, 'bold': True, 'color': WHITE, 'sa': 0, 'ls': 1.15}])
    if i < 2:
        txt(s, x + 3.8, 3.1, 0.5, 0.8, [{'t': '→', 'size': 20, 'bold': True, 'align': PP_ALIGN.CENTER}])
bar = card(s, 0.55, 5.85, 12.2, 0.95, fill=SUN, line_w=2.5, shadow=0.08)
bar.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
set_text(bar.text_frame, [{'t': '每一步都有明確驗收點——北捷不必一次下注，用示範站的真實數字決定要不要放大。', 'size': 14.5, 'bold': True, 'align': PP_ALIGN.CENTER, 'sa': 0}])
footer(s, 11)
notes(s, '（25 秒）落地策略是小步驗證，一站一站放大。第一步就是今天的原型，動線 3 分鐘可走完；'
         '第二步試辦半年，選 2 到 3 個示範站，驗收真實的開啟率、導客數和核銷率；'
         '第三步接入悠遊付生活圈擴大。每一步都有明確驗收點——北捷不必一次下注，用示範站的數字決定要不要放大。')

# ============ SLIDE 12 — 團隊 ＋ 結尾 ============
s = prs.slides.add_slide(BLANK); slide_bg(s)
header(s, 12, '私部門技術 × 點數實戰 × 公部門政策')
team = [
    ('嚴世紀', 'Numbers Protocol', '專案總指揮。可信資料架構與存證機制——負責「每一筆減碳都經得起查」。', TEAL),
    ('鍾天傑', 'LINE Pay', '點數經濟模型與遊戲化設計——負責「點數有地方賺、有地方花」。', COIN),
    ('嚴世裕', '台北市政府地政局', '市府政策對接與行政合規——負責「健康政策串得上、審查過得了」。', LEAF),
]
for i, (name, org, role, cl) in enumerate(team):
    x = 0.55 + i * 4.18
    card(s, x, 1.7, 3.85, 3.3, fill=PAPER, line_w=2.5, shadow=0.09)
    txt(s, x + 0.3, 1.95, 3.2, 0.6, [{'t': name, 'size': 24, 'bold': True}])
    chip(s, x + 0.3, 2.75, 2.6, 0.55, org, fill=cl, tcolor=(WHITE if cl != COIN else INK), size=12.5)
    txt(s, x + 0.3, 3.55, 3.25, 1.3, [{'t': role, 'size': 12.5, 'ls': 1.35}])
close = card(s, 0.55, 5.45, 12.2, 1.4, fill=TEAL, line_w=3, shadow=0.1)
txt(s, 0.95, 5.65, 11.5, 1.05, [
    {'t': '從碳客變捷客：讓 207 萬人的每一趟通勤，都被看見、被回饋、被信任。', 'size': 17.5, 'bold': True, 'color': SUN, 'sa': 4},
    {'t': '誠實標註：碳係數採北捷座談分享之參考值（104/75/29 g/人km），正式導入時以北捷確認版本為準。', 'size': 11, 'color': MINT},
])
footer(s, 12)
notes(s, '（25 秒）這個提案需要三種能力，我們剛好湊齊：Numbers Protocol 的可信資料技術，負責每一筆減碳經得起查；'
         'LINE Pay 的點數經濟實戰，負責點數有地方賺、有地方花；市府的政策與合規經驗，負責健康政策串得上、審查過得了。'
         '結尾一句話：從碳客變捷客，讓 207 萬人的每一趟通勤，都被看見、被回饋、被信任。謝謝評審。')

# ============ 附錄 A1 — 財務與點數會計細節 ============
s = prs.slides.add_slide(BLANK); slide_bg(s, PAPER)
chip(s, 0.55, 0.45, 2.3, 0.55, '附錄 A1 · 備詢用', fill=DEEP, tcolor=WHITE, size=13)
txt(s, 3.0, 0.45, 9.0, 0.6, [{'t': '財務細目與點數會計（IFRS 15）', 'size': 22, 'bold': True}])
left = card(s, 0.55, 1.4, 6.0, 5.4, fill=CREAM, line_w=2.5, shadow=0.08)
txt(s, 0.9, 1.65, 5.3, 5.0, [
    {'t': '收入（首年試算 NT$ 2,270 萬）', 'size': 14.5, 'bold': True, 'color': TEAL, 'sa': 5},
    {'t': '· 站點健康共享合作包：20 包/月 × 5 萬 × 12 = 1,200 萬', 'size': 12, 'sa': 3},
    {'t': '· 任務回饋池合作金流：37,500 次/月 × 5 點 × 1.2 元 × 12 = 270 萬', 'size': 12, 'sa': 3},
    {'t': '· ESG／健康品牌共創：2 案 × 250 萬 = 500 萬', 'size': 12, 'sa': 3},
    {'t': '· App / Go!Map / 租賃加值版位：300 萬', 'size': 12, 'sa': 8},
    {'t': '支出（首年試算 NT$ 1,525 萬）', 'size': 14.5, 'bold': True, 'color': COIN, 'sa': 5},
    {'t': '· 任務回饋履約 225 萬 · 北捷自有補貼上限 600 萬', 'size': 12, 'sa': 3},
    {'t': '· 資料治理與報表 200 萬 · 系統維運 300 萬 · 營運客服 200 萬', 'size': 12, 'sa': 8},
    {'t': '損益兩平：含共創收入約 8 個合作包/月；不含共創約 16 包/月。', 'size': 12, 'bold': True},
])
right = card(s, 6.85, 1.4, 5.9, 5.4, fill=CREAM, line_w=2.5, shadow=0.08)
txt(s, 7.2, 1.65, 5.2, 5.0, [
    {'t': '點數會計處理（依 IFRS 15）', 'size': 14.5, 'bold': True, 'color': TEAL, 'sa': 5},
    {'t': '· 發點時列「合約負債（遞延收入）」，實際核銷或逾期失效時認列收入。', 'size': 12, 'sa': 4, 'ls': 1.25},
    {'t': '· 未兌換率（Breakage）參照 LINE POINTS、OPENPOINT 等歷史區間估算，避免虛增負債。', 'size': 12, 'sa': 4, 'ls': 1.25},
    {'t': '· 點數池由合作商家出資分攤 + 北捷年上限 600 萬補貼，形成可預算化成本結構。', 'size': 12, 'sa': 4, 'ls': 1.25},
    {'t': '· 研究底稿：LINE POINTS / OPENPOINT / 星巴克 / Marriott 之點數負債與認列實務。', 'size': 12, 'sa': 8, 'ls': 1.25},
    {'t': '所有數字為提案試算；正式收入認列、點數負債與分潤拆分，需由北捷依合約與財會規範確認。', 'size': 11.5, 'color': GREY, 'ls': 1.3},
])
txt(s, 0.55, 7.08, 9.0, 0.35, [{'t': '從碳客變捷客 · 附錄（不在 7 分鐘簡報內，供評審提問時備詢）', 'size': 9, 'color': GREY}])
notes(s, '附錄頁，不在 7 分鐘內。財務或會計評審提問時使用。')

# ============ 附錄 A2 — 四個完整場景 ============
s = prs.slides.add_slide(BLANK); slide_bg(s, PAPER)
chip(s, 0.55, 0.45, 2.3, 0.55, '附錄 A2 · 備詢用', fill=DEEP, tcolor=WHITE, size=13)
txt(s, 3.0, 0.45, 9.0, 0.6, [{'t': '四個示範場景（完整版：資料／回饋／成效）', 'size': 22, 'bold': True}])
scenarios = [
    ('A · 下班健康任務', '出站推播：「離萬步差 2,000 步，步行 9 分鐘到運動中心，完成入場解鎖本月加成。」', '資料：出站站點/時間/自選健康偏好\n回饋：捷運點加成、場館券\n成效：任務完成、步行里程、減碳量', MINT),
    ('B · 雨天共享接力', '出站遇雨推播：「本站出口有 rainGo 共享傘，甲站借乙站還，累積共享任務。」', '資料：天氣/站點/共享傘供給狀態\n回饋：共享任務章、抽獎、借傘券\n成效：曝光、租借導流、減廢敘事', SUN),
    ('C · 週末低碳生活圈', '週末模式：「捷運到大安森林公園站 + YouBike 10 分鐘 + 站內亞尼克補給。」', '資料：週末模式/興趣偏好/YouBike 站點\n回饋：完成整段行程領加成或合作券\n成效：路線完成率、點擊、換券核銷', COIN),
    ('D · 轉乘空檔服務', '35 分鐘空檔：「中山站小樹屋電話亭可預約；快閃櫃可用捷運點換券；沿線快剪低等待。」', '資料：轉乘時段/站點租賃服務/偏好\n回饋：時租券、試用券、導購任務\n成效：預約、到店、核銷、租戶導客', MINT),
]
for i, (t, d, meta, cl) in enumerate(scenarios):
    x = 0.55 + (i % 2) * 6.25
    y = 1.4 + (i // 2) * 2.75
    card(s, x, y, 5.95, 2.55, fill=CREAM, line_w=2.5, shadow=0.08)
    chip(s, x + 0.25, y + 0.2, 2.5, 0.52, t, fill=cl, size=13)
    txt(s, x + 0.25, y + 0.85, 5.4, 0.7, [{'t': d, 'size': 12, 'ls': 1.2}])
    txt(s, x + 0.25, y + 1.55, 5.4, 0.95, [{'t': line, 'size': 10.5, 'color': GREY, 'sa': 1} for line in meta.split('\n')])
txt(s, 0.55, 7.08, 9.0, 0.35, [{'t': '從碳客變捷客 · 附錄（不在 7 分鐘簡報內，供評審提問時備詢）', 'size': 9, 'color': GREY}])
notes(s, '附錄頁。評審想深入單一場景的資料邊界與成效指標時使用。')

# ============ 附錄 A3 — 點數機制五步驟與任務類型表 ============
s = prs.slides.add_slide(BLANK); slide_bg(s, PAPER)
chip(s, 0.55, 0.45, 2.3, 0.55, '附錄 A3 · 備詢用', fill=DEEP, tcolor=WHITE, size=13)
txt(s, 3.0, 0.45, 9.0, 0.6, [{'t': '點數機制：先設計行為，再決定發點', 'size': 22, 'bold': True}])
steps5 = [('① 觸發', '出站、靠近共享服務、選擇健康任務'), ('② 判斷', '站點×時間×天氣×偏好選出推薦'), ('③ 行動', '步行/騎車/借傘/預約站內服務'), ('④ 回饋', '點數加成、券、任務章（設預算上限）'), ('⑤ 衡量', '開啟率、核銷、導客 → 定價依據')]
for i, (t, d) in enumerate(steps5):
    x = 0.55 + i * 2.49
    card(s, x, 1.4, 2.31, 1.5, fill=CREAM, line_w=2.5, shadow=0.07)
    txt(s, x + 0.18, 1.55, 1.99, 0.45, [{'t': t, 'size': 14, 'bold': True, 'color': TEAL}])
    txt(s, x + 0.18, 2.0, 1.99, 0.85, [{'t': d, 'size': 10.5, 'ls': 1.2}])
rows = [
    ('健康減碳', '出站步行到 U-Sport 場館 / U-Walk 目標', '點數加成、場館券', '每月上限、活動名額', '健康資料明確授權'),
    ('共享服務', '借還共享傘/行動電源、YouBike 接駁', '任務章、折抵券、抽獎', '以券量控制，廠商分攤', '事件紀錄，MVP 用 QR'),
    ('站內補給', '亞尼克 YTM、全家、黑潮等站內消費', '點數折抵、換券', '商家購買導流方案', '只回傳核銷統計'),
    ('租賃導客', '預約電話亭、快剪、快閃櫃、取貨', '會員券、點數兌換', '廠商購買導客包', '素材經北捷審查'),
]
hdrs = ['任務類型', '使用者行為', '回饋方式', '成本控制', '資料治理']
ws = [1.7, 3.6, 2.4, 2.4, 2.1]
xcur = 0.55
for j, (h, w) in enumerate(zip(hdrs, ws)):
    card(s, xcur, 3.2, w - 0.08, 0.55, fill=DEEP, line_w=1.5, shadow=0)
    txt(s, xcur + 0.08, 3.28, w - 0.2, 0.4, [{'t': h, 'size': 11.5, 'bold': True, 'color': WHITE}])
    xcur += w
for i, row in enumerate(rows):
    y = 3.8 + i * 0.75
    xcur = 0.55
    for j, (cell, w) in enumerate(zip(row, ws)):
        card(s, xcur, y, w - 0.08, 0.68, fill=CREAM, line_w=1.2, shadow=0)
        txt(s, xcur + 0.08, y + 0.06, w - 0.2, 0.58, [{'t': cell, 'size': 10, 'ls': 1.1, 'bold': (j == 0)}])
        xcur += w
txt(s, 0.55, 7.08, 9.0, 0.35, [{'t': '從碳客變捷客 · 附錄（不在 7 分鐘簡報內，供評審提問時備詢）', 'size': 9, 'color': GREY}])
notes(s, '附錄頁。評審深究點數成本控制與資料治理邊界時使用。')

out = 'personal-auto/final-deck/從碳客變捷客_決賽簡報_v6_精髓版.pptx'
prs.save(out)
print('saved', out, '| slides:', len(prs.slides._sldIdLst))
