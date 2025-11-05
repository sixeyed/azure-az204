# Kubernetes Namespaces - Exercises Narration

## Opening

Alright, welcome to the hands-on portion of our Kubernetes Namespaces lab. Make sure you have your terminal open and kubectl configured to connect to your cluster. Let's discover how Kubernetes uses namespaces under the hood, and then we'll create our own.

---

## Exercise 1: Discovering Built-in Namespaces

Let's start by seeing what namespaces already exist in your cluster.

First, we're checking what pods we see by default using kubectl get pods. Depending on what you've deployed before, you might see some pods, or you might see nothing. But here's the thing - there ARE pods running in your cluster right now, even if you don't see them.

Now let's look at all the namespaces with kubectl get namespaces. Check that out! You'll see several namespaces. There's the "default" namespace where everything we've deployed so far has landed. Then there's "kube-system", which is where Kubernetes keeps its own infrastructure components. You might also see "kube-public" and "kube-node-lease" depending on your cluster.

Next we're going to see what's actually running in the kube-system namespace using kubectl get pods with the -n flag set to kube-system. Boom! There are the hidden pods. You'll see things like the DNS server, network components, and other critical Kubernetes infrastructure. These are the pods that make your cluster work, and they're isolated in their own namespace to keep them safe from accidental changes.

The key takeaway here? The -n flag tells kubectl which namespace to use. If you don't include it, you're working with the default namespace.

---

## Exercise 2: Working with System Resources

Let's try to view the logs from the system DNS server. This is a great exercise because it shows how namespaces affect every kubectl command.

First, we're trying without specifying a namespace - running kubectl logs with the label selector for k8s-app equals kube-dns. Oops! That didn't work, did it? No pods found. That's because kubectl is looking in the default namespace, and the DNS server isn't there.

Now let's try again with the correct namespace by adding the -n kube-system flag. Perfect! Now you're seeing the logs from the DNS server. This shows you can work with system resources just like your own applications - you just need to tell kubectl where to find them.

---

## Exercise 3: Understanding Contexts

Adding the namespace flag to every command gets tedious really quickly. Luckily, kubectl has a feature called contexts that lets you set defaults.

Let's see our current context using kubectl config get-contexts. You'll see information about your cluster connection. The asterisk shows which context is currently active.

Now we're looking at the full configuration by examining the kubeconfig file at ~/.kube/config. This is your kubeconfig file. It contains all your cluster connection details, authentication information, and context settings. Be careful with this file - it's how you access your clusters!

Let's change our context to use the kube-system namespace by default using kubectl config set-context with the current context flag and the namespace parameter set to kube-system. Great! Now all our kubectl commands will run against the kube-system namespace unless we override it.

---

## Exercise 4: Testing the New Context

Let's prove the context change worked.

We're getting the pods without specifying a namespace using the short form - kubectl get po. See that? Now we're seeing the system pods by default! That's because our context is set to the kube-system namespace.

Let's check those DNS logs again, this time without the namespace flag - just kubectl logs with the label selector. Perfect! It works because we're already in the kube-system namespace.

But we can still access other namespaces explicitly by running kubectl get po with the -n default flag. This shows the pods in the default namespace, even though our context is set to kube-system.

---

## Exercise 5: Switching Back to Safety

Working in the kube-system namespace is risky. One wrong command and you could break critical infrastructure. Let's switch back to the default namespace.

We're running kubectl config set-context with the current context flag, setting the namespace back to default. Always remember to do this! When you're done working with system resources, switch back to default. It's a good habit that prevents accidents.

---

## Exercise 6: Deploying Pods to Different Namespaces

Now let's deploy the same pod specification to multiple namespaces. This demonstrates how the same YAML can be reused across namespaces.

First, we're deploying to the default namespace using kubectl apply with the -f flag pointing to our sleep pod YAML file, explicitly specifying -n default. Pod created! Notice we explicitly specified the namespace even though default is our current context. Being explicit is a good practice.

Now we're deploying the exact same spec to kube-system with the same kubectl apply command but targeting kube-system namespace. Another pod created! Same specification, different namespace.

Let's see both pods at once using kubectl get pods with the label selector for app equals sleep and the --all-namespaces flag. Excellent! The --all-namespaces flag shows us pods across the entire cluster. You can see two sleep pods, one in default and one in kube-system. They're completely isolated from each other.

---

## Exercise 7: Deploying Complete Applications with Namespaces

Now we're going to deploy a complete application that includes its own namespace definition. This is how you'd typically structure namespace-based deployments in production.

We're deploying the whoami application using kubectl apply and pointing at the directory containing all the YAML files. Notice we're pointing kubectl at a directory, not a single file. Kubectl will process all the YAML files in that directory.

Here's something important: the namespace YAML file is named with "01" at the beginning. That's because kubectl processes files alphabetically, and the namespace must exist before any resources can be created inside it. It's a simple trick but very effective!

Now let's check the services in the whoami namespace using kubectl get svc with the -n whoami flag. Perfect! You can see the services that were created. When you organize applications by namespace, you don't need as many labels because the namespace itself provides the organization.

---

## Exercise 8: Deploying Another Application

Let's deploy another application called "configurable" which demonstrates how ConfigMaps work within namespaces.

We're running kubectl apply pointing at the configurable directory. Again, kubectl processes the entire directory. The namespace gets created first, then the ConfigMap and Deployment.

Now let's list all deployments across all namespaces using kubectl get deploy with the -A flag and the --show-labels flag. The -A flag is shorthand for --all-namespaces. Look at the output - you can see deployments in different namespaces, and each has its own set of labels. This gives you a cluster-wide view of what's running.

---

## Exercise 9: Cross-Namespace Filtering

Even though resources are in different namespaces, you can still filter across namespaces using labels.

We're running kubectl get svc with the -A flag for all namespaces and a label selector for kubernetes.courselabs.co equals namespaces. This shows all services across all namespaces that have this specific label. Labels and namespaces work together - namespaces provide the primary organization, and labels let you create cross-cutting views.

---

## Exercise 10: Understanding Service DNS in Namespaces

Here's where networking gets interesting. Let's explore how DNS resolution works across namespaces.

The networking in Kubernetes is flat - any pod can talk to any other pod by IP address. But DNS resolution is namespace-aware.

First, we're trying to resolve a service name without the namespace using kubectl exec to run nslookup whoami-np from inside the sleep pod. That failed, right? The sleep pod is in the default namespace, but the whoami-np service is in the whoami namespace. Local DNS names only work within the same namespace.

Now let's use the fully-qualified domain name - running nslookup for whoami-np.whoami.svc.cluster.local. Success! The FQDN includes the namespace, so the DNS lookup works across namespaces.

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

First, we're deleting all the namespaces we created using kubectl delete ns with the label selector. Watch what happens - deleting a namespace automatically deletes everything inside it. All the deployments, services, configmaps, and pods in those namespaces are gone. That's powerful, and also why you need to be careful!

Finally, let's clean up those sleep pods we created using kubectl delete po with the -A flag for all namespaces and the label selector. Perfect! We're deleting pods across all namespaces using the label selector.

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
