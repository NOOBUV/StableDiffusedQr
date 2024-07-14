import requests
import os

def get_shorten_url(url):
    json = {
        "name": "Custom URL",
        "organization": "25635",
        "qr_type": 2,  
        "campaign": {
            "content_type": 1,
            "custom_url": url
        }
    }
    headers = {
        "Authorization": f"Token {os.getenv("AUTH_TOKEN")}"
        }
    response = requests.post("https://q.api.beaconstac.com/api/2.0/qrcodes/",headers = headers,json = json)
    return response.json()['url']