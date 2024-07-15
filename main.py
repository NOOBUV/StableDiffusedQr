import gradio as gr
from summarize import summarize
from getLogo import getLogoColors
from promptGen import getPrompt
from diffuse import generate
# from qrReader import read_qr_code
from uniqode import get_shorten_url
from refine import fixer
from urls import urls
from urllib.parse import urlparse
from urllib import request
# import openpyxl
# import boto3,uuid,os
# import concurrent.futures

def Url(url):
    try:
        urlBase = 'https://' + urlparse(url).netloc
        urlArr = url.split("/")
        arrLen = len(urlArr)
        if arrLen >= 5:
            summaryUrl = "/".join(urlArr[:5])
            # print("Summary URL: ", summaryUrl)
            summary = summarize(summaryUrl)
        else:
            summary = summarize(url)
        # print("Summary: ", summary)
        logoColors = getLogoColors(urlBase)
        summary = fixer(urlArr, urlBase, summary)
        # print("Summary after fixing: ", summary)
        prompt = getPrompt(summary,logoColors)
        short_url = get_shorten_url(url)
        # qr_codes = generate(short_url, prompt)

        # Transfer files to S3 bucket
        # print("qr_codes of ", url)
        # qr_arr = []
        # scannableArr = []
        # s3 = boto3.client('s3','us-east-1',aws_access_key_id = os.getenv('aws_access_key_id'),aws_secret_access_key = os.getenv('aws_secret_access_key'))
        # uuid_str = str(uuid.uuid4())
        # for index,qr_url in enumerate(qr_codes):
        #     naming = urlparse(url).hostname + "-" + str(index) + '.png'
        #     local_file, headers = request.urlretrieve(qr_url, naming)
        #     scannable = read_qr_code(local_file,short_url)
        #     # print("Image " + str(index) + " is scannable: " + str(scannable))
        #     uniqueName = 'gen_ai_qr_codes/' + uuid_str + "/" + urlparse(url).hostname + "-" + str(index) + '.png'
        #     try:
        #         s3.upload_file(local_file, "beacostac-forms-api-qa", uniqueName, ExtraArgs = {
        #                 'ACL': 'public-read',  
        #                 'ContentType': 'image/png',  
        #                 'ContentDisposition': f'attachment;filename={naming}'
        #             })
        #         os.remove(local_file)
        #     except Exception as e:
        #         print(e)
        #     scannableArr.append(scannable)
        #     qr_arr.append('https://beacostac-forms-api-qa.s3.amazonaws.com/gen_ai_qr_codes/' + uuid_str + "/" + urlparse(url).hostname + "-" + str(index) + '.png')
        
        # return url, summary, logoColors, prompt, qr_arr, scannableArr
        return summary,prompt,str(logoColors)
    except Exception as e:
        print(e, "Exception for url: ", url)
# ans = urls
# arr = ans.split("\n")
# urls = arr[1:-1]
# with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
#     futures = [executor.submit(Url, web_url) for web_url in urls]

#     qr_messages = []
#     for future in concurrent.futures.as_completed(futures):
#         try:
#             (web_url, summary, colors, prompt, qrcodes, scannableArr) = future.result()
#             qr_message = {}
#             qr_message['URL'] = web_url
#             qr_message['Summary'] = summary
#             qr_message['LogoColors'] =  str(colors)
#             qr_message['Prompt'] = prompt
#             for index,scannable in enumerate(scannableArr):
#             for index,qr in enumerate(qrcodes):
#             qr_messages.append(qr_message)
#                 qr_message['image ' + str(index)] = qr
#             pass
#                 qr_message['scannable ' + str(index)] = scannable
#         except Exception as e:
# # print(qr_messages)
# workbook = openpyxl.Workbook()

# # Get the active worksheet
# worksheet = workbook.active

# # Write the header row
# header = list(qr_messages[0].keys())
# worksheet.append(header)

# # Write data rows
# for row_data in qr_messages:
#     row_values = list(row_data.values())
#     worksheet.append(row_values)

# # Save the workbook to a new file
# workbook.save('output.xlsx')
demo = gr.Interface(
        fn = Url,
        inputs = ["text"],
        outputs = ["text","text","text"],
)
demo.launch()