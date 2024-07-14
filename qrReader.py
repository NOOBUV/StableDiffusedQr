from qreader import QReader
import cv2

def read_qr_code(image_path,url):
    # Create a QReader instance
    try:
        qreader = QReader()

        # Get the image that contains the QR code
        image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

        # Use the detect_and_decode function to get the decoded QR data
        decoded_text = qreader.detect_and_decode(image=image)
        # print("decoded_text:",decoded_text[0])
        # print("url: ",url)
        if len(decoded_text) == 0:
            return False
        return decoded_text[0] == url
    except Exception as e:
        print(e)
        return False
