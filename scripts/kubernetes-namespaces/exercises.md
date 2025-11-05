# Kubernetes Namespaces - Exercises Narration
## Step-by-Step Lab Walkthrough

---

## Opening

Alright, welcome to the hands-on portion of our Kubernetes Namespaces lab. Make sure you have your terminal open and kubectl configured to connect to your cluster. Let's discover how Kubernetes uses namespaces under the hood, and then we'll create our own.

---

## Exercise 1: Discovering Built-in Namespaces

Let's start by seeing what namespaces already exist in your cluster.

**[TYPE COMMAND]**

First, let's check what pods we see by default. Type:

```
kubectl get pods
```

Depending on what you've deployed before, you might see some pods, or you might see nothing. But here's the thing - there ARE pods running in your cluster right now, even if you don't see them.

**[TYPE COMMAND]**

Let's look at all the namespaces:

```
kubectl get namespaces
```

Check that out! You'll see several namespaces. There's the "default" namespace where everything we've deployed so far has landed. Then there's "kube-system", which is where Kubernetes keeps its own infrastructure components. You might also see "kube-public" and "kube-node-lease" depending on your cluster.

**[TYPE COMMAND]**

Now let's see what's actually running in the kube-system namespace:

```
kubectl get pods -n kube-system
```

Boom! There are the hidden pods. You'll see things like the DNS server, network components, and other critical Kubernetes infrastructure. These are the pods that make your cluster work, and they're isolated in their own namespace to keep them safe from accidental changes.

The key takeaway here? The `-n` flag tells kubectl which namespace to use. If you don't include it, you're working with the default namespace.

---

## Exercise 2: Working with System Resources

Let's try to view the logs from the system DNS server. This is a great exercise because it shows how namespaces affect every kubectl command.

**[TYPE COMMAND]**

First, let's try without specifying a namespace:

```
kubectl logs -l k8s-app=kube-dns
```

Oops! That didn't work, did it? No pods found. That's because kubectl is looking in the default namespace, and the DNS server isn't there.

**[TYPE COMMAND]**

Now let's try again with the correct namespace:

```
kubectl logs -l k8s-app=kube-dns -n kube-system
```

Perfect! Now you're seeing the logs from the DNS server. This shows you can work with system resources just like your own applications - you just need to tell kubectl where to find them.

---

## Exercise 3: Understanding Contexts

Adding the namespace flag to every command gets tedious really quickly. Luckily, kubectl has a feature called contexts that lets you set defaults.

**[TYPE COMMAND]**

Let's see our current context:

```
kubectl config get-contexts
```

You'll see information about your cluster connection. The asterisk shows which context is currently active.

**[TYPE COMMAND]**

Now let's look at the full configuration:

```
cat ~/.kube/config
```

This is your kubeconfig file. It contains all your cluster connection details, authentication information, and context settings. Be careful with this file - it's how you access your clusters!

**[TYPE COMMAND]**

Let's change our context to use the kube-system namespace by default:

```
kubectl config set-context --current --namespace kube-system
```

Great! Now all our kubectl commands will run against the kube-system namespace unless we override it.

---

## Exercise 4: Testing the New Context

Let's prove the context change worked.

**[TYPE COMMAND]**

Get the pods without specifying a namespace:

```
kubectl get po
```

See that? Now we're seeing the system pods by default! That's because our context is set to the kube-system namespace.

**[TYPE COMMAND]**

Let's check those DNS logs again, this time without the namespace flag:

```
kubectl logs -l k8s-app=kube-dns
```

Perfect! It works because we're already in the kube-system namespace.

**[TYPE COMMAND]**

But we can still access other namespaces explicitly:

```
kubectl get po -n default
```

This shows the pods in the default namespace, even though our context is set to kube-system.

---

## Exercise 5: Switching Back to Safety

Working in the kube-system namespace is risky. One wrong command and you could break critical infrastructure. Let's switch back to the default namespace.

**[TYPE COMMAND]**

```
kubectl config set-context --current --namespace default
```

Always remember to do this! When you're done working with system resources, switch back to default. It's a good habit that prevents accidents.

---

## Exercise 6: Deploying Pods to Different Namespaces

Now let's deploy the same pod specification to multiple namespaces. This demonstrates how the same YAML can be reused across namespaces.

**[TYPE COMMAND]**

First, let's deploy to the default namespace:

```
kubectl apply -f labs/kubernetes/namespaces/specs/sleep-pod.yaml -n default
```

Pod created! Notice we explicitly specified the namespace even though default is our current context. Being explicit is a good practice.

**[TYPE COMMAND]**

Now let's deploy the exact same spec to kube-system:

```
kubectl apply -f labs/kubernetes/namespaces/specs/sleep-pod.yaml -n kube-system
```

Another pod created! Same specification, different namespace.

**[TYPE COMMAND]**

