# Azure Front Door - AZ-204 Exam Introduction

Great work with Front Door! This topic spans multiple AZ-204 domains including security, integration, and Azure solutions implementation.

## What We'll Cover

**When to choose Front Door** versus other services is critical. Choose Front Door for: global HTTP/HTTPS applications, need CDN capabilities, require WAF protection, want session affinity across regions, need fast SSL termination. Choose Application Gateway for: regional load balancing, need AKS ingress controller, no CDN required. Choose Load Balancer for: Layer 4 (non-HTTP) traffic, regional load balancing. Choose Traffic Manager for: DNS-based routing, non-HTTP protocols. The exam heavily tests service selection.

**Front Door architecture** with profiles, endpoints, origins, origin groups, and routes needs to be understood. Profile is the top-level resource (Standard or Premium SKU). Endpoint is the public URL clients access (*.azurefd.net). Origin group contains backend applications with health probes and routing rules. Origins are the actual backend servers. Routes map requests to origin groups. The exam tests understanding of this component hierarchy.

**Security features** include WAF policies with managed rulesets (Microsoft Default for OWASP, Bot Manager for bot protection), custom rules for specific threats, prevention vs detection mode (prevent blocks requests, detect only logs them), DDoS protection (built-in, no extra config), and SSL/TLS management (automatic certificate management and renewal). The exam tests WAF configuration and troubleshooting.

**Performance optimization** includes caching (edge locations cache content closer to users), compression (reduces bandwidth for text content), routing methods (priority for failover, weighted for load distribution, latency for closest endpoint, session affinity for sticky sessions). The exam tests understanding of caching behavior and when to use different routing methods.

**Integration with containerized apps** - Front Door works with ACI, AKS, App Service Web Apps, and API Management. The exam tests designing architectures that combine Front Door with these services for global distribution.

**Troubleshooting common issues** like 502 Bad Gateway (unhealthy origins, misconfigured health probes), 403 Forbidden (WAF blocking legitimate requests - tune rules), caching issues (wrong cache duration, vary headers), SSL/TLS problems (certificate mismatch, protocol mismatch). The exam may present error scenarios requiring diagnosis.

We'll cover **CLI commands** for profiles, endpoints, origins, routes, and WAF policies, **monitoring and diagnostics**, **cost optimization**, and **common scenarios** about implementing global applications, securing HTTP services, and troubleshooting connectivity issues.

Master Front Door for the AZ-204!
