import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
# Make sure to set the tesseract_cmd to the path where Tesseract-OCR is installed
# For example, on Windows it might be:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# On Linux, it might be:
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def read_image_text(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)
        
        # Print the extracted text
        print("Extracted Text:\n", text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Take image file path as input
    image_path = input("csmt_masjid.jpeg" )
    read_image_text(image_path)
