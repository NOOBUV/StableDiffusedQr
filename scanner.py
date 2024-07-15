import requests
import openpyxl
from qreader import QReader
import cv2
from urllib import request
import os

def scannable(image_url,webUrl):

    qreader = QReader()

    local_file, headers = request.urlretrieve(image_url)

    image = cv2.cvtColor(cv2.imread(local_file), cv2.COLOR_BGR2RGB)

    decoded_text = qreader.detect_and_decode(image=image)
    return decoded_text[0] == webUrl


SLACK_AUTH_TOKEN = os.getenv('SLACK_AUTH_TOKEN')
CONVERSATION_ID = "C06N706QEDS"
jsonData = {
    "channel": CONVERSATION_ID,
    "limit": 1000
}

url = f"https://slack.com/api/conversations.history"

headers = {
    "Authorization": f"Bearer {SLACK_AUTH_TOKEN}"
}

dataArr = []
response = requests.post(url, headers=headers, json=jsonData)
dataArr.append(response.json())
while dataArr[-1]["has_more"]:
    jsonData["cursor"] = dataArr[-1]["response_metadata"]["next_cursor"]
    response = requests.post(url, headers=headers, json=jsonData)
    dataArr.append(response.json())

if response.status_code == 200:
    qr_messages = []
    count = 0
    for data in dataArr:
        messages = data.get("messages", [])
        for message in messages:
            try:
                if message["subtype"] == "bot_message":
                    qr_message = {}
                    try:
                        webUrl = ""
                        for i in range(4):
                            if i == 0:
                                qr_message["URL"] = webUrl = message["attachments"][i]["text"][1:-1]
                            else:
                                qr_message[message["attachments"][i]["title"]] = message["attachments"][i]["text"]
                        
                        for i in range(4,8):
                            qr_message["image"+str(i-3)] = message["attachments"][i]["image_url"]

                        for i in range(4,8):
                            qr_message["Image "+str(i-3)+"Scannable"] = scannable(message["attachments"][i]["image_url"],webUrl)

                        qr_messages.append(qr_message)
                    except Exception as e:
                        print(e)
                        pass
            except Exception as e:
                print(e)
                pass
    print(len(qr_messages),count)
    workbook = openpyxl.Workbook()

    # Get the active worksheet
    worksheet = workbook.active

    # Write the header row
    header = list(qr_messages[0].keys())
    worksheet.append(header)

    # Write data rows
    for row_data in qr_messages:
        row_values = list(row_data.values())
        worksheet.append(row_values)

    # Save the workbook to a new file
    workbook.save('output.xlsx')
    
else:
    print(f"Error: {response.status_code} - {response.text}")
