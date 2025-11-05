# Deploying Applications on AKS - Quickfire Questions

## Question 1
How do you deploy an application to AKS?


- A) kubectl apply with YAML manifests or Helm charts
- B) RDP to nodes
- C) Not possible
- D) Copy files manually

**Answer: A**
Kubernetes manifests (YAML) or Helm charts define application deployment, services, and configuration.
---
## Question 2
What is Helm?


- A) Package manager for Kubernetes, using charts to define applications
- B) Database
- C) Monitoring tool
- D) Ship steering wheel

**Answer: A**
Helm simplifies Kubernetes deployments with reusable, parameterized charts.
---
## Question 3
How do you expose applications to the internet from AKS?


- A) Not possible
- B) LoadBalancer service, Ingress controller, or Application Gateway Ingress Controller
- C) Manual port forwarding
- D) Direct node access

**Answer: B**
LoadBalancer for simple scenarios; Ingress for advanced routing and SSL/TLS termination.
---
## Question 4
What is an Ingress controller?


- A) Storage controller
- B) Access control
- C) Manages external HTTP/HTTPS access to services with routing rules
- D) Network controller

**Answer: C**
Ingress controllers (Nginx, Traefik) handle external traffic routing, SSL termination, host/path-based routing.
---
## Question 5
How do applications access secrets in AKS?


- A) Not possible
- B) Hardcode secrets
- C) Plain text files
- D) Kubernetes Secrets, Azure Key Vault via CSI driver, or environment variables

**Answer: D**
Use Kubernetes Secrets or Azure Key Vault with Secrets Store CSI driver for secure access.
---
## Question 6
What is a StatefulSet?


- A) Configuration state
- B) Controller for stateful applications requiring stable network identity and persistent storage
- C) Storage type
- D) Deployment type

**Answer: B**
StatefulSets manage stateful apps (databases, queues) with ordered deployment and persistent volumes.
---
## Question 7
How do you implement CI/CD for AKS?


- A) Portal only
- B) Not possible
- C) Azure Pipelines, GitHub Actions, GitLab CI with kubectl/Helm commands
- D) Manual deployments only

**Answer: C**
Automate builds (container images) and deployments (kubectl apply) using CI/CD pipelines.
---
## Question 8
What is a Horizontal Pod Autoscaler (HPA)?


- A) Manual scaling
- B) Node scaler
- C) Automatically scales pod replicas based on CPU, memory, or custom metrics
- D) Storage scaler

**Answer: C**
HPA adjusts replica count based on observed metrics, scaling applications dynamically.
---
## Question 9
How do you update applications in AKS?


- A) Rolling update strategy (default), blue-green, canary deployments
- B) Not possible
- C) Downtime required
- D) Delete and recreate

**Answer: A**
Kubernetes supports zero-downtime rolling updates; strategies like blue-green provide additional control.
---
## Question 10
Can you run background jobs in AKS?


- A) Not supported
- B) Yes, using Kubernetes Jobs (one-time) and CronJobs (scheduled)
- C) Manual execution only
- D) No background tasks

**Answer: B**
Jobs for batch processing; CronJobs for scheduled tasks (similar to cron).