We've covered what ConfigMaps are and why externalizing configuration from container images is fundamental to cloud-native development. Now let's see ConfigMaps in action with a real application that reads configuration from multiple sources.

We'll start by exploring the API specs to understand how ConfigMaps are structured in Kubernetes. Then we'll run the configurable demo app with its default settings to establish a baseline and see how the application behaves without any external configuration.

From there, we'll move on to setting config with environment variables in the Pod spec, adding configuration directly to the Deployment. This gives you a feel for how environment variables work, though it's not the most maintainable approach for larger applications.

Next, we'll improve our approach by setting config with environment variables in ConfigMaps. This is much cleaner than defining dozens of variables individually in your Deployment spec, and it lets you manage configuration separately from your Pod definitions.

Then we'll explore a more sophisticated pattern by setting config with files in ConfigMaps. You'll mount ConfigMaps as files in the container's filesystem, creating complete JSON configuration files from ConfigMap data. This demonstrates how to handle complex configuration formats that don't fit well as flat environment variables, and you'll see how configuration hierarchy works when the same settings appear in multiple sources.

The lab challenge asks you to create ConfigMaps using imperative commands instead of YAML files, using kubectl create configmap with flags for different content types. Finally, we'll do cleanup to remove all the resources we've created. The key learning here is that ConfigMaps enable the same container image to run in development, staging, and production with different configurations, demonstrating the Twelve-Factor App methodology and enabling true infrastructure as code practices.
