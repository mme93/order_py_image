from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def readTextFromImage(path):
    img = Image.open(path)
    return pytesseract.image_to_string(img)
