import requests

cs_url = 'http://www.so.com/s'
param = {'ie': 'utf-8', 'q': 'query'}
r = requests.get(cs_url, params=param)
print(r.url, r.status_code)

cs_url = 'http://www.haosou.com/s'
r = requests.get(cs_url, params=param, allow_redirects=False)
print(r.url, r.status_code, r.history)
