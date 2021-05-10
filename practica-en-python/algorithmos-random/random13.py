lst = list()
def memofib(number, memo):
    print(memo)
    if not memo[number] in memo: 
        return memo
    elif number <= 1:
        memo[number] = number
        return number
    else:
        result = memofib(number-1, memo) + memofib(number-2, memo)
        memo[number] = result
        return result
print(memofib(10, lst))

