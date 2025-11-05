# Building Custom VM Images - Exercise Walkthrough Script

## Exercise 1: Create a Base VM

Let's start by creating the foundation for our custom image - a base VM with our application deployed.

First, we'll create a Resource Group. Resource Groups are logical containers that help you organize and manage related Azure resources.

```
az group create -n labs-vm-image --tags courselabs=azure --location eastus
```

We're naming our Resource Group "labs-vm-image" and placing it in the East US region. You can choose your preferred region.

Next, we need to find the right Windows Server image. Let's query the available SKUs:

```
az vm image list-skus -l eastus -p MicrosoftWindowsServer -f WindowsServer -o table
```

This shows us all the available Windows Server versions. We'll use Windows Server 2022 Datacenter for this lab.

Now, let's create the VM:

```
az vm create -l eastus -g labs-vm-image -n app01-base --image MicrosoftWindowsServer:WindowsServer:2022-datacenter-core-g2:latest --size Standard_D2s_v5 --admin-username azureuser --public-ip-address-dns-name my-unique-dns-name --admin-password MySecurePassword123!
```

Notice we're specifying:
- The location and resource group
- A VM name of "app01-base"
- The Windows Server 2022 image
- A VM size of Standard D2s v5
- Admin credentials
- A unique DNS name for easy access

This will take a few minutes to complete. Once it's ready, we'll connect via Remote Desktop.

## Exercise 2: Deploy the Application

Now we're connected to the VM. We'll install IIS Web Server and deploy our application.

In the PowerShell terminal on the VM, run:

```
Install-WindowsFeature Web-Server,NET-Framework-45-ASPNET,Web-Asp-Net45
```

This installs IIS along with ASP.NET support. Watch as the features are installed - this would normally happen every time you create a new VM, but soon we'll bake this into our image.

Next, we'll remove the default web page and deploy our application:

```
rm -fo C:\inetpub\wwwroot\iisstart.htm

curl -o C:/inetpub/wwwroot/default.aspx https://raw.githubusercontent.com/courselabs/azure/main/labs/vm-image/app/default.aspx
```

Let's test the application locally:

```
curl.exe localhost
```

You should see HTML output that includes the name of the VM. Perfect - our application is running.

## Exercise 3: Prepare the VM for Imaging

Before we can create an image, we need to generalize the VM. This removes machine-specific information so the image can be used to create new VMs with their own identities.

For Windows VMs, we use the Sysprep tool. Run this command:

```
C:\windows\system32\sysprep\sysprep.exe
```

In the Sysprep window, select:
- "Enter System Out-of-Box Experience (OOBE)"
- Check the "Generalize" option
- Choose "Shutdown" from the dropdown

Click OK. The VM will generalize itself and shut down. You'll lose your Remote Desktop connection - this is expected.

Now, back in your local terminal, we need to deallocate the VM:

```
az vm deallocate -g labs-vm-image -n app01-base
```

This ensures Azure knows the VM is shut down. Next, mark it as generalized:

```
az vm generalize -g labs-vm-image -n app01-base
```

Let's verify the VM is ready:

```
az vm show --show-details -g labs-vm-image -n app01-base
```

Look for the power state - it should show "VM deallocated" and there should be no public IP address.

## Exercise 4: Create the Image

Now comes the easy part - creating the image. Because we used a generation 2 SKU, we need to specify that:

```
az image create -g labs-vm-image -n app01-image --source app01-base --hyper-v-generation V2
```

This creates an image reference to the OS disk. It's quick - just a few seconds.

Verify the image was created:

```
az image list -o table
```

You should see your "app01-image" listed.

## Exercise 5: Copy the Image to Another Resource Group

In practice, you'll want to keep your images separate from your application resources. They have different lifecycles - you might delete and recreate application resources frequently, but you want to keep your images.

Create a new Resource Group:

```
az group create -n labs-vmss-win --location eastus
```

Now copy the image:

```
az image copy --source-type image --source-resource-group labs-vm-image --source-object-name app01-image --target-location eastus --target-resource-group labs-vmss-win
```

This creates a snapshot and copies it. It starts slowly but speeds up quickly.

## Exercise 6: Deploy VMs from the Image

Now let's see the real benefit - deploying multiple VMs instantly with our application pre-installed:

```
az vm create -g labs-vm-image -n app-vm --image app01-image --size Standard_D2s_v5 --admin-username azureuser --count 3 -l eastus --admin-password MySecurePassword123!
```

This creates three VMs in one command, all from our custom image. Notice how much faster this is than deploying and configuring each VM individually.

## Exercise 7: Configure Network Access

The VMs are created, but we can't access the web application yet. We need to add a Network Security Group rule to allow HTTP traffic:

Open the Azure Portal, navigate to the Network Security Group for your VMs, and add an inbound rule:
- Source: Any
- Source port ranges: *
- Destination: Any
- Service: HTTP
- Action: Allow
- Priority: 1000
- Name: AllowHTTP

Now browse to the public IP address of any of your VMs. You'll see the application running, displaying the unique VM name.

## Conclusion

You've successfully created a custom VM image and deployed multiple VMs from it. This technique dramatically reduces deployment time and ensures consistency across your VM fleet.

In a production environment, you might create images with:
- Pre-installed development tools
- Configured monitoring agents
- Security baselines
- Line-of-business applications

The process is the same - configure once, image, deploy many times.
