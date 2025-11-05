# Kubernetes Container Probes - Lab Exercises Narration

**Format:** Step-by-step walkthrough with conversational voice-over
**Tone:** Friendly, instructional, encouraging

---

## Opening

Welcome to the hands-on portion of our container probes lab! In this video, we'll work through practical examples that show you exactly how container probes work in Kubernetes. We'll start with readiness probes, move on to liveness probes, and finish with a challenge lab where you'll configure probes yourself. Make sure you have your Kubernetes cluster ready, and let's get started!

---

## Part 1: Self-Healing Apps with Readiness Probes

Alright, let's talk about a common problem. Your container might be running just fine, but the application inside could be in a failed state - maybe returning five-oh-three errors. Kubernetes won't automatically know about this unless we tell it how to check.

**[SCREEN: Terminal showing kubectl command]**

We're going to use a demo application called "whoami" that has a really useful feature for testing - we can actually trigger it to fail on demand. Let's deploy it now:

```
kubectl apply -f labs/kubernetes/containerprobes/specs/whoami
```

**[SCREEN: Show deployment creating pods]**

Great! We now have two whoami pods running. Let's test the application by making some HTTP requests.

**[SCREEN: Terminal showing curl commands]**

First, let's just access the app normally:

```
curl http://localhost:8010
```

Perfect, we get a response. Now here's the interesting part - we can actually force one of the pods to start returning five-oh-three errors by posting to the health endpoint:

```
curl --data '503' http://localhost:8010/health
```

Now watch what happens when we make another request:

```
curl -i http://localhost:8010
```

**[SCREEN: Show mixed responses - some 200, some 503]**

See that? Sometimes we get a good response, sometimes we get a five-oh-three error. That's because one pod is broken, but Kubernetes is still sending traffic to it. The pod doesn't crash, so Kubernetes thinks everything is fine. This is exactly the problem readiness probes solve.

**[SCREEN: Show YAML file for deployment-with-readiness]**

Let's look at how we configure a readiness probe. In our updated deployment, we've added a readiness probe section under the container spec. This tells Kubernetes to make an HTTP GET request to the slash health endpoint every five seconds. If it gets anything other than a success response, that pod is marked as not ready.

Let's deploy this update:

```
kubectl apply -f labs/kubernetes/containerprobes/specs/whoami/update
```

**[SCREEN: Show kubectl wait command]**

And wait for the new pods to be ready:

```
kubectl wait --for=condition=Ready pod -l app=whoami,update=readiness
```

**[SCREEN: Show kubectl describe output]**

If you describe one of these pods, you'll see the readiness probe configuration right there in the output. Pretty cool, right?

Now these are brand new pods, so both are healthy. Let's break one again and see what happens:

```
curl --data '503' http://localhost:8010/health
```

**[SCREEN: Show kubectl get pods --watch]**

Now let's watch the pods in real-time:

```
kubectl get po -l app=whoami --watch
```

**[SCREEN: Highlight the Ready column changing from 1/1 to 0/1]**

Watch the Ready column! One pod just changed to zero out of one containers ready. The container is still running, but Kubernetes knows it's not healthy anymore.

Here's the magic - when a readiness check fails, Kubernetes automatically removes that pod from the service endpoints. Let's verify this:

**[SCREEN: Show endpoints]**

```
kubectl get endpoints whoami-np
```

See? Only one pod IP is listed. Now when we make requests:

```
curl http://localhost:8010
```

**[SCREEN: Show only successful responses]**

Every single response is successful! The failed pod is completely isolated from traffic. This is self-healing in action - the Service is automatically load balancing only to healthy pods.

---

## Part 2: Self-Repairing Apps with Liveness Probes

Okay, so readiness probes are great for isolating unhealthy pods, but what if we want to actually fix the problem? That's where liveness probes come in.

**[SCREEN: Show deployment-with-liveness YAML]**

A liveness probe tells Kubernetes not just to stop sending traffic to a failed pod, but to actually restart it. The configuration looks similar to a readiness probe - we're still checking the slash health endpoint - but the consequences are much more significant.

When a liveness probe fails, Kubernetes kills the container and starts a fresh one. Because of this, you might want liveness probes to run less frequently and tolerate more failures before taking action. You don't want to restart pods unnecessarily!

Let's deploy the update:

```
kubectl apply -f labs/kubernetes/containerprobes/specs/whoami/update2
```

**[SCREEN: Show kubectl wait]**

And wait for the pods to be ready:

```
kubectl wait --for=condition=Ready pod -l app=whoami,update=liveness
```

Now let's trigger a failure and see what happens:

```
curl --data '503' http://localhost:8010/health
```

**[SCREEN: Watch pods with --watch flag]**

```
kubectl get po -l app=whoami --watch
```

**[SCREEN: Highlight the pod status changes: Ready 1/1 → 0/1 → Restart → 1/1]**

Watch closely! First, the pod becomes not ready - zero out of one. Then, after the liveness probe fails enough times, the pod restarts. You'll see the restart count increment. And then, once it passes the readiness check, it becomes ready one out of one again.

**[SCREEN: Show endpoints]**

If you check the endpoints now, both pod IPs are back in the service. The restarted pod passed its health checks and rejoined the load balancer pool. That's complete self-healing - detect the problem, isolate it, fix it, and restore service automatically.

---

## Part 3: Other Probe Types

Before we move to the lab challenge, let's quickly look at other types of probes. Container probes aren't just for HTTP applications.

**[SCREEN: Show products-db YAML file]**

Here's a Postgres database pod specification. Notice it has two different types of probes. The readiness probe uses a TCP socket check - it just verifies that Postgres is listening on port fifty-four thirty-two. This is perfect for databases and other non-HTTP services.

The liveness probe uses an exec probe - it runs a command inside the container. In this case, it's executing a Postgres query to make sure the database is actually functional, not just listening.

This flexibility means you can add health checks to any type of application - web apps, databases, message queues, whatever you're running.

---

## Part 4: Lab Challenge

Alright, now it's your turn! We have a Random Number Generator API that has some reliability problems. Let's deploy it:

**[SCREEN: Show kubectl apply]**

```
kubectl apply -f labs/kubernetes/containerprobes/specs/rngapi
```

Let's test it:

**[SCREEN: Show curl commands]**

```
curl -i http://localhost:8040/rng
```

Try this a few times. You'll notice the app works at first, but then it fails and never recovers. Not great!

Here's your challenge: The application has a slash healthz endpoint you can use for health checks. Your goals are to:

One - Run five replicas of the application and ensure traffic only goes to healthy pods.

Two - Automatically restart pods when the application inside fails.

**[SCREEN: Show hint and solution file paths]**

Take some time to work on this yourself. Think about what we've learned - which probe should you use to stop traffic to failed pods? Which probe should restart them? How would you configure both?

If you get stuck, there are hints available, and you can always check the solution. But I encourage you to try it on your own first - that's the best way to learn!

---

## Closing

Great work! In this lab, we've seen how readiness probes isolate unhealthy pods from traffic, how liveness probes restart failed containers, and how different probe types work with different application architectures.

These concepts are crucial for building production-ready applications in Kubernetes, and they're important topics for the AZ-204 exam. When you're deploying containerized applications in Azure Kubernetes Service, you'll use these same techniques to ensure reliability and availability.

**[SCREEN: Show cleanup command]**

Before we finish, let's clean up our resources:

```
kubectl delete all -l kubernetes.courselabs.co=containerprobes
```

Thanks for following along, and I'll see you in the next video!

---

**[END OF EXERCISES]**
