from flask import Flask, request
from flask_cors import CORS
import json
import image.ImageWorker as iw
import image.Base64Worker as b64
import image.TextAnalyse as ta

app = Flask(__name__)
CORS(app)


@app.route("/base64", methods=["POST"])
def base64Image():
    alignImage = iw.alignImage(b64.decodedBase64String(request.data.decode("utf-8").split(",")[1]))
    resultImage = iw.initImage(alignImage)
    info = ta.readTextFromImage(resultImage)
    data = {"info": info}
    return json.dumps(data)


@app.route('/')
def hello_world():  # put application's code here
    return 'Services is alive...', 200


if __name__ == '__main__':
    app.run()
