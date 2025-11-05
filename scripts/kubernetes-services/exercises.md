# Kubernetes Services - Lab Exercises Narration

**Style:** Conversational voice-over for hands-on demonstration
**Purpose:** Step-by-step narration following the lab exercises

---

## Introduction

Welcome to the hands-on lab for Kubernetes Services! In this session, we're going to get our hands dirty with real Service configurations. We'll deploy Pods, create different types of Services, and explore how Kubernetes handles networking and service discovery.

Make sure you have your terminal ready and a Kubernetes cluster running. If you're using Docker Desktop with Kubernetes enabled or an Azure Kubernetes Service cluster, you're all set. Let's dive in!

---

## Section 1: Understanding the Basics

Before we start deploying anything, let's understand what we're working with. Every Pod in Kubernetes has its own IP address, and other Pods can reach it using that IP. But here's the thing - that IP address only exists as long as the Pod is alive. When a Pod gets replaced, the new one gets a different IP.

This is where Services come in. Services provide a consistent IP address linked to a DNS name. You'll always use Services for routing traffic into Pods, whether that traffic is coming from inside the cluster or from external sources.

Services and Pods are loosely coupled, meaning a Service finds its target Pods using label selectors. This is a really powerful pattern that you'll see throughout Kubernetes.

---

## Section 2: Deploying Sample Pods

Alright, let's deploy our first Pods. We're going to create two simple Pods using YAML definitions that include labels. These labels will be crucial when we connect Services to these Pods.

[Screen: Show the terminal ready to execute commands]

The first Pod we're deploying is called "whoami" - it's a simple web application that returns information about itself. The second is called "sleep" - we'll use this to run commands and test connectivity.

Let's apply these Pod definitions. I'm running:

```
kubectl apply -f labs/kubernetes/services/specs/pods
```

[Screen: Command executes, shows output of Pods being created]

Great! Notice that we can deploy multiple YAML files at once by pointing kubectl at a directory. Kubernetes will process all the YAML files it finds.

Now let's check the status of our Pods and see their IP addresses and labels. I'll run:

```
kubectl get pods -o wide --show-labels
```

[Screen: Shows Pod list with IP addresses and labels]

Perfect! Look at the output here. Each Pod has been assigned an IP address, and you can see the labels in the last column. The whoami Pod has the label "app=whoami" and the sleep Pod has "app=sleep". These labels will be important in just a moment.

Now, here's something interesting. Even though both Pods are running and have IP addresses, they can't find each other by name. Let's test this. I'll use the sleep Pod to try looking up the whoami Pod by name:

```
kubectl exec sleep -- nslookup whoami
```

[Screen: Shows error message - name resolution fails]

As expected, it fails. The Pod name alone isn't enough for DNS resolution. This is where Services come into play.

---

## Section 3: Creating a ClusterIP Service

Now let's deploy our first Service - a ClusterIP Service. ClusterIP is the default Service type and it creates an IP address that's only accessible within the cluster. This is perfect for internal communication between components.

[Screen: Briefly show the whoami-clusterip.yaml file contents]

Take a look at this Service definition. It has a selector that matches "app=whoami" - that's the same label we saw on our whoami Pod. The Service will listen on port 80 and forward traffic to port 80 on any matching Pods.

Let's deploy it:

```
kubectl apply -f labs/kubernetes/services/specs/services/whoami-clusterip.yaml
```

[Screen: Service creation output]

Now let's get the details of our new Service:

```
kubectl get service whoami
```

[Screen: Shows Service with ClusterIP address]

Excellent! The Service has been assigned its own IP address. This IP address is static - it won't change for the lifetime of the Service. You can also use:

```
kubectl describe svc whoami
```

[Screen: Shows detailed Service information including endpoints]

In the description, you'll see the Endpoints section - that shows the IP address of the Pod that's receiving traffic. Notice it matches the whoami Pod's IP address we saw earlier.

---

## Section 4: DNS Service Discovery

Here's where Kubernetes really shines. Kubernetes runs a DNS server inside every cluster, and every Service automatically gets a DNS entry. Let's test it!

From the sleep Pod, let's try looking up "whoami" again:

```
kubectl exec sleep -- nslookup whoami
```

[Screen: Shows successful DNS resolution with Service IP]

Look at that! Now it works. The DNS lookup returns the IP address of the Service. The first IP address you see in the response is the Kubernetes DNS server itself, and below that is the whoami Service IP.

Now our Pods can communicate using friendly DNS names. Let's actually call the whoami application:

```
kubectl exec sleep -- curl -s http://whoami
```

