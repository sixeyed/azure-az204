# Kubernetes Ingress - Hands-On Exercises Narration

**Format:** Step-by-step walkthrough with conversational voice-over
**Tone:** Friendly, instructional, educational

---

## Introduction to the Exercise

Welcome to the hands-on portion of our Kubernetes Ingress tutorial! In this exercise, we're going to deploy a complete Ingress setup from scratch. We'll start by deploying an Nginx Ingress Controller, then we'll publish multiple applications through it using different routing strategies.

By the end, you'll have a working Ingress configuration that demonstrates host-based routing, path-based routing, and response caching. So let's get started!

---

## Exercise 1: Deploying the Ingress Controller

Alright, first things first - we need to deploy the Ingress Controller itself. Remember, this is the reverse proxy that will handle all incoming traffic.

**[Screen: Show the specs/ingress-controller directory]**

Take a look at the specs in the ingress controller folder. We've got several YAML files here, and each one serves a specific purpose.

The **namespace file** creates a dedicated namespace for the Ingress Controller. This is a best practice because the controller is shared across all your applications, so it makes sense to isolate it.

The **RBAC file** sets up the permissions. The Ingress Controller needs to query the Kubernetes API to discover Services, Ingress objects, and endpoint information. These rules grant exactly those permissions.

There's a **ConfigMap** with additional Nginx configuration. In our case, we're enabling proxy caching, which we'll use later in the exercises.

The **DaemonSet** is interesting - it ensures that one Ingress Controller pod runs on every node in your cluster. This provides high availability and efficient traffic distribution.

Finally, the **Services** file creates the external access points - both a LoadBalancer service and a NodePort service, giving you flexibility in how you expose the controller.

**[Screen: Terminal ready for command]**

Let's deploy all of these together. We'll use kubectl apply with the directory path.

```
kubectl apply -f labs/kubernetes/ingress/specs/ingress-controller
```

**[Screen: Show command output]**

Great! You'll see that each resource is being created. Now let's check what we've deployed.

```
kubectl get all -n ingress-nginx
```

**[Screen: Show pods, services, daemonsets]**

Perfect! You can see the DaemonSet, the pods it's managing, and the Services for external access. Notice the LoadBalancer service and the NodePort service - these are your entry points.

Let's wait for the pods to be fully ready before we continue.

```
kubectl wait --for=condition=Ready pod -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx
```

**[Screen: Wait for completion]**

Excellent! Now here's something cool - even though we haven't deployed any applications yet, the Ingress Controller is already running. Let's test it.

**[Screen: Open browser]**

Open your browser and go to localhost on port 8000, or port 30000 if you're using the NodePort.

**[Screen: Show 404 page from Nginx]**

See that? We're getting a 404 response, but notice this is coming from Nginx, not Kubernetes. This is the Ingress Controller responding. It's saying "I'm here and working, but I don't have any routing rules yet." This is actually a good sign - our controller is up and running!

---

## Exercise 2: Publishing a Default App

Now let's fix that 404 error by deploying a default application. This will act as a catch-all, so users won't see that bare Nginx error page.

**[Screen: Show specs/default directory]**

Looking at our default app specs, we've got a simple Nginx deployment, a ConfigMap with some custom HTML, and a ClusterIP Service.

**[Screen: Terminal]**

Let's deploy it.

```
kubectl apply -f labs/kubernetes/ingress/specs/default
```

**[Screen: Show output]**

Good! The app is deployed. But if you refresh your browser right now... nothing changes. Why? Because we haven't created the Ingress routing rules yet. The controller doesn't know this app exists.

**[Screen: Show specs/default/ingress/default.yaml]**

This is the Ingress object. Notice it doesn't specify a host - this makes it a default backend. Any request that doesn't match other rules will end up here.

Let's deploy the Ingress rule.

```
kubectl apply -f labs/kubernetes/ingress/specs/default/ingress
```

Now let's see all our Ingress rules.

```
kubectl get ingress
```

**[Screen: Show ingress list]**

Perfect! You can see the default ingress rule is now active.

**[Screen: Browser]**

Refresh your browser, and... there we go! Instead of a 404, we're seeing our custom default page. Try going to any random path - like "slash a slash b c dot php" - and you still get the default response. This is working exactly as intended.

---

## Exercise 3: Publishing an App to a Specific Host

Now let's get more sophisticated. We're going to deploy the "whoami" application and publish it to a specific hostname.

**[Screen: Show specs/whoami directory]**

We've got our application deployment and service, plus an Ingress object that routes traffic for a specific domain.

```
kubectl apply -f labs/kubernetes/ingress/specs/whoami
```

