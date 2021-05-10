lst = list()
for a in range(1,1000000):
    lst.append(a)
target = 25000

# Linear Search iterable method
def linear_search(data,target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False
#print(linear_search(lst,target))

# Iterative Binary Search 
def iterative_binary_search(data,target):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
#print(iterative_binary_search(lst,target))

# recursive binary search
def recursive_binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data [mid]:
            return recursive_binary_search(data, target, low, mid-1), data[mid]
        else:
            return recursive_binary_search(data, target, mid+1, high), data[mid]
print(recursive_binary_search(lst, target, 0, len(lst)))



