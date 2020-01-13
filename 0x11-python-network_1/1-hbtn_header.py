#!/usr/bin/python3
"""
Takes in a URL
"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
    if "X-Request-Id" in header:
        print(header['X-Request-Id'])
