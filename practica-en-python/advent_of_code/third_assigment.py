date = open("input_2.txt")
right = list()
wrong = list()
i = 0
for a in date:
    i += 1 
    der = a.split()
    c = der[0].replace("-","")
    if len(c) < 4:
        c1 = int(c[:1])
    else:
        c1 = int(c[:2])
    if len(c) < 4:  
        c2 = int(c[1:])
    else:
        c2 = int(c[2:])
    d = der[1] 
    e = der[2]
    i = 0
    f = 0
    for b in e:
        if b == d[0]:
            i += 1
    if e[c1-1] == d[0] and not e[c2-1] == d[0]:
        print("right",c1, d[0],e, der[0])
        right.append(e)
    elif e[c2-1] == d[0] and not e[c1-1] == d[0]:
        print("right",d[0], c2, e, der[0])
        right.append(e)
    
    else:
        wrong.append(e)
print(len(right))
print(len(wrong))
      