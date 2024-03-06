#!/usr/bin/python3
""" script that post an email """
import requests
import sys

if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], payload)
    print(r.text)
