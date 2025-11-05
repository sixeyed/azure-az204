# Azure Application Gateway - Quickfire Questions

## Question 1
What is Azure Application Gateway?


- A) API Gateway
- B) Storage gateway
- C) Layer 7 (HTTP/HTTPS) load balancer with web application firewall capabilities
- D) Network gateway

**Answer: C**
Application Gateway is a web traffic load balancer operating at application layer (Layer 7) with advanced routing.
---
## Question 2
What layer of OSI model does Application Gateway operate at?


- A) Layer 4 (Transport)
- B) Layer 7 (Application)
- C) Layer 3 (Network)
- D) Layer 2 (Data Link)

**Answer: B**
Layer 7 enables routing based on HTTP/HTTPS attributes like URL path, host headers, cookies.
---
## Question 3
What is URL path-based routing?


- A) Routing requests to different backend pools based on URL path
- B) Random routing
- C) DNS routing
- D) IP-based routing

**Answer: A**
Example: /images/* → image servers, /api/* → API servers, enabling pattern-based traffic distribution.
---
## Question 4
What is multi-site hosting?


- A) Hosting multiple websites on same Application Gateway using different hostnames
- B) Storage hosting
- C) Load balancing only
- D) Multiple VMs

**Answer: A**
Configure multiple sites (contoso.com, fabrikam.com) on one gateway, routing based on hostname.
---
## Question 5
What is Web Application Firewall (WAF)?


- A) Network firewall
- B) Protection against common web vulnerabilities (SQL injection, XSS) using OWASP rules
- C) No security feature
- D) Physical firewall

**Answer: B**
WAF on Application Gateway protects against OWASP Top 10 vulnerabilities, bot attacks, and custom rules.
---
## Question 6
What are the WAF modes?


- A) No modes
- B) Only prevention
- C) Detection (log only) and Prevention (block attacks)
- D) Only detection

**Answer: C**
Detection mode logs threats. Prevention mode blocks malicious requests based on rules.
---
## Question 7
Does Application Gateway support SSL/TLS termination?


- A) Not supported
- B) Only pass-through
- C) Yes, terminates SSL at gateway and re-encrypts to backend if needed
- D) No

**Answer: C**
SSL offloading reduces backend CPU usage. Can decrypt at gateway, process, then re-encrypt to backend.
---
## Question 8
What is autoscaling in Application Gateway?


- A) Not supported
- B) Fixed capacity
- C) Manual only
- D) Automatically adjusts capacity based on traffic load

**Answer: D**
v2 SKU supports autoscaling from min to max capacity units based on traffic patterns.
---
## Question 9
What are the Application Gateway SKUs?


- A) Only one SKU
- B) Basic and Premium
- C) Standard, WAF, Standard_v2, WAF_v2
- D) Free and Paid

**Answer: C**
v1: Standard, WAF (deprecated path). v2: Standard_v2, WAF_v2 (autoscaling, better performance, new features).
---
## Question 10
Can Application Gateway rewrite HTTP headers?


- A) No modification
- B) Only delete headers
- C) Only read headers
- D) Yes, rewrite request/response headers and URL

**Answer: D**
Header rewrites allow modifying headers, rewriting URLs, adding/removing information in requests/responses.