"""
---------------------------------
 Author: Gilberto Rampini
 Date: 12/2021
---------------------------------
"""

import logging
import pexpect
from time import sleep


user = "admin"
pwd = "YourPaSsWoRd"
new_pwd = "admin"


def config_vrdc(hostname, mgmt_ip):

    print(f"- Configuring {hostname} with MGMT IP: {mgmt_ip}")

    child = pexpect.spawn(f"virsh console {hostname} --force", timeout=60)
    logging.debug("Got console, Logging in as admin")
    child.send("\r")
    child.send("\r")
    child.send("\r")

    child.expect(".*ogin:")
    logging.debug(f"sending user: {user}")
    child.sendline(user)

    child.expect("Password:")
    logging.debug(f"sending user: {pwd}")
    child.sendline(pwd)

    print(f"- {hostname}: Disabling Sonic ZTP")
    child.send("\r")
    child.send("\r")
    child.send("\r")
    child.send("\r")
    child.expect(".*$")
    logging.debug("disabling ZTP")
    child.sendline("sudo config ztp disable")
    child.expect(".*:")
    child.sendline("y")
    child.send("\r")
    print(f"- {hostname}: Waiting to disable Sonic ZTP. It can take around 2min ")
    sleep(150)

    print(f"- {hostname}: changing admin password to : admin")
    child.expect(".*$")
    child.send("\r")
    child.send("\r")
    logging.debug("Sending cli")
    child.sendline("sudo passwd admin")
    child.expect(".*:")
    child.sendline(new_pwd)
    child.expect(".*:")
    child.sendline(new_pwd)
    child.send("\r")
    child.send("\r")
    print(f"- {hostname}: admin password done!")

    print(f"- {hostname}: Sonic-CLI Mode")
    child.expect(".*$")
    child.send("\r")
    child.send("\r")
    logging.debug("Sending cli")
    child.sendline("sonic-cli")

    child.expect(".*#")
    logging.debug("Sending configure")
    child.sendline("configure terminal")
    child.expect(".*#")

    print(f"- {hostname}: Configuring Management Interface: {mgmt_ip}")
    logging.debug("going to interface MGMT")
    child.sendline("interface Management 0")
    child.expect(".*#")
    logging.debug("configuring interface MGMT")
    child.sendline(f"ip address {mgmt_ip}/24")

    child.expect(".*#")
    child.sendline("exit")

    print(f"- {hostname}: Configuring hostname: {hostname} ")
    child.expect(".*#")
    child.sendline(f"hostname {hostname}")

    child.send("\r")
    child.send("\r")

    print(f"- {hostname}: Saving configuration")
    child.expect(".*#")
    child.send("\r")
    child.sendline("write memory")
    child.send("\r")

    child.expect(".*#")
    child.sendline("exit")

    child.expect(".*#")
    child.sendline("exit")

    child.expect(".*$")
    child.sendline("exit")
    child.send("\r")
    child.sendcontrol("]")

    print(f"- {hostname}: configuration completed")