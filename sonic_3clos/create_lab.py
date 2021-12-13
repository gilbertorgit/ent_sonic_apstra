"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""
import subprocess
import time
import console_config
from time import sleep
from threading import Thread
import re
import os

source_sonic_image = 'images/Enterprise_SONiC_OS_3.3.0.img'

ent_sonic_image = '/var/lib/libvirt/images/Enterprise_SONiC_OS_3.3.0.img'

generic_centos = '/var/lib/libvirt/images/CentOS-7-x86_64-GenericCloud.qcow2'
image_path = '/var/lib/libvirt/images/'
apstra_image = 'aos_server_4.0.0-314.qcow2'

aos_vm = {'apstra_server': {'hostname': 'apstra_server', 'eth0': 'virbr0', 'eth1': 'none'},}


def create_vrdc_dic():
    fhandle = open('vrdc_info.csv')
    hosts=dict()
    for line in fhandle:
        words = line.split(',')
        hosts.update({words[0]: dict()})
        n = len(words)
        for i in range(1, n-1, 2):
            if words[0] in hosts.keys():
                hosts[words[0]].update({words[i]:words[i+1]})
                
    return(hosts)


def create_vm_dic():

    fhandle = open('vm_info.csv')
    hosts=dict()
    for line in fhandle:
        words = line.split(',')
        hosts.update({words[0]: dict()})
        n = len(words)
        for i in range(1, n-1, 2):
            if words[0] in hosts.keys():
                hosts[words[0]].update({words[i]:words[i+1]})

    return(hosts)


def create_lab_vrdc():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Creating vrdc DC1 Topology")

    print("--------------------------------------------------------- Creating vrdc DC1 Images")

    copy_vrdc_img = f'cp {source_sonic_image} {ent_sonic_image}'

    subprocess.call(copy_vrdc_img, shell=True)

    vrdc_hosts = create_vrdc_dic()

    for i in vrdc_hosts.keys():

        hostname = vrdc_hosts[i].get('hostname')
        mgmt_int = vrdc_hosts[i].get('mgmt_int')
        mgmt_ip = vrdc_hosts[i].get('mgmt_ip')
        dummy_int = vrdc_hosts[i].get('dummy_int')
        xe_1 = vrdc_hosts[i].get('xe_1')
        xe_2 = vrdc_hosts[i].get('xe_2')
        xe_3 = vrdc_hosts[i].get('xe_3')
        xe_4 = vrdc_hosts[i].get('xe_4')
        xe_5 = vrdc_hosts[i].get('xe_5')
        xe_6 = vrdc_hosts[i].get('xe_6')
        xe_7 = vrdc_hosts[i].get('xe_7')
        xe_8 = vrdc_hosts[i].get('xe_8')
        xe_9 = vrdc_hosts[i].get('xe_9')
        xe_10 = vrdc_hosts[i].get('xe_10')
        xe_11 = vrdc_hosts[i].get('xe_11')
        xe_12 = vrdc_hosts[i].get('xe_12')

        print(f'--------------------------------------------------------- Creating vrdc {i}')

        vrdc_vm = f'cp {ent_sonic_image} {image_path}{hostname}.img'
        subprocess.call(vrdc_vm, shell=True)

        install_vrdc = f'virt-install --name {hostname} \
        --memory 4096 \
        --vcpus=2 \
        --import \
        --os-variant generic \
        --nographics \
        --noautoconsole \
        --disk path={image_path}{hostname}.img,size=18,device=disk,bus=ide,format=qcow2 \
        --accelerate \
        --network bridge={mgmt_int},model=e1000 \
        --network bridge={dummy_int},model=e1000 \
        --network bridge={xe_1},model=e1000 \
        --network bridge={xe_2},model=e1000 \
        --network bridge={xe_3},model=e1000 \
        --network bridge={xe_4},model=e1000 \
        --network bridge={xe_5},model=e1000 \
        --network bridge={xe_6},model=e1000 \
        --network bridge={xe_7},model=e1000 \
        --network bridge={xe_8},model=e1000 \
        --network bridge={xe_9},model=e1000 \
        --network bridge={xe_10},model=e1000 \
        --network bridge={xe_11},model=e1000 \
        --network bridge={xe_12},model=e1000'

        subprocess.call(install_vrdc, bufsize=2000, shell=True)


