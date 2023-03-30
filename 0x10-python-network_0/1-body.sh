#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -siL "$1" | awk '$2 == 200 {show_body = 1} length($0) == 1 {body = 1; next} show_body == 1 && body == 1 {print $0}'
