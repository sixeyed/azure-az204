# Helm Exercises - Video Narration Script

## Introduction

Now that we understand what Helm is, let's get hands-on! In these exercises, we'll install Helm, deploy applications using charts, customize configurations, and work with chart repositories.

Let's start by getting Helm installed on our system.

---

## Exercise 1: Installing Helm CLI

First things first - we need to install the Helm command-line interface. The good news is Helm uses the same configuration as kubectl, so if you're already connected to a Kubernetes cluster, you're halfway there.

The installation is straightforward. If you're on Windows with Chocolatey, you can use choco install kubernetes-helm. On macOS with Homebrew, it's brew install helm. And on Linux, there's a convenient installation script you can download and run from the Helm GitHub releases page.

Once installed, let's verify it's working by running helm version with the short flag. You should see a version number displayed, confirming Helm is properly installed.

One important note - always use Helm version 3 or later. Earlier versions had a server component called Tiller that introduced security concerns. It required cluster-wide permissions and created a security risk. Version 3 removed this completely, making Helm a purely client-side tool, which is much more secure and simpler to manage.

---

## Exercise 2: Deploy a Chart with Default Values

Alright, now let's deploy our first application using Helm. We have a simple chart for the "whoami" application. Let me show you what's inside a chart.

The Chart file describes the application - its name, version, and description. These are standard Helm fields that every chart needs to identify itself.

The values file is where the magic happens. This defines default values for all the customizable settings in our templates. Things like replica counts, image tags, port numbers, and service types.

And here in the templates folder, we have our Kubernetes objects - but with a twist. Notice how they use variables like dot Values dot imageTag instead of hard-coded values? That's the templating in action. Helm replaces these placeholders with actual values when rendering the templates.

Let's install this chart. We'll use the helm install command, give it a release name "whoami-default," and point it to our chart folder.

Perfect! Now let's see what we've created. We'll list our Helm releases using helm ls, and then check the Kubernetes objects.

There's our release. Now let's see the actual Kubernetes resources using kubectl get all filtered by the Helm managed-by label.

Excellent! Helm created a Service and a Deployment, and you can see the object names include our release name "whoami-default." This is important - it means we could deploy this chart again with a different release name, and the two deployments wouldn't interfere with each other. They'd be completely independent.

Let's look closer at the labels on these Pods. Notice how the release name is part of the labels? That's the key to isolation.

Let's test the app by making a curl request to the service on its NodePort.

Great! And if we repeat this call, you'll see the responses are load-balanced between the two Pods. Different hostnames appear in the responses.

---

## Exercise 3: Install with Custom Values

Now here's where Helm really shines - we can install the same chart again with completely different settings. Let's create a second release called "whoami-custom" with custom configuration.

We'll set the replica count to just one pod using the set flag with replicaCount equals 1, and use a different service port to avoid conflicts with set serviceNodePort equals 30038.

Notice how we use the set flag to override values? You can use multiple set flags to customize as many values as you need. Each set flag overrides one value from the defaults.

Let's verify both releases are running. We'll list our Helm releases first.

Perfect - two releases! Now let's look at the pods with their labels.

Excellent! You can see one Pod labeled "whoami-custom" with its single replica, and two pods labeled "whoami-default" with two replicas. Two completely independent deployments from the same chart, running side by side.

And our new service should be responding on the custom port we specified. Let's curl localhost on port 30038.

There we go! Same application, different configuration, all managed elegantly by Helm.

---

## Exercise 4: Upgrade and Rollback Releases

Let's explore another powerful Helm feature - upgrading releases. Say we want to change the server mode on our custom release.

We're using helm upgrade with the release name whoami-custom, setting serverMode to V.

Oops! That failed. This is an important lesson - when you upgrade a release, Helm doesn't automatically reuse your custom values from the install. It tried to use the default port, which is already taken by our other release. This is a common mistake.

Let's try that again, but this time we'll tell Helm to reuse the values from our original installation using the reuse-values flag.

Much better! Now it kept our custom port and only changed the server mode. The reuse-values flag tells Helm to merge our new settings with the previous custom values.

Let's test it to see the new server mode in action with curl.

You'll notice the output format has changed - that's our new server mode setting working, showing verbose output.

Now, what if that upgrade didn't go as planned? Helm has you covered with rollback functionality. Let's look at the release history first using helm history.

You can see all the revisions of this release - our initial install as revision 1 and our upgrade as revision 2. Each change creates a new revision.

Let's roll back to revision 1 using helm rollback specifying the release name and revision number.

After the rollback, if we check the ReplicaSets, you'll see Kubernetes has scaled back up the original one and scaled down the upgraded one.

And testing the app confirms we're back to the quiet server mode from our original deployment. The rollback capability is crucial for production environments - you can quickly revert if an upgrade causes issues.

---

## Exercise 5: Working with Chart Repositories

So far, we've been working with local charts stored in our file system. But in the real world, you'll often want to use charts from repositories, similar to how you use package managers like npm or apt.

First, let's check what repositories we have configured using helm repo ls.

Nothing yet. Let's add a public chart repository using helm repo add with a name and URL.

And then we'll update our repository index using helm repo update, just like updating package lists in apt or yum. This downloads the latest chart metadata from all configured repositories.

Now we can search across all our repositories. Let's look for a chart called "vweb" using helm search repo with the versions flag to see all available versions.

You'll see multiple versions listed. Notice there are two version numbers - the app version and the chart version. Charts can evolve independently from the application, so the same application version might have multiple chart versions with different features or bug fixes.

Before installing, let's see what values are available in this chart using helm show values with a specific version.

This shows us all the configurable options with helpful comments explaining what each does. This is really useful when you're working with charts you didn't create yourself.

Let's install this chart. The syntax is almost identical to local charts, we just specify the repository name and chart name together, separated by a slash.

We're providing custom values for replica count, service type, and service port using multiple set flags.

Let's confirm the service is running using kubectl get svc filtered by the instance label.

Perfect! And you could browse to this application in your web browser at the port we specified.

This is how you'd install popular applications like Prometheus for monitoring, Grafana for visualization, or the Nginx Ingress Controller - all available as charts in public repositories. The Helm ecosystem has thousands of pre-built charts ready to use.

---

## Lab Challenge Introduction

Now it's your turn! For the lab challenge, you'll install the Nginx Ingress Controller using its public Helm chart. The twist? You'll use a values file instead of multiple set flags to configure it.

Take a look at the provided values file for a local environment setup. You'll need to create a new namespace for the ingress controller, install the chart with at least version 1.4.0, and verify Nginx is responding correctly on its service port.

Give it a try, and if you get stuck, there are hints and a solution available. This challenge will solidify your understanding of working with chart repositories and values files. Good luck!

---

## Closing

Great work! You've now experienced the core workflows of Helm - installing charts, customizing deployments, upgrading and rolling back releases, and working with repositories. These skills are essential for managing Kubernetes applications efficiently, especially for the AZ-204 exam.

Helm simplifies complex deployments, provides repeatable installations, and makes it easy to share application packages across teams and organizations. It's become the standard package manager for Kubernetes, and understanding it is crucial for modern cloud-native development.

In the next video, we'll focus specifically on the AZ-204 exam aspects of Helm. See you there!
