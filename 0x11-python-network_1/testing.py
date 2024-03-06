import urllib.request
req = urllib.request.Request('https://www.python.org/fish.html')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))