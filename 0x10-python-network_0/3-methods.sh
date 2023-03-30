#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept.
curl -X "OPTIONS" "$1" -sLI | grep 'Allow' | cut -d":" -f2 | sed 's/^ //'
