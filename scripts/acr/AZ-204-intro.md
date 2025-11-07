Excellent work with the hands-on exercises! Now let's focus on what the AZ-204 exam expects you to know about Azure Container Registry.

ACR falls under the implement containerized solutions domain, which represents 15 to 20 percent of the exam. You'll face questions about creating registries, managing images, authentication methods, and integration with Azure services, so let's make sure you're ready for all of it.

When it comes to registry naming and access, you need to know the DNS structure inside and out. The exam will test whether you understand how a registry name becomes registry-name dot azurecr dot io, and how full image names are formatted with that domain. The naming rules are strict: globally unique across all of Azure, between 5 and 50 characters, and only lowercase letters and numbers. No hyphens allowed, which is actually a common gotcha since most Azure resources do allow hyphens in their names.

SKU feature comparison appears frequently on the exam. You must know the differences between Basic, Standard, and Premium tiers, particularly when to recommend Premium for specific scenarios. The key differentiators are geo-replication and private endpoints, which are only available in Premium. You should memorize the storage limits too: 10GB for Basic, 100GB for Standard, and 500GB for Premium. Scenario questions often present a requirement and ask which SKU you should use, so you need to match capabilities to business needs.

Authentication methods is heavily tested material. There are four approaches you need to know: individual Azure AD identity with az acr login, which is great for development but only gives you 3-hour tokens; service principals with username and password, which work well for CI/CD pipelines; admin accounts that are only for testing and not recommended for production; and managed identities for Azure services, which are the most secure option. The exam definitely wants you to recommend managed identities over service principals whenever possible.

The essential CLI commands appear on nearly every exam. You need to know how to create registries with az acr create, log in with az acr login, and use Docker commands to push and pull images. Building images in Azure with ACR Tasks is also important, along with managing repositories. Know the syntax cold because the exam tests specific parameter names and command structure.

ACR Tasks is an important feature that deserves special attention. It lets you build container images directly in Azure without needing Docker installed locally. The exam tests your knowledge of quick tasks using az acr build, multi-step tasks for complex workflows, and triggered tasks that run automatically when source code is committed or when base images are updated.

Integration with Azure services comes up in scenario questions throughout the exam. You need to know how to deploy from ACR to Azure Container Instances, configure ACR with Azure Kubernetes Service, and set up webhooks to trigger automation. The authentication flow and configuration requirements for each integration are important details to understand.

Image management best practices round out the exam content, including tagging strategies, retention policies, and security scanning. You might see questions about container image scanning for vulnerabilities or implementing automated cleanup of old images to manage storage costs effectively.

Throughout our review, we'll work through common exam scenarios and make sure you have the quick-reference commands memorized for test day. Ready to master ACR for the AZ-204? Let's dive into the exam content!
