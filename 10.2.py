fname = input("Enter file name: ")
fh = open(fname)


counts = dict()
for line in fh:
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        words = line.split()
        time = words[5]
        hrs = time.split(':')
        counts[hrs[0]] = counts.get(hrs[0],0) + 1

    else: continue
tmp = list()
for k,v in counts.items():
    tmp.append((k,v))

tmp = sorted(tmp)
for k,v in tmp:
    print(k,v)
