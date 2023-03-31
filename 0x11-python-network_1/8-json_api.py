#!/usr/bin/python3
"""
take in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv
if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    values = {'q': ''}
    if len(argv) > 1:
        values = {'q': argv[1]}

    with requests.post(url, data=values) as res:
        try:
            dict1 = res.json()
            if len(dict1) == 0:
                print("No result")
            else:
                print(f'[{dict1["id"]}] {dict1["name"]}')
        except requests.exceptions.JSONDecodeError as err:
            print('Not a valid JSON')
