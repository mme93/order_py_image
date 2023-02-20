from flask import Flask, request
from flask_cors import CORS
import vehicle.Base64Worker as b64
import vehicle.ImageGridLayout as igl
import vehicle.TextAnalyse as ta
import vehicle.ImageWorker as iw
import vehicle.ColorWorker as cw

app = Flask(__name__)
CORS(app)


@app.route("/base64", methods=["POST"])
def base64Image():
    pngImage = b64.decodedBase64StringToPNG(request.data.decode("utf-8").split(",")[1])
    square_coords = igl.createGridCoordinatesFromImage(pngImage, 50, 50)
    whiteImage = cw.brightenImage(pngImage)
    isWhite = iw.searchWhiteBlocks(whiteImage, square_coords)
    return ta.createVehicleJson(), 200


@app.route('/')
def hello_world():  # put application's code here
    return 'Services is alive...', 200


if __name__ == '__main__':
    app.run()
