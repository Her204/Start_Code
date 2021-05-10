import numpy as np
_x_ = int(input("Enter a column number -- "))

_y_ = int(input("Enter a row number -- "))
a = np.random.randn(_x_,_y_)
count = dict()
for i in a:
    for j in i:
        e = str(np.abs(j))[0]
        for k in range(0,10):
            if int(e) == k:
                count[e] = count.get(e, 0) + 1
print(count)

