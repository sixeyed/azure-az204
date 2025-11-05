# Kubernetes Deployments: AZ-204 Exam Focus

Great work! This Deployments lab is crucial for the "Implement container solutions" objective in the AZ-204 exam. Understanding Deployment creation, scaling, and updates is fundamental to managing applications in Azure Kubernetes Service.

## What We'll Cover

We'll examine the critical difference between declarative and imperative management. Imperative commands like kubectl scale work for quick testing but declarative YAML manifests stored in source control are production-appropriate, fitting CI/CD pipelines and providing audit trails.

We'll explore deployment strategies that the exam tests extensively. Rolling updates gradually replace Pods maintaining availability when both versions can coexist briefly. Recreate strategy kills all Pods before creating new ones causing downtime but ensuring only one version runs, needed for database schema changes. Blue-green deployments use multiple Deployments with Service label selector switching for instant rollback capability.

You'll master scaling applications both manually by updating replica count in Deployment YAML and automatically using Horizontal Pod Autoscaler that scales based on CPU utilization or custom metrics. Know that HPA requires resource requests defined in Pod specs to work.

The exam tests your understanding of application lifecycle management: deploying with YAML manifests, updating by modifying container images or configuration, monitoring with kubectl rollout status and history commands, and rolling back with kubectl rollout undo including the to-revision flag for specific revisions.

We'll cover labels and selectors as fundamental to how Deployments work. Deployments use selectors to find Pods, Services use selectors to route traffic, and labels in Pod templates must match Deployment selectors or configuration fails validation.

You'll understand health checks integration - liveness probes that restart unhealthy Pods and readiness probes that ensure traffic only goes to ready Pods. During rolling updates, readiness probes are crucial as new Pods must pass checks before old Pods terminate ensuring zero downtime.

The exam includes resource management with requests as minimum guaranteed resources for scheduling decisions and limits as maximum resources preventing single Pods from consuming all node resources. Know that resource requests are essential for HPA to function.

We'll cover Azure integration including how Deployments in AKS pull images from Azure Container Registry using managed identities, monitoring with Azure Monitor Container Insights, injecting secrets from Azure Key Vault, and CI/CD pipelines via Azure DevOps or GitHub Actions applying updated manifests.

Master Deployment strategies, scaling, and lifecycle management for the AZ-204!
