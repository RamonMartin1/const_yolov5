
import torch
import pandas as pd

def run():
  model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
  model.load_state_dict(torch.load('./best.pt'))
  img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

  # Inference
  results = model(img)

  # Results
  results.print()  # or .show(), .save(), .crop(), .pandas(), etc.

run()