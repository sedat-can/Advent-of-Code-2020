fe = open("C:\\Users\\elifh\\OneDrive\\Masaüstü\\input12.txt", "r")
s = []
for i in fe:
    y = i.strip("\n")
    s.append((y[0], int(y[1:])))



def direct (lis):
    a = 0 
    b = 0
    c = "E"
    x= 10
    y = 1
    z= "E"
    view = (z,(x, y))
    po = (c , (a, b))
    for i in lis:
        deg = i[1]
        print(po)
        print(view)
        if i[0] == "N":
            y = y + i[1]
            z = "N"
        elif i[0] == "S":
            y = y - i[1]
            z = "S"
        elif i[0] == "E":
            x = x + i[1]
            z = "E"
        elif i[0] == "W":
            x = x - i[1]
            z = "W"

        elif i[0] == "F":
            b = y * i[1] + b
            a = x * i[1] + a
            po = (c , (a, b))
            view = (c, (x, y))
        
        elif i[0] == "R":
            while deg > 0:
                g = y
                h = -x
                x, y =  g, h
                deg = deg - 90
                po = (c , (a, b))
        elif i[0] == "L":
            while deg > 0:
                g = -y
                h = x
                x, y =  g, h
                deg = deg - 90
                view = (c, (-y, x))
                po = (c , (a, b))

    return (view, po)

        
"""        
        
        elif i[0] == "L":
            if i[1] == 90:
                if  po[0] == "N":
                    c = "W"
                    po  = (c, (a, b))
                    view = (c, (y, -x))
                elif  po[0] == "E":
                    c = "N"
                    po  = (c, (a, b))
                    view = (c, (-y, x))
                elif  po[0] == "S":
                    c = "E"
                    po  = (c, (a, b))
                    view = (c, (y, -x))
                elif  po[0] == "W":
                    c = "S"
                    po  = (c, (a, b))
                    view = (c, (-y, x))
            elif i[1] == 180:
                if  po[0] == "N":
                    c = "S"
                    po  = (c, (a, b))
                    view = (c, (-x, y))
                elif  po[0] == "E":
                    c = "W"
                    po  = (c, (a, b))
                    view = (c, (x, -y))
                elif  po[0] == "S":
                    c = "N"
                    po  = (c, (a, b))
                    view = (c, (-x, y))
                elif  po[0] == "W":
                    c = "E"
                    po  = (c, (a, b))
                    view = (c, (x, -y))
            elif i[1] == 270:
                if  po[0] == "N":
                    c = "E"
                    po  = (c, (a, b))
                    view = (c, (y, -x))
                elif  po[0] == "E":
                    c = "S"
                    po  = (c, (a, b))
                    view = (c, (-y, x))
                elif  po[0] == "S":
                    c = "W"
                    po  = (c, (a, b))
                    view = (c, (-y, x))
                elif  po[0] == "W":
                    c = "N"
                    po  = (c, (a, b))
                    view = (c, (y, -x))
        elif i[0] == "R":
            if i[1] == 90:
                if  po[0] == "N":
                    c = "E"
                    po  = (c, (a, b))
                    view = (c, (y, -x))
                elif  po[0] == "E":
                    c = "S"
                    po  = (c, (a, b))
                    view = (c, (-y, x))
                elif  po[0] == "S":
                    c = "W"
                    po  = (c, (a, b))
                    view = (c, (-y, x))
                elif  po[0] == "W":
                    c = "N"
                    po  = (c, (a, b))
                    view = (c, (y, -x))
            elif i[1] == 180:
                if  po[0] == "N":
                    c = "S"
                    po  = (c, (a, b))
                    view = (c, (-x, y))
                elif  po[0] == "E":
                    c = "W"
                    po  = (c, (a, b))
                    view = (c, (x, -y))
                elif  po[0] == "S":
                    c = "N"
                    po  = (c, (a, b))
                    view = (c, (-x, y))
                elif  po[0] == "W":
                    c = "E"
                    po  = (c, (a, b))
                    view = (c, (x, -y))
            elif i[1] == 270:
                if  po[0] == "N":
                    c = "W"
                    po  = (c, (a, b))
                    view = (c, (y, -x))
                elif  po[0] == "E":
                    c = "N"
                    po  = (c, (a, b))
                    view = (c, (-y, x))
                elif  po[0] == "S":
                    c = "E"
                    po  = (c, (a, b))
                    view = (c, (y, -x))
                elif  po[0] == "W":
                    c = "S"
                    po  = (c, (a, b))
                    view = (c, (-y, +x))"""
    

print(direct(s))

print(25317+4084)








