Great work completing the hands-on exercises. Now let's shift focus to what you need to know about Azure Container Instances for the AZ-204 certification exam.

ACI appears under the implement containerized solutions domain and represents 5 to 10 percent of the exam content. While that might not sound like much, the questions are very specific and test your understanding of when to use ACI versus other services like App Service or AKS.

The most critical exam topic is knowing when to use ACI versus other compute options. The exam loves scenario-based questions where you need to choose the right service, so you need to recognize the specific keywords that point to ACI. Look for words like simple, temporary, task, or single container in the question. These hint at ACI being the right answer. On the other hand, if you see requirements for orchestration, scaling multiple containers, or production workloads, those scenarios typically call for Kubernetes or App Service instead.

Azure CLI commands for creating and deploying containers are heavily tested. You need to know the az container create command inside and out, including all its parameters. Resource groups, images, ports, and DNS names are the basics, but you also need to know CPU and memory allocation flags, OS type specifications, and environment variables. Speaking of environment variables, the exam specifically tests whether you understand the difference between regular environment variables and secure ones for sensitive data like passwords or API keys.

Container networking is another frequently tested topic. You need to understand the difference between public and private IP addresses, how DNS name configuration works, and how to expose ports correctly. VNet integration is important too, and there's a common exam trick question about private ACI containers requiring dedicated subnets. Make sure you know that one.

Container groups come up regularly on the exam. These let you deploy multiple containers together that share lifecycle and network resources. This concept often appears in questions about sidecar patterns, where you have a main application container running alongside a logging or monitoring container. Understanding how containers within a group can communicate over localhost is key.

Restart policies are tested on almost every exam. You need to know when to use Always, OnFailure, or Never based on your scenario. Always is for web services that should stay running, OnFailure is for tasks that might fail and need retry logic, and Never is for one-time batch jobs that shouldn't restart even if they fail.

Storage is another key topic that trips people up. The exam specifically tests whether you know that ACI only supports Azure Files for persistent volumes, not Azure Disk. That's a classic exam gotcha. You need to understand how to mount Azure Files shares to your containers and what the limitations are.

Integration with Azure Container Registry rounds out the ACI exam content. You need to know how to pull private images securely, either using explicit credentials or using managed identities. The exam definitely prefers managed identities as the more secure, exam-friendly approach, so recommend that whenever possible.

We'll wrap up with common exam scenarios and quick reference commands to help you memorize the syntax you'll need on test day. Ready to master ACI for the AZ-204? Let's dive into the exam-focused content!
