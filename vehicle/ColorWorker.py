import cv2
import numpy as np


def brightenImage(image):
    image = np.array(image)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    white_lower = np.array([0, 0, 200], dtype=np.uint8)
    white_upper = np.array([255, 30, 255], dtype=np.uint8)
    white_mask = cv2.inRange(hsv, white_lower, white_upper)
    image[white_mask > 0] = (255, 255, 255)
    return image

