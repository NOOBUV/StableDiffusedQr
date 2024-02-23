from summarize import summarize
from getLogo import getLogoColors
from promptGen import getPrompt
from diffuse import generate

def Url(url):
    summary = summarize(url)
    logoColors = getLogoColors(url) 
    prompt = getPrompt(summary,logoColors)
    qr_codes = generate(url, prompt)
    return summary, logoColors, prompt, qr_codes[0], qr_codes[1], qr_codes[2], qr_codes[3]


images = Url("https://www.google.com")

print(images)