import requests
import re

cs_url  = 'https://github.com/login'
cs_user = 'user'
cs_psw  = 'psw'
my_headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}
sss     = requests.Session()
r       = sss.get(cs_url, headers = my_headers)
reg     = r'<input name="authenticity_token" type="hidden" value="(.*)" />'
pattern = re.compile(reg)
result  = pattern.findall(r.content.decode('utf-8'))