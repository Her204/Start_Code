def computer_lenguage_translator(z):
    b = ""
    c = ""
    d = ""
    z = z.replace(" ", "")
    for a in z:
        b += str(hex(ord(a))).upper() + " "
        c += str(bin(ord(a))).upper() + " "
        d += str(ord(a)).upper() + " "
    return d, b, c
print(computer_lenguage_translator("hello world mother fucker"))