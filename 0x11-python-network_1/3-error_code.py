#!/usr/bin/python3
""" Script that displayes if there is an error """
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            html = res.read()
        print(html.decode("UTF-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
