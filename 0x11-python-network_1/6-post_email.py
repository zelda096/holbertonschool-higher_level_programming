#!/usr/bin/python3
"""
Takes in a URL and an email
"""

import requests
import sys

if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    posted = response.text

    print(posted)
