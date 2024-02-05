import gradio as gr
from summarize import summarize
from getLogo import getLogoColors
from promptGen import getPrompt
from diffuse import generate

def Url(url):
    summary = summarize(url)
    logoColors = getLogoColors(url) 
    prompt = getPrompt(summary,logoColors)
    qr_codes = generate(url, prompt)
    return qr_codes

demo = gr.Interface(
        fn = Url,
        inputs = ["text"],
        outputs = ["image","image","image","image"],
)
demo.launch()