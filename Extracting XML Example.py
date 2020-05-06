import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

url2 = 'http://py4e-data.dr-chuck.net/comments_415471.xml'
data = urllib.request.urlopen(url2).read().decode()
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
sum = 0
for item in counts:
    sum += int(item.find('count').text)
print(sum)
