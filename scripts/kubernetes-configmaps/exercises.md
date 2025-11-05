# Kubernetes ConfigMaps - Lab Exercises Narration Script

**Format:** Conversational voice-over for hands-on lab walkthrough

---

## Introduction to the Lab

Alright, now that we understand what ConfigMaps are and why they're important, let's dive into the hands-on exercises. We're going to work with a demo application that's specifically designed to show you how configuration works in Kubernetes. This app can read settings from multiple sources and merge them together, which is exactly what you'll encounter in real-world scenarios.

---

## Exercise 1: Running the App with Default Configuration

Let's start by running the configurable demo app with its default settings. This will give us a baseline to compare against as we add configuration.

*[SHOW ON SCREEN: Terminal with kubectl run command]*

We're using the kubectl run command here, which creates a simple Pod without any YAML files. This is great for quick testing and debugging. We're running the image called sixeyed/configurable version 21.04, and we're adding a label to help us clean up later.

```
kubectl run configurable --image=sixeyed/configurable:21.04
```

*[SHOW ON SCREEN: kubectl wait command]*

Now we'll wait for the Pod to be ready. The wait command is really handy because it blocks until the condition is met, so we don't have to keep checking manually.

```
kubectl wait --for=condition=Ready pod configurable
```

*[SHOW ON SCREEN: kubectl port-forward command]*

To access the app, we'll use port forwarding. This creates a tunnel from your local machine's port 8080 to port 80 inside the container.

```
kubectl port-forward pod/configurable 8080:80
```

*[SHOW ON SCREEN: Browser showing the app at localhost:8080]*

Now, open your browser and navigate to localhost on port 8080. Take a look at what you see here. These are the default configuration settings that come from the JSON file baked into the container image. You can also see various environment variables, some from the Dockerfile, some from the container operating system, and some that Kubernetes sets automatically.

This is our baseline. Every setting you see here is hardcoded into the container image. In a moment, we'll see how to override these without rebuilding the image.

*[SHOW ON SCREEN: Ctrl-C in terminal]*

Go ahead and press Ctrl-C to exit the port-forward command. Then let's clean up this Pod since we're going to deploy the app properly using a Deployment.

```
kubectl delete pod configurable
```

Great! The Pod is deleted.

---

## Exercise 2: Setting Config with Environment Variables in Pod Spec

Now let's deploy the app using a Deployment, which is what you'd use in production. But this time, we're going to add some configuration directly in the Pod specification.

*[SHOW ON SCREEN: deployment.yaml file contents]*

If you look at the deployment YAML file, you'll see it defines an environment variable right in the container spec. This is the simplest way to add configuration, and it's perfect for single settings like a version number or a feature flag.

*[SHOW ON SCREEN: Terminal with kubectl apply command]*

Let's apply all the YAML files in the configurable specs directory. Notice we're pointing to the folder, not individual files. Kubectl will process all YAML files it finds.

```
kubectl apply -f labs/kubernetes/configmaps/specs/configurable/
```

*[SHOW ON SCREEN: Terminal output showing created resources]*

You can see that both a Deployment and a Service were created. The Deployment manages our Pods, and the Service provides networking.

Now, let's verify that our environment variable is actually set inside the container. We'll use kubectl exec to run a command inside the Pod.

*[SHOW ON SCREEN: kubectl exec command]*

```
kubectl exec deploy/configurable -- printenv | grep __
```

We're running printenv to list all environment variables, and piping it through grep to filter for variables with double underscores, which is the naming convention our app uses.

*[SHOW ON SCREEN: Terminal output showing Configurable__Release=24.01.1]*

Perfect! You can see the environment variable is set. The value is 24.01.1, which came from our YAML specification.

Now let's view this in the browser to confirm the app is using this configuration.

*[SHOW ON SCREEN: kubectl get svc command]*

First, we need to find our Service details.

```
kubectl get svc -l app=configurable
```

*[SHOW ON SCREEN: Browser showing updated configuration]*

And there it is! The release version now shows 24.01.1, which came from our environment variable instead of the default value in the image.

---

## Exercise 3: Using ConfigMaps for Environment Variables

Setting individual environment variables in the Pod spec works, but it gets messy when you have lots of settings. That's where ConfigMaps come in. Let's create a ConfigMap that holds multiple configuration values.

*[SHOW ON SCREEN: configmap-env.yaml file contents]*

Take a look at this ConfigMap YAML. It's a simple Kubernetes object with a data section containing multiple key-value pairs. We have a release version and an environment setting.

*[SHOW ON SCREEN: deployment-env.yaml file contents]*

And here's the updated Deployment. Instead of defining environment variables directly, it references the ConfigMap using the envFrom field. This tells Kubernetes to load all the values from that ConfigMap as environment variables.

*[SHOW ON SCREEN: Terminal with kubectl apply command]*

Let's apply these files.

```
kubectl apply -f labs/kubernetes/configmaps/specs/configurable/config-env/
```

*[SHOW ON SCREEN: Terminal output]*

Notice what happened here. The ConfigMap was created, and the Deployment was configured. But remember, Deployments don't manage Pods directly. They use another object called a ReplicaSet. When you update a Deployment, it creates a new ReplicaSet with the updated Pod template, and gradually replaces the old Pods with new ones. This is called a rolling update.

Let's check the environment variables in the new Pod.

*[SHOW ON SCREEN: kubectl exec command]*

