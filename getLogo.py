import requests

from colorthief import ColorThief
import matplotlib.pyplot as plt
import webcolors
from io import BytesIO

def closest_color(rgb):
    try:
        cname = webcolors.rgb_to_name(rgb)
        return cname
    except ValueError:
        differences = {}
        for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
            r,g,b = webcolors.hex_to_rgb(color_hex)
            differences[sum([(r - rgb[0]) ** 2,
                            (g - rgb[1]) ** 2,
                            (b - rgb[2]) ** 2])] = color_name
        return differences[min(differences.keys())]

def get_image_from_url(image_url):
    print("https://logo.clearbit.com/" + image_url)
    response = requests.get("https://logo.clearbit.com/" + image_url)
    return BytesIO(response.content)
def getLogoColors(url):
    image = get_image_from_url(url)
    colors = []
    try:
        ct = ColorThief(image)

        palette = ct.get_palette(color_count=5,quality = 1)
        colors = [closest_color(palette[i]) for i in range(5)]
    except Exception:
        pass
    # print(colors)
    # plt.imshow([[palette[i] for i in range(5)]])
    # plt.show()
    return colors