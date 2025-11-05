# Kubernetes Namespaces: AZ-204 Exam Focus

Great work! This namespaces lab is fundamental for the "Implement Azure solutions" domain in the AZ-204 exam. Understanding resource organization and isolation is crucial for developing containerized applications in Azure Kubernetes Service.

## What We'll Cover

We'll examine resource organization strategies that the exam tests extensively. Namespace-per-application for production clusters provides clear boundaries for policies and access controls. Namespace-per-environment for non-production clusters enables cost-efficient resource sharing between development, testing, and staging.

We'll explore Role-Based Access Control as namespaces are the fundamental unit for Kubernetes RBAC. Roles and RoleBindings are scoped to specific namespaces, integrating with Azure Active Directory to map identities to namespace-level permissions. Junior developers get limited dev namespace access while senior engineers can deploy to production.

You'll master resource quotas and limits applied per namespace including total CPU and memory limits, pod and service count restrictions, and storage resource constraints. This prevents any single application from consuming all cluster resources in shared environments.

The exam tests environment separation strategies: separate clusters for maximum security, single cluster with namespace separation for cost efficiency, or namespace-per-environment-per-app combining both approaches. Know Azure-specific integrations like Azure AD pod identity, Key Vault per namespace, and Azure Monitor with namespace filtering.

We'll cover service discovery and DNS where services reference each other by simple names within the same namespace but require fully-qualified domain names across namespaces using the format service-name.namespace.svc.cluster.local. Always use FQDNs in production configurations stored in ConfigMaps or Azure App Configuration.

You'll understand deployment patterns including proper manifest organization with namespace definitions, using kubectl with directories and -n flags, and Azure DevOps integration deploying to specific namespaces with approval gates for production.

The exam includes monitoring and logging with Azure Monitor Container Insights filtering by namespace, Log Analytics queries aggregating per namespace, and cost allocation based on namespace consumption for chargeback models.

Master namespace strategies, RBAC integration, and Azure service connections for the AZ-204!
