def lef(T):
    l = [lef(a) for a in T]
    return l
print(lef([[str(b) for b in range(a)] for a in range(10)]))
