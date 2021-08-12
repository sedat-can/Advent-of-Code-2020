fe = open("C:\\Users\\elifh\\OneDrive\\Masaüstü\\input6.txt", "r")
import json 
y = []
ce = []
for f in fe:
    if f != "\n" :
        ce.append(f.rstrip("\n"))
    else:
        y.append(ce)
        ce =[]     

C = []

for i in y:
    lu = []
    ce = []
    for x in i:
        for k in x:
            lu.append(k)
        ce.append(lu)
        lu = []
    C.append(ce)
    ce = []

from functools import reduce
Y = []
for A in C:
    Y.append(list(reduce(lambda i, j: i & j, (set(n) for n in A))))

po = 0
for i in Y:
    po = po + len(i)

print(po)
