# Kubernetes Deployments - Lab Exercises Narration Script

**Style:** Conversational voice-over following hands-on demonstration
**Target:** Step-by-step lab walkthrough

---

## Opening

Alright, let's get hands-on with Kubernetes Deployments! In this lab, we'll work through creating, scaling, and updating Deployments. Make sure you have your Kubernetes cluster ready and your terminal open. Let's dive in.

---

## Section 1: Understanding the Deployment YAML

First, let's take a look at what a Deployment actually looks like in YAML format.

**[Screen: Show the whoami-v1.yaml file]**

Here we have a Deployment manifest. At the top, you'll see the API version "apps/v1" and the kind is "Deployment".

In the metadata, we're calling this Deployment "whoami". Simple enough.

Now, the spec section is where it gets interesting. Look at the selector here. It's using matchLabels to find Pods with the label "app: whoami". This is how the Deployment knows which Pods it's responsible for managing.

Below that, we have the template section. This is your Pod blueprint. Notice in the template metadata, we're applying that same "app: whoami" label. This is crucial! The labels in your Pod template must match the labels in your selector, or Kubernetes will reject the entire manifest.

In the template spec, we define our container. We're using a simple "whoami" application image that responds with information about itself. Perfect for testing.

---

## Section 2: Creating Your First Deployment

Let's create this Deployment and see what happens.

**[Screen: Terminal ready to type]**

Type "kubectl apply" with the "-f" flag, followed by the path to our YAML file.

**[Screen: Command executes, shows "deployment.apps/whoami created"]**

Great! We get confirmation that the Deployment was created. But remember, the Deployment is a controller. It's not the actual Pod. Let's see what Pods were created.

**[Screen: Type "kubectl get pods -l app=whoami"]**

We're using the "-l" flag here to filter by label. This shows us only Pods with the "app=whoami" label.

**[Screen: Output shows one Pod with a random suffix]**

There's our Pod! Notice the name? It's "whoami" followed by a random string. The Deployment automatically generates unique names for the Pods it creates. You'll never manually specify Pod names when using Deployments.

Now let's look at the Deployment itself.

**[Screen: Type "kubectl get deployments"]**

This shows us basic information. We can see one Deployment with one ready replica.

**[Screen: Type "kubectl get deployments -o wide"]**

The wide output gives us more details, including the container image and selector.

Let's get even more information.

**[Screen: Type "kubectl describe deploy whoami"]**

**[Screen: Scroll through the output]**

Look at all this information! We can see the replica count, the selector, the Pod template, and importantly, the events at the bottom.

Notice it mentions something called a ReplicaSet? We'll come back to that concept later, but for now, just know that Deployments actually use ReplicaSets behind the scenes to manage Pods.

---

## Section 3: Scaling Deployments

Now, let's say our application is getting more traffic and we need more Pods. We can scale up!

There are two ways to scale a Deployment. First, let's try the imperative way.

**[Screen: Type "kubectl scale deploy whoami --replicas 3"]**

We're telling Kubernetes: "Scale the whoami Deployment to three replicas."

**[Screen: Command completes, type "kubectl get pods -l app=whoami"]**

Look at that! We now have three Pods running. Kubernetes quickly created two more Pods from the same template.

But here's the problem. Our running Deployment now has three replicas, but our YAML file in source control still says one replica. This is what we call configuration drift, and in production, it's a recipe for disaster.

**[Pause for emphasis]**

If someone runs an automated deployment from source control, those manual changes will get overwritten. So, the better approach is to scale declaratively by updating the YAML.

**[Screen: Show whoami-v1-scale.yaml file]**

Here's our updated manifest. It's almost identical, but notice the spec now includes "replicas: 2".

Let's apply this.

**[Screen: Type "kubectl apply -f" with the scale YAML path]**

Now check the Pods again.

**[Screen: Type "kubectl get pods -l app=whoami"]**

We're back down to two Pods. Kubernetes saw that we had three replicas running, but our desired state says two, so it terminated one Pod. This is the declarative model in action. You declare what you want, and Kubernetes makes it happen.

---

## Section 4: Working with Managed Pods

When you're working with Pods managed by a Deployment, you need to use labels because the Pod names are random.

For example, let's look at logs.

**[Screen: Type "kubectl logs -l app=whoami"]**

Using the label selector, we can see logs from all Pods with that label.

You can also execute commands at the Deployment level.

**[Screen: Type "kubectl exec deploy/whoami -- hostname"]**

**[Screen: Command fails]**

