import requests
import re

url = 'http://natas0.natas.labs.overthewire.org'
username = "natas0"
password = "natas0"

auth = (username, password)
r = requests.get(url, auth=auth)

print(r.text)

result = re.search(r'\w{32}', r.text).group()
print(result)


