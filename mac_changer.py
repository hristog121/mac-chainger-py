#!/usr/bin/env python

import subprocess

# Variables for interface and value for the new mac
interface = input("Interface > ")
new_mac = input("New MAC > ")

print("[+] Changing the MAC address for " + interface + " to " + new_mac)

# Run the ifconfig as a shell command
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
