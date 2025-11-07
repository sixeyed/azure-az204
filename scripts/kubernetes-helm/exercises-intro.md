We've covered how Helm is the package manager for Kubernetes that adds powerful templating on top of standard YAML, enabling flexible and reusable application definitions. Now let's work with Helm directly to install and manage applications.

We'll start by looking at some reference documentation to understand what's available in Helm, then move on to installing the Helm CLI which uses the same configuration as kubectl. Always use Helm version 3 or later, as earlier versions had a server component called Tiller with security concerns that version 3 removed completely.

Then we'll deploy a chart with default values, examining what's inside including the Chart file describing the application, the values file defining customizable settings, and template files containing Kubernetes objects with variables instead of hard-coded values. You'll install the chart creating a release, then explore the Kubernetes objects Helm created. Notice how object names include the release name enabling you to deploy the same chart multiple times with different configurations without conflicts.

Next, we'll install a release with custom values using the set flag to override default values. You'll see two completely independent deployments from the same chart running side by side with different replica counts and service ports. This demonstrates the power of Helm's templating approach.

From there, we'll work on upgrading a release with custom values. You'll explore upgrading and rollback functionality, learning that when upgrading releases, you need to use the reuse-values flag to merge new settings with previous custom values or they get reset to defaults. You'll use helm history to see all revisions and helm rollback to revert when upgrades cause issues.

Then we'll explore using chart repositories similar to Docker Hub but for Helm charts. After adding repositories and updating indices, you can search for charts, view available values, and install applications like Nginx Ingress Controller or Prometheus from pre-built charts published by the community.

The lab challenge asks you to install the Nginx Ingress Controller using a values file instead of multiple set flags, creating a new namespace and verifying the deployment. Finally, we'll do cleanup to remove all Helm releases. The key learning is that Helm simplifies complex deployments, provides repeatable installations, and makes sharing application packages easy, making it the standard package manager for Kubernetes essential for modern cloud-native development.
