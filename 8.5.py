fname = input("Enter file name: ")
count = 0
fh = open(fname)
lst = list()
for line in fh:
    if line.startswith('From:'):
        continue
    elif line.startswith('From '):
        lst = line.split()
        count = count + 1
        print(lst[1])
    else: continue
print('There were', count,'lines in the file with From as the first word')
