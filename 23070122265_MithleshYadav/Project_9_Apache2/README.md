# Project 9 - Apache2 Server using Kubernetes

## Objective

Create an Apache2 web server inside a Kubernetes Deployment and access it from the host machine using Kubernetes commands.

## Architecture

Host Machine / Browser
        |
        v
Kubernetes NodePort Service
        |
        v
apache2-deployment
        |
        v
Apache2 Pod
        |
        v
httpd:2.4

## Technology Stack

- Kubernetes
- Minikube
- Docker
- Apache HTTP Server
- PowerShell

## Kubernetes Resources

### Deployment

Name: apache2-deployment
Replicas: 1
Image: httpd:2.4
Container Port: 80

### Service

Name: apache2-service
Type: NodePort
Service Port: 80
NodePort: 32500

## Project Structure

Project_9_Apache2/
|
|-- apache2-deployment.yaml
|-- apache2-service.yaml
`-- README.md

## Deployment Commands

Start Minikube:

minikube start --driver=docker

Apply Deployment:

kubectl apply -f apache2-deployment.yaml

Apply Service:

kubectl apply -f apache2-service.yaml

## Verification Commands

Check Deployment:

kubectl get deployment apache2-deployment

Check Pod:

kubectl get pods -l app=apache2

Check Service:

kubectl get service apache2-service

Check Endpoint:

kubectl get endpoints apache2-service

## Host Machine Access

Run:

minikube service apache2-service --url

Open the generated URL in a browser.

The Apache default page displays:

It works!

This confirms that the Apache2 web server running inside the Kubernetes Pod is accessible from the host machine.

## Final Result

- Apache2 Deployment created
- Apache2 Pod running
- Kubernetes NodePort Service created
- Service connected to Pod
- Apache accessible from host machine
- Browser successfully displayed "It works!"

## Evidence

1. Project-9-Apache2-Deployment-Running.png
2. Project-9-Apache2-Host-Access.png
3. Project-9-Final-Kubernetes-Verification.png

## Author

Mithlesh Yadav

B.Tech - Computer Science & Engineering
Symbiosis Institute of Technology, Pune

## Project Status

Completed