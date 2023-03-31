#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status."""

import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status")as response:
        response = response.read()
        print("Body response:")
        print(f"\t- type: {type(response)}")
        print(f"\t- content: {response}")
        print(f"\t- utf8 content: {response.decode('utf-8')}")
