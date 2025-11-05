# Kubernetes ConfigMaps: AZ-204 Exam Focus

Great work! This ConfigMaps lab is essential for the "Implement containerized solutions" objective in the AZ-204 exam. Understanding how to externalize and manage application configuration is crucial for developing cloud-native solutions in Azure.

## What We'll Cover

We'll examine externalizing configuration as a core principle - your container image should be environment-agnostic, built once and used everywhere with only ConfigMaps changing. This demonstrates cloud-native patterns that appear throughout the exam.

We'll explore the critical difference between ConfigMaps and Secrets. ConfigMaps store non-sensitive data in plain text while Secrets provide basic encoding for sensitive information. Never store passwords or API keys in ConfigMaps - the exam tests whether you understand this security distinction.

You'll master two methods for consuming ConfigMap data: environment variables using env and envFrom fields, and volume mounts that create files in the container's filesystem. Know when environment variables require Pod restart for updates while volume mounts update automatically but applications must reload configuration.

The exam tests your knowledge of configuration hierarchy - understanding which sources take precedence when settings overlap. Different application frameworks have different hierarchies, and you need to know your application's order to configure correctly.

We'll cover creating ConfigMaps using both declarative YAML manifests for production and imperative kubectl commands for testing. Know the from-literal flag for key-value pairs, from-file for file contents, and from-env-file for property files.

You'll understand how ConfigMaps integrate with Azure services including Azure Key Vault for sensitive data via Secrets Store CSI driver, Azure DevOps for automated deployment, and Azure Monitor for tracking configuration changes and their impact.

Master ConfigMap management and configuration externalization for the AZ-204!