Let's see both pods at once:

```
kubectl get pods -l app=sleep --all-namespaces
```

Excellent! The `--all-namespaces` flag shows us pods across the entire cluster. You can see two sleep pods, one in default and one in kube-system. They're completely isolated from each other.

---

## Exercise 7: Deploying Complete Applications with Namespaces

Now we're going to deploy a complete application that includes its own namespace definition. This is how you'd typically structure namespace-based deployments in production.

**[TYPE COMMAND]**

Let's deploy the whoami application:

```
kubectl apply -f labs/kubernetes/namespaces/specs/whoami
```

Notice we're pointing kubectl at a directory, not a single file. Kubectl will process all the YAML files in that directory.

Here's something important: the namespace YAML file is named with "01" at the beginning. That's because kubectl processes files alphabetically, and the namespace must exist before any resources can be created inside it. It's a simple trick but very effective!

**[TYPE COMMAND]**

Let's check the services in the whoami namespace:

```
kubectl get svc -n whoami
```

Perfect! You can see the services that were created. When you organize applications by namespace, you don't need as many labels because the namespace itself provides the organization.

---

## Exercise 8: Deploying Another Application

Let's deploy another application called "configurable" which demonstrates how ConfigMaps work within namespaces.

**[TYPE COMMAND]**

Deploy the application:

```
kubectl apply -f labs/kubernetes/namespaces/specs/configurable
```

Again, kubectl processes the entire directory. The namespace gets created first, then the ConfigMap and Deployment.

**[TYPE COMMAND]**

Now let's list all deployments across all namespaces:

```
kubectl get deploy -A --show-labels
```

The `-A` flag is shorthand for `--all-namespaces`. Look at the output - you can see deployments in different namespaces, and each has its own set of labels. This gives you a cluster-wide view of what's running.

---

## Exercise 9: Cross-Namespace Filtering

Even though resources are in different namespaces, you can still filter across namespaces using labels.

**[TYPE COMMAND]**

```
kubectl get svc -A -l kubernetes.courselabs.co=namespaces
```

This shows all services across all namespaces that have this specific label. Labels and namespaces work together - namespaces provide the primary organization, and labels let you create cross-cutting views.

---

## Exercise 10: Understanding Service DNS in Namespaces

Here's where networking gets interesting. Let's explore how DNS resolution works across namespaces.

The networking in Kubernetes is flat - any pod can talk to any other pod by IP address. But DNS resolution is namespace-aware.

**[TYPE COMMAND]**

First, let's try to resolve a service name without the namespace:

```
kubectl exec pod/sleep -- nslookup whoami-np
```

That failed, right? The sleep pod is in the default namespace, but the whoami-np service is in the whoami namespace. Local DNS names only work within the same namespace.

**[TYPE COMMAND]**

Now let's use the fully-qualified domain name:

```
kubectl exec pod/sleep -- nslookup whoami-np.whoami.svc.cluster.local
```

Success! The FQDN includes the namespace, so the DNS lookup works across namespaces.

The format is: service-name DOT namespace-name DOT svc DOT cluster DOT local.

This is a best practice - always use FQDNs when communicating between namespaces. It's more explicit and prevents confusing DNS failures.

---

## Lab Challenge

Alright, here's your challenge. The kubectl commands for switching contexts and namespaces are pretty verbose and awkward. There are two amazing tools called kubens and kubectx that make this much easier.

Your task is to search for these tools, figure out how to install them on your system, and try them out. They're going to save you tons of time when working with multiple clusters and namespaces.

Take a few minutes to do this on your own, and then come back when you're ready.

---

## Cleanup

When you're done experimenting, let's clean up the resources we created.

**[TYPE COMMAND]**

First, delete all the namespaces we created:

```
kubectl delete ns -l kubernetes.courselabs.co=namespaces
```

Watch what happens - deleting a namespace automatically deletes everything inside it. All the deployments, services, configmaps, and pods in those namespaces are gone. That's powerful, and also why you need to be careful!

**[TYPE COMMAND]**

Finally, let's clean up those sleep pods we created:

```
kubectl delete po -A -l kubernetes.courselabs.co=namespaces
```

Perfect! We're deleting pods across all namespaces using the label selector.

---

## Wrap-Up

Excellent work! You've now seen how namespaces work in Kubernetes. You learned how to:

- View and work with built-in namespaces
- Switch between namespaces using contexts
- Deploy applications with their own namespaces
- Understand how DNS resolution works across namespaces
- Use labels and namespaces together for organization

Namespaces are one of those features that seem simple at first, but they're incredibly powerful. They're the foundation for multi-tenancy, resource management, and access control in Kubernetes.

As you prepare for the AZ-204 exam, remember that these concepts apply directly to Azure Kubernetes Service. The patterns you've learned here are exactly what you'll use in production Azure environments.

Great job today! See you in the next lab!
