from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def readTextFromImage(img):
    return pytesseract.image_to_string(img)

def readTextFromImages(path):
    img = Image.open(path)
    return pytesseract.image_to_string(img)
