import requests
import sys

# url = sys.argv[1]
# r = requests.get(url)
# if r.status == 200:
#     print(r.text)
# elif r.status >= 400:
#     print('Error Code: {}'.format(r.status))

r = requests.get('http://bor3y.tech')
print(r.status_code)