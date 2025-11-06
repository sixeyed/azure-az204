# AKS Ingress and Application Gateway - Podcast Script

## Welcome and Introduction

Welcome to this podcast episode on Ingress and Application Gateway in Azure Kubernetes Service. Today we're exploring how to efficiently route network traffic into a Kubernetes cluster using Azure Application Gateway as an ingress controller. Whether you're preparing for the Azure AZ-204 certification or building production Kubernetes applications, understanding ingress patterns is essential for creating scalable, production-ready deployments.

## The Networking Challenge in Kubernetes

When you start running applications on Kubernetes, you quickly face a fundamental networking challenge. How do you expose your applications to users on the internet?

The simplest approach is to use LoadBalancer Services. When you create a LoadBalancer Service in Kubernetes, your cloud provider provisions a load balancer and gives you a public IP address. Traffic to that IP address routes to your application's pods. This works fine for a single application.

But imagine you're running multiple applications on a single cluster. Maybe you have a main web application, an API backend, and an administrative portal. Do you really want to manage three separate load balancers with three random IP addresses? Probably not. You'd have to set up three different DNS entries, manage three different IP addresses, and potentially pay for three separate load balancers.

This approach doesn't scale well. What you really want is a single entry point that can route incoming traffic based on HTTP request attributes like domain names or URL paths.

## Understanding Ingress

This is where ingress comes in. Ingress is a Kubernetes concept that provides HTTP and HTTPS routing to services based on rules you define. Instead of having multiple IP addresses, you have a single entry point that routes traffic based on the hostname or URL path in the HTTP request.

With ingress, a single Kubernetes cluster can serve multiple domains. You might have myapp.com, api.myapp.com, and otherapp.co.uk all pointing to the same public IP address, with ingress rules that route each domain to the appropriate service within your cluster.

To make ingress work, you need an ingress controller. The ingress controller is the actual piece of software that implements the ingress rules. There are many ingress controllers available - NGINX, Traefik, HAProxy, and others. Each reads the Ingress objects you create in Kubernetes and configures itself accordingly.

## Azure Application Gateway

In Azure, you can use Azure Application Gateway as your ingress controller. Application Gateway is a web traffic load balancer that enables you to manage traffic to your web applications. It's much more than a standard load balancer - it operates at layer 7, the application layer, and can make routing decisions based on HTTP request attributes.

Let me explain what layer 7 means. Network traffic operates at different conceptual layers. Layer 4, the transport layer, deals with TCP and UDP connections - it knows about IP addresses and ports, but it doesn't understand HTTP. Layer 7, the application layer, understands HTTP protocols. It can read the HTTP headers, examine the hostname or URL path, and make intelligent routing decisions based on that information.

This means Application Gateway can do things a basic load balancer cannot. It can route requests for different domains to different backends. It can route requests based on URL paths. It can terminate SSL connections, offloading that work from your application. It can even include a Web Application Firewall that protects against common web exploits like SQL injection and cross-site scripting.

## Application Gateway Ingress Controller

When you combine Application Gateway with AKS, the Application Gateway acts as an ingress controller through a component called AGIC - the Application Gateway Ingress Controller.

Here's how it works: AGIC runs as a pod inside your AKS cluster. It watches for Ingress objects that you create in Kubernetes. When you create or modify an Ingress object, AGIC sees the change and automatically configures the Application Gateway with the appropriate routing rules, backend pools, and health probes.

This is powerful because it bridges the gap between Kubernetes and Azure. You define your routing rules using standard Kubernetes Ingress resources, and AGIC translates those into Application Gateway configuration. No manual configuration needed. No clicking through the Azure Portal to set up routing rules. Everything is managed through Kubernetes manifests, which means your infrastructure is defined as code.

## Building the Architecture

Let me walk you through how to build this architecture. The process involves several steps, and understanding the order and dependencies is important.

### Creating the Virtual Network

We start by creating a Virtual Network. The Application Gateway needs to be deployed into the same VNet you'll use for your AKS cluster, so we create this infrastructure first.

When you create the VNet, you specify an address space using CIDR notation, something like 10.2.0.0/16. This provides a large private IP range - in this case, about 65,000 addresses. Within that VNet, you need to create two subnets: one for AKS and one for Application Gateway.

