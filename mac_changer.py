#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    # Take arguments from the user directly on the command line
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    return parser.parse_args()


def change_mac(interface, new_mac):
    print("[+] Changing the MAC address for " + interface + " to " + new_mac)

    # Run the ifconfig as a shell command  - no protection against command injection
    # subprocess.call("ifconfig " + interface + " down", shell=True)
    # subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    # subprocess.call("ifconfig " + interface + " up", shell=True)

    # Same commands as above but command injection will bnot be possible
    subprocess.call(["ifconfig ", interface, "down"])
    subprocess.call(["ifconfig ", interface, "hw ether ", new_mac])
    subprocess.call(["ifconfig ", interface, "up"])


(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
