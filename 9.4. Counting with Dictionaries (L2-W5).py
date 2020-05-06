name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = 0
db = {}
for line in handle:
    if line.startswith('From '):
        ly = line.lstrip()
        words = ly.split()
        sent = words[1]
        db[sent] = db.get(sent, 0)+1
max_no = 0
for sent in db:
    if db[sent] > max_no:
        max_no = db[sent]
        email = sent
print(email, max_no)
