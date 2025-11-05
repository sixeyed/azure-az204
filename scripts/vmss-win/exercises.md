# Virtual Machine Scale Sets - Windows - Exercises

## Exercise 1: Create VMSS from Custom Image

### Verify Prerequisites

Let's start by verifying that we have our resource group and custom image ready. We'll check the resource group first:

```
az group show -o table -n labs-vmss-win
```

This should show our resource group is ready. Now let's check for the image:

```
az image list -o table -g labs-vmss-win
```

You should see the "app01-image" that we created in the VM images lab. If it's not there, you'll need to go back and complete those steps first.

### Create the VMSS

Now we'll create our Virtual Machine Scale Set. We need to specify several parameters - the VM size, instance count, which port to expose, the image to use, and admin credentials.

Here's the command:

```
az vmss create -n vmss-app01 -g labs-vmss-win --vm-sku Standard_D2s_v5 --instance-count 3 --backend-port 3389 --image app01-image --admin-username labs --admin-password <strong-password> -l westeurope
```

This creates a scale set with three instances, using our custom image. We're exposing port 3389 for RDP access.

This will take a few minutes to complete. While it's creating, Azure is provisioning three VMs, a load balancer, a public IP address, and configuring networking.

### Explore the Resources

Once creation is complete, let's check what VMs we have:

```
az vm list -o table -g labs-vmss-win
```

Notice there are no individual VMs listed. That's because with VMSS, you manage instances through the scale set resource, not as separate VMs.

Now let's explore in the portal. Open the resource group - you'll see several new resources including the VMSS, a load balancer, a public IP address, and networking components.

Open the VMSS resource and navigate to the Instances blade. You'll see three instances, each with its own status. They might be in different states like Running or Updating, and the instance numbers might not be sequential - we'll explain why later.

Click on one of the instances. Notice it has a private IP address but no public IP. So how do we access the application?

Back in the resource group, open the public IP address resource. It shows it's associated to the load balancer. The load balancer is how we'll route traffic to our instances.

Try browsing to the public IP address. Does the application respond?

No, it doesn't work yet. Let's fix that.

## Exercise 2: Configure Load Balancing

### Understanding the Load Balancer

The VMSS creation automatically set up a load balancer, which is a networking component that listens on the public IP and routes traffic to the VMSS instances.

But why doesn't it work? Because the default VMSS setup doesn't include load balancing rules. Without rules, the load balancer has no routing table and doesn't know where to send traffic.

Let's explore the load balancer in the portal.

First, select Backend pools. You'll see all three VMSS instances are registered and running. So the load balancer knows about our VMs.

Next, select Health probes. This is how the load balancer checks if backend resources are ready to receive traffic. Right now there are no probes configured.

Finally, select Load balancing rules. There are none, which is why our app doesn't work. The load balancer receives requests but has no rules to forward them to the backend.

### Add a Load Balancing Rule

Let's add a rule to make our application accessible. Click to add a new load balancing rule and give it any name you like.

For the frontend, select the public IP address.

For the backend pool, select the VMSS backend pool.

For both the port and backend port, enter 80.

You'll also need to create a health probe. Select HTTP as the probe type.

Save the rule and wait for it to deploy.

### Test the Application

Load balancers only send traffic to healthy endpoints, which is why the health probe is essential. It continuously checks each instance to ensure it's ready to handle requests.

Now browse to the public IP address again. You should see the application responding.

If you refresh the page multiple times, do you see responses from different VMs? The browser caching might make this hard to see.

Let's use curl instead to make GET requests:

```
curl http://<your-public-ip>
```

Repeat this command several times. You should see different VM names in the HTML response, as the load balancer distributes requests across all three instances.

## Exercise 3: Manual Scaling

### Scale Up

Currently we have three instances running. Let's scale up to five instances using the vmss scale command:

```
az vmss scale -g labs-vmss-win -n vmss-app01 --new-capacity 5
```

This command is simple - you just specify the desired capacity and Azure handles the rest.

Let's check the portal. Open the VMSS and view the Instances blade. You'll see new instances being created.

These new instances also get automatically added to the load balancer backend pool. When they become healthy according to our health probe, they'll start receiving traffic.

Windows VMs take a few minutes to provision, so be patient. You might also see more than five instances temporarily. Why?

Azure uses overprovisioning. It knows there's variation in VM startup time, so it creates more instances than you need. When the desired count are online and healthy, it removes the extra ones that may still be starting up. This is why the instance numbers aren't always sequential - the missing numbers represent instances that were removed during overprovisioning.

Once the new instances are healthy, try your curl command again:

```
curl http://<your-public-ip>
```

Repeat several times and you should see the new instances in the responses, sharing the request load.

## Exercise 4: Autoscaling

### Configure Autoscaling

So far we've been using manual scaling. But VMSS also supports autoscaling, where Azure automatically adjusts capacity based on metrics.

For VM-based autoscaling, the primary metric is CPU usage. When instances are working too hard, the VMSS adds more. When there's not enough work, instances are removed.

Let's configure autoscaling in the portal. Open the VMSS and navigate to the Scaling blade.

Switch from manual scaling to Custom autoscale.

Select "Scale based on a metric".

Set the minimum instance count to 2, maximum to 3, and default to 2.

Now add a scale-out rule: increase by one instance if average CPU is greater than 10 percent.

Add a scale-in rule: decrease by one instance if average CPU is less than 8 percent.

We're using low CPU thresholds and short timescales - 2 minutes - so we can see the scaling happen quickly during this lab.

### Observe Scaling Behavior

Currently we have five instances running from our manual scale operation. What happens when we switch to autoscaling?

The maximum is three instances, so Azure will start removing instances to comply with the autoscale rules.

After a few minutes, you should see two instances entering a deleting state, bringing the count down to the maximum of three.

Those deleting instances are automatically removed from the load balancer backend pool, so your application continues working during the scale-in operation.

After a few more minutes with low CPU activity, another instance will be removed, bringing us to the minimum of two.

Notice which instances get removed. Is it the most recent ones, or is there a different pattern? This is an interesting consideration - what happens if a VM was handling a request when it gets deleted? The load balancer and VMSS work together to drain connections gracefully before removing an instance.

## Exercise 5: Lab Challenge - Health Probes

Here's your challenge exercise. Health probes are a powerful feature for managing failure scenarios. You should test that your application works correctly when instances become unhealthy.

The task is to connect to one of the VMSS instances using Remote Desktop and stop the IIS Windows Service. This will make that instance fail its health probe.

Observe what happens. Does the load balancer stop sending traffic to that instance? Can you see the probe status change in the portal?

The application should continue working on the remaining healthy instances, demonstrating the resilience that VMSS and load balancing provide.

Take some time to work through this challenge and explore the health probe behavior.

## Cleanup

When you're finished exploring, clean up the lab resources:

```
az group delete -y -n labs-vmss-win
```

This deletes the resource group and all resources within it. When the VMSS is deleted, all the VM instances are automatically deleted too.

This concludes our Virtual Machine Scale Sets lab. You've learned how to create a VMSS from a custom image, configure load balancing, scale manually and automatically, and work with health probes.
