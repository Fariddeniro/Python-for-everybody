fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    ly = line.rstrip().split()
    for wrd in ly:
        if not wrd in lst:
            lst.append(wrd)
            lst.sort()
print(lst)