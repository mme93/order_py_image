import io
from PIL import Image
import base64


def decodedBase64String(base64Image):
    return Image.open(io.BytesIO(base64.decodebytes(bytes(base64Image, "utf-8"))))
