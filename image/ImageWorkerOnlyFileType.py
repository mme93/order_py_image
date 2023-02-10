import cv2
import numpy as np
import image.ImageWorker as iw
import matplotlib.pyplot as plt


def initImage(image):
    image_np = np.frombuffer(image.read(), np.uint8)
    img = cv2.imdecode(image_np, cv2.IMREAD_UNCHANGED)

    plt.imshow(img)
    plt.show()
    resultIMG = preprocessIMG(img)
    x, y, w, h = getCroppedCoordinates(resultIMG)
    cropped = cropIMG(20, x, y, w, h, img)
    cropIMGParts(cropped)
    preprocessIMGs = preprocessIMGToRead(cropped)
    plt.imshow(preprocessIMGs)
    plt.show()
    return preprocessIMGs

def preprocessIMGToRead(img):
    # Bild in Graustufen umwandeln
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=2)

    # apply thresholding to binarize the image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # apply median blur to smooth the edges
    return cv2.medianBlur(thresh, 3)


def cropIMGParts(img):
    height, width, channels = img.shape
    cropped_part1 = img[0:0 + height, 0:int(width // 3.5)]
    # plt.imshow(cropped_part1)
    # plt.show()

    cropped_part2 = img[0:0 + height, int(width // 3.3):int(width // 3 * 2)]
    # plt.imshow(cropped_part2)
    # plt.show()

    cropped_part3 = img[0:0 + height, int(width // 3 * 1.7):width]
    # plt.imshow(cropped_part3)
    # plt.show()


def cropIMG(puffer_x, x, y, w, h, img):
    x = x - puffer_x
    cropped = img[y:y + h, x:x + w]
    plt.imshow(cropped)
    plt.show()
    return cropped


def preprocessIMG(img):
    # Bild in Graustufen umwandeln
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=2)

    # apply thresholding to binarize the image
    thresh = cv2.threshold(opening, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # apply median blur to smooth the edges
    return cv2.medianBlur(thresh, 3)


def getCroppedCoordinates(resultIMG):
    # Alle Konturen im Bild finden
    contours, _ = cv2.findContours(resultIMG, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    resultContours = []
    min_x = 9999999;
    # Durch die Konturen iterieren und ein rotes 5 Pixel dickes Rechteck um jedes Objekt zeichnen
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if h > 200 or w > 500:
            resultContours.append(cnt)
        if min_x > x:
            min_x = x
    # Zeichnen Sie nur die größte Kontur
    x, y, w, h = cv2.boundingRect(sorted(resultContours, key=cv2.contourArea, reverse=True)[0])
    return min_x, y, (x + w), (y + h)
