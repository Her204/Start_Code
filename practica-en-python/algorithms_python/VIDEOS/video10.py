#Optimal Task Assignment
A = [ 6, 3 , 2, 7, 5, 5,6,7,4]

A = sorted(A)
print(A)
for i in range(1,len(A)//2+1):
    print((A[i],A[-i]))