Okay, that failed, but that's expected! This particular container image doesn't have a shell, so we can't execute commands in it. But the syntax is correct for Deployments that do support exec.

Let's get detailed information about our Pods.

**[Screen: Type "kubectl get pods -o wide --show-labels -l app=whoami"]**

Perfect! This shows us the Pod names, their IP addresses, which nodes they're running on, and all their labels. This information is super useful for troubleshooting.

---

## Section 5: Exposing the Deployment with Services

Now, to actually access our application, we need Services. We have two Service manifests ready: one for a LoadBalancer and one for a NodePort.

**[Screen: Show the Services directory]**

Let's apply both at once.

**[Screen: Type "kubectl apply -f" with the services directory path]**

**[Screen: Output shows two services created]**

Now let's check the endpoints.

**[Screen: Type "kubectl get endpoints whoami-np whoami-lb"]**

See those IP addresses? Those are the Pod IPs we saw earlier. The Services use the same label selector to find the Pods, and they're routing traffic to both replicas.

Let's test the application.

**[Screen: Type "curl localhost:8080"]**

**[Screen: Output shows detailed response from the application]**

There's our response! The application tells us about itself, including hostname and IP information. If we curl again, the Service will load-balance between our two Pods.

---

## Section 6: Rolling Updates

Now for one of the coolest features of Deployments: rolling updates. Let's say we want to change our application configuration.

**[Screen: Show whoami-v2.yaml file]**

In this updated manifest, we're adding an environment variable that changes how the application responds. Environment variables are fixed for the life of a Pod container, so this change requires new Pods.

Before we apply the change, let's watch what happens to the Pods in real-time.

**[Screen: Split screen - one terminal with watch command]**

In this terminal, I'll type "kubectl get pods -l app=whoami --watch". This will continuously update as things change.

**[Screen: Other terminal ready for apply command]**

Now, let's apply the update.

**[Screen: Type "kubectl apply -f" with the v2 YAML path]**

**[Screen: Watch the watch terminal showing Pods being created and terminated]**

Watch what's happening! Kubernetes is creating new Pods with the updated configuration while the old Pods are still running. Then, once the new Pods are ready, it terminates the old ones. This is a rolling update!

Your application stays available throughout the entire process. No downtime. No dropped requests. That's the power of Deployments.

Let's test the application now.

**[Screen: Type "curl localhost:8080"]**

**[Screen: Shorter output appears]**

There we go! The output is now shorter because of our configuration change. If we curl multiple times, we'll see load balancing across both new Pods.

---

## Section 7: Rolling Back Changes

What if we realize this update was a mistake? Maybe users don't like the new format. No problem! Deployments make rollbacks incredibly easy.

First, let's check the rollout history.

**[Screen: Type "kubectl rollout history deploy/whoami"]**

This shows us the revision history. We can see we're on revision 2.

To roll back to the previous version, it's just one command.

**[Screen: Type "kubectl rollout undo deploy/whoami"]**

**[Screen: Command completes]**

That's it! Kubernetes is now performing another rolling update, but this time it's going back to revision 1.

**[Screen: Type "kubectl get pods -l app=whoami"]**

See the Pod ages? These are fresh Pods running the old configuration.

Let's verify the application.

**[Screen: Type "curl localhost:8080"]**

**[Screen: Full output returns]**

Perfect! We're back to the full output. We've successfully rolled back our deployment.

---

## Section 8: Lab Challenge Introduction

Alright, now it's time for your challenge! Rolling updates are great, but sometimes you need a different deployment strategy.

**[Screen: Show lab instructions]**

Your task is to implement a blue-green deployment. That means running two separate Deployments: one for version 1 and one for version 2. Both versions will be running, but initially, only version 1 should receive traffic through the Service.

Then, you'll update the Service to switch traffic to version 2 without making any changes to the Deployments themselves. This gives you instant traffic switching and easy rollback capabilities.

Here are some hints: Think about how Services find Pods. What selects which Pods receive traffic? You'll need to use labels creatively here.

Take some time to work through this on your own. Check the hints file if you get stuck, or look at the solution when you're ready to compare approaches.

---

## Closing

Great work! You've now created Deployments, scaled them declaratively, performed rolling updates, and rolled back changes. These are fundamental skills for managing applications in Kubernetes, and they're essential for the AZ-204 exam.

Remember, Deployments are all about declaring your desired state and letting Kubernetes handle the details. Always use declarative YAML for production environments, and leverage the built-in rollback capabilities when things don't go as planned.

In the next section, we'll focus specifically on how these concepts apply to the AZ-204 certification exam. See you there!

---

**[END OF EXERCISES]**
