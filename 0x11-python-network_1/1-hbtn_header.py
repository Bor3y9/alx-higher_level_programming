#!/usr/bin/python3
""" script that display value of a header """
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.headers
    print(html['X-request-Id'])
