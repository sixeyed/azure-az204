# Virtual Machine Scale Sets - Linux: Exercise Walkthrough

## Exercise 1: Create a VM with cloud-init

### Setting Up the Resource Group

Let's start by creating a new resource group for this lab. We'll use the West Europe region and tag it appropriately:

```bash
az group create -n labs-vmss-linux --tags courselabs=azure -l westeurope
```

### Understanding cloud-init Scripts

Before we create our VM, let's talk about the cloud-init script we'll be using. The script located at `/labs/vmss-linux/setup/cloud-init.txt` is a simple init script that installs the Nginx web server. cloud-init scripts allow you to automate the complete setup of your VM as it provisions.

### Creating the VM

Now we'll create a VM from the Ubuntu LTS image, passing our cloud-init script as custom data. Azure supports this through the custom data parameter. Notice how we reference local files using the at-sign syntax:

```bash
az vm create -l westeurope -g labs-vmss-linux -n web01 --image UbuntuLTS --size <your-vm-size> --custom-data @labs/vmss-linux/setup/cloud-init.txt --public-ip-address-dns-name <your-dns-name>
```

### Verifying cloud-init Execution

After your VM is created, we can verify that the cloud-init script ran successfully. The cloud-init system writes its output to a standard log file location. Let's use the VM run-command feature to check it:

```bash
az vm run-command invoke -g labs-vmss-linux -n web01 --command-id RunShellScript --scripts "cat /var/log/cloud-init-output.log"
```

You'll see the complete install log for Nginx in the output. This confirms that our cloud-init script executed successfully during the VM provisioning process.

Let's test that the web server is actually running by making a local request:

```bash
az vm run-command invoke -g labs-vmss-linux -n web01 --command-id RunShellScript --scripts "curl localhost"
```

You should see the default Nginx welcome page HTML returned.

## Exercise 2: Use cloud-init for Linux VMSS

### Advanced cloud-init Script

Now that we understand how cloud-init works, let's look at a more sophisticated script. The `cloud-init-custom.txt` file not only installs Nginx but also writes a custom HTML page. Importantly, cloud-init allows you to inject variables into files. In this example, we're putting the VM hostname into the web page, which will help us see load balancing in action.

### Creating the VM Scale Set

The approach for using cloud-init with a VM Scale Set is essentially the same as with a single VM. Let's create a VMSS with three instances:

```bash
az vmss create -n vmss-web01 -g labs-vmss-linux --vm-sku <your-vm-sku> --instance-count 3 --image UbuntuLTS --custom-data @labs/vmss-linux/setup/cloud-init-custom.txt --public-ip-address-dns-name <unique-dns-name>
```

### Configuring the Load Balancer

As we've seen in previous labs, when Azure creates a new VM Scale Set, it automatically provisions a public IP address and a load balancer. However, the load balancer rules aren't configured by default. Let's verify this:

```bash
az network lb list -g labs-vmss-linux -o table
```

This shows us the load balancer name. Now let's check the rules:

```bash
az network lb rule list -g labs-vmss-linux -o table --lb-name <lb-name>
```

Notice there are no rules configured. We need to create both a health probe and a load balancer rule.

First, let's create the health probe for port 80:

```bash
az network lb probe create -g labs-vmss-linux -n 'http' --protocol tcp --port 80 --lb-name <lb-name>
```

Now we can create the load balancer rule that references this health probe:

```bash
az network lb rule create -g labs-vmss-linux --probe-name 'http' -n 'http' --protocol Tcp --frontend-port 80 --backend-port 80 --lb-name <lb-name>
```

### Testing the Deployment

Now you can browse to your public IP address or DNS name. You should see the custom HTML page displaying the machine's hostname. Because we have load balancing configured, you can test it with curl to see responses from different instances:

```bash
curl http://<pip-address>
```

Repeat this command several times and you'll see responses from all three instances, each showing its unique hostname.

## Exercise 3: Update VMSS

### Understanding the VMSS Model

VM Scale Sets use a model-based approach for managing updates. The VMSS model stores the desired state of instances. Each instance can be upgraded when the model changes, but this doesn't happen automatically.

Let's check the current instance status:

```bash
az vmss list-instances -g labs-vmss-linux -n vmss-web01
```

In the output, look for the `latestModelApplied` field. Right now, all instances should show true because they were just created.

### Updating the Model

We're going to update the VMSS model by changing the cloud-init script to a new version. The `cloud-init-updated.txt` file contains changes to the HTML content that Nginx serves.

Updating the custom data requires a bit of extra work because we need to Base64 encode the file content. In PowerShell, use:

```powershell
$customData=$(cat labs/vmss-linux/setup/cloud-init-updated.txt | base64)
```

Or in Bash:

```bash
customData=$(cat labs/vmss-linux/setup/cloud-init-updated.txt | base64)
```

Now we can update the VMSS model:

```bash
az vmss update -g labs-vmss-linux -n vmss-web01 --set virtualMachineProfile.osProfile.customData=$customData
```

### Model vs Instance State

After this command completes, check the instance list again:

```bash
az vmss list-instances -g labs-vmss-linux -n vmss-web01
```

This is a critical concept: the instances now show that they don't have the latest model applied. Changes to the model are not automatically applied to existing VMs. This gives you control over when updates roll out.

### Updating Instances

To apply the new model to existing instances, we need to explicitly update them:

```bash
az vmss update-instances -g labs-vmss-linux -n vmss-web01 --instance-ids '*'
```

Now check the instances again and you'll see they're all using the latest model. However, if you browse to the web page, you'll notice the HTML hasn't changed. This is because custom data is only processed at provisioning time. The VMs have been updated with the new custom data, but they haven't been reprovisioned.

### Scaling to See New Configuration

Let's scale up the VMSS. New instances will use the new model and provision with the updated content:

```bash
az vmss scale -g labs-vmss-linux -n vmss-web01 --new-capacity 5
```

Now when you make curl requests, you'll see different responses from the old instances and the new instances. The new instances show the updated HTML content.

## Lab Challenge

Your VM Scale Set is now in an inconsistent state. All the VMs show they're on the latest model and they're all healthy, making them valid targets for the load balancer. But they're running different versions of the application.

Your challenge is to force the old VMs to be recreated from the current model. You can do this through the Azure Portal or using the CLI. The key is finding the right command to reimage or recreate the instances rather than just updating them.

Take a few minutes to explore the available VMSS commands and the Portal options to solve this challenge.

## Cleanup

When you're finished with the lab, don't forget to clean up your resources:

```bash
az group delete -y -n labs-vmss-linux
```

This will remove all the resources we created during this lab.
