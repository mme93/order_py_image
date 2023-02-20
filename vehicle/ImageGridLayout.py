import cv2
import numpy as np


def createGridCoordinatesFromImage(image, block_w, block_h):
    height, width, channels = np.array(image).shape
    segment_width = width // block_w
    segment_height = height // block_h
    square_coords = []
    for i in range(block_w):
        for j in range(block_h):
            x = i * segment_width
            y = j * segment_height
            w = segment_width
            h = segment_height
            if i == 19:
                w = width - x
            if j == 19:
                h = height - y
            square_coords.append((x, y, w, h))
    return square_coords


def drawGrid(image, square_coords):
    image = np.array(image)
    for coords in square_coords:
        x, y, w, h = coords
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
    return image
