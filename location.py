#!/usr/bin/env python3

import ipaddress
import os.path
import requests
import sys

EXIT={
        "arguments": 4,
        "ip": 5,
        "keyfile": 6,
        }

URLBASE="http://api.ipstack.com/"
KEYFILE=".ipstack_key"


def checkIP(ip):
    try:
        ipaddress.ip_address(ip).is_global
    except ValueError:
        return False
    else:
        return ipaddress.ip_address(ip).is_global

def checkKeyFile(f):
    if not os.path.isfile(KEYFILE):
        return False
    else:
        return True


def getResponse(ip, test=False):
    url = f"{URLBASE}/{ip}"
        with open(KEYFILE) as f:
            access_key=f.readline().strip("\n")
            if access_key.isalnum() and access_key.islower():
                secret={'access_key': f.readline().strip("\n")}
            else:
                print ("The format of the access key is wrong")
                sys.exit(EXIT["keyformat"])
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
    if not checkKeyFile(KEYFILE):
        print ("The access_key for the IPStack is missing. Should be: %s" %KEYFILE)
        sys.exit(EXIT["keyfile"])
    response = getResponse(ipAddress)

