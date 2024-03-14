#!/usr/bin/env python3

import re
import sys

EXIT={
        "arguments": 4,
        "ip": 5,
        }

URLBASE="http://api.ipstack.com/"

def checkIP(ip):
    pattern = r"^[1-9][0-9]{1,2}(.[1-9][0-9]{1,2}){3}$"
    if not re.match(pattern,ip):
        print ("Argument is not a valid IP address.")
        sys.exit(EXIT["ip"])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Exactly one argument is required.")
        sys.exit (EXIT["arguments"])
    ipAddress = sys.argv[1]
    checkIP(ipAddress)
