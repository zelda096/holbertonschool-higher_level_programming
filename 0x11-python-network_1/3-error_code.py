#!/usr/bin/python3
"""
Takes in a URL
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
