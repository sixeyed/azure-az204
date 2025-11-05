# Kubernetes Fundamentals - Quickfire Questions

## Question 1
What is Kubernetes?


- A) Open-source container orchestration platform for automating deployment, scaling, and management
- B) Programming language
- C) Storage system
- D) Database system

**Answer: A**
Kubernetes (K8s) orchestrates containerized applications across clusters of machines.
---
## Question 2
What is a pod in Kubernetes?


- A) Smallest deployable unit, containing one or more containers sharing network/storage
- B) Database
- C) Virtual machine
- D) Storage unit

**Answer: A**
Pods wrap containers with shared networking and storage, representing application instances.
---
## Question 3
What is a deployment in Kubernetes?


- A) Declarative definition managing replica pods with rolling updates and rollback
- B) Storage deployment
- C) Manual process
- D) One-time action

**Answer: A**
Deployments manage desired state for pods: replicas, updates, scaling, self-healing.
---
## Question 4
What is a service in Kubernetes?


- A) Stable network endpoint for accessing pods (load balancing, service discovery)
- B) Microservice
- C) Database service
- D) Web service

**Answer: A**
Services provide consistent DNS/IP for accessing pod replicas, with load balancing.
---
## Question 5
What is kubectl?


- A) Container runtime
- B) Command-line tool for interacting with Kubernetes clusters
- C) Database client
- D) Programming language

**Answer: B**
kubectl manages Kubernetes resources: create, read, update, delete (CRUD) operations.
---
## Question 6
What is a namespace in Kubernetes?


- A) DNS namespace
- B) Network namespace only
- C) Virtual cluster for organizing resources and providing scope for names
- D) Storage namespace

**Answer: C**
Namespaces isolate resources, enabling multi-tenancy and environment separation (dev/test/prod).
---
## Question 7
What is a ReplicaSet?


- A) Database replica
- B) Controller maintaining specified number of identical pod replicas
- C) Backup system
- D) Storage replica

**Answer: B**
ReplicaSets ensure desired pod count, replacing failed pods automatically.
---
## Question 8
What is a ConfigMap?


- A) CPU configuration
- B) Kubernetes object storing non-sensitive configuration data as key-value pairs
- C) Location map
- D) Network map

**Answer: B**
ConfigMaps decouple configuration from container images, enabling environment-specific configs.
---
## Question 9
What is a Secret in Kubernetes?


- A) Public data
- B) Encrypted storage
- C) Configuration file
- D) Object storing sensitive data (passwords, tokens) with base64 encoding

**Answer: D**
Secrets store sensitive information separately from pod specs (base64 encoded, not encrypted by default).
---
## Question 10
What is a persistent volume (PV)?


- A) Memory volume
- B) Cluster storage resource independent of pod lifecycle
- C) Temporary storage
- D) Network volume

**Answer: B**
PVs provide durable storage that persists beyond pod lifecycle, enabling stateful applications.