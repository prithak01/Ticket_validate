import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

def perform_ocr(image):
    # Convert the PIL image to a NumPy array
    image_np = np.array(image)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to preprocess the image
    threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    # Perform text extraction
    text = pytesseract.image_to_string(threshold)
    print (text)
    
    return text

# You may need to set the path to the Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# def extract_ticket_info(image_path):
#     # Load the image from the given path
#     img = Image.open(image_path)
#     # Use pytesseract to do OCR on the image
#     text = pytesseract.image_to_string(img)
#     # Parse the text to extract relevant details
#     # This is a simplified example, actual parsing will depend on the ticket format
#     ticket_info = {}
#     lines = text.split('\n')
#     for line in lines:
#         if "Ticket No" in line:
#             ticket_info['ticket_no'] = line.split(":")[1].strip()
#         elif "Date" in line:
#             ticket_info['date'] = line.split(":")[1].strip()
#         elif "Time" in line:
#             ticket_info['time'] = line.split(":")[1].strip()
#         elif "Station" in line:
#             ticket_info['station'] = line.split(":")[1].strip()
#     return ticket_info

