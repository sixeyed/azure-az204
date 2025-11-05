# AKS Ingress Controllers - Quickfire Questions

## Question 1
What is an Ingress in Kubernetes?


- A) Storage ingress
- B) API object managing external HTTP/HTTPS access to cluster services
- C) Security group
- D) Entry point

**Answer: B**
Ingress provides HTTP routing rules, SSL termination, and name-based virtual hosting.
---
## Question 2
What is the difference between Service LoadBalancer and Ingress?


- A) LoadBalancer creates single external IP per service; Ingress shares IP for multiple services with routing
- B) LoadBalancer is deprecated
- C) Same thing
- D) Ingress is cheaper

**Answer: A**
Ingress consolidates routing, SSL, and external access for multiple services behind one IP.
---
## Question 3
What Ingress controllers are commonly used with AKS?


- A) No controllers available
- B) Nginx, Traefik, Application Gateway Ingress Controller (AGIC), Istio
- C) Custom only
- D) Only one option

**Answer: B**
Multiple options; Nginx popular for simplicity, AGIC for Azure integration.
---
## Question 4
What is Application Gateway Ingress Controller (AGIC)?


- A) Network gateway
- B) Ingress controller using Azure Application Gateway as AKS ingress
- C) Database gateway
- D) Generic ingress

**Answer: B**
AGIC integrates AKS with Azure Application Gateway, leveraging WAF and Azure networking.
---
## Question 5
How do you enable SSL/TLS termination in Ingress?


- A) Provide TLS certificate as Kubernetes Secret, reference in Ingress spec
- B) Not possible
- C) Manual configuration only
- D) Automatic only

**Answer: A**
Create Secret with TLS cert/key, configure Ingress with tls section referencing Secret.
---
## Question 6
What is cert-manager?


- A) User manager
- B) Configuration manager
- C) Kubernetes add-on automating TLS certificate management (Let's Encrypt integration)
- D) Certificate storage

**Answer: C**
Cert-manager automatically provisions and renews certificates from Let's Encrypt or other CAs.
---
## Question 7
Can Ingress route based on URL path?


- A) Random routing
- B) Hostname only
- C) No routing
- D) Yes, path-based routing (e.g., /api → backend, /static → frontend)

**Answer: D**
Ingress rules support path-based and host-based routing to different backend services.
---
## Question 8
What is host-based routing in Ingress?


- A) IP routing
- B) VM routing
- C) Not supported
- D) Routing traffic to different services based on hostname (app1.com → service1, app2.com → service2)

**Answer: D**
Virtual hosting: different domains/subdomains routed to different services.
---
## Question 9
How many external IPs does Ingress require?


- A) Unlimited
- B) No external IP
- C) One shared IP for all Ingress rules (vs LoadBalancer per service)
- D) One per service

**Answer: C**
Single ingress IP handles multiple services/domains, reducing public IP costs.
---
## Question 10
Can you implement authentication at Ingress level?


- A) Not possible
- B) Yes, using ingress authentication annotations or service mesh
- C) Application level only
- D) No authentication

**Answer: B**
Ingress controllers support authentication via annotations, or use service mesh (Istio) for advanced auth.