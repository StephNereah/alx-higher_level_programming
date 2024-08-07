#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
   uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    user_info = response.json()
    print(user_info.get('id'))
