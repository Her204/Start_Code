i = int(input("Enter a number: "))
for a in range(i):
    for e in range(10):
        if a == 1:
            print("|",a,"0","|")
            print("|","0","0","|")
            print("|","0","0","|")
        if a > 1: 
            print("|",a,"0","|")
