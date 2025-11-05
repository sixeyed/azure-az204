# Helm Package Manager: Exercises Introduction

We've covered how Helm is the package manager for Kubernetes that adds powerful templating on top of standard YAML, enabling flexible and reusable application definitions. Now let's work with Helm directly to install and manage applications.

## What You'll Do

You'll start by installing the Helm CLI which uses the same configuration as kubectl. Always use Helm version 3 or later - earlier versions had a server component called Tiller with security concerns that version 3 removed completely.

Then you'll deploy your first chart examining what's inside: the Chart file describing the application, the values file defining customizable settings, and template files containing Kubernetes objects with variables instead of hard-coded values.

You'll install the chart with default values creating a release, then explore the Kubernetes objects Helm created. Notice how object names include the release name enabling you to deploy the same chart multiple times with different configurations without conflicts.

Next, you'll install the same chart again with custom configuration using the set flag to override values. You'll see two completely independent deployments from the same chart running side by side with different replica counts and service ports.

You'll explore upgrading and rollback functionality. When upgrading releases, use the reuse-values flag to merge new settings with previous custom values or they get reset to defaults. Use helm history to see all revisions and helm rollback to revert when upgrades cause issues.

You'll work with chart repositories similar to Docker Hub but for Helm charts. After adding repositories and updating indices, you can search for charts, view available values, and install applications like Nginx Ingress Controller or Prometheus from pre-built charts.

The lab challenge asks you to install the Nginx Ingress Controller using a values file instead of multiple set flags, creating a new namespace and verifying the deployment.

The key learning: Helm simplifies complex deployments, provides repeatable installations, and makes sharing application packages easy - it's become the standard package manager for Kubernetes essential for modern cloud-native development.
