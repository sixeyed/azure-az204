# Kubernetes Secrets - Exercise Walkthrough Script

**Format:** Step-by-step lab narration
**Tone:** Conversational, encouraging, instructional
**Pace:** Moderate with pauses for hands-on work

---

## Introduction

Alright, let's get our hands dirty with Kubernetes Secrets! In this lab, we're going to work through several different ways to create and manage secrets, and see how they differ from ConfigMaps. Make sure you have your terminal open and you're connected to your Kubernetes cluster.

---

## Exercise 1: Understanding ConfigMaps vs Secrets

First, let's deploy our sample application using ConfigMaps so we can see the security issue we're trying to solve.

**[Screen: Terminal ready]**

Go ahead and run the first command to deploy the configurable app with ConfigMaps. You should see the resources being created - deployments, services, and config maps.

**[Pause for deployment]**

Great! Now let's inspect a ConfigMap to see what the problem is. Type the command to get all config maps, and you'll see our configurable environment map listed there.

Now describe that config map. See what's happening here? All the configuration values are right there in plain text. Anyone with read access to your cluster can see everything. This is fine for non-sensitive data, but what about passwords or API keys? That's definitely not good.

---

## Exercise 2: Creating Secrets from Encoded YAML

Let's fix this security issue by using Secrets instead. Our first approach will use base-64 encoded values in YAML.

**[Screen: Show the secret-encoded YAML file]**

Take a look at this YAML file. Notice it looks similar to a ConfigMap, but we're using kind Secret. The data values are base-64 encoded - they're not readable at first glance, but remember, this is encoding, not encryption.

The deployment YAML references this secret using secretRef instead of configMapRef. That's the key difference in how we load secrets into our pods.

**[Screen: Return to terminal]**

Apply the secrets-encoded configuration now. The deployment will roll out with the new secret mounted as environment variables.

**[Pause for deployment]**

Once that's complete, browse to your application. You should see the configuration value for Environment is now loaded from the secret, but to your application, it appears as plain text. That's important - secrets are always decoded inside the container so your app doesn't need to change.

---

## Exercise 3: Creating Secrets from Plain Text YAML

Base-64 encoding is a bit awkward to work with. If your YAML files are already secured - maybe they're in a private repository with strict access controls - you might want to use plain text instead.

**[Screen: Show the secret-plain YAML file]**

Notice this file uses stringData instead of data. This lets you write values in plain text, which Kubernetes will encode for you automatically when it stores the secret.

**[Screen: Return to terminal]**

Apply the secrets-plain configuration. This will update the existing secret and trigger a new rollout of your deployment.

**[Pause for deployment]**

Refresh your application in the browser, and you'll see the config value has updated. Your application picked up the new secret value automatically.

---

## Exercise 4: Working with Base-64 Values

Let's explore how secrets are actually stored and how you can decode them. This is important to understand because it shows that base-64 is not security through obscurity.

**[Screen: Terminal]**

First, describe the secret we just created. Notice that kubectl doesn't show you the actual values - just the size in bytes. This is kubectl being cautious with potentially sensitive data.

Now let's extract the actual encoded value using a JSON path query. You'll see a base-64 encoded string output to your terminal.

**[Note: If on Windows, narrator mentions the PowerShell setup needed]**

Finally, pipe that through base-64 decode, and boom - there's your plain text value. This is why base-64 encoding alone is NOT sufficient security. You need proper access controls and ideally, encryption at rest in your cluster.

---

## Exercise 5: Creating Secrets from Files

In real-world scenarios, you often have a separation of concerns. Your security team manages the actual secret values, while your DevOps team manages the deployments. Let's simulate that workflow.

**[Screen: Show the secret files]**

Here we have two files: an environment variable file and a JSON configuration file. These contain sensitive data that only the security team should access.

**[Screen: Return to terminal]**

First, let's play the role of the security team. Create a secret from the environment file using the create secret generic command with the from-env-file flag. This pulls all the key-value pairs from the file into a secret.

**[Pause for command]**

Now create another secret from the JSON file using the from-file flag. This creates a secret where the entire file becomes a single data entry.

**[Pause for command]**

Perfect! Now switch hats and play the DevOps team. They don't have access to those original files, but they can reference the secrets that were already created. Apply the deployment configuration that references these file-based secrets.

**[Pause for deployment]**

Browse to your application one more time. Now you should see an additional configuration source - the secret JSON file is mounted as a volume in your container. Your application can read it just like any other file, but it's being securely managed by Kubernetes.

---

## Lab Challenge

Okay, here's an interesting challenge for you to work through. Right now, if you update a secret that's mounted as a file, Kubernetes will push that change into the container. But your application might not notice the file changed.

The traditional approach is to manually trigger a deployment rollout to restart the pods. But that's a two-step process - update the secret, then rollout the deployment. That's error-prone.

**[Screen: Show thinking pose]**

Your challenge is to come up with a better approach. How can you make the deployment rollout happen automatically when the secret changes, all in one kubectl apply command?

**[Pause]**

Think about what triggers a deployment rollout. What would need to change in the deployment spec to force new pods to be created?

I'll give you some time to work on this. If you get stuck, there are hints available in the lab materials, and of course, there's a solution file. But try to figure it out yourself first - that's where the real learning happens!

---

## Cleanup

Once you're done experimenting, make sure to clean up your resources. Run the delete command to remove all the objects with the secrets label. This keeps your cluster tidy and ready for the next lab.

---

## Wrap Up

**[Screen: Summary slide]**

Excellent work! You've now experienced multiple ways to create and manage Kubernetes secrets. You've seen firsthand why ConfigMaps aren't suitable for sensitive data. You've worked with base-64 encoding and understood its limitations. And you've explored the workflow of separating secret management from application deployment.

Remember, in production environments, you'll want to integrate with Azure Key Vault or similar secret management systems. But the fundamental concepts you've learned here - how to reference secrets, how to mount them as environment variables or files, and how to manage secret lifecycle - these all apply regardless of where your secrets ultimately come from.

Great job, and I'll see you in the next lab!

---

**[End of exercises]**
