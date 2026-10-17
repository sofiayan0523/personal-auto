from PIL import Image
import qrcode, os
os.makedirs('personal-auto/final-deck/assets', exist_ok=True)
A = 'personal-auto/final-deck/assets'

# 1. QR code for demo URL (ink on cream)
qr = qrcode.QRCode(border=2, box_size=10)
qr.add_data('https://from-carbon-metro-vote.pages.dev/demo/')
qr.make()
img = qr.make_image(fill_color='#17231c', back_color='#fffdf2').convert('RGB')
img.save(f'{A}/qr-demo.png')

# 2. crop phone area from screenshots (phone frame approx x 680-1070, y 60-950)
for src, out in [
    ('.omni/shots/prod-demo.png', 'phone-demo.png'),
    ('.omni/shots/p3-dashboard-live.png', 'phone-dashboard.png'),
    ('.omni/shots/p4-voucher-modal3.png', 'phone-voucher.png'),
]:
    im = Image.open(src)
    w, h = im.size
    crop = im.crop((672, 55, 1080, 930))
    crop.save(f'{A}/{out}')
    print(out, crop.size)

# 3. mascot
im = Image.open('from-carbon-to-metro/assets/voting/vote-submit-v2-A-mascot-768x514.png')
im.save(f'{A}/mascot.png')
print('mascot', im.size, im.mode)
