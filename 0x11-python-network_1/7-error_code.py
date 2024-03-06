#!/usr/bin/python3
""" script that display the error code """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code == 200:
        print(r.text)
    elif r.status_code >= 400:
        print('Error Code: {}'.format(r.status_code))
