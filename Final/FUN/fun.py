a = open("yarismacilar.txt")
elems = []
for line in a.readlines():
    elems.append(line.rstrip())
elems = sorted(elems)
for elem in elems:
    print(elem)
