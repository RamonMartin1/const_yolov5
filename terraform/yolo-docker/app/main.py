import os
import sys
import urllib.request

import torch
# from datetime import date
from fastapi import FastAPI
from fastapi import Response
# from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image

dir_path = os.path.dirname(os.path.realpath(__file__))
print(f'python file is in: {dir_path}')
cwd = os.getcwd()
print(f'current working dir is: {cwd}')

@torch.no_grad()
def run():
    """
    get pytorch model
    """
    try:
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
    except:
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='app/best.pt')
    return model

app = FastAPI()
model = run()

# tmp_files = os.listdir('/tmp')
# if not 'dataframes' in tmp_files:
#     os.mkdir('/tmp/dataframes')

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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

    res = labels.to_json(orient="records")
    return Response(content=res, media_type="application/json")
    # return JSONResponse(content=res)

#working fine as web server, using the following url to test: http://127.0.0.1:8000/?url=https://img.forconstructionpros.com/files/base/acbm/fcp/image/2021/04/workers_examining_work.606ddbf099d73.png

# use `uvicorn main:app --reload` to start