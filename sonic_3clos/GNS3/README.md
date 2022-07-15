# GNS3 Environment

## Authors

**Gilberto Rampini**

## Topology

1. The topology remains the interface, however, the mapping is a bit different when using GNS3:
   1. Interface 1 -> Interface 2 ( GNS3 )
   2. Interface 2 -> Interface 3 ( GNS3 )
   3. Make sure you connect the devices accordingly!
2. CentOS Cloud Guest - https://gns3.com/marketplace/appliances/centos-cloud-guest
3. GNS3 allows you to upload .iso, please see the iso directory to automatically configure your hosts VMs
1. C1-V10-H1 and C1-V10-H4 have 3 interfaces
      1. eth0 - no use
      2. eth1 - dc1/2-leaf-1
      3. eth2 - dc1/2-leaf-2
   2. All other VMs have 2 interfaces
      1. eth0 - no use
      2. eth1 - connected to the leaf - See topology

## Basic Devices configuration - Console Mode

This document provides basic info about GNS3 Environment

```
## default user/password
admin/YourPaSsWoRd

-------------------------------------------------------------------
sudo config ztp disable -y 
## Change admin password – Password needs to be: admin
sudo passwd admin

sonic-cli
configure terminal

hostname dc1-sonic-spine-1

interface Management 0
ip address 192.168.122.215/24
no shutdown
end
write memory
exit
exit
-------------------------------------------

sudo config ztp disable -y 
## Change admin password – Password needs to be: admin
sudo passwd admin


sonic-cli
configure terminal

hostname dc1-sonic-spine-2

interface Management 0
ip address 192.168.122.216/24
no shutdown
end
write memory
exit
exit
-------------------------------------------

sudo config ztp disable -y 
## Change admin password – Password needs to be: admin
sudo passwd admin

sonic-cli
configure terminal

hostname dc1-sonic-leaf-1

interface Management 0
ip address 192.168.122.217/24
no shutdown
end
write memory
exit
exit
-------------------------------------------

sudo config ztp disable -y 
## Change admin password – Password needs to be: admin
sudo passwd admin


sonic-cli
configure terminal

hostname dc1-sonic-leaf-2

interface Management 0
ip address 192.168.122.218/24
no shutdown
end
write memory
exit
exit
-------------------------------------------

sudo config ztp disable -y 
## Change admin password – Password needs to be: admin
sudo passwd admin


sonic-cli
configure terminal

hostname dc1-sonic-leaf-3

interface Management 0
ip address 192.168.122.219/24
no shutdown
end
write memory
exit
exit

-------------------------------------------

sudo config ztp disable -y 
## Change admin password – Password needs to be: admin
sudo passwd admin


sonic-cli
configure terminal

hostname dc1-sonic-border-leaf-1

interface Management 0
ip address 192.168.122.220/24
no shutdown
end
write memory
exit
exit
```

## API - Apstra API Configuration Script

You can still use Apstra API scripts to configure the entire topology.

In your GNS3 Shell:

```
gns3vm# apt -y install software-properties-common

gns3vm# add-apt-repository --yes ppa:deadsnakes/ppa

gns3vm# add-apt-repository --yes --update ppa:ansible/ansible

gns3vm# apt -y update

gns3vm# apt -y install ansible git

gns3vm# git clone https://github.com/gilbertorgit/ent_sonic_apstra.git
```

Change the playbook
```
gns3vm# vi ent_sonic_apstra/base-pkg-kvm/playbook.yml

## remove all the roles but python

--------------

---
  - name: Install Pyhon
    hosts: localhost
    roles:
      - python
---------------

## save and run the playbook

gns3vm# ansible-playbook ent_sonic_apstra/base-pkg-kvm/playbook.yml

```

Create Python venv and run the script
```

gns3vm# cd ent_sonic_apstra/

root@gns3vm:~/ent_sonic_apstra# python3.10 -m venv my-env

root@gns3vm:~/ent_sonic_apstra# source my-env/bin/activate

root@gns3vm:~/ent_sonic_apstra# pip install -r requirements.txt

root@gns3vm:~# cd /home/lab/ent_sonic_apstra/sonic_3clos/

root@gns3vm:~/home/lab/ent_sonic_apstra/sonic_3clos# source my-env/bin/activate 

(my-env) root@gns3vm:~/home/lab/ent_sonic_apstra/sonic_3clos#  cd sonic_3clos/api_config/

(my-env) root@gns3vm:~/ent_sonic_apstra/sonic_3clos/api_config# python create_config_apstra_api.py
 
```