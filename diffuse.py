import replicate
import os

def generate(url, prompt):
    os.environ['REPLICATE_API_TOKEN'] = 'Set replicate api token here'
    # print("not breaking before running replicate")
    
    output = replicate.run(
        "qr2ai/qr2ai:f87bcd6dd6dc09e3e47756acd164fe0616a70d3059cf542a847579d670aaaa68",
        input={
            "qr_code_content": url,
            "prompt": prompt,
            "num_inference_steps": 40,
            "batch_size": 4,
            "guidance_scale": 13,
            "seed": 1,
            "strength": 0.9,
            "controlnet_conditioning_scale": 1.1,
            "negative_prompt": "ugly, disfigured, low quality, blurry"
        }
    )
    # print("not breaking after replicate")
    # print("output")
    # print(output)
    return output