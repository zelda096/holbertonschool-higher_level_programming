#!/usr/bin/python3
"""
Takes in a letter and sends a POST request
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        rdict = r.json()
        if bool(rdict) is False:
            print("No result")
        else:
            print("[{}] {}".format(rdict['id'], rdict['name']))
    except:
        print("Not a valid JSON")
