import requests

payload = {'username': 'bor3y1', 'password': '12345' }
r = requests.post("https://httpbin.org/post",data=payload)
print(r.text)