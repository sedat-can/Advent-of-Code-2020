fe = open("C:\\Users\\elifh\\OneDrive\\Masaüstü\\input6.txt", "r")


y = {}
c = 0
le = 0
for a in fe:
    th = {}
    le = le +1
    z =a.split(" contain ")
    for i in z[1].split(", "):
        i = i.strip(".\n")
        if i.endswith("s"):
            th[i[2:][0:-1]] = i[0:1]
        else:
            th[i[2:]] = i[0:1]

    y[z[0][:-1]] = th




import numbers

variable = 5
print(isinstance(5, numbers.Number))


luv = "shiny gold bag"
ye = "faded turquoise bag"

def nevar(x):
    C = 0
    for i in y:
        if i == x:
            for a in y[i]:
                if a != ' other bag':
                    C =  C + int(y[i][a]) +  nevar(a)*int(y[i][a]) 
    return C          

yel = nevar(luv)
print(yel)











