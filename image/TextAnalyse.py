import pytesseract

#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def readTextFromImage(img):
    return pytesseract.image_to_string(img)
