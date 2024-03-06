import urllib.request
req = urllib.request.Request('http://bor3y.tech')
with urllib.request.urlopen(req) as response:
    html = response.read()
print(html)