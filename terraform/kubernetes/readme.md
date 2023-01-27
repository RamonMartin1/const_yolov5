# Captain's log:
- kubernetes is working locally when running the deployment shell script.
- the frontend calls "localhost" for back end api calls. This needs to be fixed for test env
- does not work well or consistently when accessing across LAN

## To run on k8s:
download image from dockerhub (will time out otherwise): `minikube ssh docker pull rlew631/yolov5-fastapi:latest`
deploy: `kubectl create -f yolov5-fastapi.yaml`
set up port forwarding: `kubectl port-forward service/yolov5-api-svc 8000`
go to http://localhost:8000/?url=https://www.ishn.com/ext/resources/hi-vis-supply-construction-site.jpg?1617734295 in browser

if minikube isn't ruinning: `minikube start`

to see running pods: `kubectl get pods`
deployments: `kubectl get deployments`
and: `kubectl get services` ; `kubectl get rc`

to delete deployment: `kubectl delete deployment <deployment name>`
to delete all pods: `kubectl delete --all pods`.
to delete all services: `kubectl delete --all services`
^^ might have to run those multiple times to delete ALL...