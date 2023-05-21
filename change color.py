from PIL import Image
import os

walls=[f for f in os.listdir() if 'water' in f and '.png' in f]
print(walls)
for wall in walls:
    c = Image.open(wall)
    c = c.convert("RGBA")
    w, h = c.size
    cnt = 0
    for px in c.getdata():
        print(px)
        if px ==(255,255,255,255):
            c.putpixel((int(cnt % w), int(cnt / w)), (255, 255, 0, px[3]))
        cnt += 1  
    c.save('yellow_'+wall)   