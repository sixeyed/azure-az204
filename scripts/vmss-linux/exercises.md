# Virtual Machine Scale Sets - Linux: Exercise Walkthrough

## Exercise 1: Create a VM with cloud-init

### Setting Up the Resource Group

Let's start by creating a new resource group for this lab. We're using az group create with the name "labs-vmss-linux", adding our "courselabs=azure" tag for tracking, and setting the location to West Europe. The resource group provides a container for all the resources we'll create in this scale set lab.

### Understanding cloud-init Scripts

Before we create our VM, let's talk about the cloud-init script we'll be using. There's a script file located in the labs directory called cloud-init.txt that contains a simple initialization script for installing the Nginx web server. Cloud-init is an industry-standard tool that automates the complete setup of Linux VMs as they provision - it's like having a build script that runs automatically on first boot.

Cloud-init scripts allow you to define everything from package installation to file creation to user configuration, making them incredibly powerful for VM automation. Instead of manually configuring each VM after it starts, cloud-init handles everything during the provisioning process.

### Creating the VM

Now we'll create a VM from the Ubuntu LTS image, passing our cloud-init script as custom data. Azure supports this through the custom-data parameter which injects initialization scripts into new VMs.

We're using az vm create with the location West Europe, resource group "labs-vmss-linux", VM name "web01", image set to "UbuntuLTS", a size that you have quota for in your subscription, and here's the important part - the custom-data parameter with an @ symbol to reference the local file at labs/vmss-linux/setup/cloud-init.txt. We're also setting a unique public IP address DNS name for easy access.

Notice the @ symbol syntax - this tells the Azure CLI to read the file contents and pass them as the parameter value. It's a convenient way to include script files without copying and pasting their contents.

### Verifying cloud-init Execution

After your VM is created, we can verify that the cloud-init script ran successfully. The cloud-init system writes its execution output to a standard log file location on the VM at /var/log/cloud-init-output.log.

Let's use the VM run-command feature to check it without SSH-ing into the VM. We're running az vm run-command invoke with the resource group "labs-vmss-linux", VM name "web01", command-id set to "RunShellScript" for executing shell commands, and the --scripts parameter containing a cat command to display the log file contents.

You'll see the complete installation log for Nginx in the output. This confirms that our cloud-init script executed successfully during the VM provisioning process. You should see messages about updating package lists, downloading Nginx, and configuring the service.

Let's test that the web server is actually running and responding to requests. We're using run-command again, this time with a curl command to make a local HTTP request to localhost.

You should see the default Nginx welcome page HTML returned in the output. This confirms that Nginx is not only installed but actually running and serving web pages on port 80.

## Exercise 2: Use cloud-init for Linux VMSS

### Advanced cloud-init Script

Now that we understand how cloud-init works with individual VMs, let's look at a more sophisticated script. There's another file called cloud-init-custom.txt that not only installs Nginx but also writes a custom HTML page.

Importantly, cloud-init allows you to inject variables into files during creation. In this example, we're embedding the VM hostname into the web page content. This will help us see load balancing in action later - each instance will serve a page showing its own unique hostname.

### Creating the VM Scale Set

The approach for using cloud-init with a VM Scale Set is essentially the same as with a single VM. Let's create a VMSS with three instances running simultaneously.

We're running az vmss create with the name "vmss-web01", resource group "labs-vmss-linux", VM SKU parameter set to a size you have quota for, instance count set to 3 which creates three VMs immediately, image as "UbuntuLTS", custom-data pointing to our cloud-init-custom.txt file with the @ symbol, and a unique public IP address DNS name.

This command does a lot of work - it creates the scale set resource, provisions three VM instances, creates a load balancer to distribute traffic, sets up networking infrastructure, and runs cloud-init on each instance.

### Configuring the Load Balancer

As we've seen in previous labs, when Azure creates a new VM Scale Set, it automatically provisions a public IP address and a load balancer to distribute traffic across instances. However, the load balancer rules aren't configured by default - we need to set those up ourselves.

Let's verify this by listing the load balancers. We're running az network lb list with the resource group "labs-vmss-linux" and table output.

This shows us the load balancer name that was automatically created. Now let's check if there are any rules configured using az network lb rule list with the resource group, table output, and the load balancer name.

Notice there are no rules configured. Without rules, the load balancer doesn't know how to route traffic - it has no routing table. We need to create both a health probe and a load balancer rule to make this work.

First, let's create the health probe for port 80. Health probes are how the load balancer determines which instances are healthy and ready to receive traffic. We're running az network lb probe create with the resource group "labs-vmss-linux", probe name "http", protocol set to TCP which just checks if the port is open, port set to 80, and the load balancer name.

