# Helm Exercises - Video Narration Script

**Tone:** Conversational, instructional, friendly
**Style:** Step-by-step walkthrough with screen directions

---

## Introduction (15 seconds)

Now that we understand what Helm is, let's get hands-on! In these exercises, we'll install Helm, deploy applications using charts, customize configurations, and work with chart repositories.

Let's start by getting Helm installed on our system.

---

## Exercise 1: Installing Helm CLI (1 minute)

**[SCREEN: Show terminal window]**

First things first - we need to install the Helm command-line interface. The good news is Helm uses the same configuration as kubectl, so if you're already connected to a Kubernetes cluster, you're halfway there.

**[SCREEN: Show installation commands for different OS]**

The installation is straightforward. If you're on Windows with Chocolatey, you can use choco install kubernetes-helm. On macOS with Homebrew, it's brew install helm. And on Linux, there's a convenient installation script you can download and run.

**[SCREEN: Run helm version command]**

Once installed, let's verify it's working by running helm version with the short flag. You should see a version number displayed.

One important note - always use Helm version 3 or later. Earlier versions had a server component called Tiller that introduced security concerns. Version 3 removed this completely, making Helm a purely client-side tool, which is much more secure.

---

## Exercise 2: Deploy a Chart with Default Values (2 minutes)

**[SCREEN: Show chart directory structure]**

Alright, now let's deploy our first application using Helm. We have a simple chart for the "whoami" application. Let me show you what's inside a chart.

**[SCREEN: Highlight Chart.yaml file]**

The Chart file describes the application - it's name, version, and description. These are standard Helm fields that every chart needs.

**[SCREEN: Highlight values.yaml file]**

The values file is where the magic happens. This defines default values for all the customizable settings in our templates. Things like replica counts, image tags, and port numbers.

**[SCREEN: Show deployment template]**

And here in the templates folder, we have our Kubernetes objects - but with a twist. Notice how they use variables like dot-Values-dot-imageTag instead of hard-coded values? That's the templating in action.

**[SCREEN: Back to terminal]**

Let's install this chart. We'll use the helm install command, give it a release name "whoami-default," and point it to our chart folder.

**[TYPE: helm install whoami-default labs/kubernetes/helm/charts/whoami]**

Perfect! Now let's see what we've created. We'll list our Helm releases, and then check the Kubernetes objects.

**[TYPE: helm ls]**

There's our release. Now let's see the actual Kubernetes resources.

**[TYPE: kubectl get all -l app.kubernetes.io/managed-by=Helm]**

Excellent! Helm created a Service and a Deployment, and you can see the object names include our release name "whoami-default."

**[SCREEN: Show pod labels]**

Let's look closer at the labels on these Pods. Notice how the release name is part of the labels? This is key - it means we could deploy this chart again with a different release name, and the two deployments wouldn't interfere with each other.

**[SCREEN: Test the application]**

Let's test the app by making a curl request to the service.

**[TYPE: curl localhost:30028]**

Great! And if we repeat this call, you'll see the responses are load-balanced between the two Pods.

---

## Exercise 3: Install with Custom Values (1.5 minutes)

**[SCREEN: Terminal]**

Now here's where Helm really shines - we can install the same chart again with completely different settings. Let's create a second release called "whoami-custom" with custom configuration.

We'll set the replica count to just one pod, and use a different service port to avoid conflicts.

**[TYPE: helm install whoami-custom --set replicaCount=1 --set serviceNodePort=30038 labs/kubernetes/helm/charts/whoami]**

Notice how we use the set flag to override values? You can use multiple set flags to customize as many values as you need.

**[SCREEN: Validate deployment]**

Let's verify both releases are running. We'll list our Helm releases first.

**[TYPE: helm ls]**

Perfect - two releases! Now let's look at the pods with their labels.

**[TYPE: kubectl get pods -l component=server -L app]**

Excellent! You can see one Pod labeled "whoami-custom" and two pods labeled "whoami-default." Two completely independent deployments from the same chart.

**[SCREEN: Test new service]**

And our new service should be responding on the custom port we specified.

**[TYPE: curl localhost:30038]**

There we go! Same application, different configuration, all managed elegantly by Helm.

---

## Exercise 4: Upgrade and Rollback Releases (2.5 minutes)

**[SCREEN: Terminal]**

