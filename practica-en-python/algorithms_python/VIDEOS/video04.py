input_str_1="abc de"
input_str_2="LuCiDProGramMinG"

vowel="aeiou"

def iterative_count_consonants(input_str):
    count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowel and input_str[i].isalpha():
            count += 1
    return count

print(iterative_count_consonants(input_str_2))

def recursive_count_consonants(input_str):
    if input_str == "":
        return 0
    if input_str[0].lower() not in vowel and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])
print(recursive_count_consonants(input_str_2))
print(recursive_count_consonants(input_str_1))