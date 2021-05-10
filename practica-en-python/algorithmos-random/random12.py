#recursividad
def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(5))
def recursividad(x):
    if len(x) <= 1:
        return x[0]
    else:
        return x[-1] + recursividad(x[-len(x):-1])
print(recursividad("aleman231adasdadsada"))
