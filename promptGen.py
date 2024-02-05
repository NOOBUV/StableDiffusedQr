import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def getPrompt(summary,colors):
    text = "website info: " + summary + "\n" + "colors: " + str(colors[:3])
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo-16k",
        messages = [
            {"role" : "system", 
             "content": "You are a prompt generator for stable diffusion, i will provide you with website info and color palettes, if color palette is [] use sample output 8, if summary is not available use output 2.\n\nExamples of Prompt Generation:\n\nSample Input 1:\nSpotify offers a Premium subscription with a 2-month trial for ₹119/month. The subscription provides ad-free, offline, and organised music listening with various payment options and plans for individuals, students, couples, and families. Users can easily cancel or switch their plan. Prices vary for different plans in India.\n['mediumseagreen', 'honeydew', 'mediumaquamarine', 'palegreen', 'mediumaquamarine']\n\nSample Output 1:\na person messaging with his phone, standing and listening music, laughing, mediumseagreen, honeydew and mediumaquamarine color background\n\nSample Input 2:\n There is no information provided to summarise.\n['mediumseagreen', 'honeydew', 'mediumaquamarine', 'palegreen', 'mediumaquamarine']\n\nSample Output 2:\nA person messaging with phone, standing, laughing, mediumseagreen, honeydew mediumaquamarine\n\nSample Input 3:\nSnapchat is a social media platform with features like chatting, sharing stories, and watching videos. It has a business section for advertising and support, options for privacy and safety, and is available in multiple languages. There are also tools for creators and developers, and the app can be downloaded. \n['yellow', 'black', 'gainsboro', 'olivedrab', 'olivedrab']\n\nSample Output 3:\nMultiple person messaging with their phones, standing, laughing, yellow background\n\nSample Input 4:\nFacebook is a social media platform that allows users to connect and communicate with others, create accounts and pages, and access various features such as Messenger, video, marketplace, and advertising options. It also offers services, job opportunities, and developer tools. A new feature called Meta helps users predict and control their privacy settings. \n['dodgerblue', 'lavender', 'cornflowerblue', 'darkcyan', 'lightskyblue']\n\nSample Output 4:\nmultiple person messaging with their phones, standing and smiling, dodgerblue and lavender color in background\n\nSample Input 5:\nGoogle provides a range of services including images, maps, YouTube, news, Gmail, and Drive. Users can access advanced search options, change settings, and sign in to their account. The website is available in multiple languages and offers advertising and business solutions. Google prioritizes privacy and has terms of use in place.\n['seagreen', 'tomato', 'royalblue', 'orange', 'steelblue']\n\nSample Output 5:\nperson watching computer screen, sitting, seagreen, royalblue and tomato color in background\n\nSample Input 6:\nNetflix is a popular streaming service that offers a variety of movies, TV shows, and original content for a fixed monthly fee. It can be accessed on multiple devices and has parental controls for kids' profiles. Users can cancel their subscription at any time.\n['black', 'firebrick', 'red', 'maroon', 'black']\n\nSample Output 6:\nfamily sitting and watching movie together, laughing, firebrick and red color background\n\nSample Input 7:\nNetflix is a popular streaming service that offers a variety of movies, TV shows, and original content for a fixed monthly fee. It can be accessed on multiple devices and has parental controls for kids' profiles. Users can cancel their subscription at any time.\n['black', 'firebrick', 'red', 'maroon', 'black']\n\nSample Output 7:\nfamily sitting and watching television, laughing in a room, red color background \nSample Input 8:\nUniqode (formerly Beaconstac) is a trusted platform for businesses to generate and customize QR codes and digital business cards. It offers dynamic QR codes for tracking and editing, as well as enterprise-grade security measures. The platform has been highly rated by customers and offers features such as single sign-on and GDPR compliance. Uniqode also provides an anomaly detection framework for team collaboration and control, with integrations and world-class support.\n[]\nSample Output 8:\na person holding phone to capture blue and white color background\nSample Input 9:\nThere is no information provided to summarize.\n['antiquewhite', 'deeppink', 'orangered', 'crimson', 'plum']\nSample Ouput 9:\nmultiple person messaging with their phones, standing, laughing, antiquewhite and deeppink color backgroun\nSample Input 10:\nSpotify is a free music and podcast streaming service that offers features such as creating playlists, discovering new music, and a Data Saver mode. It does not require a credit card for sign up and offers job opportunities and support for artists and developers.\n[]\nSample Output 10:\nA person listening to music on their phone, smiling, with a mediumseagreen, honeydew, and mediumaquamarine color background."},
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

    return content
