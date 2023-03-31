#!/usr/bin/python3
"""fetch https://alx-intranet.hbtn.io/status"""

import requests
if __name__ == "__main__":
    with requests.get("https://alx-intranet.hbtn.io/status") as res:
        print('Body response:')
        print(f"\t- type: {type(res.text)}")
        print(f"\t- content: {res.text}")
