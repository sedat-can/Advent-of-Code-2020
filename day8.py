fe = open("C:\\Users\\elifh\\OneDrive\\Masaüstü\\input8.txt", "r")

dictin = []

for a in fe:
    dictin.append((a[0:3], a[4:].strip("\n")))

cel =list(enumerate(dictin))
c =[]
def reco (liste, fir=0, y=0, c = []): 
    for i in liste:
        if i in c:
            return (fir, y, c)
        else:
            if i[1][0] == "acc":
                c.append(i)
                y = y+1
                if i[1][1][0] == "-":
                    fir = fir  - int(i[1][1][1:])
                elif i[1][1][0] == "+":
                    fir = fir  + int(i[1][1][1:])

            elif i[1][0] == "nop":
                fir =fir
                c.append(i)
                y = y+1
            elif i[1][0] == "jmp":
                c.append(i)
                if i[1][1][0] == "-":
                    y = y - int(i[1][1][1:])
                    return reco(cel[y:], fir, y, c)
                elif i[1][1][0] == "+":
                    y = y + int(i[1][1][1:])  
                    return reco(cel[y:], fir, y, c)
    return c 




 
def searchh (liste, a, b):
    v = []
    sonuc = reco(liste)
    print(sonuc)
    if sonuc[2][-1] == cel[-1]:
        return ("bu dogru0", sonuc[0] )
    else :
        for i in cel:
            if i[1][0] == "nop":
                if a == b :
                    v.append((i[0], ("jmp", (i[1][1]))))
                    b = b + 1
                else:
                    v.append(i)
                    a = a + 1
            elif i[1][0] == "jmp":
                if a == b :
                    v.append((i[0], ("nop", (i[1][1]))))
                    b = b + 1
                else:
                    v.append(i)
                    a = a + 1
            else:
                v.append(i)
        searchh(v, 0, b )





print(searchh(cel, 0, 0))

