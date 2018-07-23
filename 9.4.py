fname = input("Enter file name: ")
fh = open(fname)


counts = dict()
for line in fh:
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        words = line.split()
        counts[words[1]] = counts.get(words[1],0) + 1

    else: continue

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
