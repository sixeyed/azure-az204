# Kubernetes ConfigMaps - Podcast Script

## Welcome and Introduction

Welcome to this podcast episode on Kubernetes ConfigMaps. If you're preparing for the Azure AZ-204 certification or working with containerized applications in Azure Kubernetes Service, understanding how to externalize and manage configuration is absolutely fundamental.

Today we're going to explore one of the most important concepts in cloud-native application development: how to separate configuration from code in containerized environments. This separation is central to building applications that work consistently across different environments.

## What Are ConfigMaps?

A ConfigMap is a Kubernetes object that stores configuration data as key-value pairs. Think of it as a configuration store that lives outside your container images. This means you can keep your application code completely separate from your configuration settings.

ConfigMaps can store data in two main formats. First, simple key-value pairs that your application reads as environment variables. Second, full text files like JSON or YAML configuration files that get mounted into your container's filesystem.

The beauty of ConfigMaps is that they enable you to build your container image once and use it everywhere - development, testing, production - with different configurations. The code is the same, the image is the same, only the configuration changes.

## Why ConfigMaps Matter

Let's think about the traditional approach to application configuration. Without ConfigMaps, you'd need to rebuild your container image every time you changed a configuration setting - a database connection string, an API endpoint, a feature flag. That's slow, error-prone, and goes against the principles of immutable infrastructure.

Imagine you're troubleshooting a production issue and you need to change a setting. Without ConfigMaps, you'd have to rebuild the entire image, push it to your registry, and redeploy. With ConfigMaps, you update the configuration and restart the application. The image never changes.

ConfigMaps also enable environment-specific configuration. Your development environment might point to a local database, staging to a test database, and production to the production database. Same application code, same container image, different ConfigMaps. This is the Twelve-Factor App methodology in action - specifically, the principle of strict separation between configuration and code.

Another key benefit is separation of concerns. Your developers can focus on application code without worrying about environment-specific details. Your operations team manages configuration appropriate for each environment. Configuration becomes data that operations manages, not code that developers must change.

## Two Methods of Using ConfigMaps

There are two primary ways to use ConfigMaps, and understanding both is essential for the AZ-204 exam.

The first method is injecting ConfigMap data as environment variables. This is perfect for simple settings like feature flags, API endpoints, version numbers, or any single-value configuration. Your application reads these just like any other environment variable - through standard environment variable APIs in whatever language you're using.

You can inject individual values using the env field in your Pod specification, referencing specific keys from a ConfigMap. Or you can inject all values from a ConfigMap at once using envFrom, which creates an environment variable for every key-value pair in the ConfigMap.

The second method is mounting ConfigMaps as files in your container's filesystem. This approach is better for complex configuration - complete JSON settings files, XML configuration, INI files, or any structured configuration format. You define the ConfigMap with the file contents, and Kubernetes mounts it at a path you specify in the container.

File mounting has some advantages. It supports complex, hierarchical configuration that doesn't fit well into flat environment variables. It's more secure because the configuration isn't visible to all processes in the container. And importantly, mounted files are automatically updated when you change the ConfigMap, whereas environment variables are set once at container startup.

## Creating ConfigMaps

ConfigMaps can be created in several ways, and the exam may test your knowledge of these different approaches.

The most common method in production is using YAML manifests. You define a ConfigMap object with a metadata section containing the name, and a data section containing your key-value pairs. This is declarative and fits well with GitOps practices where all your Kubernetes manifests are stored in version control.

For simple key-value pairs, the YAML is straightforward - each key followed by a colon and its value. For file contents, you use YAML's multiline string syntax with a pipe character, and indent the file contents beneath the key.

You can also create ConfigMaps imperatively using kubectl create configmap. This command has several useful flags. The from-literal flag lets you specify key-value pairs directly on the command line. The from-file flag creates a ConfigMap from a file, using the filename as the key and file contents as the value. The from-env-file flag reads a properties-style file with multiple key-value pairs.

Imperative creation is useful for quick testing or when you have existing configuration files you want to load into Kubernetes without templating them into YAML.

## ConfigMaps as Environment Variables

Let me walk through how environment variable injection works in practice.

In your Pod specification's container definition, you add an env or envFrom field. With env, you specify individual environment variables, each referencing a specific key from a ConfigMap using the valueFrom and configMapKeyRef syntax. This gives you fine-grained control over which ConfigMap values become which environment variables, and lets you rename them if needed.

With envFrom, you reference an entire ConfigMap, and Kubernetes automatically creates environment variables for all key-value pairs in that ConfigMap. The keys become the environment variable names, and the values become the environment variable values. This is more convenient when you have many settings, but be careful about naming conflicts - if a key matches an existing environment variable, you might override something important.

Environment variables are set when the container starts. They're part of the process's environment. If you update the ConfigMap after the container is running, those environment variables don't change in the running container. You must restart the container - typically by updating the Deployment which triggers a rolling update - for new values to take effect.

This immutability is actually useful for consistency. During a container's lifetime, its environment variables don't change unexpectedly. But it means configuration updates require Pod restarts.

## ConfigMaps as Volume Mounts

