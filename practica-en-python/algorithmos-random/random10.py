def buscar_palabras(texto, palabra):
    n = len(texto)
    m = len(palabra)
    for i in range(n):
        j = 0
        while j < m and i+j < n and texto[i+j] == palabra[j]:
            j = j+1
        if j == m:
             return True
    return False
print(buscar_palabras("hola soy herbert", "h"))