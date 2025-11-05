# Kubernetes Container Probes - Introduction Script

**Duration:** 2-3 minutes
**Tone:** Conversational, friendly, educational

---

## Slide 1: Title Slide
**[SCREEN: Title slide with "Kubernetes Container Probes"]**

Hello and welcome! In this video, we're going to explore one of the most important production-ready features in Kubernetes: container probes. If you're preparing for the AZ-204 exam or working with containerized applications in Azure, understanding container probes is absolutely essential.

---

## Slide 2: The Problem
**[SCREEN: Diagram showing a running container with a non-responsive application]**

Here's the thing - just because a container is running doesn't mean your application is healthy. Imagine this scenario: your web app is up, the container shows as running, but internally the application is returning five-oh-three errors. Your users are getting failures, but Kubernetes has no idea there's a problem because the container process hasn't crashed.

This is where container probes come to the rescue.

---

## Slide 3: What Are Container Probes?
**[SCREEN: Three icons representing the three probe types]**

Container probes are health checks that Kubernetes runs against your containers to determine their status. Think of them as a doctor doing regular check-ups on your applications. There are three types of probes, and each serves a specific purpose:

First, we have **Readiness Probes** - these tell Kubernetes whether your container is ready to accept traffic.

Second, **Liveness Probes** - these determine if your container is still running properly, or if it needs to be restarted.

And third, **Startup Probes** - these give slow-starting applications extra time to initialize before the other probes kick in.

---

## Slide 4: How Probes Work
**[SCREEN: Flow diagram showing probe execution cycle]**

So how do they actually work? Kubernetes repeatedly performs the health check you define - this could be an HTTP GET request to a specific endpoint, a TCP socket check, or even running a custom command inside the container. You configure how often to run the check, how many failures to tolerate, and what timeouts to use.

Based on the results, Kubernetes takes action automatically. A failing readiness probe removes the pod from service endpoints. A failing liveness probe restarts the container. This is self-healing infrastructure in action!

---

## Slide 5: Probe Types Explained
**[SCREEN: Side-by-side comparison of HTTP, TCP, and Exec probes]**

You can implement probes in three different ways. HTTP probes are perfect for REST APIs and web applications - Kubernetes makes an HTTP request and expects a success status code. TCP probes simply check if a port is open - great for databases and non-HTTP services. And exec probes run a command inside your container - the most flexible option when you need custom health logic.

---

## Slide 6: AZ-204 Exam Relevance
**[SCREEN: AZ-204 exam objectives with container health monitoring highlighted]**

For the AZ-204 exam, you need to understand how container probes relate to application health monitoring in Azure Kubernetes Service. Know when to use each probe type, how they affect container lifecycle management, and how they integrate with Azure's container monitoring solutions. This is a key part of developing cloud-native applications that are production-ready and resilient.

---

## Slide 7: What's Next
**[SCREEN: Preview of hands-on lab environment]**

Alright, now that you understand the concepts, let's get hands-on. In the next section, we'll deploy real applications with different types of probes, see how Kubernetes responds to failures, and configure health checks that keep your apps running smoothly.

Let's dive in!

---

**[END OF INTRO]**
