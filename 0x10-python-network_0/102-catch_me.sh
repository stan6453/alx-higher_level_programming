#!/bin/bash
#Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
curl -vL -k -X "PUT" -d "user_id=98&school=School&coming_from=School" -H "Referer: School" -A "School" -c "./cookie/catch_me_cookies" -b "./cookie/catch_me_cookies" "$1"