Now we can create the load balancer rule that references this health probe. We're running az network lb rule create with the resource group, the probe-name set to "http" to link it to the probe we just created, rule name "http", protocol TCP, frontend port 80 which is what clients connect to, backend port 80 which is where the VMs are listening, and the load balancer name.

This rule tells the load balancer: listen on port 80 externally, forward traffic to port 80 on the backend instances, and only send traffic to instances that pass the health probe check.

### Testing the Deployment

Now you can browse to your public IP address or DNS name in a web browser. You should see the custom HTML page displaying the machine's hostname. The hostname will be something like "vmss-web01_0" or "vmss-web01_1" indicating which instance served your request.

Because we have load balancing configured, you can test it with curl to see responses from different instances. We're running curl with your public IP or DNS name.

Repeat this command several times and you'll see responses from all three instances, each showing its unique hostname. The load balancer is distributing requests in a round-robin pattern across the healthy instances.

## Exercise 3: Update VMSS

### Understanding the VMSS Model

VM Scale Sets use a model-based approach for managing updates. The VMSS model stores the desired state of instances - what image to use, what size, what configuration. Each instance can be upgraded when the model changes, but this doesn't happen automatically - you control when instances are updated.

Let's check the current instance status using az vmss list-instances with the resource group "labs-vmss-linux" and scale set name "vmss-web01".

In the output, look for the "latestModelApplied" field in each instance. Right now, all instances should show true because they were just created from the current model.

### Updating the Model

We're going to update the VMSS model by changing the cloud-init script to a new version. There's a file called cloud-init-updated.txt that contains changes to the HTML content that Nginx serves - perhaps a different message or styling.

Updating the custom data requires a bit of extra work because we need to Base64 encode the file content before passing it to the update command. This is a requirement of the Azure API for this particular setting.

In PowerShell, we're creating a variable by running cat to read the file contents and piping it to base64 for encoding.

In Bash, the syntax is similar with the variable assignment using equals.

Now we can update the VMSS model using az vmss update with the resource group "labs-vmss-linux", scale set name "vmss-web01", and the --set parameter to modify the virtualMachineProfile.osProfile.customData property to our base64-encoded value.

### Model vs Instance State

After this command completes, check the instance list again using az vmss list-instances.

This is a critical concept to understand: the instances now show that they don't have the latest model applied. The "latestModelApplied" field will be false. Changes to the model are not automatically applied to existing VMs - the model represents the desired state, but Azure doesn't force that state onto running instances. This gives you control over when updates roll out, which is crucial for managing service availability.

### Updating Instances

To apply the new model to existing instances, we need to explicitly update them using az vmss update-instances with the resource group "labs-vmss-linux", scale set name "vmss-web01", and instance-ids parameter set to asterisk which means all instances.

Now check the instances again and you'll see they're all using the latest model - "latestModelApplied" is back to true. However, if you browse to the web page, you'll notice the HTML hasn't actually changed. Why?

This is because custom data is only processed at provisioning time - when the VM first boots. The VMs have been updated with the new custom data setting in their configuration, but they haven't been reprovisioned, so the cloud-init script with the new HTML hasn't run.

### Scaling to See New Configuration

Let's scale up the VMSS to add new instances. New instances will use the new model and provision with the updated content.

We're running az vmss scale with the resource group "labs-vmss-linux", scale set name "vmss-web01", and new-capacity set to 5 which adds two more instances.

Now when you make curl requests to the load balancer, you'll see different responses from the old instances and the new instances. The original three instances show the old HTML content, while the two new instances created after the model update show the updated HTML content. This demonstrates how the model works - it affects new instances but doesn't automatically change existing ones.

## Lab Challenge

Your VM Scale Set is now in an inconsistent state, and this is your challenge to solve. All the VMs show they're on the latest model and they're all healthy, making them valid targets for the load balancer. But they're running different versions of the application - some show the old HTML, some show the new HTML.

Your challenge is to force the old VMs to be recreated from the current model so they all show consistent content. You can do this through the Azure Portal or using the CLI.

The key is finding the right command to reimage or recreate the instances rather than just updating them. Think about the difference between updating an instance configuration versus reimaging it from scratch. Look for commands like "az vmss reimage" that actually rebuild the instances.

Take a few minutes to explore the available VMSS commands and the Portal options to solve this challenge. This is a practical skill you'll need when managing scale sets in production.

## Cleanup

When you're finished with the lab, don't forget to clean up your resources to avoid ongoing charges.

We're running az group delete with the -y flag to skip confirmation and the resource group name "labs-vmss-linux".

This will remove all the resources we created during this lab - the scale set, all VM instances, the load balancer, the public IP, networking components, and everything else. The cleanup takes a few minutes as Azure tears down the infrastructure.
