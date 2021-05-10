x = 34534
y = 456

def iterative_product(x, y):
    d = 0
    for a in range(y):
        d += x
    return d
print(iterative_product(x,y))

def recursive_product(x, y):    
    if x < y:
        return recursive_product(y, x)
    if y == 0:
        return 0
    return x + recursive_product(x, y-1)
print(recursive_product(x,y))