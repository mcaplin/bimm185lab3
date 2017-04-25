import sys

inp = open(sys.argv[1], 'r')

gc = 0
l = ''
for line in imp:
  if line[0] != '>' #ignore any lines that start with '>'
    l += (line.strip())
l = list(l)
for i in l:
  if i == 'G' or i == 'C':
    gc += 1
print float(gc)/len(l)
