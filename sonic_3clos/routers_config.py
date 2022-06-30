"""
---------------------------------
 Author: Gilberto Rampini
 Date: 12/2021
---------------------------------
"""

import time
from time import sleep
import console_config
import create_lab
import threading


class ConfigureRouter(threading.Thread):
    def __init__(self, mgmt_ip: str, hostname: str):
        threading.Thread.__init__(self)
        self.mgmt_ip = mgmt_ip
        self.hostname = hostname

    def run(self):
        console_config.config_vrdc(self.hostname, self.mgmt_ip)


def configure_vrdc():
    threads = []

    print("We will wait around 2 minutes to start the initial vrdc configuration")
    start_time = time.time()
    sleep(120)
    run_time = time.time() - start_time
    print("** Time waiting: %s sec" % round(run_time, 2))
    sleep(5)
    print("########## Basic MGMT Configuration - hostname and ip")

    vrdc_hosts = create_lab.create_vrdc_dic()

    for i in vrdc_hosts.keys():
        hostname = vrdc_hosts[i].get('hostname')
        mgmt_ip = vrdc_hosts[i].get('mgmt_ip')

        thread = ConfigureRouter(mgmt_ip=mgmt_ip, hostname=hostname)
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()



def configure_sonic_ztp():

    threads = []

    print("Wait 1 minute to disable Sonic ZTP")
    start_time = time.time()
    sleep(60)
    run_time = time.time() - start_time
    print("** Time waiting: %s sec" % round(run_time, 2))
    print("########## Basic MGMT Configuration - hostname and ip")


    virtual_hosts = create_lab.create_vrdc_dic()

    """
    for i in virtual_hosts.keys():
        hostname = virtual_hosts[i].get('hostname')

        thread = ConfigureRouter(hostname=hostname, virtual_image='sonic')
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()
    """

    for i in virtual_hosts.keys():
        hostname = virtual_hosts[i].get('hostname')

        console_config.config_virtual_sonic_ztp(hostname)



def configure_virtual_router():

    print("Wait 4 minutes to start MGMT configuration")
    sleep(240)
    print("########## Basic MGMT Configuration - hostname and ip")

    virtual_hosts = create_lab.create_vrdc_dic()

    for i in virtual_hosts.keys():
        hostname = virtual_hosts[i].get('hostname')
        mgmt_ip = virtual_hosts[i].get('mgmt_ip')

        console_config.config_virtual_sonic(hostname, mgmt_ip)
