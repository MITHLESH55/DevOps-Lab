# Project 10 — Docker Volumes & Data Persistence

## Aim
To implement Docker volume-based data persistence for a containerized Flask application.

## Objective
- Build a Flask application using Docker.
- Create and use a named Docker volume.
- Mount the volume to /app/data.
- Store application logs outside the container filesystem.
- Verify that data persists after container deletion and recreation.

## Technologies Used
- Docker
- Docker Engine
- Docker Volumes
- Python
- Flask
- PowerShell

## Project Structure

Project_11_Docker_Volumes/
+-- app.py
+-- Dockerfile
+-- requirements.txt
+-- README.md

## Implementation

The Flask application writes timestamped greeting records to:

/app/data/greeting_log.txt

A named Docker volume is mounted using:

project11_data:/app/data

## Docker Commands

### Build Image

docker build -t project11-flask:v1 .

### Create Volume

docker volume create project11_data

### Run Container

docker run -d --name project11-container -p 5001:5001 -v project11_data:/app/data project11-flask:v1

### Verify Container

docker ps

### Verify Volume

docker volume inspect project11_data

### Verify Mount

docker inspect project11-container --format "{{json .Mounts}}"

## Persistence Verification

1. Start the container.
2. Access the Flask application at http://localhost:5001.
3. Generate a greeting log entry.
4. Remove the container.
5. Recreate a new container using the same project11_data volume.
6. Access the application again.
7. Verify that the previous timestamped log entries are still available.

## Result

The Docker volume successfully persisted application data independently of the container lifecycle. The previously generated greeting log remained available after the original container was removed and a new container was created using the same named volume.

## Evidence

- SS-01_Project11_Files_Setup.png
- SS-02_Project11_Docker_Image_Build.png
- SS-03_Project11_Volume_Container_Run.png
- SS-04_Project11_Data_Persistence.png

