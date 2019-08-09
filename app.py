from collections import Counter
from PIL import Image

image = Image.open('checkerboardx.png')
# image = Image.open('checkerboardxi.png')
w, h = image.size
im = image.load()

print("Size:",w,h)

pos = []
pos1 = []
posa = []
posh = []

d = 0
for i in range(4, 480, 16):
    c = 0
    b = 0 # black counter
    for j in range(4, 480, 16):
        rgb = im[i, j]
        print(d, c, rgb)
        if(rgb[0]<230):
            b += 1
        if(rgb[0]==221):
            pos.append(b)
            pos1.append(b-1)
            posa.append(chr(b+97))
            posh.append(hex(b)[2])

        c += 1
    d += 1

print(pos)
print(pos1)
print(posa)
print(posh)
print("----")
print(pos[::-1])
print(pos1[::-1])
print(posa[::-1])
print(posh[::-1])