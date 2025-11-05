# Kubernetes Ingress: Exercises Introduction

We've covered how Ingress provides the front door to your Kubernetes applications with the Ingress Controller acting as reverse proxy and Ingress objects defining routing rules. Now let's deploy a complete Ingress setup from scratch.

## What You'll Do

You'll start by deploying the Nginx Ingress Controller examining the collection of resources that make it work: dedicated namespace for isolation, RBAC rules for querying the Kubernetes API, ConfigMap for Nginx configuration including proxy caching, DaemonSet ensuring one controller pod per node for high availability, and Services for external access via LoadBalancer and NodePort.

You'll verify the controller is running even before deploying applications. Testing shows a 404 from Nginx confirming the controller works but has no routing rules yet.

Then you'll deploy a default application as catch-all so users don't see bare Nginx error pages. The Ingress object doesn't specify a host field making it the default backend - any request not matching other more specific rules ends up here.

Next, you'll publish the whoami application to a specific hostname using host-based routing. After adding the domain to your hosts file, you'll see how the Ingress Controller load balances requests across multiple replicas automatically with hostname changes in responses demonstrating distribution.

You'll explore response caching with the Pi calculator app that performs heavy computation. Initially each request takes time to calculate, but after adding caching annotations to the Ingress object, subsequent requests with the same parameters return instantly from the Ingress Controller's cache - all without changing application code.

The lab challenge asks you to create your own Ingress routing for the configurable web app and reconfigure the Ingress Controller to use standard web ports 80 and 443 instead of high-numbered ports by modifying the Service.

The key learning: Ingress provides a single entry point that intelligently routes to multiple backend services with sophisticated features like SSL termination, load balancing, response caching, and rate limiting configured at the routing layer keeping application code focused on business logic.
