# Kubernetes Namespaces: Exercises Introduction

We've covered how namespaces are virtual clusters within your physical cluster that provide organization and isolation. Now let's explore how Kubernetes uses namespaces and how to manage applications across them.

## What You'll Do

You'll discover built-in namespaces including default where your deployments land, kube-system containing Kubernetes infrastructure components, and understanding that the -n flag tells kubectl which namespace to use.

You'll learn to work with system resources by viewing logs from kube-system DNS servers and understanding how namespaces affect every kubectl command requiring explicit namespace specification.

Then you'll explore kubectl contexts that set default namespaces avoiding tedious -n flags on every command. You'll change contexts to kube-system seeing system pods by default, then switch back to default for safety since working in kube-system risks breaking critical infrastructure.

You'll deploy pods to different namespaces using the same YAML specification demonstrating complete isolation. Using --all-namespaces flag shows resources across the entire cluster organized by namespace.

Next, you'll deploy complete applications with their own namespace definitions, using alphabetically-ordered filenames ensuring namespaces exist before resources are created. You'll see how namespace organization reduces the need for complex label selectors.

You'll understand cross-namespace DNS resolution where local service names only work within the same namespace, requiring fully-qualified domain names (service.namespace.svc.cluster.local) for cross-namespace communication.

The lab challenge asks you to discover and install kubens and kubectx tools that dramatically simplify namespace and context switching, saving time in multi-cluster, multi-namespace environments.

The key learning: Namespaces provide logical isolation for applications and environments, enable proper security boundaries with RBAC, and allow resource quotas preventing any single application from consuming all cluster resources - essential for multi-tenant Kubernetes clusters.
