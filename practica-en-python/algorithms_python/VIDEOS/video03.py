input_str = "LucidProgramming"

#print(len(input_str))

def iterative_Str_len(input_str):
    e = 0
    for a in input_str:
        e += 1
    return e 

#print(iterative_Str_len(input_str))

def recursive_str_len(input_str):
    if input_str == "":
        return 0
    return 1+recursive_str_len(input_str[1:])

print(recursive_str_len(input_str))