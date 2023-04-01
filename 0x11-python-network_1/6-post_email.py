#!/usr/bin/python3
"""
takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response
"""

import requests
import sys

if len(sys.argv) < 3:
    print("Usage: {} <url> <email>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

print("Your email is:", email)

response = requests.post(url, data={'email': email})

print(response.text)
