# Docker Compose - Quickfire Questions

## Question 1
What is Docker Compose?


- A) A container registry
- B) A tool for defining and running multi-container Docker applications using YAML
- C) A monitoring tool
- D) An orchestrator for production

**Answer: B**
Docker Compose uses a YAML file (docker-compose.yml) to define multi-container applications and their configuration.
---
## Question 2
What is the default Docker Compose file name?


- A) containers.yml
- B) compose.yaml
- C) dockerfile.yml
- D) docker-compose.yml (or docker-compose.yaml)

**Answer: D**
By default, Docker Compose looks for `docker-compose.yml` or `docker-compose.yaml` in the current directory.
---
## Question 3
What command starts all services defined in docker-compose.yml?


- A) docker-compose run
- B) docker-compose up
- C) docker-compose begin
- D) docker-compose start

**Answer: B**
`docker-compose up` builds, creates, and starts all services. Add `-d` for detached mode.
---
## Question 4
How do you define a service's image in docker-compose.yml?


- A) container: nginx
- B) image: nginx:latest
- C) base: nginx
- D) FROM: nginx

**Answer: B**
Under a service definition, use `image: imagename:tag` to specify which image to use.
---
## Question 5
How do you map ports in Docker Compose?


- A) port_map: 8080:80
- B) expose: "8080:80"
- C) network: 8080:80
- D) ports: - "8080:80"

**Answer: D**
The `ports` section maps host to container ports: `ports: - "host:container"`
---
## Question 6
What is the purpose of volumes in Docker Compose?


- A) Network configuration
- B) Increase container size
- C) Persist data and share files between host and containers or between containers
- D) Image storage

**Answer: C**
Volumes persist data beyond container lifecycle and enable file sharing between host and containers.
---
## Question 7
How do containers in the same Compose file communicate?


- A) Only through public internet
- B) Using IP addresses only
- C) By service name on the default network Compose creates
- D) They cannot

**Answer: C**
Compose creates a default network where services can reach each other using service names as hostnames.
---
## Question 8
What command stops and removes containers, networks defined in docker-compose.yml?


- A) docker-compose down
- B) docker-compose clean
- C) docker-compose remove
- D) docker-compose stop

**Answer: A**
`docker-compose down` stops containers and removes containers, networks created by `up`. Add `-v` to remove volumes too.
---
## Question 9
How do you specify environment variables for a service?


- A) env: VAR=value
- B) config: VAR=value
- C) vars: VAR=value
- D) environment: - VAR=value or environment file

**Answer: D**
Use `environment:` list or `env_file:` to specify environment variables for a service.
---
## Question 10
Can Docker Compose be used in production?


- A) No, only for testing
- B) Only on Windows
- C) Yes, it's the recommended production tool
- D) It can be, but orchestrators like Kubernetes or Docker Swarm are better for production

**Answer: D**
Compose is great for development and testing. For production, Kubernetes, Docker Swarm, or Azure Container Apps provide better orchestration.