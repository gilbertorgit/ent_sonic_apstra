"""
---------------------------------
 Author: Gilberto Rampini
 Date: 12/2021
---------------------------------
"""

import subprocess
from time import sleep
import create_lab
import routers_config
import time

"""
In case you have a kernel with bridge lacp, stp enable you need to change to 65535
"""
#bridge_echo = 65535
bridge_echo = 16384


def clean_memory():

    """
    Clean linux memory
    """
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Clean Memory")
    check_memory = 'free -g'
    free_memory = 'sync; echo 3 > /proc/sys/vm/drop_caches'
    subprocess.call(check_memory, shell=True)
    sleep(2)
    subprocess.call(free_memory, shell=True)
    subprocess.call(check_memory, shell=True)
    sleep(5)


def defining_interfaces():

    """
    define Lx virtual interfaces to connect Virtual Router DC (spine, leafs, etc)
    """
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Generate Bridges")
    interface_list = []
    for fabric_interface in range(1, 40):
        interface_temp = "L" + str(fabric_interface)
        interface_list.append(interface_temp)

    return interface_list


def defining_dummy_interfaces():

    """
    Define dummy interfaces to populate unused ports
    """
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Generate dummy interfaces")
    dummy_interface_list = []

    for vrdc_internal_interface in range(1, 20):
        interface_temp = "dummy-int-" + str(vrdc_internal_interface)
        dummy_interface_list.append(interface_temp)

    return dummy_interface_list


