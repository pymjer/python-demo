import requests
import re

cs_url = 'https://github.com/login'
cs_user = "pymjer"
cs_psw = "qrpylxaqsh-5"

my_headers = {
    'Accept': 'text/html,'
    'application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;'
    'q=0.6,id;q=0.4,ja;q=0.2,zh-TW;q=0.2',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    ' AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/48.0.2564.116 Safari/537.36',
}

req = requests.Session()
res = req.get(cs_url, headers=my_headers)
reg = r'<input name="authenticity_token" type="hidden" value="(.*)" />'

patt = re.compile(reg)

result = patt.findall(res.content.decode('utf-8'))

token = result[0]
my_data = {
    'commit': 'Sign in',
    'utf8': '%E2%9C%93',
    'authenticity_token': token,
    'login': cs_user,
    'password': cs_psw
}

cs_url = 'https://github.com/session'
r = req.post(cs_url, headers=my_headers, data=my_data)
print(r.url, r.status_code, r.history)
