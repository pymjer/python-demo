import requests
import pickle

webContent = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
pwc = pickle.loads(webContent.content)
print(pwc)
print('\n'.join([''.join([p[0] * p[1] for p in row]) for row in pwc]))
