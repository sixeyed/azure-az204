# Application Gateway with WAF - AZ-204 Exam Introduction

Great job implementing Application Gateway with Web Application Firewall! This is an important networking and security topic for the AZ-204. Let's focus on what you need to know for the exam.

## What We'll Cover

**Layer 7 vs Layer 4 load balancing** is fundamental. Layer 4 (Azure Load Balancer) routes based on IP address and TCP/UDP port - it's fast, low-latency, protocol-agnostic, but not content-aware. Layer 7 (Application Gateway) routes based on HTTP attributes like domain names, URL paths, headers, and cookies - it's more intelligent with content-based routing but adds some latency. The exam tests when to choose each based on requirements.

**Application Gateway components** need to be understood: Frontend IP (public or private IP for incoming requests), Listeners (wait for requests on specific ports, multi-site listeners match specific host headers), Backend pools (groups of backend servers like VMs, VMSS, App Service, ACI), Routing rules (with priority evaluation - lower numbers evaluated first), Health probes (check backend availability), and HTTP settings (port, protocol, cookie affinity, timeouts). Questions test how these components work together.

**SKU tiers** appear in scenario questions. Standard_v2 provides basic layer 7 load balancing, auto-scaling, zone redundancy, and static VIP. WAF_v2 includes everything in Standard_v2 plus Web Application Firewall with OWASP rule sets (3.2, 3.1, 3.0). The exam tests when to choose WAF_v2 (when security protection is needed) versus Standard_v2 (when just load balancing is required).

**WAF modes and protection** is important. Detection mode logs threats but doesn't block them (good for testing to avoid false positives). Prevention mode actively blocks malicious requests returning 403 Forbidden (production mode). OWASP rulesets protect against SQL injection, XSS, command injection, path traversal, and other Top 10 vulnerabilities. The exam may ask about WAF behavior or how to tune rules.

**Routing types** need to be memorized. Basic routing sends all requests to a single backend pool. Path-based routing routes based on URL path (/api/* to API pool, /images/* to image pool). Multi-site routing routes based on host header (app1.contoso.com to pool1, app2.contoso.com to pool2). The exam tests which routing type to use for different scenarios.

**SSL/TLS termination** concepts appear frequently. SSL termination at Application Gateway (decrypt at gateway, forward HTTP to backends - reduces backend CPU, centralizes certificate management). End-to-end SSL (decrypt at gateway, re-encrypt to backends - more secure, ensures encryption throughout). The exam tests when to use each pattern.

**Troubleshooting 502 Bad Gateway** is a common scenario. Causes include: no matching routing rule for the request, backend unhealthy or unreachable, backend timeout (no response within configured timeout), NSG or firewall rules blocking traffic between gateway and backends, or backend returning invalid responses. Know how to diagnose each.

**Service comparison** questions test understanding when to use Application Gateway (regional layer 7) versus Azure Load Balancer (layer 4 TCP/UDP), Traffic Manager (global DNS-based routing), Azure Front Door (global layer 7 with CDN), or API Management (often deployed together with Application Gateway for API throttling/transformation).

Master Application Gateway for the AZ-204!
