# **[Stable Diffused Branded Qr] Design Document**


## **1. Introduction**

This document is an explanation of the project Stable Diffused Branded Qr, this project is an experimental project with an aim to automate the diffusion prompt that is needed to form the diffused images.
[Google Doc](https://docs.google.com/document/d/1rnjQ2Kh-AZnMhBUtN9daZyCuXjE9Ov8yp6p-eWh9KHA/edit?usp=sharing).


### **1.1 Purpose**


### The aim of this project is to generate a branded qr that is related to the website it is redirecting. Problem that is being solved with this project is automation of diffusion prompt generation that is used to generate diffused qr.


### **1.2 Scope**

Currently project is generating 4 qr images to scan (for variety), 


## **2. Project Overview**

Website is using [Gradio](https://www.gradio.app/docs/interface) as frontend. The main tech stack used is Python.
<div align="center">
  <img src="https://github.com/utkarsh-vijay/StableDiffusedQr/assets/157091515/845be1b6-4329-4459-976d-c9742a7165f8" alt="flow">
  <h3>Flow Diagram</h3>
</div>


### **2.1. Scrapping Logo**

Tool used for Scrapping Logo is api provided by Clearbit, ex: [Google Logo](https://logo.clearbit.com/https://www.google.com)


### **2.2. Extracting Colors**

[ColorThief](https://github.com/fengsp/color-thief-py) api is used to extract colors from logo images.

ColorThief gives rgb codes and then rgb codes are converted to color names using [webcolors](https://pypi.org/project/webcolors/).

Ex: [Facebook logo](https://logo.clearbit.com/https://www.facebook.com)

Output: ['dodgerblue', 'lavender', 'cornflowerblue', 'dark cyan', 'lightskyblue']


### **2.3. Summarization using langchain**

[Langchain](https://python.langchain.com/docs/get_started/introduction) is a library used to scrape and summarize documents, pdf, website, etc. Here the langchain library is used to load the url, then it is splitted into several chunks and summarized with the help of openAi api.


### **2.4. Training Gpt**

While training the gpt to give prompt for stable diffusion there are several parameters to take care. First is how would you like the chatGpt to behave when you give it some input. In our case we want it to behave like a prompt generator that generates good prompts. Hence we need to set the Temperature of api, Token Limit (to limit word, short prompts are good) and instructions.


#### **2.4.1** **Instructions**

Instructions include how the gpt should behave. Instructions i gave:

	

For full instructions you can see: [Github](https://github.com/utkarsh-vijay/StableDiffusedQr/blob/main/Instructions.py)


#### **2.4.2 Temperature**

A temperature of 0 means the responses will be very straightforward, almost deterministic.

(meaning you almost always get the same response to a given prompt).

A temperature of 1 means the responses can vary wildly.

Mastering temperature is a hit and trial method.

Temperature range: 0 - 2

Most-common range: 0 - 1


### **2.5. Qr image Diffuser**

The model that we are using to make this diffusion possible is : [Model](https://huggingface.co/DionTimmer/controlnet_qrcode)

Model deployed on replicate: [qr2ai](https://replicate.com/qr2ai/qr2ai)

Parameters to control:



* Qr_code_content: url or text to code
* Prompt: For generating stable diffused qr image
* Negative Prompt: Things to ignore while diffusing image
* Num_interference_steps: Number of diffusion steps
* Guidance_scale: Degree of how much diffuser is bounded to follow prompt (more the scale more it will follow the prompt)

    Difference between [diffusion steps and guidance_scale (cfg scale)](https://drive.usercontent.google.com/download?id=1lAVuhic6gXzoofmwZWY1UhmdRzkL1E90&export=view&authuser=0)

* Seed: Random number used to generate reproducible images
* Strength: Image strength in qr
* ControlNet_conditioning_scale: to what degree the conditioning scale should be applied to the image. 

## **3. Scope and Limitations**

There’s a lot we can do in branding the qr code further, like putting the logo in between the qr code that we are fetching above with clearbit, and a lot of fine tuning the instructions for openAi for different inputs and output.

**Current Limitations**:



* Hallucinations of gpt in generating prompt
* Produces good results but for selected websites only
* Websites don’t allow scraping hence missing summary
* Api limitation and time to boot the replicate api
* General purpose qr diffusion model

**Solutions**:



* Fine tuning prompt engineering
* Fine tuning or training diffusion model on controlled images such as of brand’s logo, or business related images to serve our purpose.