def delete_lab_vrdc():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Deleting vrdc Topology")

    delete_vrdc_image = f'rm -f {ent_sonic_image}'

    subprocess.call(delete_vrdc_image, shell=True)

    get_vrdc_name = subprocess.Popen("virsh list --all | egrep 'dc[1-2]-' | awk '{print $2}'", shell=True,
                                     stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    li_vrdc = list(get_vrdc_name.split("\n"))
    result = [x for x in li_vrdc if x]

    for image in result:

        print(f"--------------------------------------------------------- Deleting {image}")

        destroy_image = f'virsh destroy {image}'
        undefine_image = f'virsh undefine {image}'
        subprocess.call(destroy_image, shell=True)
        subprocess.call(undefine_image, shell=True)

    vrdc_hosts = create_vrdc_dic()

    for i in vrdc_hosts.keys():
        delete_image = f"rm -f {image_path}{vrdc_hosts[i].get('hostname')}.img"
        subprocess.call(delete_image, shell=True)


def create_lab_vms():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Creating Hosts VMs ")

    copy_cloud_image = f'cp images/CentOS-7-x86_64-GenericCloud.qcow2 {image_path}'
    subprocess.call(copy_cloud_image, shell=True)

    customer_vm = create_vm_dic()

    for i in customer_vm.keys():

        hostname = customer_vm[i].get('hostname')
        bond = customer_vm[i].get('bond')
        eth0 = customer_vm[i].get('eth0')
        eth1 = customer_vm[i].get('eth1')
        eth2 = customer_vm[i].get('eth2')

        print(f'--------------------------------------------------------- Creating VM {i}')

        create_img = f'qemu-img create -f qcow2 -o preallocation=metadata {image_path}{hostname}.qcow2 15G'
        exapand_img = f'virt-resize --expand /dev/sda1 {generic_centos} {image_path}{hostname}.qcow2'
        add_metadata = f'genisoimage -output {image_path}{hostname}-config.iso -volid cidata ' \
                       f'-joliet -r vm_config/{hostname}/user-data ' \
                       f'vm_config/{hostname}/meta-data vm_config/{hostname}/network-config'

        subprocess.call(create_img, shell=True)
        subprocess.call(exapand_img, shell=True)
        subprocess.call(add_metadata, shell=True)

        if bond == "True":
            install_c_vm = f'virt-install --import --name {hostname} \
            --ram 1024 --vcpus 1 \
            --disk {image_path}{hostname}.qcow2,format=qcow2,bus=virtio \
            --disk {image_path}{hostname}-config.iso,device=cdrom \
            --network bridge={eth0},model=e1000 \
            --network bridge={eth1},model=e1000 \
            --network bridge={eth2},model=e1000 \
            --os-type=linux --os-variant=rhel7 \
            --noautoconsole \
            --accelerate'
            subprocess.call(install_c_vm, shell=True)
        else:
            install_c_vm = f'virt-install --import --name {hostname} \
            --ram 1024 --vcpus 1 \
            --disk {image_path}{hostname}.qcow2,format=qcow2,bus=virtio \
            --disk {image_path}{hostname}-config.iso,device=cdrom \
            --network bridge={eth0},model=e1000 \
            --network bridge={eth1},model=e1000 \
            --os-type=linux --os-variant=rhel7 \
            --noautoconsole \
            --accelerate'
            subprocess.call(install_c_vm, shell=True)


def delete_lab_vms():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Deleting Host VMs")

    delete_cloud_image = f'rm -f /var/lib/libvirt/images/CentOS-7-x86_64-GenericCloud.qcow2'
    subprocess.call(delete_cloud_image, shell=True)

    get_c_vm_name = subprocess.Popen("virsh list --all | egrep 'c[1-2]_v' | awk '{print $2}'", shell=True,
                                     stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    li_vm = list(get_c_vm_name.split("\n"))
    result = [x for x in li_vm if x]

    for image in result:

        print(f"--------------------------------------------------------- Deleting {image}")

        destroy_image = f'virsh destroy {image}'
        undefine_image = f'virsh undefine {image}'
        subprocess.call(destroy_image, shell=True)
        subprocess.call(undefine_image, shell=True)

    customer_vm = create_vm_dic()

    for i in customer_vm.keys():
        delete_image = f"rm -f {image_path}{customer_vm[i].get('hostname')}.qcow2"
        delete_iso = f"rm -f {image_path}{customer_vm[i].get('hostname')}-config.iso"
        subprocess.call(delete_image, shell=True)
        subprocess.call(delete_iso, shell=True)


def create_lab_aos():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Creating AOS Server ")

    aos_vm.get('key1', {}).get('key2')

    hostname = aos_vm['apstra_server'].get('hostname')
    eth0 = aos_vm['apstra_server'].get('eth0')
    eth1 = aos_vm['apstra_server'].get('eth1')

    copy_aos_image = f'cp images/{apstra_image} {image_path}{hostname}.qcow2'
    subprocess.call(copy_aos_image, shell=True)

    install_aos = f'virt-install --name={hostname} \
    --vcpu=8 \
    --ram=32768 \
    --import \
    --disk={image_path}{hostname}.qcow2 \
    --os-type=linux --os-variant ubuntu16.04 \
    --network bridge={eth0},model=virtio \
    --noautoconsole'

    subprocess.call(install_aos, shell=True)


def delete_lab_aos():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Deleting AOS Server")

    get_c_vm_name = subprocess.Popen("virsh list --all | egrep 'apstra_server' | awk '{print $2}'", shell=True,
                                     stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    li_vm = list(get_c_vm_name.split("\n"))
    result = [x for x in li_vm if x]

    for image in result:

        print(f"--------------------------------------------------------- Deleting {image}")

        destroy_image = f'virsh destroy {image}'
        undefine_image = f'virsh undefine {image}'
        subprocess.call(destroy_image, shell=True)
        subprocess.call(undefine_image, shell=True)

        delete_image = f"rm -f {image_path}apstra_server.qcow2"
        subprocess.call(delete_image, shell=True)

"""
def configure_vrdc():

    print("We will wait around 2 minutes to start the initial vrdc configuration")
    start_time = time.time()
    sleep(120)
    run_time = time.time() - start_time
    print("** Time waiting: %s sec" % round(run_time, 2))
    sleep(5)
    print("########## Basic MGMT Configuration - hostname and ip")

    vrdc_hosts = create_vrdc_dic()

    for i in vrdc_hosts.keys():
        hostname = vrdc_hosts[i].get('hostname')
        mgmt_ip = vrdc_hosts[i].get('mgmt_ip')

        console_config.config_vrdc(hostname, mgmt_ip)
"""


def configure_routers(hostname, mgmt_ip):

    console_config.config_vrdc(hostname, mgmt_ip)


try:
    def configure_vrdc():

        print("We will wait around 2 minutes to start the initial vrdc configuration")
        start_time = time.time()
        sleep(120)
        run_time = time.time() - start_time
        print("** Time waiting: %s sec" % round(run_time, 2))
        sleep(5)
        print("########## Basic MGMT Configuration - hostname and ip")

        vrdc_hosts = create_vrdc_dic()

        for i in vrdc_hosts.keys():
            hostname = vrdc_hosts[i].get('hostname')
            mgmt_ip = vrdc_hosts[i].get('mgmt_ip')

            Thread.start_new_thread( configure_routers, (hostname, mgmt_ip))
except:
    print("The operation cannot be performed")
