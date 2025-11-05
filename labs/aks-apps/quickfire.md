# Deploying Applications on AKS - Quickfire Questions

## Question 1
How do you deploy an application to AKS?

- A) Copy files manually
- B) kubectl apply with YAML manifests or Helm charts
- C) RDP to nodes
- D) Not possible

**Answer: B**
Kubernetes manifests (YAML) or Helm charts define application deployment, services, and configuration.

---

## Question 2
What is Helm?

- A) Ship steering wheel
- B) Package manager for Kubernetes, using charts to define applications
- C) Monitoring tool
- D) Database

**Answer: B**
Helm simplifies Kubernetes deployments with reusable, parameterized charts.

---

## Question 3
How do you expose applications to the internet from AKS?

- A) Not possible
- B) LoadBalancer service, Ingress controller, or Application Gateway Ingress Controller
- C) Direct node access
- D) Manual port forwarding

**Answer: B**
LoadBalancer for simple scenarios; Ingress for advanced routing and SSL/TLS termination.

---

## Question 4
What is an Ingress controller?

- A) Access control
- B) Manages external HTTP/HTTPS access to services with routing rules
- C) Network controller
- D) Storage controller

**Answer: B**
Ingress controllers (Nginx, Traefik) handle external traffic routing, SSL termination, host/path-based routing.

---

## Question 5
How do applications access secrets in AKS?

- A) Hardcode secrets
- B) Kubernetes Secrets, Azure Key Vault via CSI driver, or environment variables
- C) Plain text files
- D) Not possible

**Answer: B**
Use Kubernetes Secrets or Azure Key Vault with Secrets Store CSI driver for secure access.

---

## Question 6
What is a StatefulSet?

- A) Configuration state
- B) Controller for stateful applications requiring stable network identity and persistent storage
- C) Deployment type
- D) Storage type

**Answer: B**
StatefulSets manage stateful apps (databases, queues) with ordered deployment and persistent volumes.

---

## Question 7
How do you implement CI/CD for AKS?

- A) Manual deployments only
- B) Azure Pipelines, GitHub Actions, GitLab CI with kubectl/Helm commands
- C) Not possible
- D) Portal only

**Answer: B**
Automate builds (container images) and deployments (kubectl apply) using CI/CD pipelines.

---

## Question 8
What is a Horizontal Pod Autoscaler (HPA)?

- A) Manual scaling
- B) Automatically scales pod replicas based on CPU, memory, or custom metrics
- C) Node scaler
- D) Storage scaler

**Answer: B**
HPA adjusts replica count based on observed metrics, scaling applications dynamically.

---

## Question 9
How do you update applications in AKS?

- A) Delete and recreate
- B) Rolling update strategy (default), blue-green, canary deployments
- C) Downtime required
- D) Not possible

**Answer: B**
Kubernetes supports zero-downtime rolling updates; strategies like blue-green provide additional control.

---

## Question 10
Can you run background jobs in AKS?

- A) No background tasks
- B) Yes, using Kubernetes Jobs (one-time) and CronJobs (scheduled)
- C) Manual execution only
- D) Not supported

**Answer: B**
Jobs for batch processing; CronJobs for scheduled tasks (similar to cron).
