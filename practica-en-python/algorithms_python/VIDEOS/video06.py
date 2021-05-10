# String Processing: Look- and- Say Sequence
#The sequence starts with the number: 1

# We then say how many of each integer exists 
# in the sequence to generate the next term. For intance,
#  there is "one 1". This gives the next term: 11

#Given some integer, n. Deermine the n.th term in the "look-and-say" sequence.
#Example:
#For n=4, the 4.th term in the sequence is 1211.


def iterative_look_and_say_sequence(number):
    result = []
    i = 0
    while i < len(number):
        count = 1
        while i + 1 < len(number) and number[i] == number[i+1]:
            i += 1
            count += 1
        result.append(str(count) + number[i])
        i += 1
    return "".join(result)
s = "1"
n = 10
for a in range(n):
    s = iterative_look_and_say_sequence(s)
    print(s)





    
        