The AKS subnet needs to be fairly large if you're using the Azure CNI network plugin. With Azure CNI, each pod in your cluster gets an IP address from the VNet, so you need enough addresses for all your nodes and all the pods they might run. A subnet with a /21 CIDR provides over 2000 addresses, which is appropriate for a moderate-sized cluster.

The Application Gateway needs its own dedicated subnet. It cannot share a subnet with other resources. The Application Gateway subnet can be smaller - a /24 CIDR providing 256 addresses is typically sufficient.

### Creating the Public IP

Application Gateway needs a public IP address since it's going to be the entry point for traffic from the internet. You create a Standard SKU public IP because Application Gateway v2 only works with Standard SKUs.

When you create the public IP, you can also set a DNS name label. This gives you a friendly DNS name instead of just an IP address. The full DNS name will be something like your-label.region.cloudapp.azure.com. This is what you'll point your application domains to.

### Creating Application Gateway

Now you create the Application Gateway itself. This is an unusual Azure resource - the Portal setup has several configuration pages that must be completed in order. The Basics page is where you choose between fixed scale and autoscaling, select a tier, and specify the VNet. The Frontends page is where you configure the public IP address. The Backends page is where you define backend pools, though these will be empty initially because AGIC will configure them later. The Configuration page is where you set up routing rules.

However, when creating Application Gateway from the CLI for use with AKS, you need to ensure you're using a v2 SKU - either Standard_v2 or WAF_v2. The older v1 SKU is not compatible with the AGIC add-on.

The creation process takes several minutes because Application Gateway is a complex resource with multiple backend components. While it's creating, you can move on to creating the AKS cluster.

### Creating the AKS Cluster

For the AKS cluster, you need to use the Azure network plugin and deploy the cluster into the AKS subnet you created earlier. This is essential for the Application Gateway integration to work properly.

When you integrate AKS with a VNet, the cluster needs permission to manage network resources. Azure handles this by creating role assignments automatically, but your account needs elevated permissions in the subscription - typically Contributor or Owner - for this to work. You might see a message about waiting for Azure AD role assignments to propagate, which is Azure setting up these permissions.

### Integrating with AGIC

Once both the Application Gateway and AKS cluster are ready, you enable the Application Gateway Ingress Controller add-on. This installs AGIC into your cluster and establishes the connection between AKS and the Application Gateway.

The setup takes a few minutes as Azure installs the controller, configures permissions, and verifies connectivity. What you're creating here is a production-grade deployment pattern. AGIC will automatically configure the Application Gateway based on Kubernetes Ingress resources you create, completely eliminating manual configuration.

## Deploying an Application

Once the infrastructure is ready, deploying an application and exposing it through ingress is straightforward.

First, you deploy your application to Kubernetes. This typically involves creating a Deployment for your application pods and a Service to expose them within the cluster. You use a ClusterIP Service, which means the service is only accessible from within the cluster - it doesn't get a public IP on its own.

Then you create an Ingress object. The Ingress specifies the rules for routing traffic to your service. You define which hostname the Ingress responds to, and which service receives the traffic for that hostname.

When you apply the Ingress object, AGIC sees it and springs into action. It configures the Application Gateway with a backend pool pointing to your AKS nodes, sets up health probes to check if your pods are healthy, creates HTTP settings for how the Application Gateway should communicate with the backends, and adds routing rules that match incoming requests to the backend pool.

Within a minute or two, the configuration is complete and your application is accessible via the Application Gateway's public IP and DNS name. When users make requests to your application's domain, the traffic routes to Application Gateway, which forwards it to your Kubernetes service, which load balances it across your pods.

## How Traffic Flows

Let's trace the path of a request through this architecture to understand how all the pieces fit together.

A user types your application's domain name into their browser. DNS resolves that domain to the public IP address of your Application Gateway. The user's browser sends an HTTP request to that IP address. Application Gateway receives the request and examines the Host header to see which domain was requested. Based on the routing rules configured by AGIC, it determines which backend pool should handle this request.

Application Gateway forwards the request to one of the nodes in your AKS cluster. The Azure CNI network plugin ensures that traffic can route directly to pods, so the node forwards the request to one of your application's pods. The pod processes the request and sends a response back through the same path.

