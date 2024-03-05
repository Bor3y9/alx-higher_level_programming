#!/usr/bin/python3
""" script that send a POST request with an email param,
then displays the body of the response decoded in utf-8. """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    param = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(param)
    data = urllib.encode('UTF-8')
    req = url.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
