#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import urllib.error
import urllib.request
from sys import argv
try:
    with urllib.request.urlopen(argv[1]) as res:
        print(res.read().decode('utf-8'))
except urllib.error.HTTPError as err:
    print(f"Error code: {err.code}")
