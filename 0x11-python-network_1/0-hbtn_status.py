#!/usr/bin/python3
"""Module that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status' #Define url

#Open and fetch response from URL
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status' #Define url
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body.decode('utf-8')}")
