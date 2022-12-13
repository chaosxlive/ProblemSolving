import requests

url = 'http://mercury.picoctf.net:45028/index.php'

s = requests.session()
resp = s.head(url)
print(resp.headers['flag'])
