#!/usr/bin/python3
"""
take in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv
if __name__ == "__main__":
    url = 'http://4f0e93769549.a6cecdaa.alx-cod.online:5000/search_user'
    values = {'q': ''}
    if len(argv) > 1:
        values = {'q': argv[1]}

    with requests.post(url, data=values) as res:
        try:
            obj = res.json()
            if len(obj) == 0:
                print("No result")
            else:
                print(f'[{obj["id"]}] {obj["name"]}')
        except requests.exceptions.JSONDecodeError:
            print('Not a valid JSON')
