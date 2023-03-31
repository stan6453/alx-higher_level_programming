#!/usr/bin/python3
"""
takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}

    with requests.post(argv[1], data=values) as res:
        print(res.text)
