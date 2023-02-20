import matplotlib.pyplot as plt
from PIL import ExifTags
import numpy as np


def searchWhiteBlocks(whiteImage, square_coords):
    isWhiteResult = []
    for square in square_coords:
        x, y, w, h = square
        result, rate = is_white_similar(whiteImage, x, y, w, h)
        isWhiteResult.append([result, rate])
    return isWhiteResult


def is_white_similar(image, x, y, w, h):
    brightness_values = image[y:y + h, x:x + w, 0] * 0.299 \
                        + image[y:y + h, x:x + w, 1] * 0.587 \
                        + image[y:y + h, x:x + w, 2] * 0.114
    num_bright_pixels = np.count_nonzero(brightness_values > 200)
    total_pixels = w * h
    if num_bright_pixels / total_pixels >= 0.95:
        return True, num_bright_pixels / total_pixels
    else:
        return False, num_bright_pixels / total_pixels


def alignImage(image):
    exif = image._getexif()
    if exif:
        exif = {ExifTags.TAGS[k]: v for k, v in exif.items() if k in ExifTags.TAGS}
        orientation = exif.get("Orientation", None)
        if orientation == 3:
            image = image.rotate(180, expand=True)
        elif orientation == 6:
            image = image.rotate(270, expand=True)
        elif orientation == 8:
            image = image.rotate(90, expand=True)
    return image


def plotImage(image):
    plt.imshow(image)
    plt.show()
