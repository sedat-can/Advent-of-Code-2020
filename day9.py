fe = open("C:\\Users\\elifh\\OneDrive\\Masaüstü\\input9.txt", "r")
y = []
for i in fe:
    y.append(i.strip("\n"))


def check (a, c):
    ley = []
    for x in c:
        for xy in c:
            if int(xy) == int(x):
                pass
            elif int(a) == int(x) + int(xy):
                return True


c = 0
z = 25
lis = []
for a in y[25:]:
    if check(a, y[c:z]):
        lis.append(a)
    c = c + 1
    z = z + 1


for i in y[25:]:
    if i in lis:
        pass
    else:
        print(i)
from functools import reduce
h = 0
import queue
def weak (a, lis):
    queue = []
    for x in lis:
        queue.append(int(x))
        h = reduce(lambda x,y: x+y, queue)
        if h == int(a):
            return queue
        elif h > int(a):
            while h > a:
                queue.pop(0)
                h = reduce(lambda x,y: x+y, queue)
            if h == int(a):
                return queue

print(weak (542529149, y))

print(52489498 + 23189120)









    

    