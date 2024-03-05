import urllib.request
with urllib.request.urlopen("https://alx-intranet.hbtn.io") as response:
    html = response.headers
print(html['X-request-Id'])