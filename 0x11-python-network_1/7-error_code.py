#!/usr/bin/env python3
"""
takes in a URL, sends a request to the URL & displays the body of the response
"""
import requests
import sys

url = sys.argv[1]

response = requests.get(url)

if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    print(response.text)
