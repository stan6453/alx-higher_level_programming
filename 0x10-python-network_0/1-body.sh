#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -sSL -w '%{http_code}\n' "$1" | sed -n '/^200$/ {n;p;}'
