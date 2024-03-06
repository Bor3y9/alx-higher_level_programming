import requests
payload = {'username':"youssef",'password':"12312412"}

r = requests.post('https://httpbin.org/post',data=payload)
print(r.json())