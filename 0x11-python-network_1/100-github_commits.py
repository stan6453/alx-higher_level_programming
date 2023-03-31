#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""

import requests
from sys import argv
if __name__ == "__main__":
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    with requests\
        .get(f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits',
             headers=headers) as res:
        list1 = res.json()

        list1.sort(reverse=True,
                   key=lambda dict1: dict1['commit']['author']['date'])

        for elem in list1:
            print(
                f"{elem['sha']} \
{elem['commit']['author']['name']}")
