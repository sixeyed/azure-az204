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

- A) compose.yaml
- B) docker-compose.yml (or docker-compose.yaml)
- C) dockerfile.yml
- D) containers.yml

**Answer: B**
By default, Docker Compose looks for `docker-compose.yml` or `docker-compose.yaml` in the current directory.

---

## Question 3
What command starts all services defined in docker-compose.yml?

- A) docker-compose start
- B) docker-compose up
- C) docker-compose run
- D) docker-compose begin

**Answer: B**
`docker-compose up` builds, creates, and starts all services. Add `-d` for detached mode.

---

## Question 4
How do you define a service's image in docker-compose.yml?

- A) FROM: nginx
- B) image: nginx:latest
- C) container: nginx
- D) base: nginx

**Answer: B**
Under a service definition, use `image: imagename:tag` to specify which image to use.

---

## Question 5
How do you map ports in Docker Compose?

- A) expose: "8080:80"
- B) ports: - "8080:80"
- C) network: 8080:80
- D) port_map: 8080:80

**Answer: B**
The `ports` section maps host to container ports: `ports: - "host:container"`

---

## Question 6
What is the purpose of volumes in Docker Compose?

- A) Increase container size
- B) Persist data and share files between host and containers or between containers
- C) Network configuration
- D) Image storage

**Answer: B**
Volumes persist data beyond container lifecycle and enable file sharing between host and containers.

---

## Question 7
How do containers in the same Compose file communicate?

- A) They cannot
- B) By service name on the default network Compose creates
- C) Only through public internet
- D) Using IP addresses only

**Answer: B**
Compose creates a default network where services can reach each other using service names as hostnames.

---

## Question 8
What command stops and removes containers, networks defined in docker-compose.yml?

- A) docker-compose stop
- B) docker-compose down
- C) docker-compose remove
- D) docker-compose clean

**Answer: B**
`docker-compose down` stops containers and removes containers, networks created by `up`. Add `-v` to remove volumes too.

---

## Question 9
How do you specify environment variables for a service?

- A) env: VAR=value
- B) environment: - VAR=value or environment file
- C) vars: VAR=value
- D) config: VAR=value

**Answer: B**
Use `environment:` list or `env_file:` to specify environment variables for a service.

---

## Question 10
Can Docker Compose be used in production?

- A) Yes, it's the recommended production tool
- B) It can be, but orchestrators like Kubernetes or Docker Swarm are better for production
- C) No, only for testing
- D) Only on Windows

**Answer: B**
Compose is great for development and testing. For production, Kubernetes, Docker Swarm, or Azure Container Apps provide better orchestration.
