import requests

# data1 = {'page':25,'count':3}
r = requests.get('https://alx-intranet.hbtn.io')
print(r.headers['X-Request-Id'])