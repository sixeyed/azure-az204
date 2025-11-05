# Kubernetes Ingress - Hands-On Exercises Narration

## Introduction to the Exercise

Welcome to the hands-on portion of our Kubernetes Ingress tutorial! In this exercise, we're going to deploy a complete Ingress setup from scratch. We'll start by deploying an Nginx Ingress Controller, then we'll publish multiple applications through it using different routing strategies.

By the end, you'll have a working Ingress configuration that demonstrates host-based routing, path-based routing, and response caching. So let's get started!

---

## Exercise 1: Deploying the Ingress Controller

Alright, first things first - we need to deploy the Ingress Controller itself. Remember, this is the reverse proxy that will handle all incoming traffic.

Take a look at the specs in the ingress controller folder. We've got several YAML files here, and each one serves a specific purpose.

The namespace file creates a dedicated namespace called ingress-nginx for the Ingress Controller. This is a best practice because the controller is shared infrastructure across all your applications, so it makes sense to isolate it from application namespaces.

The RBAC file sets up the permissions. The Ingress Controller needs to query the Kubernetes API to discover Services, Ingress objects, and endpoint information. It watches for changes in real-time. These rules grant exactly those permissions - nothing more, following the principle of least privilege.

There's a ConfigMap with additional Nginx configuration. In our case, we're enabling proxy caching, which we'll use later in the exercises to demonstrate caching behavior.

The DaemonSet is interesting - it ensures that one Ingress Controller pod runs on every node in your cluster. This provides high availability and efficient traffic distribution. Requests can be handled by any node without extra network hops.

Finally, the Services file creates the external access points - both a LoadBalancer service for cloud environments and a NodePort service for local development, giving you flexibility in how you expose the controller.

Let's deploy all of these together using kubectl apply pointing to the directory.

Great! You'll see that each resource is being created - namespace, config map, service account, cluster roles, daemon set, and services. Now let's check what we've deployed using kubectl get all in the ingress-nginx namespace.

Perfect! You can see the DaemonSet, the pods it's managing, and the Services for external access. Notice the LoadBalancer service and the NodePort service - these are your entry points to the cluster.

Let's wait for the pods to be fully ready before we continue using kubectl wait with the condition parameter.

Excellent! Now here's something cool - even though we haven't deployed any applications yet, the Ingress Controller is already running. Let's test it.

Open your browser and go to localhost on port 8000, or port 30000 if you're using the NodePort.

See that? We're getting a 404 response, but notice this is coming from Nginx, not Kubernetes. The page shows the Nginx branding. This is the Ingress Controller responding. It's saying "I'm here and working, but I don't have any routing rules yet." This is actually a good sign - our controller is up and running, listening for requests!

---

## Exercise 2: Publishing a Default App

Now let's fix that 404 error by deploying a default application. This will act as a catch-all, so users won't see that bare Nginx error page when they hit undefined routes.

Looking at our default app specs, we've got a simple Nginx deployment serving static content, a ConfigMap with some custom HTML for the default page, and a ClusterIP Service to expose the pods internally.

Let's deploy it using kubectl apply.

Good! The app is deployed and running. But if you refresh your browser right now... nothing changes. Still the Nginx 404. Why? Because we haven't created the Ingress routing rules yet. The controller doesn't know this app exists or where to route traffic.

This is the Ingress object. Notice it doesn't specify a host field in the rules - this makes it a default backend. Any request that doesn't match other, more specific rules will end up here. It's the catch-all route.

Let's deploy the Ingress rule using kubectl apply.

Now let's see all our Ingress rules using kubectl get ingress.

Perfect! You can see the default ingress rule is now active.

Refresh your browser, and... there we go! Instead of a generic 404, we're seeing our custom default page. Try going to any random path - like /a/b/c dot php - and you still get the default response. This is working exactly as intended, catching all unmatched routes.

---

## Exercise 3: Publishing an App to a Specific Host

Now let's get more sophisticated. We're going to deploy the "whoami" application and publish it to a specific hostname using host-based routing.

We've got our application deployment and service, plus an Ingress object that routes traffic for a specific domain name - whoami dot local.

Let's deploy it using kubectl apply.

Let's check our Ingress rules now.

