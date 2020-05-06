fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    ly = line.rstrip().split()
    for wrd in ly:
        if wrd not in lst:
            lst.append(wrd)
            lst.sort()
print(lst)
