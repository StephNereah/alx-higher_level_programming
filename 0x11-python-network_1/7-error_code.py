#!/usr/bin/python3
"""
sends a request to the passed URL and displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    body = response.text
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(body)
