is_permutation_1 = "google"
is_permutation_2 = "ooggle"

not_permutation_1 = "not"
not_permutation_2 = "top"
#Time complexity: O(n log n)
#Space Complexity: O(l)
def is_perm_1(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    str_1 = str_1.replace(" ","")
    str_2 = str_2.replace(" ","")
    if len(str_1) != len(str_2):
        return False

    str_1 = "".join(sorted(str_1))
    str_2 = "".join(sorted(str_2))

    n = len(str_1)
    for i in range(n):
        if str_1[i] != str_2[i]:
            return False    
    return True



def is_perm_2(str_1,str_2):
    count = dict()
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    str_1 = str_1.replace(" ","")
    str_2 = str_2.replace(" ","")
    if len(str_1) != len(str_2):
        return False
    m = len(str_1)
    for a in range(m):
        count[str_1[a]] = count.get(str_1[a],0) + 1
        count[str_2[a]] = count.get(str_2[a],0) - 1
    for v in count.values():
        if v != 0:
            return False, count
    return True, count


print(is_perm_1(is_permutation_1,is_permutation_2))
print(is_perm_1(not_permutation_1,not_permutation_2))


print(is_perm_2(is_permutation_1,is_permutation_2))
print(is_perm_2(not_permutation_1,not_permutation_2))
