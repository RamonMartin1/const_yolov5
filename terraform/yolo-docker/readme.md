## Commands:

put the yolov5 image and put it and `trusted_list` in ./.cache/torch/hub/

to build:
`docker build . -t rlew631/yolov5-fastapi`
to run:
`docker run -d --name yolocontainer -p 8000:8000 rlew631/yolov5-fastapi`
to stop/remove:
`docker stop yolocontainer`
`docker rm yolocontainer`
push to dockerhub:
`docker push rlew631/yolov5-fastapi:latest`