[Screen: Shows whoami response with Pod information]

Perfect! The whoami application responds with information about itself. Notice it shows the Pod name and IP address. This traffic went through the Service to reach the Pod.

---

## Section 5: Testing Service Resilience

Now let's test something really important. What happens when a Pod is replaced? Let's find out.

First, let's check the current IP address of the whoami Pod:

```
kubectl get pods -o wide -l app=whoami
```

[Screen: Shows Pod with current IP]

Note that IP address. Now let's delete this Pod:

```
kubectl delete pods -l app=whoami
```

[Screen: Pod deletion]

Notice we're using a label selector here too. The "-l" flag lets us select resources by their labels. This is a really powerful feature for managing groups of resources.

Now let's recreate the Pod:

```
kubectl apply -f labs/kubernetes/services/specs/pods
```

And check the new Pod's IP address:

```
kubectl get pods -o wide -l app=whoami
```

[Screen: Shows new Pod with different IP address]

See that? The new Pod has a completely different IP address. But watch what happens when we test connectivity.

Let's check the Service:

```
kubectl exec sleep -- nslookup whoami
```

[Screen: Shows same Service IP as before]

The Service IP hasn't changed. And when we call the application:

```
kubectl exec sleep -- curl -s http://whoami
```

[Screen: Shows response from new Pod]

It still works! Even though the Pod IP changed, the Service automatically updated its routing. If you look at the response, you'll see it's coming from the new Pod, but our client code didn't need to change at all. This is the power of Services.

---

## Section 6: External Services - LoadBalancer and NodePort

So far we've been working with internal cluster communication. But what about exposing applications to the outside world? That's where LoadBalancer and NodePort Services come in.

There are two ways to make applications accessible from outside the cluster. LoadBalancer Services are the easier option and they're fully supported on Azure Kubernetes Service. NodePort Services work on any cluster, but they're typically used more for development.

Let's deploy both and see how they work. I'm running:

```
kubectl apply -f labs/kubernetes/services/specs/services/whoami-nodeport.yaml -f labs/kubernetes/services/specs/services/whoami-loadbalancer.yaml
```

[Screen: Both Services being created]

Great! Now we have three Services all routing to the same whoami Pod. Let's see them:

```
kubectl get svc -l app=whoami
```

[Screen: Shows all three Services - ClusterIP, NodePort, and LoadBalancer]

Look at this output. We've got our original ClusterIP Service, plus the new NodePort and LoadBalancer Services.

The NodePort Service shows a port in the 30000 range - that's the port you can use to access the application on any node in your cluster.

The LoadBalancer Service has an external IP address. On Azure Kubernetes Service, this would be an actual Azure Load Balancer that was automatically provisioned for you. In Docker Desktop, it just uses localhost.

Now we can access our application from outside the cluster. Let me try both methods:

```
curl http://localhost:8080
```

[Screen: Shows whoami response]

That's using the LoadBalancer Service. And we can also use:

```
curl http://localhost:30010
```

[Screen: Shows whoami response]

That's the NodePort Service. Both are routing traffic to the same Pod, but they're doing it in different ways.

---

## Section 7: Lab Challenge

Now it's your turn to experiment! The lab challenge asks you to test two specific scenarios:

First, what happens when a Service's label selector doesn't match any Pods? In other words, zero Pods match the label spec.

Second, what happens when multiple Pods match the label selector?

These are really important scenarios to understand. Try creating new Service definitions and Pod configurations to test them out.

Here's a hint: when you describe a Service, look at the Endpoints section. That will show you which Pods the Service has found. And when you have multiple matching Pods, try making multiple requests and see if the traffic gets distributed.

Take your time with this. Understanding how Services route traffic and what happens in edge cases will really solidify your knowledge.

---

## Cleanup

When you're done experimenting, cleanup is really easy. Every resource in this lab has been tagged with a specific label. So we can delete everything with one command:

```
kubectl delete pod,svc -l kubernetes.courselabs.co=services
```

[Screen: Shows resources being deleted]

And just like that, we're back to a clean cluster.

---

## Conclusion

Great work! You've now created ClusterIP, NodePort, and LoadBalancer Services. You've seen how DNS service discovery works, how Services automatically update when Pods are replaced, and how to expose applications both internally and externally.

These are fundamental concepts that you'll use constantly when working with Kubernetes, whether you're deploying to Azure Kubernetes Service or any other Kubernetes platform. And they're absolutely essential knowledge for the AZ-204 exam.

Keep practicing with different Service configurations, and in the next session, we'll build on these concepts to explore more advanced networking patterns. Thanks for following along!
