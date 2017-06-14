import re


patt = re.compile('(\d)(\1*)')

res = re.findall(patt, '')
print(res)

 
