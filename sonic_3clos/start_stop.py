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

virsh_list_filter = ["apstra_server", "dc1-sonic-", "dc2-sonic-", "c1_v", "c2_v"]


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


def get_virtual_machines_status(virsh_status="running", *args):

    """
        create a list with all destroyed or running virtual machine
        virsh_status: destroyed or running
        *args: list of virtual machines
    """

    li_vrdc = []
    for vm in args:

        cmd_virsh_list = ''
        if virsh_status == "destroyed":
            cmd_virsh_list = f"virsh list --all | egrep {vm} | awk '{{print $2}}'"
        if virsh_status == "running":
            cmd_virsh_list = f"virsh list | egrep {vm} | awk '{{print $2}}'"

        # get the output of the cmd_virsh_list, strip and decode in utf-8 - necessary to clean the list output
        vrdc_info = subprocess.Popen(cmd_virsh_list, shell=True, stdout=subprocess.PIPE).stdout.read().strip().decode('utf-8')

        # creates list of the vrdc_info and clean the empty spaces
        li_vrdc.extend(vrdc_info.split("\n"))

    return li_vrdc

    # Legacy code - remove any empty spaces
    # result = [ x for x in li_vrdc if x ]


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


def start_stop_virtual_machine(virsh_action, virsh_status, *args):

    """
    :param virsh_action: start or destroy
    :param virsh_status: running or destroyed
    :param vm_description: i.e Virtual Sonic, Linux VM, Apstra, etc
    :param args: List of virtual machines, i.e: virsh_list_filter = ["dc1-sonic-", "dc2-sonic-", "c1_v", "c2_v"]
    :subprocess.call: run the virsh command with the action + vm
    """
    print(f"########################################################## Start/Stop Virtual Machines")

    server_list = get_virtual_machines_status(virsh_status, *args)

    for server in server_list:
        if server != '':
            command = f'/usr/bin/virsh {virsh_action} {server}'
            print(f'- Start/Stop {server}')
            subprocess.call(command, shell=True)
            sleep(2)


def start_topology():

    print("########################################################## Start Topology")
    clean_memory()
    create_fabric_interface()
    start_stop_virtual_machine("start", "destroyed", *virsh_list_filter)


def stop_topology():

    print("########################################################## Stop Topology")
    start_stop_virtual_machine("destroy", "running", *virsh_list_filter)
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