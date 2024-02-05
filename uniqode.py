import requests
import os
from dotenv import load_dotenv

load_dotenv()

def uniqode(url):
    uniqodeUrl = requests.post(url="https://q.api.beaconstac.com/api/2.0/qrcodes/",
                               headers = {
                                   "Authorization": f"Token {os.getenv("AUTH_TOKEN")}"
                               },
                               json = {
                                    "name": "Custom URL",
                                    "organization": "24558",
                                    "qr_type": 2,
                                    "campaign": {
                                        "content_type": 1,
                                        "custom_url": url
                                    },
                                })
    print(uniqodeUrl.content.url)
uniqode("https://www.google.com")