```
kubectl exec deploy/configurable -- printenv | grep __
```

*[SHOW ON SCREEN: Terminal output showing both variables]*

Excellent! Now you can see the release is version 24.01.2, and there's a new environment variable for the environment setting, which is set to "uat" for user acceptance testing. Both of these came from our ConfigMap, not from hardcoded values in the Deployment spec.

---

## Exercise 4: Mounting ConfigMaps as Files

Environment variables are useful, but they have some limitations. They're visible to all processes running in the container, which could be a security risk. And if you have complex configuration with nested settings, environment variables can become unwieldy.

The solution is to use the filesystem. We can create a ConfigMap that contains an entire configuration file, and mount it into the container's filesystem.

*[SHOW ON SCREEN: configmap-json.yaml file contents]*

Look at this ConfigMap. Instead of simple key-value pairs, it contains a complete JSON file. The filename is the key, and the file contents come after the pipe and dash separator. Notice the indentation—this is important. The file contents must be indented one level more than the filename.

*[SHOW ON SCREEN: deployment-json.yaml file contents]*

Now look at the Deployment. There are two new sections here. At the bottom, under volumes, we define a volume that references our ConfigMap. Then, in the container spec, we mount that volume into the filesystem at the path slash app slash config. The readOnly flag means the container can't modify the file.

Notice this Deployment still loads environment variables from the previous ConfigMap. So we're using both methods at once.

*[SHOW ON SCREEN: Terminal with kubectl apply command]*

Let's apply this configuration.

```
kubectl apply -f labs/kubernetes/configmaps/specs/configurable/config-json/
```

*[SHOW ON SCREEN: Browser refresh showing new settings]*

If you refresh the web app, you'll see new settings appearing. These are coming from the override.json file that we mounted from the ConfigMap.

Let's explore the container filesystem to see exactly what happened.

*[SHOW ON SCREEN: kubectl exec commands]*

```
kubectl exec deploy/configurable -- ls /app/
```

*[SHOW ON SCREEN: Terminal output showing files]*

Here are the files in the app directory. You can see the original appsettings.json file that was built into the image, plus a config subdirectory.

```
kubectl exec deploy/configurable -- ls /app/config/
```

*[SHOW ON SCREEN: Terminal output]*

And inside the config directory, there's our override.json file. This came from the ConfigMap volume mount.

Let's look at the actual file contents.

```
kubectl exec deploy/configurable -- cat /app/config/override.json
```

*[SHOW ON SCREEN: Terminal output showing JSON content]*

Perfect! There's our JSON configuration, exactly as we defined it in the ConfigMap.

---

## Understanding Configuration Hierarchy

Now, here's something interesting that you need to understand for real-world applications. Let's look at both the file and the environment variables together.

*[SHOW ON SCREEN: Split screen showing both commands]*

```
kubectl exec deploy/configurable -- cat /app/config/override.json
kubectl exec deploy/configurable -- printenv | grep __
```

*[SHOW ON SCREEN: Highlighting the Release setting in both outputs]*

Notice something? The JSON file has a Release setting, and there's also an environment variable for Release. But in the web app, which one is being used?

*[SHOW ON SCREEN: Browser showing the app]*

If you check the browser, you'll see the Release value is coming from the environment variable, not from the file. This is because of configuration hierarchy. This particular application gives priority to environment variables over file-based settings.

Different applications have different hierarchies. Some read environment variables first, others prioritize config files, and some let you specify the order explicitly. When you're working with your own applications, you need to understand their configuration hierarchy to model your ConfigMaps correctly.

---

## Lab Challenge

Alright, you've learned how to create ConfigMaps using YAML files. But there's another way to create ConfigMaps that some organizations prefer. Kubernetes lets you create ConfigMaps directly from values or from existing files, without writing any YAML at all.

*[SHOW ON SCREEN: deployment-lab.yaml file]*

Your challenge is to create two new ConfigMaps to support this Deployment. You need to set an environment variable for the Release with the value "21.04-lab", and you need to create a JSON file that sets a feature flag for Dark Mode to true.

But here's the twist: don't use YAML files to create these ConfigMaps. Use the kubectl create configmap command instead. This is a useful skill because sometimes you want to quickly create a ConfigMap from an existing file without templating it into YAML.

Take your time with this. If you get stuck, there are hints available, and there's a full solution you can reference. The key is understanding the kubectl create configmap command and its various flags for different data sources.

Good luck! This is where you really solidify your understanding of ConfigMaps.

---

## Cleanup

Once you're done with the lab, it's good practice to clean up your resources. We've been adding labels to all our objects, which makes cleanup really easy.

*[SHOW ON SCREEN: Terminal with cleanup command]*

```
kubectl delete configmap,deploy,svc,pod -l kubernetes.courselabs.co=configmaps
```

This single command deletes all ConfigMaps, Deployments, Services, and Pods that have our lab label. No need to delete each object individually.

*[SHOW ON SCREEN: Terminal output showing deleted resources]*

And we're clean! All the resources from this lab are removed.

---

## Wrap Up

Great work! You've now experienced ConfigMaps in action. You've seen how to create them with YAML, how to inject them as environment variables, how to mount them as files, and how configuration hierarchy affects which settings win.

These skills are essential for the AZ-204 exam and for working with Kubernetes in production. ConfigMaps are one of those fundamental building blocks that you'll use in virtually every Kubernetes deployment.

Keep practicing, and you'll be managing application configuration like a pro!
