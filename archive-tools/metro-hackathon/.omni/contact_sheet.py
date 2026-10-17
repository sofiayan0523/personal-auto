from PIL import Image
def sheet(nums, out):
    imgs = [Image.open(f'.omni/deckqa/slide-{n:02d}.png').resize((640, 360)) for n in nums]
    cols = 2; rows = (len(imgs)+1)//2
    canvas = Image.new('RGB', (cols*640, rows*360), 'white')
    for i, im in enumerate(imgs):
        canvas.paste(im, ((i%cols)*640, (i//cols)*360))
    canvas.save(out)
sheet([2,4,5,6], '.omni/deckqa/sheet-a.png')
sheet([7,9,10,12], '.omni/deckqa/sheet-b.png')
sheet([13,14,15,16], '.omni/deckqa/sheet-c.png')
print('ok')
