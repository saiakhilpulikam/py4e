fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    lst = lst + line.split()


for word in lst:
    lst.remove(word)
    if word not in lst:
        lst.append(word)


lst.sort()
print(lst)
    
