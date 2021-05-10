lst = list()
for i in range(10):
    lst.append(i)
lst = lst + [a for a in range(10,100) if a%2==0]
print(lst)
