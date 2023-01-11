import os
import urllib.request

import torch
# from datetime import date
from fastapi import FastAPI
from PIL import Image

@torch.no_grad()
def run():
    """
    get pytorch model
    """
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
    return model

app = FastAPI()
model = run()

tmp_files = os.listdir('/tmp')
if not 'dataframes' in tmp_files:
    os.mkdir('/tmp/dataframes')

@app.get("/")
def main(url: str):
    """
    input: url of jpg
    output: json of the results
    """
    # today = str(date.today())
    # didn't include file extension, works with png, jpg etc.
    urllib.request.urlretrieve(url, '/tmp/pic')
    img = Image.open('/tmp/pic')
    labels = model(img).pandas().xyxy[0]

    # output images and labels, needs to be redirected to s3 or whatever
    # model(img).save(save_dir = '/tmp/data/labelled')
    # labels.to_csv('/tmp/dataframes/results.csv')

    return labels.to_json(orient="records")

#working fine as web server, using the following url to test: http://127.0.0.1:8000/?url=https://img.forconstructionpros.com/files/base/acbm/fcp/image/2021/04/workers_examining_work.606ddbf099d73.png

# use `uvicorn main:app --reload` to start