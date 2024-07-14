import requests

from colorthief import ColorThief
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
        color = differences[min(differences.keys())]
        return color if color != 'tomato' else 'tomato-red'

def get_image_from_url(image_url):
    response = requests.get("https://www.google.com/s2/favicons?sz=128&domain_url=" + image_url)
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
    # print("colors:", colors)
    return colors