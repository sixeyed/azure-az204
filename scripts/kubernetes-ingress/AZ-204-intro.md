# Kubernetes Ingress: AZ-204 Exam Focus

Great work! This Ingress lab is crucial for the "Implement containerized solutions" objective in the AZ-204 exam. Understanding how to manage external access to applications is essential for developing production-ready solutions in Azure Kubernetes Service.

## What We'll Cover

We'll examine HTTP routing as a fundamental exam topic. Host-based routing directs traffic to different services based on hostname in requests - multiple applications on a single IP address. Path-based routing uses URL paths to segment different application parts. The exam expects you to read and understand Ingress YAML specifications identifying key fields: rules containing host definitions, paths array with Prefix or Exact matching, and backend service references.

We'll explore SSL and TLS termination as high-value exam content. The Ingress Controller handles encryption and decryption with external clients connecting over HTTPS while backend services use unencrypted HTTP inside the cluster. This centralizes certificate management instead of configuring every individual service. Know that Ingress uses Kubernetes Secrets to store TLS certificates and private keys referenced in the TLS section.

You'll master external access patterns that the exam tests extensively. ClusterIP for internal-only communication, NodePort for simple development exposure, LoadBalancer creating cloud load balancers per service getting expensive with multiple services, and Ingress providing layer 7 load balancing with single entry point for multiple services as the production solution. Exam tip: questions mentioning cost-effective solutions for multiple web applications point to Ingress.

We'll cover Azure-specific considerations including Application Gateway Ingress Controller as Azure's managed option using Application Gateway instead of running controllers in-cluster with tight Azure integration and Web Application Firewall capabilities. Know that AKS uses standard Kubernetes Ingress while Azure Container Apps uses its own ingress model.

The exam tests load balancing concepts with Ingress Controllers automatically load balancing requests across pod replicas. Session affinity requires specific configuration through annotations when applications need sticky sessions where same client requests always reach the same pod.

You'll understand Ingress annotations for extending functionality without changing application code. Common exam-relevant examples include rewrite rules for modifying request paths, response caching for performance, rate limiting for API protection, and authentication requirements. Know that annotations are controller-specific.

We'll cover troubleshooting scenarios the exam includes: users can't access applications requires checking if Ingress Controller runs, backend service exists with healthy endpoints, and DNS/host configuration matches. Some paths return 404 usually means Ingress rules don't cover all paths checking Prefix versus Exact matching. SSL not working requires verifying TLS secret exists in same namespace with correct certificate data.

The exam expects best practices: use namespaces appropriately with controller in its own namespace, apply least privilege with proper RBAC, centralize TLS certificate management integrating with Key Vault, use labels and selectors consistently, and monitor at Ingress layer integrating with Azure Monitor or Application Insights.

Master Ingress routing, SSL termination, and Azure service integration for the AZ-204!
