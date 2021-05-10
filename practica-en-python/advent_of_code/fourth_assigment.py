date = open("input_3.txt")
posicion = 0
lst = []
i = 0
e = 0
f = 0
for a in date:
    lst.append(a[:31] * 323)
    i += 1
    if i > 1:
        posicion += 3
        a = a[:31] * 100
        objetivo = a[posicion]
        if objetivo == ".":
            e += 1
        if objetivo == "#":
            f += 1
        print(len(a))
        print(posicion)
        objetivo = a[posicion]
        print(objetivo)
print(e,".",f,"#",e+f, i )
