# Kubernetes ConfigMaps - Introduction Script

**Duration:** 2-3 minutes
**Format:** Presentation with slides

---

## Slide 1: Title Slide
*[SHOW ON SCREEN: "Kubernetes ConfigMaps - Externalizing Application Configuration"]*

Welcome to this session on Kubernetes ConfigMaps! Today we're going to explore one of the most fundamental concepts in cloud-native application development: how to externalize configuration from your containerized applications.

---

## Slide 2: What Are ConfigMaps?

*[SHOW ON SCREEN: ConfigMap icon and definition]*

So, what exactly are ConfigMaps? A ConfigMap is a Kubernetes object that stores configuration data as key-value pairs. Think of it as a configuration store that lives outside your container images. This means you can keep your application code completely separate from your configuration settings.

ConfigMaps can store data in two main formats: simple key-value pairs, which your application reads as environment variables, or full text files, like JSON or YAML configuration files, which get mounted into your container's filesystem.

---

## Slide 3: Why ConfigMaps Matter

*[SHOW ON SCREEN: Diagram showing container image + ConfigMap = Configured application]*

Now, why are ConfigMaps so important? Let's think about the traditional approach. Without ConfigMaps, you'd need to rebuild your container image every time you changed a configuration setting. That's slow, error-prone, and goes against the principles of immutable infrastructure.

With ConfigMaps, you build your container image once, and then apply different configurations for different environments. Your dev, staging, and production environments all use the same container image, but with different ConfigMaps. This is the Twelve-Factor App methodology in action!

ConfigMaps also support separation of concerns. Your developers can focus on code, while your operations team manages configuration. No more hardcoded connection strings or environment-specific values baked into your images.

---

## Slide 4: ConfigMaps in Azure Kubernetes Service

*[SHOW ON SCREEN: Azure Kubernetes Service logo with ConfigMap integration]*

When working with Azure Kubernetes Service, or AKS, ConfigMaps become even more powerful. You can integrate them with Azure Key Vault for sensitive data, use them alongside Azure App Configuration, and manage them through Azure DevOps pipelines for automated deployments.

ConfigMaps work seamlessly with AKS managed identities, and they're essential for implementing proper configuration management in your AKS workloads.

---

## Slide 5: Two Methods of Using ConfigMaps

*[SHOW ON SCREEN: Split screen showing Environment Variables vs. Volume Mounts]*

There are two primary ways to use ConfigMaps. First, you can inject them as environment variables. This is perfect for simple settings like feature flags, API endpoints, or version numbers. Your application reads these just like any other environment variable.

Second, you can mount them as files in your container's filesystem. This approach is better for complex configuration files, like a complete JSON settings file or an XML configuration. You define the ConfigMap with the file contents, and Kubernetes mounts it at a path you specify.

---

## Slide 6: AZ-204 Exam Connection

*[SHOW ON SCREEN: AZ-204 exam topics checklist]*

For the AZ-204 exam, ConfigMaps are crucial because they demonstrate your understanding of several key objectives. You need to know how to implement containerized solutions, configure application settings, and manage configuration data across different environments.

The exam may test your knowledge of when to use ConfigMaps versus Secrets, how to mount configuration as volumes, and how to update running applications with new configuration. You'll also need to understand the relationship between ConfigMaps and environment variables, and how configuration hierarchy works.

---

## Slide 7: What You'll Learn Today

*[SHOW ON SCREEN: Lab objectives bullet points]*

In today's hands-on lab, you'll work with a real application that reads configuration from multiple sources. You'll create ConfigMaps using YAML manifests, inject them as environment variables, mount them as files, and see how configuration hierarchy affects which settings take precedence.

By the end of this lab, you'll be comfortable creating and managing ConfigMaps, and you'll understand the best practices for externalizing configuration in Kubernetes.

Let's get started!

---

*[TRANSITION TO: Lab exercises]*
