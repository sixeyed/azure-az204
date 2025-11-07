# Kubernetes Pods

## Reference

Pods are the smallest deployable units in Kubernetes and represent a single instance of a running process in your cluster. Each Pod can contain one or more containers that share networking and storage resources, and Kubernetes manages their lifecycle automatically. Understanding Pods is fundamental to working with any container orchestration platform because every other Kubernetes resource builds on this core concept.

## Opening

Alright, let's get hands-on with Kubernetes Pods! In this lab, we're going to deploy some Pods, explore them, and see how they communicate. Make sure you have your Kubernetes cluster ready to go - we'll be using kubectl throughout this exercise.

---

## Understanding Pod YAML Specifications

Before we deploy anything, let's take a quick look at what a Pod specification looks like.

Looking at a Pod YAML file, every Kubernetes resource needs four essential fields. First is the API version - resources are versioned to maintain backwards compatibility. Then the kind, which tells Kubernetes what type of object we're creating. We've got metadata, which includes the name and other identifying information. And finally, the spec, which describes the actual resource.

For Pods, the spec is pretty straightforward. We define a list of containers, and for each container, we specify a name and a container image to run. The indentation matters here - YAML uses spaces to show the nested structure, so be careful with your formatting.

---

## Deploying Your First Pod

Let's deploy our first Pod!

We're going to use the kubectl apply command with the -f flag to specify our YAML file. The file is located in the labs kubernetes pods specs directory, and it's called whoami-pod.yaml.

Nice! You'll see output confirming that the Pod was created. Now here's something cool about Kubernetes - it works on desired state deployment. If you run that same command again, it tells us nothing has changed. Kubernetes looked at what we wanted and saw it already existed, so it didn't create a duplicate.

---

## Viewing Pod Information

Now let's see what we've got running.

We're running kubectl get pods to see a list of all Pods in the current namespace. There's our whoami Pod! You can see its status, how many restarts it's had, and how long it's been running.

Want more details? Let's use the short name "po" instead of "pods" and add the -o wide flag for extra columns. Now we can see additional information like the Pod's IP address and which node it's running on. This is really useful information when you're troubleshooting.

If you want to see everything about a Pod in a readable format, you can use the describe command - kubectl describe pod whoami shows all the details including events, resource usage, and the current state.

---

## Working with Pod Logs

Let's check what's happening inside our Pod by looking at the logs.

We're running kubectl logs followed by the Pod name, which is whoami. And there you go - these are the logs from the container running inside the Pod. This is incredibly useful for debugging and monitoring your applications.

---

## Executing Commands Inside Pods

Now let's try connecting to the container inside the Pod.

We'll use kubectl exec with the -it flags for interactive terminal, specify the Pod name, then use double dash to separate our kubectl options from the command we want to run inside the container. We'll try to start a shell with sh.

Oops! This doesn't work. The error message tells us that the container doesn't have a shell installed. This is actually pretty common with minimal container images that are designed to be small and secure.

No problem - let's deploy a different Pod that does have a shell.

---

## Deploying the Sleep Pod

We have another spec file called sleep-pod.yaml. This runs a container that just sleeps, but it includes useful tools we can use for testing.

Let's deploy it using kubectl apply. And we'll verify it's running with kubectl get pods. Perfect! Now we have two Pods running - whoami and sleep.

---

## Exploring Inside a Container

Now let's connect to the sleep Pod's container using kubectl exec -it sleep -- sh.

Excellent! We're now inside the container. Notice how our prompt has changed - we're literally running a shell session inside the container.

Let's explore a bit. First, we're checking the hostname. See how the hostname matches the Pod name? That's a Kubernetes convention.

Now let's see what user we're running as with the whoami command. We're running as root in this case, though in production you'd typically run as a non-root user for security.

---

## Exploring the Kubernetes Network

Now let's explore the Kubernetes network from inside the container.

We're running nslookup to look up the Kubernetes service. There it is! The Kubernetes API server is accessible from inside every Pod. This allows applications to interact with the Kubernetes API if they need to.

Now let's try to ping it. And... this fails. That's expected - Kubernetes internal addresses don't support ICMP ping. They use HTTP or HTTPS instead.

Let's exit this shell session and we're back to our local terminal.

---

## Pod-to-Pod Communication

Now here's where it gets really interesting - let's see how Pods communicate with each other.

First, we need the IP address of our whoami Pod. We're running kubectl get pods -o wide whoami. There's the IP address in the IP column - this is the internal IP address that any other Pod in the cluster can use to connect.

Now we're going to make an HTTP request from the sleep Pod to the whoami Pod. We'll use kubectl exec to run a curl command inside the sleep Pod, targeting the whoami Pod's IP address.

Boom! We got a response from the whoami server. This output shows the hostname, the IP addresses, and other information about the whoami container. This demonstrates that Pods can directly communicate with each other using their IP addresses.

---

## Lab Challenge: Understanding Pod Restarts

Alright, here's your challenge. Pods are designed to provide high availability by automatically restarting containers that fail. Let's see this in action.

Your task is to write a Pod spec that runs a container from the image "courselabs/bad-sleep" - and yes, it's intentionally badly configured! The container will keep exiting, and you'll watch how Kubernetes handles this.

Take a few minutes to create your YAML file and deploy it. Then watch what happens using kubectl get pods with the -w flag for watch mode. You'll see the restart count increase as Kubernetes keeps trying to make it work.

After about 30 seconds, notice what happens. Then keep watching for a couple of minutes. Kubernetes implements a backoff strategy, so the time between restarts increases.

Give it a try! And when you're done, remember to clean up by deleting the Pod.

---

## Cleanup

Speaking of cleanup, let's remove all the Pods we created today.

You can delete multiple Pods in one command by listing their names - kubectl delete pod sleep whoami sleep-lab. The sleep-lab is the Pod from your lab exercise. If you named yours differently, adjust the command accordingly.

And there we go - all cleaned up!

---

## Wrap Up

Great work! You've successfully deployed Pods, explored them from inside, viewed logs, and demonstrated Pod-to-Pod communication. You've also seen how Kubernetes automatically restarts failed containers to maintain availability.

These are fundamental skills you'll use constantly when working with Kubernetes on Azure. In the next section, we'll look at the specific AZ-204 exam concepts you need to master around Pods.

See you there!
