# AKS Ingress Controllers - Quickfire Questions

## Question 1
What is an Ingress in Kubernetes?

- A) Entry point
- B) API object managing external HTTP/HTTPS access to cluster services
- C) Security group
- D) Storage ingress

**Answer: B**
Ingress provides HTTP routing rules, SSL termination, and name-based virtual hosting.

---

## Question 2
What is the difference between Service LoadBalancer and Ingress?

- A) Same thing
- B) LoadBalancer creates single external IP per service; Ingress shares IP for multiple services with routing
- C) Ingress is cheaper
- D) LoadBalancer is deprecated

**Answer: B**
Ingress consolidates routing, SSL, and external access for multiple services behind one IP.

---

## Question 3
What Ingress controllers are commonly used with AKS?

- A) Only one option
- B) Nginx, Traefik, Application Gateway Ingress Controller (AGIC), Istio
- C) No controllers available
- D) Custom only

**Answer: B**
Multiple options; Nginx popular for simplicity, AGIC for Azure integration.

---

## Question 4
What is Application Gateway Ingress Controller (AGIC)?

- A) Generic ingress
- B) Ingress controller using Azure Application Gateway as AKS ingress
- C) Database gateway
- D) Network gateway

**Answer: B**
AGIC integrates AKS with Azure Application Gateway, leveraging WAF and Azure networking.

---

## Question 5
How do you enable SSL/TLS termination in Ingress?

- A) Not possible
- B) Provide TLS certificate as Kubernetes Secret, reference in Ingress spec
- C) Manual configuration only
- D) Automatic only

**Answer: B**
Create Secret with TLS cert/key, configure Ingress with tls section referencing Secret.

---

## Question 6
What is cert-manager?

- A) Certificate storage
- B) Kubernetes add-on automating TLS certificate management (Let's Encrypt integration)
- C) User manager
- D) Configuration manager

**Answer: B**
Cert-manager automatically provisions and renews certificates from Let's Encrypt or other CAs.

---

## Question 7
Can Ingress route based on URL path?

- A) No routing
- B) Yes, path-based routing (e.g., /api → backend, /static → frontend)
- C) Hostname only
- D) Random routing

**Answer: B**
Ingress rules support path-based and host-based routing to different backend services.

---

## Question 8
What is host-based routing in Ingress?

- A) VM routing
- B) Routing traffic to different services based on hostname (app1.com → service1, app2.com → service2)
- C) IP routing
- D) Not supported

**Answer: B**
Virtual hosting: different domains/subdomains routed to different services.

---

## Question 9
How many external IPs does Ingress require?

- A) One per service
- B) One shared IP for all Ingress rules (vs LoadBalancer per service)
- C) No external IP
- D) Unlimited

**Answer: B**
Single ingress IP handles multiple services/domains, reducing public IP costs.

---

## Question 10
Can you implement authentication at Ingress level?

- A) No authentication
- B) Yes, using ingress authentication annotations or service mesh
- C) Application level only
- D) Not possible

**Answer: B**
Ingress controllers support authentication via annotations, or use service mesh (Istio) for advanced auth.
