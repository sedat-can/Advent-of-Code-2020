fe = open("C:\\Users\\elifh\\OneDrive\\Masaüstü\\input11.txt", "r")
s = []
for i in fe:
    s.append((i.strip("\n")))



def seat (leap, lis):
    x, y = leap
    if  lis[y][x] == "L":
        for a , b in [(1,0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                if True:
                    gep  = y
                    gen = x
                    while 0 <= gep +b <= len(s) -1 and 0 <= gen+a <= len(s[0]) -1 :
                        gep = gep + b
                        gen = gen +a
                        if lis[gep][gen] == "L":
                            break
                        elif lis[gep][gen] == "#":
                            return  "L" 
                        elif lis[gep][gen] == ".":
                            pass  
        return "#"
    
    elif  lis[y][x] == ".":
        return "."
    elif lis[y][x] == "#":
        z = 0
        for a , b in [(1,0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
            if  True:
                gep  = y
                gen = x
                while 0 <= gen +a <= len(s) -1 and 0 <= gep+b <= len(s[0]) -1  :
                    gep = gep + b
                    gen = gen +a
                    if lis[gep][gen] == "L":
                        break
                    elif lis[gep][gen] == "#":
                        z = z + 1
                        break 
                    elif lis[gep][gen] == ".":
                        pass
            if z >= 5:
                return "L"
        return "#"


def search( lis, y = 0):
    g = []
    for x in range(len(lis)):
        c = ""
        for i in range(len(lis[0])):
            c = c + seat((i, x), lis) 
        g.append(c)
    y = y + 1
    if y == 252 :
        return g
    else:

        return (search(g, y))




gel = search(s)

c = 0
for i in gel:

    for z in i:
        if z == "#":
            c = c + 1

print(c)