def getting_destroyed_vrdc():

    """
    create a list with all destroyed vrdc
    """
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Get destroyed vrdc")

    vrdc_info = subprocess.Popen("virsh list --all | egrep 'dc[1-2]-' | awk '{print $2}'", shell=True,
                                 stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    # creates list of the vrdc_info and clean the empty spaces
    li_vrdc = list(vrdc_info.split("\n"))
    result = [ x for x in li_vrdc if x ]
    return result


def getting_destroyed_servers():

    """
    create a list with all destroyed customer vm and Apstra Server
    """
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Get destroyed Servers")

    vrdc_info = subprocess.Popen("virsh list --all | egrep 'c[1-2]_v|apstra_server' | awk '{print $2}'", shell=True,
                                 stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    # creates list of the vrdc_info and clean the empty spaces
    li_vrdc = list(vrdc_info.split("\n"))
    result = [ x for x in li_vrdc if x ]
    return result


def getting_running_vrdc():

    """
    create a list with all running vrdc
    """
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Get Running vrdc")

    vrdc_info = subprocess.Popen("virsh list | egrep 'dc[1-2]-' | awk '{print $2}'", shell=True,
                                 stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    # creates list of the vrdc_info and clean the empty spaces
    li_vrdc = list(vrdc_info.split("\n"))
    result = [ x for x in li_vrdc if x ]
    return result


def getting_running_servers():

    """
    create a list with all running vQFX customer vm and Apstra Server
    """
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Get Running Servers")

    vrdc_info = subprocess.Popen("virsh list | egrep 'c[1-2]_|apstra_server' | awk '{print $2}'", shell=True,
                                 stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    # creates list of the vrdc_info and clean the empty spaces
    li_vrdc = list(vrdc_info.split("\n"))
    result = [ x for x in li_vrdc if x ]
    return result


def create_fabric_interface():

    """
    Create logical interfaces
    """
    interface_list = defining_interfaces()
    dummy_interface_list = defining_dummy_interfaces()

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Create fabric bridges")

    for br_interface in interface_list:

        cmd_brctl = f'/sbin/brctl addbr {br_interface}'
        cmd_ifconfig = f'/sbin/ifconfig {br_interface} up'
        subprocess.call(cmd_brctl, shell=True)
        subprocess.call(cmd_ifconfig, shell=True)

        lacp_ldp = f'echo {bridge_echo} > /sys/class/net/{br_interface}/bridge/group_fwd_mask'
        subprocess.call(lacp_ldp, shell=True)

        print(f'- Creating Interface {br_interface}')

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Create dummy bridges")

    for dummy in dummy_interface_list:

        cmd_brctl = f'/sbin/brctl addbr {dummy}'
        subprocess.call(cmd_brctl, shell=True)

        print(f'- Creating Interface {dummy}')


def delete_fabric_interface():

    interface_list = defining_interfaces()
    dummy_interface_list = defining_dummy_interfaces()

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Delete Bridges")

    print("--------------------------------------------------------- Delete fabric Bridges")
    for br_interface in interface_list:


        cmd_brctl = f'/sbin/brctl delbr {br_interface}'
        cmd_ifconfig = f'/sbin/ifconfig {br_interface} down'
        subprocess.call(cmd_ifconfig, shell=True)
        subprocess.call(cmd_brctl, shell=True)

        print(f'- Deleting Interface {br_interface}')

    print("--------------------------------------------------------- Delete dummy Bridges")

    for dummy in dummy_interface_list:

        cmd_brctl = f'/sbin/brctl delbr {dummy}'
        cmd_ifconfig = f'/sbin/ifconfig {dummy} down'
        subprocess.call(cmd_ifconfig, shell=True)
        subprocess.call(cmd_brctl, shell=True)

        print(f'- Deleting Interface {dummy}')


def start_servers():

    print("########################################################## Start Host VMs and Apstra Server")
    server_list = getting_destroyed_servers()

    for server in server_list:
        command = f'/usr/bin/virsh start {server}'
        print(f'- Starting {server}')
        subprocess.call(command, shell=True)
        sleep(2)


def stop_servers():

    print("########################################################## Destroy Servers")
    server_list = getting_running_servers()

    for server in server_list:
        command = f'/usr/bin/virsh destroy {server}'
        print(f'- {server}')
        subprocess.call(command, shell=True)
        sleep(1)


def start_vrdc():

    print("########################################################## Start vQFX")
    vqfx_list = getting_destroyed_vrdc()

    for vqfx in vqfx_list:
        command = f'/usr/bin/virsh start {vqfx}'
        print(f'- Starting {vqfx}')
        subprocess.call(command, shell=True)
        sleep(2)


def stop_vrdc():

    print("########################################################## Destroy vQFX")
    vqfx_list = getting_running_vrdc()

    for vqfx in vqfx_list:
        command = f'/usr/bin/virsh destroy {vqfx}'
        print(f'- {vqfx}')
        subprocess.call(command, shell=True)
        sleep(1)


def start_topology():

    print("########################################################## Start Topology")
    clean_memory()
    create_fabric_interface()
    start_vrdc()
    start_servers()


def stop_topology():

    print("########################################################## Stop Topology")
    stop_vrdc()
    stop_servers()
    delete_fabric_interface()
    clean_memory()


def create_topology():

    print("########################################################## Create Topology")
    clean_memory()
    create_fabric_interface()
    create_lab.create_lab_aos()
    sleep(5)
    create_lab.create_lab_vrdc()
    sleep(5)
    create_lab.create_lab_vms()
    sleep(5)
    routers_config.configure_vrdc()


def delete_topology():

    print("########################################################## Delete Topology")
    create_lab.delete_lab_vrdc()
    create_lab.delete_lab_vms()
    create_lab.delete_lab_aos()
    delete_fabric_interface()
    clean_memory()


if __name__ == "__main__":

    print("1 - Start Topology\n")
    print("2 - Stop Topology\n")
    print("3 - Clean Memory Only\n")
    print("4 - Create topology\n")
    print("5 - Delete topology\n")

    select_function = input("Select one Option: ") or None

    if select_function == '1':
        start_time = time.time()
        start_topology()
        run_time = time.time() - start_time
        run_time_min = run_time / 60
        print(f'Time to configure: {run_time_min}')
    elif select_function == '2':
        start_time = time.time()
        stop_topology()
        run_time = time.time() - start_time
        run_time_min = run_time / 60
        print(f'Time to configure: {run_time_min}')
    elif select_function == '3':
        start_time = time.time()
        clean_memory()
        run_time = time.time() - start_time
        run_time_min = run_time / 60
        print(f'Time to configure: {run_time_min}')
    elif select_function == '4':
        print("Are you sure you want to create a topology from scratch?")
        select_function = input("Type 'yes' or 'no': ").upper() or None
        if select_function == 'YES' or None:
            start_time = time.time()
            create_topology()
            run_time = time.time() - start_time
            run_time_min = run_time / 60
            print(f'Time to configure: {run_time_min}')
            print("- Default user and password")
            print("- VMs: lab/lab123 and root/lab123, Sonic: admin/admin, Apstra: admin/admin")
        else:
            print("Wrong option!! Nothing to do!")
            exit()
    elif select_function == '5':
        print("Are you sure you want to delete everything?")
        select_function = input("Type 'yes' or 'no': ").upper() or None
        if select_function == 'YES' or None:
            start_time = time.time()
            delete_topology()
            run_time = time.time() - start_time
            run_time_min = run_time / 60
            print(f'Time to configure: {run_time_min}')
        else:
            print("Wrong option!! Nothing to do!")
            exit()
    else:
        print("Wrong option!! Nothing to do!")