#!/usr/bin/env python

import subprocess

# Run the ifconfig as a shell command
subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)