Let's check our Ingress rules now.

```
kubectl get ingress
```

**[Screen: Show both ingress rules - default and whoami]**

Excellent! Now we have two Ingress rules. The default one, and a new one for "whoami dot local".

To test this locally, we need to add an entry to our hosts file. I'll run the script that does this for us.

**[Screen: Terminal - show appropriate command for OS]**

On Windows with PowerShell running as admin, we'll use the PowerShell script. On Mac or Linux, we'll use the shell script with sudo.

**[Screen: Show script execution]**

The script adds "whoami dot local" pointing to localhost in our hosts file. This tricks our browser into thinking that domain exists locally.

**[Screen: Browser - navigate to whoami.local:8000]**

Now when we browse to "whoami dot local" on port 8000... brilliant! We see the whoami application.

**[Screen: Refresh browser several times]**

Keep refreshing, and watch what happens. See how the pod name changes? This demonstrates the load balancing feature. We deployed multiple replicas, and the Ingress Controller is distributing requests across all of them. This happens automatically - no extra configuration needed.

---

## Exercise 4: Response Caching with Ingress

For our final exercise, let's explore a more advanced feature - response caching. We're going to deploy a Pi calculator app that performs some heavy computation.

**[Screen: Show specs/pi directory]**

Here's our Pi app deployment, service, and a basic Ingress rule.

```
kubectl apply -f labs/kubernetes/ingress/specs/pi
```

Let's check the status.

```
kubectl get ingress
```

And verify our pods are running.

```
kubectl get po -l app=pi-web
```

**[Screen: Run hosts file script again]**

We need to add "pi dot local" to our hosts file as well.

**[Screen: Browser - navigate to pi.local:8000/pi?dp=25000]**

Now browse to "pi dot local" on port 8000, with the path "slash pi," and we'll add a query parameter for "dp equals 25000" - that's asking for 25,000 decimal places of Pi.

**[Screen: Wait for response]**

Notice it takes a second or two to calculate. This is doing real computation.

**[Screen: Refresh several times]**

Watch carefully as you refresh. See how the pod name keeps changing? That's load balancing. But also notice that each time, there's a delay because it's recalculating. Not ideal for performance, right?

Now here's where Ingress annotations come in. We can enable response caching without changing any application code.

**[Screen: Show specs/pi/update/ingress-with-cache.yaml]**

Look at this updated Ingress object. See those annotations? These are Nginx-specific settings that enable caching. The Ingress Controller reads these annotations and configures Nginx accordingly.

Let's apply this update.

```
kubectl apply -f labs/kubernetes/ingress/specs/pi/update
```

**[Screen: Browser - same URL]**

Now refresh the Pi calculator page again. The first request still takes time to calculate, but watch what happens when you refresh.

**[Screen: Rapid refreshes]**

Instant! The response is being served from cache. The Ingress Controller is doing all this caching work transparently. Your application doesn't need to know anything about it.

This is the power of Ingress - you can add sophisticated features like caching, rate limiting, or authentication at the routing layer, keeping your application code focused on business logic.

---

## Lab Challenge

Alright! Now it's your turn. We have a lab challenge with two parts.

**[Screen: Show challenge description]**

First, deploy the configurable web app and create your own Ingress routing for it. The app is already deployed with this command, but you need to write the Ingress rules yourself.

```
kubectl apply -f labs/kubernetes/ingress/specs/configurable
```

Think about what hostname you want to use, what paths you might need, and whether you want any special features enabled.

The second challenge is more advanced - can you reconfigure the Ingress Controller to use the standard web ports? That means port 80 for HTTP and port 443 for HTTPS, instead of the high-numbered ports we're using now.

**[Pause for effect]**

Give these challenges a try on your own. If you get stuck, there are hints available in the hints file, and if you need it, a complete solution as well.

---

## Cleanup

When you're finished experimenting, you can clean up all the resources we created with this single command.

```
kubectl delete all,secret,ingress,clusterrolebinding,clusterrole,ns,ingressclass -l kubernetes.courselabs.co=ingress
```

**[Screen: Show cleanup command executing]**

This uses label selectors to remove everything related to our Ingress exercises. Nice and tidy!

---

## Wrap Up

Great work! You've now deployed a complete Ingress setup, configured routing rules for multiple applications, implemented caching, and seen how Ingress provides a powerful, flexible way to manage external access to your Kubernetes applications.

These concepts are essential for the AZ-204 exam and for real-world container orchestration. Keep practicing with different Ingress configurations, and you'll be well-prepared for both the certification and production deployments.

Thanks for following along, and happy learning!
