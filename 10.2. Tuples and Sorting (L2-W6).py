name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=0
db=dict()
for line in handle:
    if line.startswith('From '):
        ly=line.rstrip()
        words=ly.split()
        HR=words[5].split(':')
        hour=HR[0]
        db[hour]=db.get(hour,0)+1
sortdb=sorted(db.items())
for k, v in sortdb:
    print(k, v)
    
