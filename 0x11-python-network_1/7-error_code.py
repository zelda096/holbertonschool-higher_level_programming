#!/usr/bin/python3
"""
Takes in a URL and an email
"""

import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code == requests.codes.ok:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
