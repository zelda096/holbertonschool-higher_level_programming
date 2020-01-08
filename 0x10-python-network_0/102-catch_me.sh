#!/bin/bash
#makes a request that causes the server to respond with 'You got me!'
curl -s "0.0.0.0:5000/catch_me" -LX PUT -H "Origin: HolbertonSchool" -d "user_id=98"
