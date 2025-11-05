# Azure Front Door - Quickfire Questions

## Question 1
What is Azure Front Door?

- A) Physical door
- B) Global Layer 7 load balancer with CDN, WAF, and application acceleration
- C) Storage service
- D) Virtual machine

**Answer: B**
Front Door is a global HTTP/HTTPS load balancer providing fast, secure, and scalable application delivery.

---

## Question 2
What is the difference between Front Door and Application Gateway?

- A) Same service
- B) Front Door is global; Application Gateway is regional
- C) Application Gateway is global
- D) No difference

**Answer: B**
Front Door operates globally across Azure edge locations. Application Gateway is deployed in specific regions.

---

## Question 3
What is Anycast routing in Front Door?

- A) Random routing
- B) Traffic routed to nearest Front Door POP (point of presence) for low latency
- C) Unicast only
- D) Broadcast routing

**Answer: B**
Anycast routes users to closest edge location, then uses Azure's global network to reach backend.

---

## Question 4
What routing methods does Front Door support?

- A) Only round-robin
- B) Priority, Weighted, Latency, Session affinity
- C) Random only
- D) No routing

**Answer: B**
Priority (failover), Weighted (distribution), Latency (fastest backend), Session affinity (sticky sessions).

---

## Question 5
Does Front Door include CDN capabilities?

- A) No CDN
- B) Yes, caches static content at edge for faster delivery
- C) Only load balancing
- D) Requires separate CDN

**Answer: B**
Front Door caches static/semi-static content globally, reducing origin load and improving performance.

---

## Question 6
What is backend pool in Front Door?

- A) Physical pool
- B) Set of backend endpoints (App Service, VMs, etc.) receiving traffic
- C) Storage pool
- D) IP pool

**Answer: B**
Backend pools contain application endpoints across regions or clouds that Front Door distributes traffic to.

---

## Question 7
Can Front Door perform SSL offload?

- A) No SSL support
- B) Yes, terminates TLS at edge and can re-encrypt to backend
- C) Only pass-through
- D) HTTP only

**Answer: B**
Front Door terminates TLS at edge, reducing latency and backend CPU load, with optional end-to-end encryption.

---

## Question 8
What is health probing in Front Door?

- A) Network testing
- B) Regular checks to backend endpoints to detect failures and route around unhealthy backends
- C) Security scanning
- D) Performance testing

**Answer: B**
Health probes monitor backend availability, automatically removing unhealthy endpoints from rotation.

---

## Question 9
Does Front Door support custom domains?

- A) No, only .azurefd.net
- B) Yes, custom domains with automatic SSL certificate management
- C) Only subdomains
- D) Requires manual certificate

**Answer: B**
Front Door supports custom domains with Azure-managed or bring-your-own certificates.

---

## Question 10
What is Front Door Rules Engine?

- A) Database engine
- B) Configurable routing and header manipulation based on conditions
- C) Search engine
- D) Not available

**Answer: B**
Rules Engine allows conditional logic: redirect, rewrite URLs, modify headers based on request attributes.
