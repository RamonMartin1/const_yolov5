import torch
import pandas as pd
import os
from datetime import date
from gcloud import storage

#from google.cloud import storage as strg


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    bucket_name = "ingestion_img_bucket"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)
    pics = []
    for blob in blobs:
      pics.append(blob.name)
    return pics

@torch.no_grad()
def run():
  model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt') 
  return model
  
def main(*args):
  model = run()

  df = pd.DataFrame()
  path = 'gs://ingestion_img_bucket'
  pics = list_blobs('ingestion_img_bucket')

  today = str(date.today())

  client = storage.Client()
  bucket = client.get_bucket('file-dump-bucket')

  for pic in pics:
    img  = path + '/' + pic

    # output dataframes
    tempdf = model(img).pandas().xyxy[0]
    tempdf['img'] = pic
    df = pd.concat([df,tempdf])

    #output images 
    model(img).save(save_dir = '/tmp/data/labelled')

  tmp_files = os.listdir('/tmp')
  if not ('dataframes' in tmp_files):
    os.mkdir('/tmp/dataframes')
  
  filename = '/tmp/dataframes/' + today + '_results.csv'
  df.to_csv(filename)
  
  blob = bucket.blob(today + '.csv')
  blob.upload_from_filename(filename)

  labelled_pics = os.listdir('/tmp/data/labelled')

  # print(labelled_pics)

  bucket2 = client.get_bucket('file-dump-bucket2')
  for img in labelled_pics:
    picblob = bucket2.blob(img)
    picblob.upload_from_filename('/tmp/data/labelled/' + img)

  return "successs!!!!"
