# Project 4 – Architecting Jenkins Pipeline for Scale

## Objective
Distribute the Maven build pipeline across two different Jenkins agent nodes.
The Compile stage runs on one agent and the Test stage runs on another agent.

## Project Structure
`	ext
Project_4_Distributed_Jenkins_Maven/
├── Jenkinsfile
├── portfolio/
└── p3 SS/
`",
",

The Jenkins pipeline uses two separate agents:

- Agent 1 – Compile: Executes the Maven compile stage.
- Agent 2 – Test: Executes the Maven test stage.

## Technologies Used
- Jenkins
- Jenkins Pipeline
- Maven
- Java
- GitHub

## Pipeline Stages
### 1. Compile
Checks out the project and executes:
`ash
mvn clean compile
`",
",

Runs the Maven test phase on the second Jenkins agent:
`ash
mvn test
`",
",

The Maven pipeline successfully distributes execution between two Jenkins agents, demonstrating scalable Jenkins pipeline execution.

## Repository
https://github.com/MITHLESH55/DevOps-Lab.git
