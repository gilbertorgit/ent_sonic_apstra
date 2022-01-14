# Virtual Sonic Enterprise 3.3.0 - Powered by Dell and Apstra 4.0.2

## Authors

**Gilberto Rampini**

### Eve Configuration

This document is not intended to be used as a support for installing EVE-NG, as implies that the user has this prerequisite.
Once you have installed your server you can load the lab template “_Exports_eve-ng_export-ZZZZ (Github)”. You will also have to download your own Apstra, Virtual Enterprise Sonic, and additional images. 

**Additional Considerations:**

- When configuring Enterprise Sonic with non-interface-naming ( Apstra Use Case ):
  - Ethernet0 = MGMT 
  - Ethernet1 = No USE (dummy interface)
  - Ethernet2 to EthernetX = Usable
- Customer VMs – Linux Centos7
  - Configure virtualNic to e1000
- Although Apstra is configuring an External Router Connection, there is no external router in this topology, in order to have the full connectivity, you will need to set up your own External Route and configure it accordingly.

For more information about EVE-NG images:
https://www.eve-ng.net/index.php/documentation/howtos/

Below is how I have configured the images directories and templates

Apstra Template with KVM enabled

```
root@eve-ng:~# cat /opt/unetlab/html/includes/custom_templates.yml
---
custom_templates:
  - name: generic
    listname: generic template
  - name: Apstra
    listname: Apstra
  - name: Enterprise-Sonic
    listname: Enterprise-Sonic
...

root@eve-ng:~# cat /opt/unetlab/html/templates/intel/Apstra.yml 
---
type: qemu
description: Apstra
name: Apstra
cpulimit: 8
icon: Server.png
cpu: 8
ram: 16384
ethernet: 1
console: telnet
shutdown: 1
qemu_arch: x86_64
qemu_version: 4.1.0
qemu_nic: virtio-net-pci
qemu_options: -enable-kvm -cpu host
eth_format: eth{0}
...
```

```
root@eve-ng:~# cat /opt/unetlab/html/templates/intel/enterprise-sonic.yml
---
type: qemu
name: Enterprise-Sonic
description: Enterprise Sonic Switch
cpulimit: 2
icon: Switch L32.png
cpu: 2
ram: 4096
ethernet: 16
eth_name:
- MGMT
- Dummy
eth_format: Ethernet{1}
console: telnet
shutdown: 1
qemu_arch: x86_64
qemu_version: 3.1.0
qemu_nic: e1000
qemu_options: -machine type=pc,accel=kvm -vga std -usbdevice tablet -boot order=cd

```

Directories Images
```
root@eve-ng:~# mkdir /opt/unetlab/addons/qemu/enterprise-sonic-3-3-0/
root@eve-ng:~# mkdir /opt/unetlab/addons/qemu/Apstra-4-0-0

mv /root/Enterprise_SONiC_OS_3.3.0.img /opt/unetlab/addons/qemu/enterprise-sonic-3-3-0/hda.qcow2
mv /root/aos_server_4.0.0-314.qcow2 /opt/unetlab/addons/qemu/Apstra-4-0-0/hda.qcow2


root@eve-ng:~# ls -l /opt/unetlab/addons/qemu/enterprise-sonic-3-3-0/hda.qcow2
-rw-r--r-- 1 root root 2473066496 Dec 15 10:46 /opt/unetlab/addons/qemu/enterprise-sonic-3-3-0/hda.qcow2
root@eve-ng:~# ls -l /opt/unetlab/addons/qemu/Apstra-4-0-0/hda.qcow2
-rw-r--r-- 1 root root 1996657664 Dec 15 10:46 /opt/unetlab/addons/qemu/Apstra-4-0-0/hda.qcow2

```


### Basic Sonic Configuration

You will need to connect to every single Enterprise Sonic and configuring the steps below, for management interface, respect the IPs below:
The IP in your case can change, in my case, my MGMT IP is 192.168.0.0/24. If possible, change the subnets accordingly based on your lab, but maintain the host IP, so it will be easier to follow the procedure. 


```
User: admin
Password: YourPaSsWoRd

## disable ZTP - it takes some minutes
sudo config ztp disable

•	Active ZTP session will be stopped and disabled, continue? [y/N]: y
## Change admin password – Password needs to be admin
sudo passwd admin

## exit and re-enter to test the new password

## Go to sonic cli
sonic-cli

## Configuring hostname
configure terminal 

hostname <hostname>

## Configuring MGMT IP

interface Management 0
ip address <IP Address>
no shutdown

## Saving and exit
end 
write memory 
exit
exit

```

