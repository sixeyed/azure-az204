# Kubernetes Troubleshooting - Introduction Script

**Duration:** 2-3 minutes
**Style:** Conversational presentation with slides

---

## Opening (15 seconds)

Welcome back! Today we're diving into one of the most practical skills you'll need as an Azure developer: troubleshooting applications in Kubernetes. If you're preparing for the AZ-204 exam or working with Azure Kubernetes Service in production, this is where theory meets reality. Let's jump in!

---

## Slide 1: Why Troubleshooting Matters (30 seconds)

Here's the thing about Kubernetes - it's incredibly powerful, but it's also complex. When you deploy an application, Kubernetes validates that your YAML syntax is correct, but it doesn't guarantee your app will actually work.

Think of it like this: Kubernetes checks your spelling and grammar, but not whether your sentences make sense. You can have perfectly valid specs that still produce a completely broken application. And trust me, you'll spend a significant amount of your time tracking down these issues.

---

## Slide 2: Common Points of Failure (45 seconds)

Let's talk about where things typically go wrong. On your screen, you'll see the main trouble spots:

First, there's the relationship between Deployments, ReplicaSets, and Pods. These objects use label selectors to find each other, and if those labels don't match up, your Pods won't be created or managed correctly.

Second, Services and their connection to Pods. Services route traffic based on selectors and port configurations. Get any of these wrong, and your app becomes unreachable.

Third, container configuration - image names, commands, resource requests, and health probes. Each of these can silently fail in ways that aren't immediately obvious.

The tricky part? These components are loosely coupled. A typo in one place can break everything, but Kubernetes won't tell you directly what's wrong.

---

## Slide 3: Your Troubleshooting Toolkit (45 seconds)

So how do we diagnose these problems? You'll rely heavily on kubectl commands. Let me walk you through the essentials:

Start with "kubectl get" - this gives you the high-level status of your resources. Is your Pod running? Is it pending? Is it crashing?

Next, "kubectl describe" - this is your diagnostic deep-dive. It shows events, configuration details, and error messages that explain why something isn't working.

Don't forget "kubectl logs" - when your container actually starts but behaves incorrectly, the logs tell you what's happening inside.

And finally, "kubectl port-forward" - this lets you bypass the Service layer and connect directly to a Pod, helping you isolate whether the problem is in the container or the networking configuration.

---

## Slide 4: The Systematic Approach (30 seconds)

Here's the methodology that works: start from the top and work your way down. Check your Deployment first - did it create a ReplicaSet? Did that ReplicaSet create Pods? Are those Pods actually running?

Then move to networking. Does your Service have endpoints? Do the selectors match? Are the ports configured correctly?

This systematic approach keeps you from jumping to conclusions and missing the actual root cause.

---

## Slide 5: AZ-204 Connection (20 seconds)

For the AZ-204 exam, Microsoft expects you to understand container monitoring, diagnostics, and troubleshooting strategies. You won't just be writing manifests - you'll be debugging them. This lab gives you hands-on practice with the exact scenarios the exam tests.

---

## Closing (10 seconds)

Alright, let's put this into practice. In this lab, you'll encounter a broken application with multiple issues. Your mission: diagnose the problems and fix them until the app runs successfully. Ready? Let's troubleshoot!
