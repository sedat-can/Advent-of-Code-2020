fe = open("C:\\Users\\elifh\\OneDrive\\Masaüstü\\input22.txt", "r")

class alergen:
    def __init__(self, data):
        self.adata = data  

    def datalist(self):
        l = []
        for i in self.adata:
            c =[]
            y =[]
            for a in i.strip("\n").split("("):
                if a.startswith("contains"):
                    y.extend(a[8:].strip(")").split())
                else:
                    c.extend(a.split())
            l.append((c, y))
        return l




ye = alergen(fe)
print(ye.datalist())


"""def gey (x):
    c =[]
    y =[]
    for a in x:
        if a is str:
        c.append(a[0])
        y.append(a[1])
    return c
a = gey(y)
def gay (x):
    c =[]
    y =[]
    for a in x:
        c.append(a[0])
        y.append(a[1].rstrip(")"))
    return y

z = gay(y)

y = []
for i in z:
    y = i.split() + y
celil = []
for i in y:
    celil.append(i.rstrip(","))


def fgl(z):
    c = []
    for i in z:
        c = c + i.split()
    return c
def fgf(z):
    c = []
    for i in z:
        c = c + i[8:].split(",")
    return c


y = fgf(z)
c = fgl(a)



def ghg(a):
    y = {}
    for i in a:
       y[i] = + a.count(i)
    return y

al = ghg(celil)
ing = ghg(c)

kl = ing.values()
ka = al.values()
c = 0
for i in kl:
    c = i + c
g = 0
for i in ka:
    g = i + g"""
    