Excellent! Now we have two Ingress rules. The default one with no host, and a new one for "whoami dot local". The controller will match the most specific rule first, then fall back to the default.

To test this locally, we need to add an entry to our hosts file so whoami dot local resolves to localhost. I'll run the script that does this for us.

On Windows with PowerShell running as admin, we'll use the PowerShell script. On Mac or Linux, we'll use the shell script with sudo.

The script adds "whoami dot local" pointing to 127.0.0.1 in our hosts file. This tricks our browser and any local tools into thinking that domain exists and resolves locally.

Now when we browse to whoami dot local on port 8000... brilliant! We see the whoami application response.

Keep refreshing, and watch what happens. See how the pod name and IP address change? This demonstrates the load balancing feature. We deployed multiple replicas of whoami, and the Ingress Controller is distributing requests across all of them. The controller maintains session affinity when needed but load balances by default. This happens automatically - no extra configuration needed.

---

## Exercise 4: Response Caching with Ingress

For our final exercise, let's explore a more advanced feature - response caching. We're going to deploy a Pi calculator app that performs some heavy computation to calculate digits of Pi.

Here's our Pi app deployment, service, and a basic Ingress rule routing traffic for the domain pi dot local.

Let's deploy it using kubectl apply.

Let's check the status with kubectl get ingress.

And verify our pods are running.

We need to add "pi dot local" to our hosts file as well, so we'll run the hosts file script again.

Now browse to pi dot local on port 8000, with the path /pi, and we'll add a query parameter dp equals 25000 - that's asking for 25,000 decimal places of Pi.

Notice it takes a second or two to calculate. This is doing real computation - generating those digits mathematically.

Watch carefully as you refresh. See how the pod name keeps changing? That's load balancing across multiple replicas. But also notice that each time, there's a delay because it's recalculating. The app doesn't cache - it computes every time. Not ideal for performance, right?

Now here's where Ingress annotations come in. We can enable response caching without changing any application code. Look at this updated Ingress object. See those annotations? These are Nginx-specific settings that enable caching. The Ingress Controller reads these annotations and configures Nginx accordingly to cache responses based on the request path and query parameters.

Let's apply this update using kubectl apply.

Now refresh the Pi calculator page again. The first request still takes time to calculate, but watch what happens when you refresh.

Instant! The response is being served from the Ingress Controller's cache. Subsequent requests with the same parameters get the cached result. The Ingress Controller is doing all this caching work transparently at the proxy layer. Your application doesn't need to know anything about it.

This is the power of Ingress - you can add sophisticated features like caching, rate limiting, authentication, or SSL termination at the routing layer, keeping your application code focused on business logic.

---

## Lab Challenge

Alright! Now it's your turn. We have a lab challenge with two parts.

First, deploy the configurable web app and create your own Ingress routing for it. The app is already deployed, but you need to write the Ingress rules yourself. Think about what hostname you want to use, what paths you might need, and whether you want any special features enabled.

The second challenge is more advanced - can you reconfigure the Ingress Controller to use the standard web ports? That means port 80 for HTTP and port 443 for HTTPS, instead of the high-numbered ports we're using now. You'll need to modify the Service that exposes the Ingress Controller.

Give these challenges a try on your own. If you get stuck, there are hints available in the hints file, and if you need it, a complete solution as well.

---

## Cleanup

When you're finished experimenting, you can clean up all the resources we created with this single command using kubectl delete with multiple resource types and a label selector.

This uses label selectors to remove everything related to our Ingress exercises - all Ingress objects, Services, Deployments, ConfigMaps, RBAC resources, and the namespace. Nice and tidy!

---

## Wrap Up

Great work! You've now deployed a complete Ingress setup, configured routing rules for multiple applications using both default backends and host-based routing, implemented response caching using annotations, and seen how Ingress provides a powerful, flexible way to manage external access to your Kubernetes applications.

These concepts are essential for the AZ-204 exam and for real-world container orchestration. Ingress is how you expose applications in production Kubernetes clusters, whether on Azure Kubernetes Service or any other platform.

Keep practicing with different Ingress configurations, and you'll be well-prepared for both the certification and production deployments.

Thanks for following along, and happy learning!
