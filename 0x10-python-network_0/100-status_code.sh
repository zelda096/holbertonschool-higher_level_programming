#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
