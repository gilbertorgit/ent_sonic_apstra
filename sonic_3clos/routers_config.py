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