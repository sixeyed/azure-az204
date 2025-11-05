# Docker Fundamentals - Quickfire Questions

## Question 1
What is a Docker container?

- A) A virtual machine
- B) A lightweight, standalone executable package containing code, runtime, libraries, and dependencies
- C) A storage volume
- D) A network protocol

**Answer: B**
Containers package application code with dependencies, running as isolated processes sharing the host OS kernel.

---

## Question 2
What is the difference between a Docker image and a container?

- A) They are the same
- B) Image is a template/blueprint; container is a running instance of an image
- C) Image is larger
- D) Container is read-only

**Answer: B**
Images are immutable templates. Containers are running instances created from images with a writable layer.

---

## Question 3
What is a Dockerfile?

- A) A log file
- B) A text file containing instructions to build a Docker image
- C) A configuration for Docker daemon
- D) A database schema

**Answer: B**
Dockerfile contains step-by-step instructions (FROM, RUN, COPY, etc.) to build a Docker image.

---

## Question 4
What command builds a Docker image from a Dockerfile?

- A) docker run
- B) docker build
- C) docker create
- D) docker make

**Answer: B**
`docker build` creates an image from a Dockerfile, typically: `docker build -t name:tag .`

---

## Question 5
What command runs a container from an image?

- A) docker start
- B) docker run
- C) docker execute
- D) docker launch

**Answer: B**
`docker run` creates and starts a container from an image. Example: `docker run -d -p 8080:80 nginx`

---

## Question 6
What does the `-p` flag do in `docker run -p 8080:80`?

- A) Sets password
- B) Maps host port 8080 to container port 80
- C) Sets process priority
- D) Enables persistence

**Answer: B**
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

- A) Deletes container after run
- B) Runs container in detached mode (background)
- C) Enables debug mode
- D) Sets data directory

**Answer: B**
`-d` (detached) runs the container in the background, returning control to your terminal.

---

## Question 9
How do you view running containers?

- A) docker list
- B) docker ps
- C) docker show
- D) docker containers

**Answer: B**
`docker ps` shows running containers. Add `-a` to see all containers including stopped ones.

---

## Question 10
What is a container registry?

- A) A database
- B) A repository for storing and distributing container images
- C) A monitoring service
- D) A file system

**Answer: B**
Container registries (Docker Hub, Azure Container Registry, etc.) store, manage, and distribute container images.
