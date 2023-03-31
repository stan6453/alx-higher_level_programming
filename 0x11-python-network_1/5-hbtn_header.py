#!/usr/bin/python3
"""
take in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""

import urllib.request
from sys import argv
with urllib.request.urlopen(argv[1]) as res:
    print(res.headers.get("X-Request-Id"))
