from PIL import Image
from io import BytesIO
import requests


def if_grey_scale(RGBA):
    if RGBA[0] == RGBA[1] == RGBA[2]:
        return True
    else:
        return False


def if_grey_scale_line(linePx):
    for px in linePx[:10]:
        if not if_grey_scale(px):
            return False
        else:
            pass
    return True


def get_line_px(image, width, heightNum):
    return [image.getpixel((i, heightNum)) for i in range(width)]

imageWeb = Image.open(BytesIO(requests.get(
    'http://www.pythonchallenge.com/pc/def/oxygen.png').content))
width, height = imageWeb.size
print(width, height)

if __name__ == '__main__':
    for h in range(height):
        if if_grey_scale(get_line_px(imageWeb, width, h)):
            print(h)
        else:
            pass
    linepx = get_line_px(imageWeb, width, 45)
    print(''.join([chr(imageWeb.getpixel((j, 47))[0])
                   for j in range(0, width, 7)]))
    print(''.join([chr(j)
                   for j in [105, 110, 116, 101, 103, 114, 105, 116, 121]]))
