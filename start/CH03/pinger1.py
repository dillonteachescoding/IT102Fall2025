#!/usr/bin/env python3
# First example of pinging from Python
# By Dillon ping? importing functions

#Libraries
import platform
import os

ip = input("Please enter a valid IP address with x.x.x.x: ")

#Build a ping command
ping_cmd = f"ping -c 1 -w 2 {ip}"

#Exectue command and capture output
exit_code = os.system(ping_cmd)

#Print the ouput
print(exit_code)