Volume mounting works differently and has some advantages for certain scenarios.

To mount a ConfigMap as a volume, you follow a two-step process. First, in the Pod specification's volumes section, you define a volume that references your ConfigMap by name. Then, in the container specification's volumeMounts section, you mount that volume to a specific path in the container's filesystem.

When the container starts, Kubernetes creates files in that mount path. For simple ConfigMaps, each key becomes a file where the filename is the key and the file contents are the value. For ConfigMaps with file-style data, you typically have one key representing the filename and its value is the file contents.

The mounted files are read-only by default, which is appropriate since they're configuration data, not writable storage. Your application reads these files like any other file on the filesystem.

Here's an important advantage: when you update a ConfigMap that's mounted as a volume, Kubernetes automatically updates the files in running containers. There's a short propagation delay - typically a few seconds to a minute - but the files update without restarting the container.

However, your application still needs to notice the file changed and reload the configuration. Some application frameworks support hot reload - they watch configuration files and automatically reload when they change. Others require explicit signals or restarts. But at least the files themselves update automatically, which is more than you get with environment variables.

## Configuration Hierarchy

Understanding configuration hierarchy is crucial for real-world applications and for the AZ-204 exam.

Most applications read configuration from multiple sources. They might have default values built into the code, read configuration files, load environment variables, and accept command-line arguments. When the same setting exists in multiple places, there's a priority order that determines which value wins.

A common hierarchy is: command-line arguments override environment variables, which override configuration files, which override default values. But the exact hierarchy depends on the application framework. ASP.NET Core follows one order. Spring Boot follows another. Node.js applications might be different still.

When you're using ConfigMaps, you need to understand your application's hierarchy to configure it correctly. If environment variables take precedence over files, and you set a value in both an envFrom ConfigMap and a volume-mounted ConfigMap, the environment variable wins. If files take precedence, the mounted file wins.

This becomes important when troubleshooting. You update a value in a ConfigMap file, but the application still uses the old value. Why? Because an environment variable is overriding it, and environment variables have higher priority in that application's hierarchy. Test your assumptions about configuration hierarchy - don't just guess.

## ConfigMaps versus Secrets

A critical distinction for the exam is knowing when to use ConfigMaps versus Secrets.

ConfigMaps are for non-sensitive configuration data. API endpoints, feature flags, application settings, timeout values, cache sizes - these are appropriate for ConfigMaps. ConfigMaps store data as plain text. Anyone with access to your Kubernetes cluster can read them using kubectl.

Secrets are for sensitive information like passwords, API keys, connection strings containing credentials, certificates, and tokens. Secrets provide basic encoding - base64, not encryption - and have additional access controls. They're stored more securely by Kubernetes, and can be encrypted at rest in etcd if configured.

For the exam, know that you should never store passwords, API keys, or sensitive credentials in ConfigMaps. If a scenario involves database passwords or API tokens, Secrets or Azure Key Vault is the answer, not ConfigMaps.

In Azure Kubernetes Service specifically, you can integrate with Azure Key Vault using the Secrets Store CSI driver. This lets you reference Key Vault secrets directly from your Pod specs without storing them in Kubernetes at all. This is considered best practice for production workloads with sensitive data.

## Updating Configuration

Let's talk about what happens when you need to update configuration in running applications.

If your Pods use environment variables from ConfigMaps, those environment variables don't automatically change in running Pods. Remember, environment variables are set at container startup and are immutable during the container's lifetime. To apply updated configuration, you must restart the Pods.

The typical approach is to update the Deployment. Even a minimal change to the Deployment spec - like adding an annotation - triggers a rolling update where Kubernetes gradually replaces old Pods with new ones that have the updated environment variables. This provides zero-downtime updates.

If your Pods use volume mounts, the files are automatically updated in running containers after a short delay. But your application must reload the configuration. How this works depends on your application framework. Some support hot reload where configuration changes are detected and applied automatically. Others require you to send a signal to the process or restart it manually.

For production applications, you need a strategy for configuration updates. Will you always restart Pods? Will you implement hot reload? Will you use a sidecar container to watch for changes and signal the main container? These are operational decisions you need to make.

## ConfigMaps in Azure Kubernetes Service

When working specifically with Azure Kubernetes Service, ConfigMaps work exactly the same as in any Kubernetes cluster - they're a standard Kubernetes feature. But you have additional integration options with Azure services.

You can use Azure DevOps or GitHub Actions to automate ConfigMap deployment as part of your CI/CD pipelines. Store ConfigMap YAML files in Azure Repos or GitHub alongside your application code, and apply them automatically during deployment.

For sensitive configuration, integrate with Azure Key Vault. The Azure Key Vault provider for Secrets Store CSI driver lets you mount Key Vault secrets as files in your containers, completely bypassing Kubernetes Secrets and ConfigMaps for sensitive data.

Azure App Configuration can also integrate with Kubernetes for more advanced configuration management scenarios, including feature flags and dynamic configuration.

And Azure Monitor can track configuration changes and correlate them with application behavior, helping you understand the impact of configuration changes on performance and reliability.

## Best Practices

Let me highlight best practices that are important for the exam and for production use.

