# Azure Front Door - Exercises Introduction

We've covered Azure Front Door as Microsoft's modern cloud CDN with global load balancing and security. Now let's implement a globally distributed application with WAF protection.

## What You'll Do

You'll start by **creating a Front Door Premium profile** (required for WAF support). Then you'll **deploy backend applications** - Azure Container Instances in multiple regions. This simulates a globally distributed application with instances in US, Europe, and Asia.

Next comes the Front Door configuration: **create origin groups** with health probes (to detect unhealthy backends) and weighted routing (to control traffic distribution). You'll **create endpoints and routes** to connect clients to backends - the endpoint is the public URL clients access, routes define how requests flow to origin groups.

You'll **enable compression** to reduce bandwidth and improve performance for text-based content (HTML, CSS, JavaScript). This happens automatically at the Front Door edge locations worldwide.

Then you'll configure **Web Application Firewall with managed rulesets**. You'll apply the **Microsoft Default Rule Set** (OWASP Top 10 protection) and **Bot Manager** (bot detection and blocking). WAF operates in Prevention mode, actively blocking malicious requests.

The security test is exciting: you'll **simulate SQL injection attacks** against your application. When accessing the container directly (bypassing Front Door), malicious requests succeed with 200 OK. But when going through Front Door, WAF blocks them with **403 Forbidden** responses! You'll see detailed WAF logs showing which rules triggered and why requests were blocked.

The **challenge** involves **adding a Pi application with its own endpoint**, demonstrating multi-application routing through a single Front Door instance.

Let's build a globally secure application!
