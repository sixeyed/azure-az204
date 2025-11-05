# Kubernetes Namespaces - Introduction Script
## Duration: 2-3 minutes

---

## SLIDE 1: Title Slide
**[ON SCREEN: "Kubernetes Namespaces: Isolating Workloads"]**

Hey everyone! Welcome back. Today we're diving into Kubernetes Namespaces, one of the most powerful features for organizing and isolating workloads in your cluster.

If you're preparing for the AZ-204 exam or working with Azure Kubernetes Service, understanding namespaces is absolutely essential. So let's get started!

---

## SLIDE 2: What Are Namespaces?
**[ON SCREEN: Diagram showing a Kubernetes cluster divided into separate namespace sections]**

So, what exactly are namespaces? Think of them as virtual clusters within your physical cluster. They're containers for other Kubernetes resources, giving you a way to divide your cluster into separate, isolated environments.

One of the coolest things about Kubernetes is that you can run any type of application. Many organizations want to migrate their entire application landscape onto Kubernetes. But without a way to segregate the cluster, operations could get really messy, really fast.

That's where namespaces come in.

---

## SLIDE 3: Use Cases & Scenarios
**[ON SCREEN: Two scenarios side-by-side]**

Let me give you some real-world examples.

On your production cluster, you might create a different namespace for each application. So your e-commerce app lives in one namespace, your inventory system in another, and your customer portal in a third.

On your non-production cluster, you might organize by environment. You'd have separate namespaces for development, testing, and UAT. This way, your dev team can experiment freely without worrying about breaking the test environment.

---

## SLIDE 4: Resource Isolation Benefits
**[ON SCREEN: Bullet points appearing one by one]**

Why does this matter? Namespaces give you three major benefits:

First, resource isolation. You can apply resource quotas per namespace, preventing one application from consuming all your cluster resources.

Second, security boundaries. You can use Role-Based Access Control to restrict who can see and modify resources in each namespace. Your junior developers might have access to the dev namespace but not production.

Third, simplified management. Instead of using complex label selectors everywhere, you can organize resources naturally by namespace. It's cleaner and easier to understand.

---

## SLIDE 5: Multi-Tenancy
**[ON SCREEN: Diagram showing multiple teams sharing one cluster safely]**

Here's where it gets really interesting for enterprise scenarios: multi-tenancy.

Namespaces let you safely run multiple teams, projects, or even customers on the same Kubernetes cluster. Each tenant gets their own namespace with strict isolation, resource limits, and access controls.

This is huge for cost optimization. Instead of spinning up separate clusters for every team or project, you can consolidate workloads while maintaining the security and isolation you need.

---

## SLIDE 6: AZ-204 Relevance
**[ON SCREEN: AZ-204 exam topics highlighted]**

Now, why is this critical for the AZ-204 exam?

Microsoft expects you to understand how to implement Azure solutions, and that includes container-based deployments. You need to know how to organize applications, implement proper security boundaries, and manage resources efficiently.

Namespaces are the foundation for all of these. You'll need to demonstrate knowledge of resource organization, RBAC implementation, and environment separation strategies.

In Azure Kubernetes Service, namespaces work exactly the same way as standard Kubernetes, so everything we cover today applies directly to your AKS deployments.

---

## SLIDE 7: What We'll Cover Today
**[ON SCREEN: Lab overview with key topics]**

In today's hands-on lab, we're going to explore:

First, how to create and manage namespaces using kubectl.

Second, how to deploy applications into specific namespaces.

Third, how namespaces affect service discovery and DNS resolution.

And finally, we'll look at some practical tools that make working with namespaces much easier.

---

## SLIDE 8: Important Considerations
**[ON SCREEN: Key points with icons]**

Before we dive in, here's what you need to know:

Namespaces introduce some complexity, that's true. You need to be more explicit about where things live. But the safeguards they provide are absolutely worth it.

With namespaces, you can confidently run multiple workloads on a single cluster without compromising scale or security. That's the promise of Kubernetes, and namespaces make it possible.

Also, remember: namespaces can't be nested. It's a single-level hierarchy. Keep your organization strategy simple and clear.

---

## SLIDE 9: Let's Get Started
**[ON SCREEN: Terminal window ready to go]**

Alright, enough talking! Let's jump into the practical exercises and see namespaces in action.

By the end of this lab, you'll be comfortable creating namespaces, deploying applications across different namespaces, and understanding how they interact. This is foundational knowledge you'll use every single day when working with Kubernetes.

Let's do this!

---

**[TRANSITION TO EXERCISES]**
