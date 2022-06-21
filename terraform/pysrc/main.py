import torch
import pandas as pd
import os
from datetime import date

@torch.no_grad()
def run():
  model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt') 
  return model
  
model = run()

df = pd.DataFrame()
path = 'data/images'
pics = os.listdir(path)
for pic in pics:
  img  = path + '/' + pic

  # output dataframes
  tempdf = model(img).pandas().xyxy[0]
  tempdf['img'] = pic
  df = pd.concat([df,tempdf])

  #output images 
  model(img).save(save_dir = 'data/labelled')

today = str(date.today())
filename = today + '_results.csv'
df.to_csv(filename)
