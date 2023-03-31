#!/usr/bin/python3
"""fetch https://alx-intranet.hbtn.io/status"""

import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        print('Body response:')
        print(f"\t- type: {type(res.read().decode('utf-8'))}")
        print(f"\t- content: {res.read().decode('utf-8')}")
