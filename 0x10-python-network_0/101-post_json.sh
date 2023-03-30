#!/bin/bash
#sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -L -H 'Content-Type: application/json' -X "POST" -d @"${2}" "$1"
