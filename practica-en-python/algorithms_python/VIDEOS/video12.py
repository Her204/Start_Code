
r = open(input("enter a file--"))
def palindrom_perm(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()
    d = dict()
    for i in input_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    odd_count = 0
    for k, v in d.items():
        if v%2 != 0 and odd_count == 0:
            odd_count += 1
        elif v%2 != 0 or odd_count != 0:
            return False
        grads = {"bool":True, "value":d}
    return grads
i = 0
lst = []
for a in range(0,10):
    lst.append(str(a))
for a in r:
    ar = a.split()
    for b in ar:
        if palindrom_perm(b) != False and len(b) > 1:
            if len(palindrom_perm(b)["value"].keys()) > 2:
                if not b[0] in lst:
                    print(palindrom_perm(b)["value"], b)
                    i += 1
print(i)
            
      