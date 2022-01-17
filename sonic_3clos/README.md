# Using Virtual Sonic Enterprise Powered by Dell and Apstra to build a DC - (KVM environment)

## Authors

**Gilberto Rampini**

## Topology

![Topology](https://github.com/gilbertorgit/ent_sonic_apstra/blob/main/sonic_3clos/topology_prints/Topology.png)

![MGMT IP](https://github.com/gilbertorgit/ent_sonic_apstra/blob/main/sonic_3clos/topology_prints/MGMT-IP.png)

## Getting Started

This document provides some basic configuration examples for lab purposes only in order to help you get started with Virtual Sonic Enterprise Powered by Dell and Apstra Intent Based-Networking. 

* **This lab guide does not intend to cover any best practice and/or production configuration. All the configuration provided in this guide, are just "simple examples"**

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

This project will make available:

1. Python script to create, start, stop and delete the entire topology
2. All the necessary steps to create a full lab using Virtual Sonic Enterprise Powered by Dell and Apstra
3. Python script to create all Apstra configuration is provided in the folder "api_config"
4. Alternatively, there is a PDF document providing all steps to configure your entire topology
   1. If you are a Partner, contact your account manager to have access
   2. If you are an end customer, contact your partner to have access
5. MPLS Core configuration
6. Lab Topology

Following this guide, you will be able to build

1. DC1 - 3-Stage Clos network using Virtual Enterprise Sonic and Apstra

Important Information
- The python script available in this guide will create and delete all resources as well as start and stop the entire topology.
- It's very important to keep the names and file paths as shown here otherwise, you're likely to face issues
- It's very important to keep the versions of the images, otherwise you are likely to face issues.   
- Default user and password: -> (You can change it by editing the python script)
  - root/lab123 
  - lab/lab123 
- Lab Network IP and Interface information:
  - 192.168.122.0/24 -> default KVM bridge network (You can change it by editing the python script)
  - virbr0 - default KVM bridge interface
- When creating the topology from scratch, you will need to configure your AOS Server. Please see "Apstra_Installation" Folder
  - https://portal.apstra.com/docs/configure_aos.html
    
## Prerequisites configs

This test lab has been built and tested using:

```
1. Ubuntu 18.04.5 LTS
2. Server with:
  2.1. 128GB RAM
  2.2. I9 with 14 Cores
  2.3. 500GB - SSD
3. Virtual Sonic Enterprise 3.3.0 - Powered by Dell
4. Apstra 4.0.2
5. CentOS-7-x86_64-GenericCloud.qcow2
```

***Although we are downloading and copying packages and configurations within the /home/lab user directory, it's worth mentioning that I'm using root user access for every single step described here.***

## Pre-deployment Server Configs and Basic Packages

**Packages Installation and configuration**

```
lab@lab:~$ sudo su -

root@lab:~$ cd /home/lab

root@lab:/home/lab# apt -y install software-properties-common

root@lab:/home/lab# add-apt-repository --yes ppa:deadsnakes/ppa

root@lab:/home/lab# add-apt-repository --yes --update ppa:ansible/ansible

root@lab:/home/lab# apt -y update

root@lab:/home/lab# apt -y install ansible git

root@lab:/home/lab# git clone https://github.com/gilbertorgit/ent_sonic_apstra.git

root@lab:/home/lab# ansible-playbook ent_sonic_apstra/base-pkg-kvm/playbook.yml
```

**Change default virbr0 dhcp range from .254 to .100**
```
root@lab:/home/lab# virsh net-edit default

from:
<range start='192.168.122.2' end='192.168.122.254'/>
to
<range start='192.168.122.2' end='192.168.122.100'/>
```

**Reboot your server to confirm all changes are working**

```
root@lab:/home/lab# shutdown -r now

root@lab:/home/lab# sudo su -

root@lab:~$ cd /home/lab

```

## Preparing the environment

### Download the images and copy to ent_sonic_apstra/sonic_3clos/images

* aos_server_4.0.0-314.qcow2 - https://support.juniper.net/support/downloads/?p=apstra-fabric-conductor

* CentOS-7-x86_64-GenericCloud.qcow2 - https://cloud.centos.org/centos/7/images/

* Enterprise_SONiC_OS_3.3.0.img - 

```
root@lab:/home/lab# cp aos_server_4.0.2-142.qcow2 Enterprise_SONiC_OS_3.3.0.img CentOS-7-x86_64-GenericCloud.qcow2 /home/lab/ent_sonic_apstra/sonic_3clos/images/

```

***Make sure you download the right version as described in this guide. 
You will have a directory like that one:***

```
root@lab:/home/lab/# ls -l /home/lab/ent_sonic_apstra/sonic_3clos/images/

-rwx------ 1 root root 1972913664 Jan 14 08:55 aos_server_4.0.2-142.qcow2
-rw-r--r-- 1 root root  858783744 Jan 14 08:55 CentOS-7-x86_64-GenericCloud.qcow2
-rw-r--r-- 1 root root 2473066496 Jan 14 08:55 Enterprise_SONiC_OS_3.3.0.img
-rwx------ 1 root root         53 Dec 13 15:38 README.md

```

## Python Script

### Create Infrastructure

1. - Start Topology - It will start the entire topology (you have to create it first - Option 4)
2. - Stop Topology - It will stop the entire topology
3. - Clean Memory Only - It will clean your server memory
4. - Create Topology - It will create the entire topology from scratch
5. - Delete Topology - It will delete and remove the entire topology and images

```
root@lab:~# cd /home/lab/ent_sonic_apstra/sonic_3clos/

root@lab:/home/lab/ent_sonic_apstra/sonic_3clos/# python3.7 start_stop.py 

1 - Start Topology

2 - Stop Topology

3 - Clean Memory Only

4 - Create topology

5 - Delete topology

Select one Option: 
```


## Apstra Server initial configuration

***After creating the topology from scratch you will need to configure your Apstra server. A

Access Apstra server using the console and check the instructions in the folder Apstra_Installation

* Apstra Server IP: 192.168.122.180 

* Default user and password: admin/admin
```
root@lab:~# virsh console apstra_server
```

* If you want to know more, please check the link below for further information:
  * https://portal.apstra.com/docs/configure_aos.html

***Configure ssh tunnel to access the Apstra UI*** 

* configure your ssh configuration to allow root, TCP and X11 Forwarding
```
root@lab:~# vi /etc/ssh/sshd_config

PermitRootLogin yes
AllowTcpForwarding yes
X11Forwarding yes
```

***SSH Tunnel Example using linux terminal***

```
ssh -L 8101:192.168.122.180:443 root@<YOUR_SERVER_IP> example:
ssh -L 8101:192.168.122.180:443 root@192.168.0.1
```

***SSH Tunnel Example using SecureCRT***

Create a connection to your server and go to "Properties" and configure the relevant parameters, example below:

![SecureCRT](https://github.com/gilbertorgit/ent_sonic_apstra/blob/main/sonic_3clos/topology_prints/SecureCRT-1.png)

![SecureCRT](https://github.com/gilbertorgit/ent_sonic_apstra/blob/main/sonic_3clos/topology_prints/SecureCRT-2.png)

## Apstra API Configuration Script

Before run the API Script, it's always good to check the management connectivity:

```
ping 192.168.122.215
ping 192.168.122.216
ping 192.168.122.217
ping 192.168.122.218
ping 192.168.122.219
ping 192.168.122.220
```

In case you face any issues, you can configure it manually:
```
root@lab:# virsh list
 Id    Name                           State
----------------------------------------------------
 13    apstra_server                  running
 14    dc1-sonic-leaf-1               running
 15    dc1-sonic-leaf-2               running
 16    dc1-sonic-leaf-3               running
 17    dc1-sonic-spine-1              running
 18    dc1-sonic-spine-2              running
 19    dc1-border-sonic-leaf-1        running
 20    c1_v10_h1                      running
 21    c1_v10_h2                      running
 22    c1_v20_h3                      running
 23    c2_v100_h1                     running
 24    c2_v200_h2                     running

* admin/admin (or YourPaSsWoRd -> Default Sonic Password)
root@lab:# virsh console dc1-sonic-leaf-1

* Disable ZTP
# sudo config ztp disable

* configures admin as password
# sudo passwd admin
Enter new: admin
Enter new: admin

# sonic-cli
# configure terminal

* Based on topology names
# hostname <hostname> 

# interface Management 0
# ip address 192.168.122.217/24
# no shutdown
# exit
# exit
# write memory
# exit
# exit
```

* The script below will configure the entire topology using APIs
```
root@lab:# cd /home/lab/ent_sonic_apstra/sonic_3clos/api_config/

root@lab:/home/lab/ent_sonic_apstra/sonic_3clos/api_config# python3.7 create_config_apstra_api.py
```

**You can check some scripts output in the folder "Output_Script_Example**

## Customer VMs Access

* Default user and password: lab/lab123

```
root@lab:# virsh console <VM_NAME>

root@lab:# virsh console c1_v10_h1
```

***In case your bond0 (vm_v10_h1) is not working properly, you will need to update the interface configuration***
```
root@lab:~# virsh console c1_v10_h1

--> login using root credentials: root/lab123

[root@c1_v10_h1 ~]#vi /etc/sysconfig/network-scripts/ifcfg-bond0

Add the line below to the end of the file: 

BONDING_OPTS="mode=4 miimon=100 lacp_rate=1"

[root@c1_v10_h1 ~]# shutdown -r now
```

