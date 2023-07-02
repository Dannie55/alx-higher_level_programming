#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""

  response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

try:
    data = response.json()
    if data:
        user_id = data.get('id')
        user_name = data.get('name')
        if user_id and user_name:
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")

