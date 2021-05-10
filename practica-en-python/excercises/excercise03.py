lst = []
for a in range(0,10):
    if a%2 == 0:
        lst.append(str(a))
for b in range(1,100):
    if not str(b)[-1] in lst:
        print(b)
print(lst)