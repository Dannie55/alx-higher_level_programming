#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays it.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as content:
        request_id = content.header['X-Request-id']
        print(request_id)
