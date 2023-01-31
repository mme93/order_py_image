from flask import Flask, request
import webdav.WebDavWorker as wdw
import image.ImageWorker as iw
import image.TextAnalyse as ta

app = Flask(__name__)


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


@app.route('/')
def hello_world():  # put application's code here
    return 'Services is alive...', 200


if __name__ == '__main__':
    app.run()
