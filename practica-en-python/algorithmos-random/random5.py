def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s
a = input("Enter some words: ")
print(reverse(a))