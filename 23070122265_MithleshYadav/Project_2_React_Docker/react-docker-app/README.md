# Project 2: Deploy React Application in Docker Container

## Objective

To create a React application and deploy it inside a Docker container.

## Technologies Used

- React
- Vite
- Node.js
- Docker
- Nginx

## Steps Performed

1. Created a React application using Vite.
2. Tested the application locally.
3. Created a Dockerfile.
4. Built the Docker image.
5. Created and started the Docker container.
6. Exposed the application on port 3000.
7. Verified the application in the browser.

## Docker Build

docker build -t project2-react .

## Run Container

docker run -d -p 3000:80 --name project2-react-container project2-react

## Verification

The React application was successfully deployed using Docker and accessed through localhost:3000.

PRN: 23070122265
