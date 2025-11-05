# Kubernetes Troubleshooting - Exercises Narration

## Introduction to the Exercise

Alright, let's get our hands dirty! This exercise is all about real-world troubleshooting. We have a broken Pi application, and our job is to fix it. The goal is simple: make the application accessible at localhost on port 8020 or 30020, with a healthy Pod that's not crashing.

Now, I know it's tempting to jump straight to the solution, but resist that urge! These are exactly the kinds of issues you'll encounter in production. Building your troubleshooting muscles now will save you hours of frustration later.

Let's start by deploying the broken application and see what happens.

---

## Step 1: Deploy the Application

First, we'll apply the manifests from the pi-failing directory. Watch what happens on the screen as we run kubectl apply pointing at the pi-failing specs directory.

Okay, Kubernetes accepted our deployment. No errors from kubectl, which might make you think everything is fine. But here's the first lesson: just because kubectl accepts your YAML doesn't mean your application will work.

Let's check the status of what we just created.

---

## Step 2: Initial Investigation

Let's see what Pods we have using kubectl get pods. Hmm, interesting. We're seeing that there are no Pods, or possibly a Pod in a pending or error state. This is our first clue that something's wrong.

Let's check the Deployment itself with kubectl get deployment pi-web. Notice the Ready column. We're seeing zero out of zero, or zero out of something. That's not good. We should have at least one Pod ready.

Let's get more details about this Deployment using kubectl describe deployment pi-web. Scroll through the output with me. Look at the Events section at the bottom - this is where Kubernetes tells us what's happening behind the scenes.

---

## Step 3: Problem 1 - Replica Count

Ah, here's our first issue! Look at the Replicas field - it shows zero replicas desired. That's technically valid in Kubernetes. You might want zero replicas to save resources when an app isn't in use, but it's definitely not what we want right now.

We need to edit the deployment manifest and change the replica count to 1. We're opening the deployment YAML file and changing the replicas field from 0 to 1.

Now let's reapply with kubectl apply. Let's check our Pods again.

---

## Step 4: Problem 2 - Label Selectors

Now we're getting somewhere. We might see a Pod being created, but let's check if it's actually being managed by our Deployment using kubectl get pods --show-labels.

Look at the labels on screen. The Pod has the label "app equals pi-web-app", but if we check our Deployment selector using kubectl get deployment pi-web -o yaml, we'll see that the selector is looking for "app equals pi-web", but the Pod template is creating labels with "app equals pi-web-app". They don't match!

This is a really common mistake. The Deployment selector and the Pod template labels must align perfectly. Let's fix that in our YAML. We'll change the Pod template label to match the selector: "app colon pi-web".

We're reapplying the changes and watching what happens to our Pod.

---

## Step 5: Problem 3 - Resource Requests

After reapplying, let's check the Pod status again with kubectl get pods. The Pod might be showing as Pending. Let's describe it to find out why using kubectl describe pod with the pod name.

Look at the Events section. You're probably seeing something like "Insufficient CPU" or "Insufficient memory". Scroll up to the resource requests in the YAML on screen.

Whoa! Thirty-two CPUs and one hundred twenty-eight gigabytes of memory? That's wildly excessive for this simple application. Most clusters won't have nodes that can provide these resources.

Let's be realistic here. This is a small web app. Let's reduce these to something reasonable - maybe 250 millicores for CPU and 128 megabytes for memory. We're editing the YAML on screen.

We're applying the changes and our Pod should get scheduled now.

---

## Step 6: Problem 4 - Image Pull Error

Let's check the Pod status with kubectl get pods. Now we might see something different - the Pod is created and scheduled, but the status shows ImagePullBackOff or ErrImagePull. Let's describe the Pod again with kubectl describe pod.

Look at the events. Kubernetes is trying to pull an image but failing. Let's check the image name in our deployment spec.

There it is on screen: "kiamol slash ch05 dash pi dash app". Let me verify the correct image name. According to the documentation, it should be "kiamol slash ch05 dash pi", without the "-app" suffix.

This happens more often than you'd think - a typo in the image name, or maybe you haven't pushed the image to your registry yet. Let's fix the image name and reapply.

---

## Step 7: Problem 5 - Container Command Error

After fixing the image, we're checking the Pod status again with kubectl get pods. We might see a new error: RunContainerError or CrashLoopBackOff. Let's check the logs using kubectl logs with the pod name.

And let's describe the Pod using kubectl describe pod. The error message shows that the container can't start. Look at the command in the YAML on screen: "donet Pi.Web.dll".

