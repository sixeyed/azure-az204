# Kubernetes ConfigMaps: Exercises Introduction

We've covered what ConfigMaps are and why externalizing configuration from container images is fundamental to cloud-native development. Now let's see ConfigMaps in action with a real application that reads configuration from multiple sources.

## What You'll Do

You'll start by running the configurable demo app with its default settings to establish a baseline. Then you'll deploy the app using a Deployment and add configuration directly in the Pod spec with environment variables.

Next, you'll create ConfigMaps that hold multiple configuration values and inject them as environment variables using the envFrom field. This is much cleaner than defining dozens of variables individually in your Deployment spec.

You'll then mount ConfigMaps as files in the container's filesystem, creating a complete JSON configuration file from ConfigMap data. This demonstrates how to handle complex configuration formats that don't fit well as flat environment variables.

You'll explore configuration hierarchy - understanding which settings take precedence when the same configuration exists in multiple sources. Environment variables from one ConfigMap and file mounts from another can coexist.

The lab challenge asks you to create ConfigMaps using imperative commands instead of YAML files. You'll use kubectl create configmap with the from-literal flag for key-value pairs and the from-file flag for file contents.

The key learning: ConfigMaps enable the same container image to run in development, staging, and production with different configurations - demonstrating the Twelve-Factor App methodology and enabling true infrastructure as code practices.
