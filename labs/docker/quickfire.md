# Docker Fundamentals - Quickfire Questions

## Question 1
What is a Docker container?


- A) A storage volume
- B) A virtual machine
- C) A lightweight, standalone executable package containing code, runtime, libraries, and dependencies
- D) A network protocol

**Answer: C**
Containers package application code with dependencies, running as isolated processes sharing the host OS kernel.
---
## Question 2
What is the difference between a Docker image and a container?


- A) Container is read-only
- B) Image is larger
- C) They are the same
- D) Image is a template/blueprint; container is a running instance of an image

**Answer: D**
Images are immutable templates. Containers are running instances created from images with a writable layer.
---
## Question 3
What is a Dockerfile?


- A) A log file
- B) A database schema
- C) A configuration for Docker daemon
- D) A text file containing instructions to build a Docker image

**Answer: D**
Dockerfile contains step-by-step instructions (FROM, RUN, COPY, etc.) to build a Docker image.
---
## Question 4
What command builds a Docker image from a Dockerfile?


- A) docker build
- B) docker run
- C) docker create
- D) docker make

**Answer: A**
`docker build` creates an image from a Dockerfile, typically: `docker build -t name:tag .`
---
## Question 5
What command runs a container from an image?


- A) docker launch
- B) docker run
- C) docker start
- D) docker execute

**Answer: B**
`docker run` creates and starts a container from an image. Example: `docker run -d -p 8080:80 nginx`
---
## Question 6
What does the `-p` flag do in `docker run -p 8080:80`?


- A) Maps host port 8080 to container port 80
- B) Sets password
- C) Enables persistence
- D) Sets process priority

**Answer: A**
`-p` publishes container ports to the host: `-p [host-port]:[container-port]`
---
## Question 7
What is Docker Hub?


- A) A monitoring tool
- B) A public registry for storing and sharing Docker images
- C) A container orchestrator
- D) A development IDE

**Answer: B**
Docker Hub is the default public registry where you can pull official images and push your own.
---
## Question 8
What does the `-d` flag do in `docker run -d`?


- A) Runs container in detached mode (background)
- B) Sets data directory
- C) Deletes container after run
- D) Enables debug mode

**Answer: A**
`-d` (detached) runs the container in the background, returning control to your terminal.
---
## Question 9
How do you view running containers?


- A) docker show
- B) docker containers
- C) docker list
- D) docker ps

**Answer: D**
`docker ps` shows running containers. Add `-a` to see all containers including stopped ones.
---
## Question 10
What is a container registry?


- A) A database
- B) A repository for storing and distributing container images
- C) A file system
- D) A monitoring service

**Answer: B**
Container registries (Docker Hub, Azure Container Registry, etc.) store, manage, and distribute container images.