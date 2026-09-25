# Project 5 - Containerizing Spring Boot Application and Docker Image Security

## Objective

Deploy a Spring Boot retail application using Docker and prepare the Docker image for DTR security scanning.

## Application

The application represents a retail company's web application and provides REST APIs for product information.

## Technology Stack

- Java 21
- Spring Boot 4.1.1
- Maven
- Apache Tomcat
- Docker
- Dockerfile
- Docker Trusted Registry (DTR)

## Application APIs

### Health Check

GET /api/health

Response:

Retail application is healthy

### Product List

GET /api/products

Returns the available retail products.

### Product by ID

GET /api/products/{id}

Example:

GET /api/products/1

## Build and Test

Run:

mvn clean test

Package the application:

mvn clean package -DskipTests

## Docker Image

Build:

docker build -t retail-app:1.0 .

Verify:

docker images

Image:

retail-app:1.0

## Docker Container

Run:

docker run -d --name retail-app-container -p 8081:8081 retail-app:1.0

Verify:

docker ps

Application:

http://localhost:8081

## Dockerized Application Verification

Health:

http://localhost:8081/api/health

Products:

http://localhost:8081/api/products

## DTR Security Scanning

Docker image prepared for registry scanning:

retail-app:1.0

The local environment does not currently contain a DTR/MSR server.

The image is ready to be pushed to the institution-provided DTR/registry when access is available.

### DTR Workflow

Build Application
    |
    v
Build Docker Image
    |
    v
retail-app:1.0
    |
    v
Push Image to DTR
    |
    v
DTR Repository
    |
    v
Security Scan
    |
    v
Review Results

## Evidence

1. 01-maven-build-success.png
2. 02-retail-app-build-success.png
3. 03-retail-api-health.png
4. 04-retail-api-products.png
5. 05-docker-image-build.png
6. 06-docker-container-running.png
7. 07-dockerized-retail-api.png

## Result

The Spring Boot retail application was successfully built, tested, containerized, deployed as a Docker container, and verified through REST APIs.

The Docker image is ready for DTR security scanning when the institution-provided registry is available.
