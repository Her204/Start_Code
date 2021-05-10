date = open("input_1.txt")
lst = list()
lst2 = list()
lst3 = list()
for a in date:
    lst.append(int(a))
    lst2.append(int(a))
    lst3.append(int(a))
for i in lst:
    for y in lst2:
        for z in lst3:
            if i + y + z== 2020 and i != y and i != z and z != y:
                print( i * y * z, i + y + z)
print(len(lst))