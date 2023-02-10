import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import ExifTags


def alignImage(image):
    exif = {ExifTags.TAGS[k]: v for k, v in image._getexif().items() if k in ExifTags.TAGS}
    orientation = exif.get("Orientation", None)
    if orientation == 3:
        image = image.rotate(180, expand=True)
    elif orientation == 6:
        image = image.rotate(270, expand=True)
    elif orientation == 8:
        image = image.rotate(90, expand=True)
    return image


def initImage(alignImage):
    resultIMG = preprocessIMG(alignImage)
    plt.imshow(resultIMG)
    plt.show()
    x, y, w, h = getCroppedCoordinates(resultIMG)
    cropImg = cropIMG(20, x, y, w, h, resultIMG)
    # cropIMGParts(output_path, output_path_part_1, output_path_part_2, output_path_part_3)
    return preprocessIMGToRead(cropImg)


def preprocessIMGToRead(resultIMG):
    img_np = np.array(resultIMG)
    if len(img_np.shape) == 3:
        gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    else:
        gray = img_np
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=2)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return cv2.medianBlur(thresh, 3)


def cropIMGParts(output_path, output_path_part_1, output_path_part_2, output_path_part_3):
    img = cv2.imread(output_path)
    height, width, channels = img.shape
    cropped_part1 = img[0:0 + height, 0:int(width // 3.5)]
    cv2.imwrite(output_path_part_1, cropped_part1)
    cropped_part2 = img[0:0 + height, int(width // 3.3):int(width // 3 * 2)]
    cv2.imwrite(output_path_part_2, cropped_part2)
    cropped_part3 = img[0:0 + height, int(width // 3 * 1.7):width]
    cv2.imwrite(output_path_part_3, cropped_part3)


def cropIMG(puffer_x, x, y, w, h, resultIMG):
    x = x - puffer_x
    cropped = resultIMG[y:y + h, x:x + w]
    plt.imshow(cropped)
    plt.show()
    return cropped


def preprocessIMG(alignImage):
    img_np = np.array(alignImage)
    gray = cv2.cvtColor(img_np.astype('uint8'), cv2.COLOR_BGR2GRAY)
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=2)
    thresh = cv2.threshold(opening, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return cv2.medianBlur(thresh, 3)


def getCroppedCoordinates(resultIMG):
    contours, _ = cv2.findContours(resultIMG, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    resultContours = []
    min_x = 9999999;
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if h > 200 or w > 500:
            resultContours.append(cnt)
        if min_x > x:
            min_x = x
    x, y, w, h = cv2.boundingRect(sorted(resultContours, key=cv2.contourArea, reverse=True)[0])
    return min_x, y, (x + w), (y + h)


def plotImage(img):
    plt.imshow(img)
    plt.show()