*** Please check your connectivity!

### Configuring Apstra – EVE-NG Only

For further information, please check the link below to configure your Apstra Server:
https://portal.apstra.com/docs/configure_aos.html
- Initial user/password
  - admin/admin
- Web password
  - admin/admin

You can follow the previous Apstra Installation. Make sure to configure the right IP address based on your subnet. 
The IP in your case can change, in my case, my MGMT IP is 192.168.0.0/24. If possible, change the subnets accordingly based on your lab, but maintain the host IP, so it will be easier to follow the procedure. 

**Apstra Server -> 192.168.0.180**


### Configuring Apstra – EVE-NG Only

For more information about Linux EVE-NG images and configuration:
https://www.eve-ng.net/index.php/documentation/howtos/
You will need to configure the Customers VMs based on the table below:

* c1_v10_h1 – Make sure the interface virtualization is e1000 ( Enterprise Sonic only supports e1000 )

* Make sure you have the routes configured accordingly, example below (c1_v10_h1 – 192.168.10.0/24 subnet):
```
[root@c1_v10_h1 ~]# cat /etc/sysconfig/network-scripts/route-bond0
ADDRESS0=192.168.20.0
GATEWAY0=192.168.10.1
NETMASK0=255.255.255.0
```

Centos7 bonding example

```
[root@c1_v10_h1 ~]# modprobe bonding

[root@c1_v10_h1 ~]# lsmod | grep bonding
bonding               152979  0

[root@c1_v10_h1 ~]# modinfo bonding
filename:       /lib/modules/3.10.0-1127.el7.x86_64/kernel/drivers/net/bonding/bonding.ko.xz
author:         Thomas Davis, tadavis@lbl.gov and many others
description:    Ethernet Channel Bonding Driver, v3.7.1
version:        3.7.1
license:        GPL
alias:          rtnl-link-bond
retpoline:      Y
rhelversion:    7.8
srcversion:     02BB340820F6F1A042A3033
depends:
intree:         Y
vermagic:       3.10.0-1127.el7.x86_64 SMP mod_unload modversions


[root@c1_v10_h1 ~]# cat /etc/sysconfig/network-scripts/ifcfg-eth1
BOOTPROTO=none
DEVICE=eth1
MASTER=bond0
ONBOOT=yes
SLAVE=yes
TYPE=Ethernet
USERCTL=no
[root@c1_v10_h1 ~]# cat /etc/sysconfig/network-scripts/ifcfg-eth2
BOOTPROTO=none
DEVICE=eth2
MASTER=bond0
ONBOOT=yes
SLAVE=yes
TYPE=Ethernet
USERCTL=no
[root@c1_v10_h1 ~]# cat /etc/sysconfig/network-scripts/ifcfg-bond0
BONDING_MASTER=yes
BONDING_OPTS=mode=802.3ad
BONDING_SLAVE0=eth1
BONDING_SLAVE1=eth2
BOOTPROTO=none
DEVICE=bond0
IPADDR=192.168.10.11
NETMASK=255.255.255.0
ONBOOT=yes
TYPE=Bond
USERCTL=no
```

* After configuring, please reboot the VMs to make sure the configurations have been succeeded.

### Configuring Apstra – EVE-NG Only

For KVM topology please visit the link below for further instructions and to download the scripts to build the topology and configure Apstra using APIs.
Considering you are using EVE-NG, you can still use the API script to configure your entire topology with no manual configuration. If it’s your case, please follow the steps below:

Download the github repository: https://github.com/gilbertorgit/sonic-3-stage-clos-api.git

You will need to changes some IPs based on your MGMT subnet, or based on the IPs you have allocated to your lab. In my case, I’m using 192.168.0.0, the default subnet configured is 192.168.122.0. 
Below are the files you will need to change the IPs:
- create_config_apstra_api.py
- blueprint_staged.py
- urls_base_apstra.py

To run the script, install the required modules and run the create_config_apstra_api.py. The script has been tested using python 3.7

```
root@lab:# cd api_config/
root@lab:# python3.7 create_config_apstra_api.py
```