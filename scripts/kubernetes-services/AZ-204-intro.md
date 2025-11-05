# Kubernetes Services: AZ-204 Exam Focus

Great work! This Services lab is crucial for the "Implement containerized solutions" objective in the AZ-204 exam. Understanding service networking and discovery is essential for Azure Kubernetes Service.

## What We'll Cover

We'll examine Service types that the exam tests extensively. ClusterIP provides internal-only access as the default type for inter-service communication within the cluster. NodePort exposes services on node ports for development but rarely used in production. LoadBalancer creates cloud load balancers as the standard for external access in AKS. ExternalName maps services to external DNS names for integration with external services.

We'll explore service discovery mechanisms where Kubernetes DNS provides automatic service name resolution, environment variables inject service endpoints into pods, and cluster DNS resolves service-name.namespace.svc.cluster.local to service IPs.

You'll master load balancing and traffic management with services distributing requests across healthy backend pods, session affinity controlling sticky sessions when needed, and readiness probes determining which pods receive traffic from services.

The exam tests Azure Load Balancer integration where LoadBalancer services automatically provision Azure Load Balancers, public IP addresses get assigned from Azure IP pools, and load balancer SKUs determine features and pricing. Know that multiple LoadBalancer services can share a single Azure Load Balancer using annotations.

We'll cover endpoints and endpoint slices where services maintain lists of pod IPs matching selectors, endpoints update automatically as pods are created or deleted, and endpoint slices provide scalability for services with many backends.

You'll understand headless services for stateful workloads where ClusterIP None provides direct pod IP discovery, StatefulSets use headless services for predictable network identities, and DNS returns individual pod IPs instead of service IP enabling custom load balancing.

The exam includes troubleshooting scenarios: services not routing traffic often indicates selector mismatches or missing pods, connection timeouts suggest health probe failures or network policy blocks, and DNS resolution failures point to CoreDNS issues or incorrect service names.

Master Service types, load balancing, and Azure integration for the AZ-204!
