# GNS3 Environment

## Authors

**Gilberto Rampini**

## Topology

The topology remains the interface, however, the mapping is a bit different when using GNS3:
- Interface 1 -> Interface 2 ( GNS3 )
- Interface 2 -> Interface 3 ( GNS3 )

Make sure you connect the devices accordingly!

**c1_v10_h1 - Needs to have 3 Interfaces**
- eth0 - No use
- eth1 - leaf
- eth2 - leaf 
**All other c1[2] VMs need to have 2 Interfaces**
- eth0 - No use
- eth1 - to leaf

## Image Info

**CentOS Cloud Guest**
https://gns3.com/marketplace/appliances
The .iso here can be attached to the specific image. 

**To install Apstra**
- go to edit -> Preferences -> Qemu VMs -> New
- RAM: 32768
- Console: Telnet
- Upload Apstra Image
- go to the new image created -> edit
- change vCPUs to 8
- then -> OK -> Apply -> OK
