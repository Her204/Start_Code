date = open("input_4.txt")
lst = list()
lst2 = []
i = 0
ia = 0
e = ""
total = 0
for a in date:
    q = a
    ia += 1
    if a != "\n":
        e += q[:-1] + " "
    if a == "\n":
        if ia >= 2 and ia <= 7:
            lst.append(e)
        quark = e[:-1].split(" ")
        quark.sort()
        print(quark)
        if len(quark) >= 7:
            lst2.append(quark)
        total += 1
        e = ""
        ia = 0 
        continue
lst_ = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
print(total)
range = 0
count = dict()
al = 0
for element in lst2:
    range += 1
    if element[1].split(":")[0] != "cid" and len(element) == 7:
        #print(len(element), "without cid", element)
        count[element[-1]] = count.get(element[-1], 0) + 1
        el = element
        i += 1
    if len(element) == 8:
        i += 1
        #print(len(element), "full", element)
        count[element[-1]] = count.get(element[-1], 0) + 1
        
        
print(i)
print(range)
print(len(count))
