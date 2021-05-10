# Crear un algoritmo recursivo capaz de transformar un numero en su equivalente ordenado basado en el orden de las letras ejemplo
# 1: a, 2:b, aa:27...
def num_a_letras_new(a,b):
    lst = list()
    for q in range(1,len(a)):
        lst.append(q)
    return num_a_letras_new(a[a-1:],b-1)
print(num_a_letras_new("sad",123))

d = input("Escribe algunas letras siempre y cuando todas sean distintas: ")
for a in range(c):
    for b in range(len(d)):
        q = d[b]
        if a%b==0:
            a = 
            