import excercise as ex
def recursive_computer_lenguage_translator(z):
    if z == "":
        b = ""
        return b
    else:
        b = str(hex(ord(z[0])))
        return b + " " + recursive_computer_lenguage_translator(z[1:len(z)])
a = input("Enter a input--")
print(recursive_computer_lenguage_translator(a))
print(ex.computer_lenguage_translator(a))