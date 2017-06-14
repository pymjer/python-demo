import urllib
from io import BytesIO
from PIL import Image
import requests

im = Image.open(BytesIO(requests.get(
    'http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg').content))
w, h = im.size

imgs = [Image.new(im.mode, (int(w / 2), int(h / 2))) for dummy in range(4)]
imgs_load = [i.load() for i in imgs]
org = im.load()


for i in range(w):
    for j in range(h):
        org_pos = (i, j)
        new_pos = (i // 2, j // 2)
        imgs_load[i % 2 + j % 2 * 2][new_pos] = org[org_pos]


[imgs[i].save('%d.png' % i) for i in range(4)]
