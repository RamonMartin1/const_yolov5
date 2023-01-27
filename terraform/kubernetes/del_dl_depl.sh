#!/bin/bash
#delete the deployment and load balancer
kubectl delete deployment yolov5-api
kubectl delete service lb-service
#download the latest model from dockerhub
minikube ssh docker pull rlew631/yolov5-fastapi:latest
#deploy
kubectl create -f ./yolov5-fastapi.yaml
#show running pods
kubectl get pods
#set up port forwarding
kubectl port-forward service/lb-service 3000 &
kubectl port-forward service/lb-service 8000 &
