# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
xval = 0
xtotal = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find(':')
        xval = float(line[pos+1:])
        xtotal = xtotal + xval
        count = count + 1

print(xtotal/count)
