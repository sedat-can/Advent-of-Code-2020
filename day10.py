fe = open("C:\\Users\\elifh\\OneDrive\\Masaüstü\\day10.txt", "r")
y = []
for i in fe:
    y.append(int(i.strip("\n")))

ve = y.append(max(y) + 3)

lus = []
z = 0
acc = 0
acc2 = 0
while z <= max(y):
    if (z +1) in y:
        lus.append(z+1)
        z = z+ 1 
        acc = acc + 1
    elif (z + 3) in y:
        lus.append(z+3)
        z = z + 3
        acc2 = acc2 + 1
    else:
        break
print(lus)

key = {}
def adop (lih, x = [],  z = 0):
    if z in key:
        return key[z]
    if z == max(y):
        return 1
    total = 0
    if z+1 in lih:
        total  = total + adop(lih, x, z+1)
    if z+2 in lih:
        total  = total + adop(lih, x, z+2)
    if z+3 in lih:
        total  = total + adop(lih, x, z+3)
    key[z] = total
    return total
      
print(adop(y))





