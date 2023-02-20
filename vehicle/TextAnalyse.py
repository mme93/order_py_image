import pytesseract
import json

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def readTextFromImage(img):
    return removeNextLine(pytesseract.image_to_string(img))


def removeNextLine(text):
    text = text.replace("\n", " ").replace("|", "").replace("«", "")
    return text.strip()


def createVehicleJson():
    return json.dumps({
        "kennzeichen": 'Test',
        "vorname": 'Test',
        "nachname": 'Test',
        "adress": 'Test',
        "FIN": 'Test',
        "kilowatt": 'Test',
        "reifen": 'Test',
        "erstzulassung": 'Test',
        "krafstoff": 'Test',

    })
