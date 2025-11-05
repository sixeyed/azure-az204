# Azure Application Gateway - Quickfire Questions

## Question 1
What is Azure Application Gateway?

- A) API Gateway
- B) Layer 7 (HTTP/HTTPS) load balancer with web application firewall capabilities
- C) Network gateway
- D) Storage gateway

**Answer: B**
Application Gateway is a web traffic load balancer operating at application layer (Layer 7) with advanced routing.

---

## Question 2
What layer of OSI model does Application Gateway operate at?

- A) Layer 3 (Network)
- B) Layer 7 (Application)
- C) Layer 4 (Transport)
- D) Layer 2 (Data Link)

**Answer: B**
Layer 7 enables routing based on HTTP/HTTPS attributes like URL path, host headers, cookies.

---

## Question 3
What is URL path-based routing?

- A) DNS routing
- B) Routing requests to different backend pools based on URL path
- C) IP-based routing
- D) Random routing

**Answer: B**
Example: /images/* → image servers, /api/* → API servers, enabling pattern-based traffic distribution.

---

## Question 4
What is multi-site hosting?

- A) Multiple VMs
- B) Hosting multiple websites on same Application Gateway using different hostnames
- C) Load balancing only
- D) Storage hosting

**Answer: B**
Configure multiple sites (contoso.com, fabrikam.com) on one gateway, routing based on hostname.

---

## Question 5
What is Web Application Firewall (WAF)?

- A) Physical firewall
- B) Protection against common web vulnerabilities (SQL injection, XSS) using OWASP rules
- C) Network firewall
- D) No security feature

**Answer: B**
WAF on Application Gateway protects against OWASP Top 10 vulnerabilities, bot attacks, and custom rules.

---

## Question 6
What are the WAF modes?

- A) Only detection
- B) Detection (log only) and Prevention (block attacks)
- C) Only prevention
- D) No modes

**Answer: B**
Detection mode logs threats. Prevention mode blocks malicious requests based on rules.

---

## Question 7
Does Application Gateway support SSL/TLS termination?

- A) No
- B) Yes, terminates SSL at gateway and re-encrypts to backend if needed
- C) Only pass-through
- D) Not supported

**Answer: B**
SSL offloading reduces backend CPU usage. Can decrypt at gateway, process, then re-encrypt to backend.

---

## Question 8
What is autoscaling in Application Gateway?

- A) Manual only
- B) Automatically adjusts capacity based on traffic load
- C) Fixed capacity
- D) Not supported

**Answer: B**
v2 SKU supports autoscaling from min to max capacity units based on traffic patterns.

---

## Question 9
What are the Application Gateway SKUs?

- A) Only one SKU
- B) Standard, WAF, Standard_v2, WAF_v2
- C) Basic and Premium
- D) Free and Paid

**Answer: B**
v1: Standard, WAF (deprecated path). v2: Standard_v2, WAF_v2 (autoscaling, better performance, new features).

---

## Question 10
Can Application Gateway rewrite HTTP headers?

- A) No modification
- B) Yes, rewrite request/response headers and URL
- C) Only read headers
- D) Only delete headers

**Answer: B**
Header rewrites allow modifying headers, rewriting URLs, adding/removing information in requests/responses.
