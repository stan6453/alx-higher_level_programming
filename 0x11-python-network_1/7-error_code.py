#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import requests
from sys import argv

if __name__ == "__main__":
        with requests.get(argv[1]) as res:
            if res.status_code >= 400:
                  print(f"Error code: {res.status_code}")
            else:
                  print(res.text)
