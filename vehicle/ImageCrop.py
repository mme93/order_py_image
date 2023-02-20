import vehicle.TextAnalyse as ta


def cropIMGParts(cropImg):
    img = cropImg
    if len(img.shape) == 3:
        height, width, channels = img.shape
    else:
        height, width = img.shape
        channels = 1  # set number of channels to 1 for grayscale image
    kennzeichen = img[int(height / 100 * 45):int(height / 100 * 50), 0:int(width // 3.5)]
    vorname = img[int(height / 100 * 52):int(height / 100 * 60), 0:int(width // 3.5)]
    nachname = img[int(height / 100 * 65):int(height / 100 * 70), 0:int(width // 3.5)]
    adress = img[int(height / 100 * 73):int(height / 100 * 83), 0:int(width // 3.5)]
    FIN = img[int(height / 100 * 12):int(height / 100 * 16), int(width // 3.3):int(width // 3 * 2)]
    kilowatt = img[int(height / 100 * 3):int(height / 100 * 10), int(width // 3 * 2):width]
    reifen = img[int(height / 100 * 40):int(height / 100 * 50), int(width // 3 * 2):width]
    erstzulassung = img[int(height / 100 * 3):int(height / 100 * 8), int(width // 3.3):int(width // 3 * 2 * 0.666)]
    krafstoff = img[int(height / 100 * 60):int(height / 100 * 65), int(width // 3.3):int(width // 3 * 2 * 0.666)]
    return {
        "kennzeichen": ta.readTextFromImage(kennzeichen),
        "vorname": ta.readTextFromImage(vorname),
        "nachname": ta.readTextFromImage(nachname),
        "adress": ta.readTextFromImage(adress),
        "FIN": ta.readTextFromImage(FIN),
        "kilowatt": ta.readTextFromImage(kilowatt),
        "reifen": ta.readTextFromImage(reifen),
        "erstzulassung": ta.readTextFromImage(erstzulassung),
        "krafstoff": ta.readTextFromImage(krafstoff)

    }


def cropIMG(puffer_x, x, y, w, h, resultIMG):
    x = x - puffer_x
    cropped = resultIMG[y:y + h, x:x + w]
    return cropped