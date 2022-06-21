
import torch
import pandas as pd
from pathlib import Path

img = '/Users/ramonmartin/Documents/pytorch_projects/const_yolov5/terraform/pysrc/data/images/hd88.jpg'  # or file, Path, PIL, OpenCV, numpy, list
  

@torch.no_grad()
def run():
  model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt') 

  #model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
  #model.load_state_dict(torch.load('best.pt')['model'].state_dict())
  #model.fuse()
  #model.load_state_dict(torch.load('best.pt'))
  #img = '/Users/ramonmartin/Documents/pytorch_projects/const_yolov5/terraform/pysrc/data/images/hd88.jpg'  # or file, Path, PIL, OpenCV, numpy, list
  # Inference
  results = model(img)

  # Results
  results.save()  # or .show(), .save(), .crop(), .pandas(), etc.

run()