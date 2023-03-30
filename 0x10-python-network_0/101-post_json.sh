#!/bin/bash
#sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -L -d @"${2}" "$1" -H 'Content-Type: application/json'
