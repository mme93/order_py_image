import base64
import io

from PIL import Image, ExifTags
from flask import Flask, request
from flask_cors import CORS
import json
import image.ImageWorker as iw
import image.ImageWorkerOnlyFileType as iwoft
import image.Base64Worker as b64
import image.TextAnalyse as ta

app = Flask(__name__)
CORS(app, origins=['http://localhost:4200'])


@app.route('/readImage', methods=['POST'])
def readImage():
    try:
        input_path = 'assets\\download\\example_one.jpg'
        output_path = 'assets\\result\\out_put.jpg'
        output_path_part_1 = 'assets\\result\\out_put_part1.jpg'
        output_path_part_2 = 'assets\\result\\out_put_part2.jpg'
        output_path_part_3 = 'assets\\result\\out_put_part3.jpg'
        data = request.get_json()
        file_path = data.get('file_path')
        file_content = data.get('file_content')
        iw.initImage(input_path, output_path, output_path_part_1, output_path_part_2, output_path_part_3)
        return ta.readTextFromImage(output_path_part_1), 200
    except Exception as e:
        # code that will be executed if any exception is raised
        print(f"An error occurred: {e}")
        return e, 404


@app.route('/upload', methods=['POST'])
def upload_image():
    text = ta.readTextFromImages(iwoft.initImage(request.files['image']))
    print(text)
    return text, 200


@app.route("/base64", methods=["POST"])
def image():
    alignImage = iw.alignImage(b64.decodedBase64String(request.data.decode("utf-8").split(",")[1]))
    info = ta.readTextFromImage(iw.initImage(alignImage))
    data = {"info": info}
    return json.dumps(data)


@app.route('/')
def hello_world():  # put application's code here
    return 'Services is alive...', 200


if __name__ == '__main__':
    app.run()
