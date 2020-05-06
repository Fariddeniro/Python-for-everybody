name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=0
db={}
for line in handle:
    if line.startswith('From '):
        ly=line.lstrip()
        words=ly.split()
        sent=words[1]
        db[sent]=db.get(sent,0)+1
a=0
for sent in db:
    if db[sent]>a:
        a=db[sent]
        b=sent
print(b, a)

