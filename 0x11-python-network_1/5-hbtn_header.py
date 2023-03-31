#!/usr/bin/python3
"""
take in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""

import requests
from sys import argv
if __name__ == "__main__":
    with requests.get(argv[1]) as res:
        print(res.headers.get("X-Request-Id"))
