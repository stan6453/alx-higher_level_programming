#!/usr/bin/python3
"""
takes your GitHub credentials (username and password) and uses the GitHub API to display your id
"""

import urllib.parse
import urllib.request
from sys import argv
if __name__ == "__main__":
    req = urllib.request.Request('https://api.github.com/user',
                                 headers={'Authorization': f"Bearer {argv[2]}"})
    with urllib.request.urlopen(req) as res:
        res_body = res.read().decode('utf-8')
        res_body = res_body.replace('"', '')
        res_body = res_body[1:-1].split(',')
        for ele in res_body:
            items = ele.split(':')
            if items[0] == "id":
                print(items[1])

