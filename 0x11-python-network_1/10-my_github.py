#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from sys import argv
if __name__ == "__main__":
    with requests.post('https://api.github.com/user',
                       headers={'Authorization': f"Bearer {argv[2]}"}) as res:
        print(res.json()['id'])
