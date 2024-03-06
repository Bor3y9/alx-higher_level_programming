#!/usr/bin/python3
""" Script that displayes if there is an error """
import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
