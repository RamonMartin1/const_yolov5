## Commands:

put the yolov5 image and put it and `trusted_list` in ./.cache/torch/hub/

`docker build . -t rlew631/yolov5-fastapi`
`docker run -d --name yolocontainer -p 8000:8000 yolov5-fastapi`
`docker push rlew631/yolov5-fastapi:latest`