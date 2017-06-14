import requests
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
pageNo = '63579'
while True:
    r = requests.get(url + pageNo)
    nextPage = re.findall('(\d+)', r.content.decode('utf-8'))
    if len(nextPage) == 1:
        pageNo = nextPage[0]
        print(pageNo)
    else:
        break
