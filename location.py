#!/usr/bin/env python3

import ipaddress
import requests
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

def getResponse(ip, test=False):
    url = f"{URLBASE}/{ip}"
    if not test:
        with open(f".ipstack_key") as f:
            secret={'access_key': f.readline().strip("\n")}
    else:
        secret={}
    r = requests.get(url, params=secret)
    return dict(r.json())


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
    response = getResponse(ipAddress)
    print (response)

