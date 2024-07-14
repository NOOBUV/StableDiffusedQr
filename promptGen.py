import openai
import os
from dotenv import load_dotenv
from Instructions import instructions

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def getPrompt(summary,colors):
    text = "website info: " + summary + "\n" + "colors: " + str(colors[:3])
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo-16k",
        messages = [
            {"role" : "system", 
             "content": instructions},
            {"role" : "user", "content": text}
        ],
        temperature=0.1,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    prompt = response.choices[0].message.content
    content = prompt
    if prompt.startswith("Prompt:"):
        content = prompt.split("Prompt:")[1].strip()
    # print("prompt: ", content)
    return content
