import requests
import re

username = "natas0"
password = "natas0"

url = f'http://{username}.natas.labs.overthewire.org'

auth = (username, password)
r = requests.get(url, auth=auth)

print(r.text)

result = re.search(r'\w{32}', r.text).group()
print(result)


