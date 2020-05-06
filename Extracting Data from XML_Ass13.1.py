import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_415474.json'
uh = urllib.request.urlopen(url)
data = uh.read()
info = json.loads(data)
total = 0
for i in range(0, len(info['comments'])):
    total += info['comments'][i]['count']
print(total)