Let's explore another powerful Helm feature - upgrading releases. Say we want to change the server mode on our custom release.

**[TYPE: helm upgrade whoami-custom --set serverMode=V labs/kubernetes/helm/charts/whoami]**

**[SCREEN: Show error message]**

Oops! That failed. This is an important lesson - when you upgrade a release, Helm doesn't automatically reuse your custom values from the install. It tried to use the default port, which is already taken by our other release.

Let's try that again, but this time we'll tell Helm to reuse the values from our original installation.

**[TYPE: helm upgrade whoami-custom --reuse-values --set serverMode=V labs/kubernetes/helm/charts/whoami]**

Much better! Now it kept our custom port and only changed the server mode.

**[SCREEN: Test the application]**

Let's test it to see the new server mode in action.

**[TYPE: curl localhost:30038]**

You'll notice the output format has changed - that's our new server mode setting working.

**[SCREEN: Terminal]**

Now, what if that upgrade didn't go as planned? Helm has you covered with rollback functionality. Let's look at the release history first.

**[TYPE: helm history whoami-custom]**

You can see all the revisions of this release - our initial install and our upgrade. Let's roll back to revision 1.

**[TYPE: helm rollback whoami-custom 1]**

**[SCREEN: Show ReplicaSets]**

After the rollback, if we check the ReplicaSets, you'll see Kubernetes has scaled back up the original one.

**[TYPE: kubectl get rs -l app=whoami-custom]**

**[SCREEN: Test application]**

And testing the app confirms we're back to the quiet server mode from our original deployment.

**[TYPE: curl localhost:30038]**

This rollback capability is crucial for production environments - you can quickly revert if an upgrade causes issues.

---

## Exercise 5: Working with Chart Repositories (2 minutes)

**[SCREEN: Terminal]**

So far, we've been working with local charts. But in the real world, you'll often want to use charts from repositories. Let's see how that works.

**[SCREEN: Show helm repo commands]**

First, let's check what repositories we have configured.

**[TYPE: helm repo ls]**

Nothing yet. Let's add a public chart repository.

**[TYPE: helm repo add kiamol https://kiamol.net]**

And then we'll update our repository index, just like updating package lists in apt or yum.

**[TYPE: helm repo update]**

**[SCREEN: Search for charts]**

Now we can search across all our repositories. Let's look for a chart called "vweb."

**[TYPE: helm search repo vweb --versions]**

You'll see multiple versions listed. Notice there are two version numbers - the app version and the chart version. Charts can evolve independently, so the same application version might have multiple chart versions with different features.

**[SCREEN: Show values for a specific version]**

Before installing, let's see what values are available in this chart.

**[TYPE: helm show values kiamol/vweb --version 2.0.0]**

This shows us all the configurable options with helpful comments. This is really useful when you're working with charts you didn't create.

**[SCREEN: Install from repository]**

Let's install this chart. The syntax is almost identical to local charts, we just specify the repository name and chart name together.

**[TYPE: helm install --set replicaCount=1 --set serviceType=NodePort --set servicePort=30039 vweb kiamol/vweb --version 2.0.0]**

**[SCREEN: Verify deployment]**

Let's confirm the service is running.

**[TYPE: kubectl get svc -l app.kubernetes.io/instance=vweb]**

Perfect! And you could browse to this application in your web browser at the port we specified.

This is how you'd install popular applications like Prometheus, Grafana, or the Nginx Ingress Controller - all available as charts in public repositories.

---

## Lab Challenge Introduction (30 seconds)

**[SCREEN: Show lab challenge]**

Now it's your turn! For the lab challenge, you'll install the Nginx Ingress Controller using its public Helm chart. The twist? You'll use a values file instead of multiple set flags to configure it.

Take a look at the provided values file for a local environment setup. You'll need to create a new namespace, install the chart with at least version 1.4.0, and verify Nginx is responding correctly.

Give it a try, and if you get stuck, there are hints and a solution available. Good luck!

---

## Closing (15 seconds)

Great work! You've now experienced the core workflows of Helm - installing charts, customizing deployments, upgrading and rolling back releases, and working with repositories. These skills are essential for managing Kubernetes applications efficiently, especially for the AZ-204 exam.

In the next video, we'll focus specifically on the AZ-204 exam aspects of Helm. See you there!
