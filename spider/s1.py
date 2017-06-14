import requests
import re


qsbk_url = 'http://www.qiushibaike.com/'
res = requests.get(qsbk_url)
content = res.content.decode('utf-8')[500:10000]
pattern = re.compile(
    '<div.*?article.*?h2>(.*?)</h2>.*?<div.*?content">(.*?)</div>', re.S)
print('模式编译完成，开始查找...')
items = re.findall(pattern, content)
print('开始打印....')
for item in items:
    print('作者：%s' % item[0])
    print('内容：%s' % item[1].strip().replace('<br/>', '\n'))
    print('-----------------------------------')
print('匹配完成')
