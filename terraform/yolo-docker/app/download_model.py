import os
import urllib.request

import torch

@torch.no_grad()
def run():
    """
    get pytorch model
    """
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
    return model

model = run()
# torch.save(model.state_dict(), 'yolov5')
torch.save_model('const_yolov5.pth')