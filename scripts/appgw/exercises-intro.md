# Application Gateway with WAF - Exercises Introduction

We've covered Application Gateway as a layer 7 load balancer and Web Application Firewall for security. Now let's deploy a complete solution with multi-site routing and attack protection.

## What You'll Do

You'll start by **creating the infrastructure**: resource group, Standard public IP with DNS, virtual network (10.4.0.0/16), and a dedicated subnet (10.4.10.0/24) for Application Gateway - it needs its own subnet that can't contain other resources. You'll **create a WAF policy** with OWASP 3.2 ruleset in Prevention mode to actively block attacks.

Then you'll **deploy Application Gateway** with WAF_v2 SKU (includes Web Application Firewall). Next comes the backends: **create three ACI containers** - two simple-web instances (for load balancing demonstration) and one pi-web instance (different application).

The interesting part is **configuring multi-site routing**. You'll create separate backend pools for the two applications, multi-site listeners that match specific host headers (simple.appgw and pi.appgw domains), and routing rules with proper priority settings to route traffic correctly.

**Testing** involves configuring your local hosts file to create fake domains pointing to the Application Gateway IP. You'll **verify load balancing** by refreshing and seeing different backend instances respond. Then comes the security test: you'll **simulate SQL injection attacks**. When accessing containers directly, malicious requests succeed (200 OK). But when going through Application Gateway with WAF, those same requests are blocked (403 Forbidden)!

You'll **view WAF logs** showing all blocked requests with details about which OWASP rule triggered. Optionally, you can run **GoTestWAF with 500+ attack simulations** to see comprehensive protection against SQL injection, XSS, path traversal, and other OWASP Top 10 vulnerabilities.

Let's build a secure, load-balanced application gateway!
