import io
from PIL import Image
import base64


def decodedBase64StringToPNG(base64String):
    image = Image.open(io.BytesIO(base64.decodebytes(bytes(base64String, "utf-8"))))
    if image.format in ['JPEG']:
        return castJPEGtoPNG(image)
    else:
        return image


def castJPEGtoPNG(img):
    png_bytes_io = io.BytesIO()
    img.save(png_bytes_io, format='PNG')
    png_bytes_io.seek(0)
    return Image.open(png_bytes_io)