Application Gateway also performs health checks. It periodically probes your application to ensure it's healthy. If a pod becomes unhealthy, Kubernetes stops routing traffic to it, and Application Gateway's health probes will reflect this change.

## The Portal Configuration

After deploying an application with ingress, it's valuable to explore the Application Gateway configuration in the Azure Portal to understand what AGIC has created.

In the Backend Pools section, you'll see that AGIC has automatically created a backend pool. The pool contains IP addresses - these are the IP addresses of your AKS nodes. In the Backend Health section, you can see the results of health probes. If everything is working correctly, all your backends should show as healthy.

The HTTP Settings section shows how Application Gateway communicates with the backends - which ports, protocols, and timeout settings to use. The Routing Rules section shows how incoming requests are matched to backend pools. The Listeners section shows which ports and protocols Application Gateway is listening on.

Understanding this configuration helps you troubleshoot issues and optimize your deployments. You can see exactly how AGIC translated your Kubernetes Ingress resources into Application Gateway configuration.

## Advantages of This Architecture

This architecture provides several significant advantages for production deployments.

Single Entry Point: You have one public IP address for all your applications, making DNS management much simpler. You can route multiple domains and subdomains to the same IP.

Automatic Configuration: AGIC handles all the Application Gateway configuration automatically. You define everything in Kubernetes manifests, and the controller keeps Application Gateway synchronized. This is infrastructure as code at its finest.

Layer 7 Routing: You can route based on hostnames, URL paths, HTTP headers, and other application-layer attributes. This enables sophisticated routing patterns for microservices architectures.

SSL Termination: Application Gateway can terminate SSL connections, offloading that cryptographic work from your application. This improves performance and simplifies certificate management.

Web Application Firewall: You can enable WAF on Application Gateway to protect against common web exploits. This provides an additional layer of security in front of your applications.

Scalability: Application Gateway can autoscale to handle increased traffic, and Kubernetes can scale your pods horizontally. Both layers can scale independently based on demand.

## Relevance to the AZ-204 Exam

Understanding AKS ingress and Application Gateway is important for the Azure AZ-204 Developer Associate certification. Let me connect these concepts to specific exam objectives.

### Implementing Containerized Solutions

The exam tests your knowledge of deploying and managing containers using Azure Kubernetes Service. You need to understand how to create AKS clusters with specific network configurations, the differences between network plugins, how to integrate AKS with existing Azure Virtual Networks, how to manage AKS add-ons, and how to work with kubectl to deploy applications.

Key concepts for the exam include knowing when to use Azure CNI versus kubenet network plugins, understanding VNet integration requirements and subnet sizing, using Azure CLI to manage AKS resources, and deploying applications to AKS using kubectl.

### Connecting Azure Services

The exam tests your understanding of how to expose applications and route traffic. You need to know about Application Gateway as a Layer 7 load balancer, public IP address configuration, DNS configuration for Azure resources, integration between multiple Azure services, and using add-ons to extend AKS functionality.

Important concepts include the difference between Layer 4 and Layer 7 load balancing, when to use Application Gateway versus Azure Load Balancer, the difference between public IP SKUs, how routing rules and backend pools work, and health probe configuration.

### Network Security

The exam includes questions about Virtual Network segmentation, proper IP address planning, role-based access control for service principals, and secure communication between Azure services.

### Common Exam Question Patterns

Let me share some typical question patterns you might see on the exam.

A scenario-based question might say: "You need to expose multiple web applications running on AKS using a single public IP address and route traffic based on the domain name. Which Azure service should you use?" The answer is Azure Application Gateway with Ingress Controller.

Another scenario might be: "You're deploying an AKS cluster that needs to integrate with existing Azure networking infrastructure. Which network plugin should you use?" The answer is Azure CNI.

Or: "What is required to allow AKS to manage Application Gateway routing automatically?" The answer is the Application Gateway Ingress Controller add-on.

### Understanding Service Types

The exam often tests your understanding of when to use different Kubernetes service types.

NodePort exposes the service on each node's IP at a static port. This is rarely used in production because it requires managing individual node IPs.

LoadBalancer creates a cloud load balancer with a dedicated public IP. This is simple but doesn't scale well for many applications because you need multiple load balancers and IP addresses.

