# Azure Front Door - Quickfire Questions

## Question 1
What is Azure Front Door?


- A) Physical door
- B) Global Layer 7 load balancer with CDN, WAF, and application acceleration
- C) Virtual machine
- D) Storage service

**Answer: B**
Front Door is a global HTTP/HTTPS load balancer providing fast, secure, and scalable application delivery.
---
## Question 2
What is the difference between Front Door and Application Gateway?


- A) Front Door is global; Application Gateway is regional
- B) Application Gateway is global
- C) Same service
- D) No difference

**Answer: A**
Front Door operates globally across Azure edge locations. Application Gateway is deployed in specific regions.
---
## Question 3
What is Anycast routing in Front Door?


- A) Random routing
- B) Unicast only
- C) Traffic routed to nearest Front Door POP (point of presence) for low latency
- D) Broadcast routing

**Answer: C**
Anycast routes users to closest edge location, then uses Azure's global network to reach backend.
---
## Question 4
What routing methods does Front Door support?


- A) Only round-robin
- B) No routing
- C) Priority, Weighted, Latency, Session affinity
- D) Random only

**Answer: C**
Priority (failover), Weighted (distribution), Latency (fastest backend), Session affinity (sticky sessions).
---
## Question 5
Does Front Door include CDN capabilities?


- A) Yes, caches static content at edge for faster delivery
- B) Only load balancing
- C) No CDN
- D) Requires separate CDN

**Answer: A**
Front Door caches static/semi-static content globally, reducing origin load and improving performance.
---
## Question 6
What is backend pool in Front Door?


- A) IP pool
- B) Storage pool
- C) Physical pool
- D) Set of backend endpoints (App Service, VMs, etc.) receiving traffic

**Answer: D**
Backend pools contain application endpoints across regions or clouds that Front Door distributes traffic to.
---
## Question 7
Can Front Door perform SSL offload?


- A) HTTP only
- B) Only pass-through
- C) No SSL support
- D) Yes, terminates TLS at edge and can re-encrypt to backend

**Answer: D**
Front Door terminates TLS at edge, reducing latency and backend CPU load, with optional end-to-end encryption.
---
## Question 8
What is health probing in Front Door?


- A) Regular checks to backend endpoints to detect failures and route around unhealthy backends
- B) Security scanning
- C) Network testing
- D) Performance testing

**Answer: A**
Health probes monitor backend availability, automatically removing unhealthy endpoints from rotation.
---
## Question 9
Does Front Door support custom domains?


- A) Requires manual certificate
- B) No, only .azurefd.net
- C) Yes, custom domains with automatic SSL certificate management
- D) Only subdomains

**Answer: C**
Front Door supports custom domains with Azure-managed or bring-your-own certificates.
---
## Question 10
What is Front Door Rules Engine?


- A) Database engine
- B) Not available
- C) Search engine
- D) Configurable routing and header manipulation based on conditions

**Answer: D**
Rules Engine allows conditional logic: redirect, rewrite URLs, modify headers based on request attributes.