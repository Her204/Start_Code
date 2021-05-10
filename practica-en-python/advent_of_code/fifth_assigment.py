date = open("input_3.txt")
date1 = open("input_3.txt")
date2 = open("input_3.txt")
date3 = open("input_3.txt")
date4 = open("input_3.txt")

def find_tree(date, q, c, f=0, e=0, i=0, posicion=0):
    for a in date:
        i += 1
        if (i-1)%(c) == 0 and i > 1:
            posicion += q
            a = a[:31] * 323
            objetivo = a[posicion]
            if objetivo == ".":
                e += 1
            if objetivo == "#":
                f += 1
            objetivo = a[posicion]
    return [e, f, e+f]

a1 = find_tree(date, 1, 1) 
b1 = find_tree(date1, 3, 1)
c1 = find_tree(date2, 5, 1) 
d1 = find_tree(date3, 7, 1)
e1 = find_tree(date4, 1, 2)
print( a1, b1, c1, d1, e1)
print( a1[1]* b1[1]* c1[1]* d1[1]* e1[1])