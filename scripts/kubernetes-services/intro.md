# Kubernetes Services - Introduction Script

**Duration:** 2-3 minutes
**Target:** AZ-204 candidates learning Kubernetes networking

---

## SLIDE 1: Title Slide
[On screen: "Kubernetes Services - Networking Made Simple"]

Hello everyone! Today we're diving into one of the most essential concepts in Kubernetes: Services. If you're preparing for the AZ-204 exam or working with Azure Kubernetes Service, understanding Services is absolutely critical. Let's explore how Kubernetes handles networking and service discovery.

---

## SLIDE 2: The Problem - Pod IP Addresses
[On screen: Diagram showing Pods with dynamic IP addresses being created and destroyed]

Here's the challenge: every Pod in Kubernetes gets its own IP address. Sounds great, right? Well, there's a catch. That IP address only exists for the lifetime of the Pod. When a Pod crashes and gets replaced, or when you scale your application, those IP addresses change.

So how do other parts of your application reliably communicate with these constantly changing Pods? This is exactly the problem that Services solve.

---

## SLIDE 3: What is a Kubernetes Service?
[On screen: Service icon with stable IP and DNS name connected to multiple Pods]

A Kubernetes Service is a networking abstraction that provides a stable IP address and DNS name for accessing a group of Pods. Think of it as a load balancer with built-in service discovery.

Services use label selectors to find their target Pods. This loose coupling means you can replace, scale, or update Pods without breaking connectivity. The Service stays constant while the Pods behind it can change dynamically.

---

## SLIDE 4: Service Type - ClusterIP
[On screen: Diagram showing ClusterIP Service with internal cluster communication]

Let's talk about the three main Service types you'll encounter. First up is ClusterIP, which is the default type.

ClusterIP Services get an IP address that's only accessible within the cluster. This is perfect for internal communication between microservices. For example, your frontend Pods can reliably communicate with your backend API using a ClusterIP Service, regardless of how many backend Pods are running or when they get replaced.

---

## SLIDE 5: Service Type - NodePort
[On screen: Diagram showing NodePort Service exposing port on all nodes]

Next is NodePort. This Service type exposes your application on a static port on each node in your cluster, typically in the range 30000 to 32767.

NodePort is useful for development and testing, or when you need direct access to your cluster without a cloud load balancer. Any traffic hitting any node's IP address on that specific port gets routed to your Pods.

---

## SLIDE 6: Service Type - LoadBalancer
[On screen: Diagram showing LoadBalancer Service with cloud provider integration]

The third type is LoadBalancer, and this is what you'll typically use in production environments on Azure Kubernetes Service.

When you create a LoadBalancer Service on AKS, Azure automatically provisions an Azure Load Balancer for you. This gives you a public IP address that distributes traffic across your Pods. It's the most straightforward way to expose applications to the internet on managed Kubernetes platforms.

---

## SLIDE 7: Service Discovery with DNS
[On screen: Diagram showing DNS resolution flow from Pod to Service]

One of Kubernetes' killer features is automatic service discovery through DNS. Every Service automatically gets a DNS entry in the cluster's internal DNS server.

This means your Pods can communicate using friendly DNS names instead of IP addresses. When you create a Service named "my-api," any Pod in the same namespace can reach it using that name. Kubernetes handles all the DNS resolution and routing behind the scenes.

---

## SLIDE 8: AZ-204 Exam Relevance
[On screen: List of AZ-204 topics related to Kubernetes Services]

For the AZ-204 exam, make sure you understand these key points:

- How to configure networking for containerized applications in AKS
- The differences between Service types and when to use each one
- How service discovery works with DNS
- How Services integrate with Azure Load Balancer
- Label selectors and how Services route traffic to Pods

These concepts frequently appear in exam scenarios about deploying and managing containerized solutions on Azure.

---

## SLIDE 9: What's Next
[On screen: "Hands-On Lab - Let's Build Services Together"]

Now that you understand the concepts, it's time to get hands-on. In our lab exercises, we'll create all three types of Services, explore DNS resolution, and see how traffic routing works in real-time.

You'll deploy Pods, create Services with different configurations, and test scenarios like Pod failures and scaling. This practical experience will solidify your understanding and prepare you for real-world scenarios.

Let's jump into the exercises!

---

## SLIDE 10: Summary
[On screen: Key takeaways bullet points]

Quick recap: Kubernetes Services provide stable networking endpoints for dynamic Pods. ClusterIP for internal communication, NodePort for direct access, and LoadBalancer for production external access. Service discovery happens automatically through DNS, making your applications resilient and scalable.

Alright, let's get building!
