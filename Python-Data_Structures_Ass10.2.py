name = input("Enter file:")
import re
if len(name) < 1 : name = "regex_sum_415469.txt"
handle = open(name)
lines=handle.read()
total=0
no = re.findall('[0-9]+', lines)
for i in range(0, len(no)):
    total=total+int(no[i])
print(total)
