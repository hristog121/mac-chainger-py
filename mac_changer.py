#!/usr/bin/env python

import subprocess

# Variables for interface and value for the new mac
interfece = "eth0"
new_mac = "00:11:22:33:44:77"

print("[+] Changing the MAC address for " + interfece + " to " + new_mac)

# Run the ifconfig as a shell command
subprocess.call("ifconfig " + interfece + " down", shell=True)
subprocess.call("ifconfig " + interfece + " hw ether" + new_mac, shell=True)
subprocess.call("ifconfig " + interfece + " up", shell=True)
