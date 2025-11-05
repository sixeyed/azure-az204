# Kubernetes Container Probes - Lab Exercises Narration

## Opening

Welcome to the hands-on portion of our container probes lab! In this video, we'll work through practical examples that show you exactly how container probes work in Kubernetes. We'll start with readiness probes, move on to liveness probes, and finish with a challenge lab where you'll configure probes yourself. Make sure you have your Kubernetes cluster ready, and let's get started!

---

## Part 1: Self-Healing Apps with Readiness Probes

Alright, let's talk about a common problem. Your container might be running just fine, but the application inside could be in a failed state - maybe returning five-oh-three errors. Kubernetes won't automatically know about this unless we tell it how to check.

We're going to use a demo application called "whoami" that has a really useful feature for testing - we can actually trigger it to fail on demand. Let's deploy it now using kubectl apply with the file path pointing to our whoami specs.

Great! We now have two whoami pods running. Let's test the application by making some HTTP requests.

First, let's just access the app normally using curl to localhost on port 8010. Perfect, we get a response. Now here's the interesting part - we can actually force one of the pods to start returning five-oh-three errors by posting to the health endpoint with curl using the data flag to send '503' as the payload.

Now watch what happens when we make another request with curl, including the -i flag to show HTTP headers.

See that? Sometimes we get a good response, sometimes we get a five-oh-three error. That's because one pod is broken, but Kubernetes is still sending traffic to it. The pod doesn't crash - the container keeps running - so Kubernetes thinks everything is fine. This is exactly the problem readiness probes solve.

Let's look at how we configure a readiness probe. In our updated deployment, we've added a readiness probe section under the container spec. This tells Kubernetes to make an HTTP GET request to the /health endpoint every five seconds. If it gets anything other than a success response - anything that's not a 2xx status code - that pod is marked as not ready.

Let's deploy this update using kubectl apply pointing to the update directory.

And wait for the new pods to be ready using kubectl wait with the for condition equals Ready parameter and a label selector.

If you describe one of these pods, you'll see the readiness probe configuration right there in the output. Pretty cool, right?

Now these are brand new pods, so both are healthy. Let's break one again by posting '503' to the health endpoint.

Now let's watch the pods in real-time using kubectl get pods with the watch flag.

Watch the Ready column! One pod just changed to zero out of one containers ready. The container is still running - the status is Running - but Kubernetes knows it's not healthy anymore based on the readiness probe.

Here's the magic - when a readiness check fails, Kubernetes automatically removes that pod from the service endpoints. Let's verify this using kubectl get endpoints for the whoami-np service.

See? Only one pod IP is listed. Now when we make requests using curl, every single response is successful! The failed pod is completely isolated from traffic. This is self-healing in action - the Service is automatically load balancing only to healthy pods.

---

## Part 2: Self-Repairing Apps with Liveness Probes

Okay, so readiness probes are great for isolating unhealthy pods, but what if we want to actually fix the problem? That's where liveness probes come in.

A liveness probe tells Kubernetes not just to stop sending traffic to a failed pod, but to actually restart it. The configuration looks similar to a readiness probe - we're still checking the /health endpoint - but the consequences are much more significant.

When a liveness probe fails, Kubernetes kills the container and starts a fresh one. Because of this, you might want liveness probes to run less frequently and tolerate more failures before taking action. You don't want to restart pods unnecessarily - restarts disrupt service and reset state.

Let's deploy the update using kubectl apply with our update2 directory.

And wait for the pods to be ready using kubectl wait with the appropriate label selector.

Now let's trigger a failure by posting '503' to the health endpoint.

Let's watch the pods with kubectl get pods and the watch flag.

Watch closely! First, the pod becomes not ready - zero out of one. Then, after the liveness probe fails enough times - it checks every ten seconds and allows three failures - the pod restarts. You'll see the restart count increment. And then, once it passes the readiness check again, it becomes ready one out of one again.

If you check the endpoints now using kubectl get endpoints, both pod IPs are back in the service. The restarted pod passed its health checks and rejoined the load balancer pool. That's complete self-healing - detect the problem, isolate it, fix it by restarting, and restore service automatically.

---

## Part 3: Other Probe Types

Before we move to the lab challenge, let's quickly look at other types of probes. Container probes aren't just for HTTP applications.

Here's a Postgres database pod specification. Notice it has two different types of probes. The readiness probe uses a TCP socket check - it just verifies that Postgres is listening on port five four three two. This is perfect for databases and other non-HTTP services where you just need to know if the port is accepting connections.

The liveness probe uses an exec probe - it runs a command inside the container. In this case, it's executing a Postgres query command to make sure the database is actually functional, not just listening. The exec probe can run any command available in the container.

This flexibility means you can add health checks to any type of application - web apps, databases, message queues, whatever you're running. HTTP probes for REST APIs, TCP probes for network services, and exec probes for command-line checks.

---

## Part 4: Lab Challenge

Alright, now it's your turn! We have a Random Number Generator API that has some reliability problems. Let's deploy it using kubectl apply pointing to the rngapi specs.

Let's test it using curl with the -i flag to see headers, making a request to localhost port 8040 at the /rng path.

Try this a few times. You'll notice the app works at first, but then it fails and never recovers. Not great for production!

Here's your challenge: The application has a /healthz endpoint you can use for health checks. Your goals are to run five replicas of the application and ensure traffic only goes to healthy pods. That's your readiness probe. And automatically restart pods when the application inside fails. That's your liveness probe.

Take some time to work on this yourself. Think about what we've learned - which probe should you use to stop traffic to failed pods? Which probe should restart them? How would you configure both? What intervals and thresholds make sense?

If you get stuck, there are hints available in the hints file, and you can always check the solution. But I encourage you to try it on your own first - that's the best way to learn and really understand how probes work!

---

## Closing

Great work! In this lab, we've seen how readiness probes isolate unhealthy pods from traffic, how liveness probes restart failed containers, and how different probe types work with different application architectures.

These concepts are crucial for building production-ready applications in Kubernetes, and they're important topics for the AZ-204 exam. When you're deploying containerized applications in Azure Kubernetes Service, you'll use these same techniques to ensure reliability and availability.

Before we finish, let's clean up our resources using kubectl delete all with a label selector for our containerprobes lab.

Thanks for following along, and I'll see you in the next video!