First, never store sensitive data in ConfigMaps. Always use Secrets or Azure Key Vault for passwords, tokens, and credentials.

Second, use descriptive names for ConfigMaps. Something like "api-config-production" is much clearer than "config1". This becomes important when you have dozens of ConfigMaps across multiple applications.

Third, version your ConfigMaps or use labels to track versions. Some teams include version numbers in ConfigMap names like "app-config-v1" and "app-config-v2". This makes rollbacks easier when a configuration change causes problems.

Fourth, store ConfigMap YAML files in version control alongside your application code. This provides an audit trail of configuration changes and enables GitOps workflows where configuration changes go through the same code review process as application code.

Fifth, validate ConfigMaps before applying them. Make sure they have the correct format and all required keys. Consider using admission controllers or policy engines to enforce configuration standards.

Sixth, document your application's configuration hierarchy. Make it clear which configuration sources take precedence so your team doesn't waste time debugging why configuration isn't being applied.

And seventh, in Azure Kubernetes Service, use managed identities and Azure RBAC to control who can create and modify ConfigMaps. Configuration changes can break applications just as effectively as code changes, so they need similar governance.

## Common Exam Scenarios

Let me walk through typical exam scenarios involving ConfigMaps.

Scenario one: "An application needs different database connection strings for development, staging, and production environments. The solution must not require rebuilding the container image. What approach should you use?"

The answer involves creating environment-specific ConfigMaps - one for dev, one for staging, one for production - each containing the appropriate connection string. The same container image is deployed to all environments, but with different ConfigMaps providing environment-specific values.

Scenario two: "After updating a ConfigMap with new settings, the application still uses the old values. What could be the cause?"

If the application uses environment variables from the ConfigMap, the Pods must be restarted for changes to take effect. If it uses volume mounts, check whether the application supports hot reload, or if it needs to be signaled or restarted to reload configuration.

Scenario three: "You need to store database passwords for an application running in Kubernetes. Should you use ConfigMaps?"

No. Passwords are sensitive data and should never be stored in ConfigMaps. Use Kubernetes Secrets or, better yet, Azure Key Vault with the Secrets Store CSI driver.

Scenario four: "An application requires a complete JSON configuration file with nested settings. What's the best way to provide this using ConfigMaps?"

Mount the ConfigMap as a volume. Create a ConfigMap with the JSON file contents using YAML's multiline string syntax, then mount it to a path where the application expects to find the configuration file.

## Troubleshooting

For the exam, know how to troubleshoot common ConfigMap issues.

If configuration isn't being applied, first verify the ConfigMap exists and contains the expected data using kubectl get configmap and kubectl describe configmap.

Check that the Pod specification correctly references the ConfigMap - the name must match exactly, and both must be in the same namespace.

Use kubectl exec to run commands inside the container and verify environment variables are set correctly or files are mounted at expected paths.

If updates aren't taking effect, remember the difference between environment variables and volume mounts. Environment variables require Pod restart. Volume mounts update automatically but applications must reload configuration.

If you get "ConfigMap not found" errors, verify the ConfigMap and Pod are in the same namespace, or use a fully qualified name if they're in different namespaces.

## Key Takeaways for the AZ-204 Exam

Let me summarize what you absolutely must understand for exam success.

ConfigMaps store non-sensitive configuration data. They externalize configuration from container images, enabling environment-specific settings without image rebuilds.

ConfigMaps can be consumed as environment variables or as files through volume mounts. Environment variables require Pod restart for updates. Volume mounts update automatically but applications must reload configuration.

Always use Secrets or Azure Key Vault for sensitive data, never ConfigMaps. This is a fundamental security practice.

ConfigMaps support cloud-native patterns, particularly the Twelve-Factor App principle of configuration separation. The same image runs in all environments with different ConfigMaps.

In Azure Kubernetes Service, ConfigMaps integrate with Azure DevOps, Azure Key Vault, and other Azure services for comprehensive application lifecycle management.

Understand configuration hierarchy - know that applications often read from multiple sources and have precedence rules determining which values win.

Know how to create ConfigMaps both declaratively with YAML and imperatively with kubectl commands. Both approaches have their uses.

## Final Thoughts

Kubernetes ConfigMaps are a fundamental building block for cloud-native applications. They enable proper separation of configuration and code, support environment-specific deployments, and integrate with broader Azure ecosystems.

For the AZ-204 exam, ConfigMaps demonstrate your understanding of containerized solutions, configuration management, and cloud-native patterns. Questions about externalizing configuration, managing environment-specific settings, or securing application data often involve ConfigMaps or related concepts.

The key is understanding not just what ConfigMaps are, but when and how to use them effectively. Practice creating ConfigMaps both ways, injecting them as environment variables and mounting them as files. Experience the difference in update behavior. Understand the security boundaries between ConfigMaps and Secrets.

This hands-on experience gives you the confidence to answer exam questions correctly and the skills to build production applications properly.

Thanks for listening to this episode on Kubernetes ConfigMaps. I hope this gives you both the conceptual understanding and practical knowledge you need for AZ-204 success. Good luck with your certification journey!
