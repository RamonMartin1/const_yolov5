## To run on k8s:
download image from dockerhub (will time out otherwise): `minikube ssh docker pull rlew631/yolov5-fastapi:latest`
deploy: `kubectl create -f yolov5-fastapi.yaml`
set up port forwarding: `kubectl port-forward service/yolov5-api-svc 8000`
go to http://localhost:8000/?url=https://www.ishn.com/ext/resources/hi-vis-supply-construction-site.jpg?1617734295 in browser