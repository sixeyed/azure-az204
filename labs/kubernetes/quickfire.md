# Kubernetes Fundamentals - Quickfire Questions

## Question 1
What is Kubernetes?

- A) Database system
- B) Open-source container orchestration platform for automating deployment, scaling, and management
- C) Programming language
- D) Storage system

**Answer: B**
Kubernetes (K8s) orchestrates containerized applications across clusters of machines.

---

## Question 2
What is a pod in Kubernetes?

- A) Storage unit
- B) Smallest deployable unit, containing one or more containers sharing network/storage
- C) Virtual machine
- D) Database

**Answer: B**
Pods wrap containers with shared networking and storage, representing application instances.

---

## Question 3
What is a deployment in Kubernetes?

- A) One-time action
- B) Declarative definition managing replica pods with rolling updates and rollback
- C) Manual process
- D) Storage deployment

**Answer: B**
Deployments manage desired state for pods: replicas, updates, scaling, self-healing.

---

## Question 4
What is a service in Kubernetes?

- A) Web service
- B) Stable network endpoint for accessing pods (load balancing, service discovery)
- C) Microservice
- D) Database service

**Answer: B**
Services provide consistent DNS/IP for accessing pod replicas, with load balancing.

---

## Question 5
What is kubectl?

- A) Container runtime
- B) Command-line tool for interacting with Kubernetes clusters
- C) Programming language
- D) Database client

**Answer: B**
kubectl manages Kubernetes resources: create, read, update, delete (CRUD) operations.

---

## Question 6
What is a namespace in Kubernetes?

- A) DNS namespace
- B) Virtual cluster for organizing resources and providing scope for names
- C) Network namespace only
- D) Storage namespace

**Answer: B**
Namespaces isolate resources, enabling multi-tenancy and environment separation (dev/test/prod).

---

## Question 7
What is a ReplicaSet?

- A) Backup system
- B) Controller maintaining specified number of identical pod replicas
- C) Storage replica
- D) Database replica

**Answer: B**
ReplicaSets ensure desired pod count, replacing failed pods automatically.

---

## Question 8
What is a ConfigMap?

- A) Network map
- B) Kubernetes object storing non-sensitive configuration data as key-value pairs
- C) Location map
- D) CPU configuration

**Answer: B**
ConfigMaps decouple configuration from container images, enabling environment-specific configs.

---

## Question 9
What is a Secret in Kubernetes?

- A) Encrypted storage
- B) Object storing sensitive data (passwords, tokens) with base64 encoding
- C) Public data
- D) Configuration file

**Answer: B**
Secrets store sensitive information separately from pod specs (base64 encoded, not encrypted by default).

---

## Question 10
What is a persistent volume (PV)?

- A) Temporary storage
- B) Cluster storage resource independent of pod lifecycle
- C) Memory volume
- D) Network volume

**Answer: B**
PVs provide durable storage that persists beyond pod lifecycle, enabling stateful applications.
