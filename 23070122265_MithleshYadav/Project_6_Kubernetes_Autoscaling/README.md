\# Project 6 – Social Media Application Kubernetes Autoscaling



\## Objective



To deploy a Social Media application on Kubernetes and demonstrate application scalability using Horizontal Pod Autoscaler (HPA).



\## Technologies Used



\- Python

\- Flask

\- Docker

\- Kubernetes

\- Minikube

\- Metrics Server

\- Horizontal Pod Autoscaler (HPA)



\## Application



The application provides:



\- Health check API

\- Social media posts API

\- CPU-load endpoint for autoscaling demonstration



\## Kubernetes Components



\### Deployment



The application is deployed using:



\- 2 minimum replicas

\- Docker image: `social-media-app:1.1`

\- CPU request: `100m`

\- CPU limit: `500m`



\### Service



A Kubernetes NodePort Service exposes the application:



\- Service Port: `80`

\- Target Port: `5001`

\- NodePort: `30080`



\### Horizontal Pod Autoscaler



HPA configuration:



\- Minimum replicas: `2`

\- Maximum replicas: `5`

\- CPU target: `50%`



\## Autoscaling Demonstration



The application was subjected to CPU load using the `/api/load` endpoint.



Observed behavior:



```text

Normal load

2 Pods

&#x20;  ↓

High CPU load

CPU reached approximately 283%

&#x20;  ↓

HPA scaled

2 Pods → 5 Pods

&#x20;  ↓

Load stopped

&#x20;  ↓

HPA scaled down

5 Pods → 2 Pods

