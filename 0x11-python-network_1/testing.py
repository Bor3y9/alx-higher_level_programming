import requests

# data1 = {'page':25,'count':3}
r = requests.get('https://httpbin.org/')
print(r.content)