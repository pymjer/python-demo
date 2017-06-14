import zipfile
import re
import requests
from io import BytesIO

webContent = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip')
unzipped = zipfile.ZipFile(BytesIO(webContent.content))
nameLi = unzipped.namelist()
print(nameLi)
nextId = '90052'
patt = re.compile('(\d+)')
comment = ''
while True:
    readme = unzipped.read('%s.txt' % nextId)
    match = patt.search(readme.decode('utf-8'))
    if match:
        nextId = match.group(1)
        comment += unzipped.getinfo('%s.txt' % nextId).comment.decode('utf-8')
        print('now we are goint to %s' % nextId)
    else:
        print(readme)
        print(comment)
        break
