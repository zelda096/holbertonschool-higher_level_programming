#!/bin/bash
#json file in the host
curl -sH "Content-Type: application/json" --request POST --data @"$2" "$1"