Ingress uses a single load balancer or gateway with routing rules. This is the production best practice because it consolidates traffic through a single entry point with sophisticated routing capabilities.

### Network Plugin Comparison

Understanding the differences between network plugins is important for the exam.

Azure CNI gives each pod an IP address from the VNet. This provides direct network communication and better performance, but requires more IP addresses. Pods are directly addressable from other resources in the VNet. This is what we used in our architecture.

Kubenet uses NAT for pods. Nodes get VNet IPs, but pods do not. This requires fewer IP addresses but adds an additional hop in routing and can complicate network policies.

The exam might present a scenario where you need to choose between these plugins based on requirements like IP address availability or performance needs.

## Practical Exam Preparation

To prepare for the exam, focus on understanding the "why" behind architectural decisions. Don't just memorize commands - understand why you'd choose Application Gateway over a simple LoadBalancer, why subnet sizing matters, and how the different components work together.

Remember SKU requirements. Application Gateway needs Standard_v2 or WAF_v2 to work with AKS. The older v1 SKU is not compatible with AGIC.

Understand the creation order and dependencies. You need a resource group first, then public IP, then VNet and subnets, then Application Gateway, then AKS cluster, then enable the AGIC add-on, then deploy applications, and finally create Ingress resources. Each step depends on the previous ones.

Practice Azure CLI commands. The exam may include questions where you need to identify correct command syntax or parameters.

## Real-World Applications

Beyond the exam, think about how you'd use these patterns in production scenarios.

For multi-tenant applications, you could run one AKS cluster serving multiple customers with different domains, all routing through a single Application Gateway.

For microservices architectures, you could route to different services based on URL paths. Requests to /api go to your API service, /admin goes to your administrative portal, and everything else goes to your main web application.

For blue-green deployments, you could use Ingress to switch traffic between different versions of your application. Deploy the new version alongside the old one, then update the Ingress rules to switch traffic.

For cost optimization, you could consolidate multiple applications behind a single Application Gateway instead of deploying separate load balancers for each application.

## Related Topics

To fully prepare for AKS-related exam questions, also review Azure Container Registry integration with AKS, AKS scaling options like cluster autoscaler and horizontal pod autoscaler, AKS monitoring with Azure Monitor and Container Insights, AKS security features including Azure Policy and Pod Security Standards, storage options for AKS like Azure Disks and Azure Files, and secret management with Azure Key Vault.

Each of these topics builds on the foundations we've covered today.

## Key Takeaways

Let me summarize the essential points about AKS Ingress and Application Gateway.

Ingress provides a way to expose multiple applications through a single entry point, with routing based on HTTP attributes. This is more scalable and manageable than using multiple LoadBalancer services.

Application Gateway is a Layer 7 load balancer that can make routing decisions based on HTTP request attributes. It provides features beyond basic load balancing, including SSL termination and Web Application Firewall capabilities.

The Application Gateway Ingress Controller bridges Kubernetes and Azure, automatically configuring Application Gateway based on Ingress objects you create in Kubernetes. This provides infrastructure as code for your routing configuration.

Network planning is important. You need properly sized subnets for both AKS and Application Gateway, and they must be in the same VNet. Azure CNI requires more IP addresses but provides better performance and simpler networking.

For the AZ-204 exam, understand the architecture, know when to use ingress versus other approaches, be familiar with Azure CLI commands, and understand how the different components integrate.

## Final Thoughts

Ingress and Application Gateway represent a production-grade pattern for exposing Kubernetes applications in Azure. The architecture provides scalability, security, and sophisticated routing capabilities while maintaining infrastructure as code principles.

For the AZ-204 exam, this topic tests both your Kubernetes knowledge and your understanding of Azure networking services. The exam includes scenario-based questions that require you to choose appropriate architectures based on requirements, so understanding the trade-offs between different approaches is crucial.

As you prepare for the exam, practice building these architectures yourself. Create the infrastructure, deploy applications, create Ingress resources, and explore the resulting Application Gateway configuration. This hands-on experience will give you the practical knowledge you need both for the exam and for real-world Azure development.

Thanks for listening to this episode on AKS Ingress and Application Gateway. I hope this gives you a solid understanding of how to expose Kubernetes applications using Azure Application Gateway and how these concepts relate to the AZ-204 certification. Good luck with your studies!
