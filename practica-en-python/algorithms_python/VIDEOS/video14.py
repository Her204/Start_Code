unique_str = "AbCDefG"
non_unique_str = "non Unique STR"

def normalize(str_1):
    str_1 = str_1.replace(" ", "")
    return str_1.lower()

def is_unique_1(input_str):
    d = dict()
    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = d.get(i,0) + 1
    return True, d 

def is_unique_2(input_str):
    return len(set(input_str)) == len(input_str), set(input_str)

def is_unique_3(input_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False, alpha
    return True, alpha

print(is_unique_1(normalize(unique_str)))
print(is_unique_1(normalize(non_unique_str)))

print(is_unique_2(normalize(unique_str)))
print(is_unique_2(normalize(non_unique_str)))

print(is_unique_3(normalize(unique_str)))
print(is_unique_3(normalize(non_unique_str)))