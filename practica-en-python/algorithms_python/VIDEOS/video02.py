input_str_1 = "lucidProgramming"
input_str_2 = "LucidPrograming"
input_str_3 = "lucidprogramming"

def find_uppercase_iterative(input_str):
    for a in input_str:
        if a.isupper():
            return a
    return "No uppercase character found"
#print(find_uppercase_iterative(input_str_1))
#print(find_uppercase_iterative(input_str_2))
#print(find_uppercase_iterative(input_str_3))

def find_uppercase_recursive(input_str, idx =0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str)-1:
        return "No uppercase character found"
    return find_uppercase_recursive(input_str,idx+1)

print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))