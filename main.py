import gradio as gr
from summarize import summarize
from getLogo import getLogoColors
from promptGen import getPrompt
from diffuse import generate

# get url from here
# pass url to info extractor + logo extractor
def Url(url):
    summary = summarize(url)
    logoColors = getLogoColors(url) 
    print(summary + "\n" + str(logoColors))
    prompt = getPrompt(summary,logoColors)
    qr_codes = generate(url, prompt)
    return qr_codes

demo = gr.Interface(
        fn = Url,
        inputs = ["text"],
        outputs = ["image","image","image","image"],
)
demo.launch()