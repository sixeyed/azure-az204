# Kubernetes Secrets

## Reference

Secrets are Kubernetes objects designed to store sensitive information like passwords, tokens, and API keys, providing basic protection through base64 encoding and access controls. Unlike ConfigMaps which store data in plain text, Secrets offer additional security features including RBAC integration and the option to encrypt data at rest in etcd. Understanding the distinction between Secrets and ConfigMaps is crucial for implementing proper security practices in containerized applications.

## Introduction

Alright, let's get our hands dirty with Kubernetes Secrets! In this lab, we're going to work through several different ways to create and manage secrets, and see how they differ from ConfigMaps. Make sure you have your terminal open and you're connected to your Kubernetes cluster.

---

## Exercise 1: Understanding ConfigMaps vs Secrets

First, let's deploy our sample application using ConfigMaps so we can see the security issue we're trying to solve.

We're running the first command to deploy the configurable app with ConfigMaps. You should see the resources being created - deployments, services, and config maps.

Great! Now let's inspect a ConfigMap to see what the problem is. We're getting all config maps, and you'll see our configurable environment map listed there.

Now we're describing that config map. See what's happening here? All the configuration values are right there in plain text. Anyone with read access to your cluster can see everything. This is fine for non-sensitive data, but what about passwords or API keys? That's definitely not good.

---

## Exercise 2: Creating Secrets from Encoded YAML

Let's fix this security issue by using Secrets instead. Our first approach will use base-64 encoded values in YAML.

Take a look at this YAML file. Notice it looks similar to a ConfigMap, but we're using kind Secret. The data values are base-64 encoded - they're not readable at first glance, but remember, this is encoding, not encryption.

The deployment YAML references this secret using secretRef instead of configMapRef. That's the key difference in how we load secrets into our pods.

We're applying the secrets-encoded configuration now. The deployment will roll out with the new secret mounted as environment variables. Once that's complete, we're browsing to the application. You should see the configuration value for Environment is now loaded from the secret, but to your application, it appears as plain text. That's important - secrets are always decoded inside the container so your app doesn't need to change.

---

## Exercise 3: Creating Secrets from Plain Text YAML

Base-64 encoding is a bit awkward to work with. If your YAML files are already secured - maybe they're in a private repository with strict access controls - you might want to use plain text instead.

Notice this file uses stringData instead of data. This lets you write values in plain text, which Kubernetes will encode for you automatically when it stores the secret.

We're applying the secrets-plain configuration now. This will update the existing secret and trigger a new rollout of your deployment. Refreshing the application in the browser, you'll see the config value has updated. Your application picked up the new secret value automatically.

---

## Exercise 4: Working with Base-64 Values

Let's explore how secrets are actually stored and how you can decode them. This is important to understand because it shows that base-64 is not security through obscurity.

First, we're describing the secret we just created. Notice that kubectl doesn't show you the actual values - just the size in bytes. This is kubectl being cautious with potentially sensitive data.

Now let's extract the actual encoded value using a JSON path query. You'll see a base-64 encoded string output to your terminal.

Finally, we're piping that through base-64 decode, and boom - there's your plain text value. This is why base-64 encoding alone is NOT sufficient security. You need proper access controls and ideally, encryption at rest in your cluster.

---

## Exercise 5: Creating Secrets from Files

In real-world scenarios, you often have a separation of concerns. Your security team manages the actual secret values, while your DevOps team manages the deployments. Let's simulate that workflow.

Here we have two files: an environment variable file and a JSON configuration file. These contain sensitive data that only the security team should access.

First, let's play the role of the security team. We're creating a secret from the environment file using the create secret generic command with the from-env-file flag. This pulls all the key-value pairs from the file into a secret.

Now we're creating another secret from the JSON file using the from-file flag. This creates a secret where the entire file becomes a single data entry.

Perfect! Now we're switching hats and playing the DevOps team. They don't have access to those original files, but they can reference the secrets that were already created. We're applying the deployment configuration that references these file-based secrets.

Browsing to the application one more time, you should see an additional configuration source - the secret JSON file is mounted as a volume in your container. Your application can read it just like any other file, but it's being securely managed by Kubernetes.

---

## Lab Challenge

Okay, here's an interesting challenge for you to work through. Right now, if you update a secret that's mounted as a file, Kubernetes will push that change into the container. But your application might not notice the file changed.

The traditional approach is to manually trigger a deployment rollout to restart the pods. But that's a two-step process - update the secret, then rollout the deployment. That's error-prone.

Your challenge is to come up with a better approach. How can you make the deployment rollout happen automatically when the secret changes, all in one kubectl apply command?

Think about what triggers a deployment rollout. What would need to change in the deployment spec to force new pods to be created?

I'll give you some time to work on this. If you get stuck, there are hints available in the lab materials, and of course, there's a solution file. But try to figure it out yourself first - that's where the real learning happens!

---

## Cleanup

Once you're done experimenting, make sure to clean up your resources. We're running the delete command to remove all the objects with the secrets label. This keeps your cluster tidy and ready for the next lab.

---

## Wrap Up

Excellent work! You've now experienced multiple ways to create and manage Kubernetes secrets. You've seen firsthand why ConfigMaps aren't suitable for sensitive data. You've worked with base-64 encoding and understood its limitations. And you've explored the workflow of separating secret management from application deployment.

Remember, in production environments, you'll want to integrate with Azure Key Vault or similar secret management systems. But the fundamental concepts you've learned here - how to reference secrets, how to mount them as environment variables or files, and how to manage secret lifecycle - these all apply regardless of where your secrets ultimately come from.

Great job, and I'll see you in the next lab!
