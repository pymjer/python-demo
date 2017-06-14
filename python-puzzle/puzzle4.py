import re
puzzle = ''.join([c for c in open('./puzzle4.txt')])
result = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', puzzle)
print(''.join(result))