Do you see it? There's a typo - "donet" instead of "dotnet". The container is trying to run a command that doesn't exist. Let's fix that typo and reapply.

This is why checking logs and Pod descriptions is so important - they often reveal the exact error message you need.

---

## Step 8: Problem 6 - Readiness Probe

Now let's check if our Pod is running with kubectl get pods. Great! The Pod is running, but look at the Ready column - it shows zero out of one. The container is running, but it's not ready to accept traffic. Let's find out why using kubectl describe pod.

Scroll to the Conditions section and the Events. You'll see readiness probe failures. Let's look at the readiness probe configuration in our YAML.

See this? The readiness probe is checking a TCP socket on port 8020. But wait - look at the container port. The container exposes port 80, not 8020. Port 8020 is what the Service exposes externally, but the probe needs to check the actual container port.

Let's fix the readiness probe to check port 80 instead of 8020. We're applying the changes and watching the Pod status. After a few seconds, you should see it become ready.

---

## Step 9: Problem 7 - Liveness Probe

Even though the Pod is ready, we need to verify the liveness probe is working correctly. Let's give it some time and watch using kubectl get pods --watch.

If the Pod starts restarting, we have a liveness probe issue. We're hitting Control-C to stop watching, and checking the probe configuration.

Look at the liveness probe in the YAML - it's checking the path "/healthy" on port 80. But does that endpoint actually exist in our application? Let's port-forward to the Pod and test directly using kubectl port-forward to map local port 9000 to container port 80.

Now in another terminal, we're curling the root path and the /healthy path. You'll see that the root path works but /healthy returns a 404. The probe endpoint doesn't exist!

For this application, let's change the liveness probe to check the root path "/" instead of "/healthy". We're applying the changes.

---

## Step 10: Service Troubleshooting - NodePort

Now our Pod is healthy! But can we access it through the Service? Let's try to browse to localhost:30020.

Nothing? Let's investigate the Service using kubectl get service pi-np. Look at the NodePort value on screen. It's showing 8020. Here's the problem: NodePorts in Kubernetes must be in the range 30000 to 32767. The value 8020 is outside that range.

Let's fix the service manifest. We'll change the nodePort to 30020 instead. We're applying the changes.

---

## Step 11: Service Troubleshooting - Selectors

We're trying to access the app again at localhost:30020. Still nothing? Let's dig deeper using kubectl describe service pi-np.

Look at the Endpoints section. It's empty! That means the Service isn't finding any Pods to route traffic to. This is a selector mismatch.

Let's check the Service selector in the YAML. It shows "app: pi-web-pod". Now look at the Pod labels we set earlier - we have "app: pi-web". They don't match!

We're changing the Service selector to match the actual Pod label: "app: pi-web". Applying the changes and describing the Service again. Now you should see an endpoint listed - that's the IP address of our Pod.

---

## Step 12: Service Troubleshooting - Target Port

Let's try accessing the app one more time. If it's still not working, we have one more issue to check - the target port configuration.

Look at the Service spec on screen. The targetPort is set to "app". This means it's looking for a named port called "app" in the Pod's container spec.

Now look at the container ports in the deployment YAML. The container port is named "http", not "app". The names must match!

Let's fix the Service to use targetPort: http instead of targetPort: app. We're applying that final change.

---

## Step 13: Verification and Success

Alright, moment of truth! Let's check everything one more time using kubectl get pods and kubectl get services.

The Pod shows one out of one ready, and the Service shows proper endpoints. Let's test the application using curl to hit localhost:8020.

There we go! We're getting a response from the Pi application. You can also access it via the NodePort at localhost:30020.

Success! We've systematically worked through multiple issues - replica counts, label mismatches, resource constraints, image errors, command typos, probe configurations, and Service networking. Each problem required a different diagnostic approach, but the systematic methodology got us there.

---

## Wrap-Up

This exercise demonstrates what troubleshooting in Kubernetes really looks like. You'll rarely have just one problem - issues often cascade, and you need to fix them layer by layer. The key is staying systematic: check the Deployment, then the ReplicaSet, then the Pods, then the Services.

Remember, kubectl get, kubectl describe, and kubectl logs are your best friends. Use them liberally, read the output carefully, and you'll become a troubleshooting pro in no time.

---

## Cleanup

When you're done experimenting, clean up your resources using kubectl delete all with the label selector for kubernetes.courselabs.co equals troubleshooting.

This removes all objects with that label, keeping your cluster tidy. Great work on completing this troubleshooting marathon!
