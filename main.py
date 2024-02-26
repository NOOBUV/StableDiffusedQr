from summarize import summarize
from getLogo import getLogoColors
from promptGen import getPrompt
from diffuse import generate
from urllib.parse import urlparse

def Url(url):
    urlBase = 'https://' + urlparse(url).netloc
    print(urlBase)
    summary = summarize(urlBase)
    logoColors = getLogoColors(urlBase) 
    prompt = getPrompt(summary,logoColors)
    qr_codes = generate(urlBase, prompt)
    return summary, logoColors, prompt, qr_codes[0], qr_codes[1], qr_codes[2], qr_codes[3]


(summary, colors, prompt, *qrcodes) = Url("https://jkawfindia.in/index.php/news/")

print(qrcodes)