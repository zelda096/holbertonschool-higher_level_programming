#!/usr/bin/python3
"""
Takes in a URL
"""

import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    header = response.headers
    if "X-Request-Id" in header:
        print(header['X-Request-Id'])
