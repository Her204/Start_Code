cdf = str(input("Enter-"))

def a_pizza_strange_function(asd):
    asd = asd.replace(" ", "").upper()
    b = ""
    for a in asd:
        b = a + b
    return b
print(a_pizza_strange_function(cdf))
