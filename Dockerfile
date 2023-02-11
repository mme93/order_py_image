FROM python:3.9.5

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install tesseract-ocr -y
RUN apt-get install tesseract-ocr-eng -y


COPY . .

EXPOSE 4999

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]