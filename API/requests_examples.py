import requests
from pprint import pprint

print('1st try')
url1 = "http://www.google.com/"
response_1 = requests.get(url1)
pprint(dict(response_1.headers))
print('-'*20)

print('2nd try')
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
url2 = "https://www.google.com/"
response_2 = requests.get(url2, headers=headers)
pprint(dict(response_2.headers))
print()