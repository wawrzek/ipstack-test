#!/usr/bin/env python3

import ipaddress
import sys

EXIT={
        "arguments": 4,
        "ip": 5,
        }

URLBASE="http://api.ipstack.com/"

def checkIP(ip):
    try:
        ipaddress.ip_address(ip).is_global
    except ValueError:
        return False
    else:
        return ipaddress.ip_address(ip).is_global



def tuneOutput(response):
    important=["latitude", "longitude"]
    returns = []
    for i in important:
        returns.append(response[i])
    return returns

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Exactly one argument is required.")
        sys.exit (EXIT["arguments"])
    ipAddress = sys.argv[1]
    if not checkIP(ipAddress):
        print ("Argument is not a valid, global IP address.")
        sys.exit(EXIT["ip"])
