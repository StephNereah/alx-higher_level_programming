#!/usr/bin/python3
"""
script that takes 2 arguments in order to list 10 commits (from the most
recent to oldest)
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
        sys.exit(1)

    repoName = sys.argv[1]
    ownerName = sys.argv[2]

    url = f"https://api.github.com/repos/{ownerName}/{repoName}/commits"
    response = requests.get(url, params={'per_page': 10})

    if response.status_code != 200:
        print(f"Error: Unable to fetch commits for {ownerName}/{repoName}")
        sys.exit(1)

    commits = response.json()
    for commit in commits:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")
