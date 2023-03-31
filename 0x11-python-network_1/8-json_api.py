#!/usr/bin/python3
"""
take in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import urllib.parse
import urllib
import urllib.request
from sys import argv
if __name__ == "__main__":
    url = 'http://4f0e93769549.a6cecdaa.alx-cod.online:5000/search_user'
    value = {'q': ''}
    if len(argv) > 1:
        value = {'q': argv[1]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as res:
        res_body = res.read().decode('utf-8')
        if res.headers.get("Content-Type") != 'application/json':
            print("Not a valid JSON")
        elif res_body[0] == '{' and res_body[1] == '}':
            print("No result")
        else:
            res_body = res_body.replace("{", "").replace('}', '')\
                .replace(',', '')\
                .replace('"', '').replace(':', ' ').replace('\n', '')\
                .replace('id', '').replace('name', '')
            res_body = res_body.strip()
            res_body = res_body.split(' ')

            print(f'[{res_body[0]}] {res_body[1]}')
