# Kubernetes Pods - Hands-On Lab Narration
## Conversational Voice-Over Script

---

## Opening

Alright, let's get hands-on with Kubernetes Pods! In this lab, we're going to deploy some Pods, explore them, and see how they communicate. Make sure you have your Kubernetes cluster ready to go - we'll be using kubectl throughout this exercise.

---

## Understanding Pod YAML Specifications

Before we deploy anything, let's take a quick look at what a Pod specification looks like.

**[On screen: Show the whoami-pod.yaml file]**

Every Kubernetes resource needs four essential fields. First is the API version - resources are versioned to maintain backwards compatibility. Then the kind, which tells Kubernetes what type of object we're creating. We've got metadata, which includes the name and other identifying information. And finally, the spec, which describes the actual resource.

For Pods, the spec is pretty straightforward. We define a list of containers, and for each container, we specify a name and a container image to run. The indentation matters here - YAML uses spaces to show the nested structure, so be careful with your formatting.

---

## Deploying Your First Pod

Let's deploy our first Pod!

**[On screen: Show terminal, ready to type command]**

We're going to use the kubectl apply command with the flag dash f to specify our YAML file. The file is located in the labs kubernetes pods specs directory, and it's called whoami-pod.yaml.

**[On screen: Execute kubectl apply command]**

```
kubectl apply -f labs/kubernetes/pods/specs/whoami-pod.yaml
```

Nice! You'll see output confirming that the Pod was created. Now here's something cool about Kubernetes - it works on desired state deployment. If you run that same command again...

**[On screen: Run the command again]**

See? It tells us nothing has changed. Kubernetes looked at what we wanted and saw it already existed, so it didn't create a duplicate.

---

## Viewing Pod Information

Now let's see what we've got running.

**[On screen: Terminal ready for next command]**

Type kubectl get pods to see a list of all Pods in the current namespace.

**[On screen: Execute kubectl get pods]**

```
kubectl get pods
```

There's our whoami Pod! You can see its status, how many restarts it's had, and how long it's been running.

Want more details? Let's use the short name "p-o" instead of "pods" and add the dash o wide flag for extra columns.

**[On screen: Execute kubectl get po -o wide]**

```
kubectl get po -o wide
```

Now we can see additional information like the Pod's IP address and which node it's running on. This is really useful information when you're troubleshooting.

If you want to see everything about a Pod in a readable format, you can use the describe command - try running kubectl describe pod whoami to see all the details.

---

## Working with Pod Logs

Let's check what's happening inside our Pod by looking at the logs.

**[On screen: Terminal showing kubectl logs command]**

Simply type kubectl logs followed by the Pod name, which is whoami.

**[On screen: Execute command]**

```
kubectl logs whoami
```

And there you go - these are the logs from the container running inside the Pod. This is incredibly useful for debugging and monitoring your applications.

---

## Executing Commands Inside Pods

Now let's try connecting to the container inside the Pod.

**[On screen: Show terminal]**

We'll use kubectl exec with the flags dash i t for interactive terminal, specify the Pod name, then use double dash to separate our kubectl options from the command we want to run inside the container. We'll try to start a shell with s-h.

**[On screen: Execute command]**

```
kubectl exec -it whoami -- sh
```

Oops! This doesn't work. The error message tells us that the container doesn't have a shell installed. This is actually pretty common with minimal container images that are designed to be small and secure.

No problem - let's deploy a different Pod that does have a shell.

---

## Deploying the Sleep Pod

**[On screen: Show sleep-pod.yaml briefly]**

We have another spec file called sleep-pod.yaml. This runs a container that just sleeps, but it includes useful tools we can use for testing.

Let's deploy it.

**[On screen: Execute command]**

```
kubectl apply -f labs/kubernetes/pods/specs/sleep-pod.yaml
```

And let's verify it's running:

```
kubectl get pods
```

Perfect! Now we have two Pods running - whoami and sleep.

---

## Exploring Inside a Container

Now let's connect to the sleep Pod's container.

**[On screen: Execute command]**

```
kubectl exec -it sleep -- sh
```

Excellent! We're now inside the container. Notice how our prompt has changed - we're literally running a shell session inside the container.

Let's explore a bit. First, let's check the hostname:

**[On screen: Type hostname]**

```
hostname
```

See how the hostname matches the Pod name? That's a Kubernetes convention.

Now let's see what user we're running as:

```
whoami
```

We're running as root in this case, though in production you'd typically run as a non-root user for security.

---

## Exploring the Kubernetes Network

Now let's explore the Kubernetes network from inside the container.

**[On screen: Type nslookup command]**

Let's look up the Kubernetes service:

```
nslookup kubernetes
```

There it is! The Kubernetes API server is accessible from inside every Pod. This allows applications to interact with the Kubernetes API if they need to.

Now let's try to ping it:

**[On screen: Type ping command]**

```
ping kubernetes
```

And... this fails. That's expected - Kubernetes internal addresses don't support ICMP ping. They use HTTP or HTTPS instead.

Let's exit this shell session:

```
exit
```

And we're back to our local terminal.

---

## Pod-to-Pod Communication

Now here's where it gets really interesting - let's see how Pods communicate with each other.

First, we need the IP address of our whoami Pod.

**[On screen: Execute command]**

```
kubectl get pods -o wide whoami
```

There's the IP address in the IP column - this is the internal IP address that any other Pod in the cluster can use to connect.

**[On screen: Highlight the IP address shown in the output]**

Now we're going to make an HTTP request from the sleep Pod to the whoami Pod. We'll use kubectl exec to run a curl command inside the sleep Pod.

**[On screen: Execute command with actual IP from previous output shown on screen]**

```
kubectl exec sleep -- curl -s [IP ADDRESS SHOWN ON SCREEN]
```

Boom! We got a response from the whoami server. This output shows the hostname, the IP addresses, and other information about the whoami container. This demonstrates that Pods can directly communicate with each other using their IP addresses.

---

## Lab Challenge: Understanding Pod Restarts

Alright, here's your challenge. Pods are designed to provide high availability by automatically restarting containers that fail. Let's see this in action.

**[On screen: Show the lab challenge text]**

Your task is to write a Pod spec that runs a container from the image "courselabs/bad-sleep" - and yes, it's intentionally badly configured! The container will keep exiting, and you'll watch how Kubernetes handles this.

Take a few minutes to create your YAML file and deploy it. Then watch what happens using kubectl get pods with the dash w flag for watch mode. You'll see the restart count increase as Kubernetes keeps trying to make it work.

After about 30 seconds, notice what happens. Then keep watching for a couple of minutes. Kubernetes implements a backoff strategy, so the time between restarts increases.

Give it a try! And when you're done, remember to clean up by deleting the Pod.

---

## Cleanup

Speaking of cleanup, let's remove all the Pods we created today.

**[On screen: Show terminal]**

You can delete multiple Pods in one command by listing their names:

```
kubectl delete pod sleep whoami sleep-lab
```

The sleep-lab is the Pod from your lab exercise. If you named yours differently, adjust the command accordingly.

**[On screen: Execute command]**

And there we go - all cleaned up!

---

## Wrap Up

Great work! You've successfully deployed Pods, explored them from inside, viewed logs, and demonstrated Pod-to-Pod communication. You've also seen how Kubernetes automatically restarts failed containers to maintain availability.

These are fundamental skills you'll use constantly when working with Kubernetes on Azure. In the next section, we'll look at the specific AZ-204 exam concepts you need to master around Pods.

See you there!

---

**[End of exercises video]**
