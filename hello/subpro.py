import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['ls'])
print('Exit code:', r)
