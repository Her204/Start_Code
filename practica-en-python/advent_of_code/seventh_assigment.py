date = open("input_4.txt")
lst = list()
i = 0
e = ""
total = 0
for a in date:
    q = a
    if a != "\n":
        e += q[:-1] + " "
    if a == "\n":
        quark = e[:-1].split(" ")
        quark.sort()
        lst.append(quark)
        total += 1
        e = ""
        continue

right = 0
error = 0
range = 0
count = dict()
eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
lst_ = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
for element in lst:
    range += 1
    if element[1].split(":")[0] != "cid" and len(element) == 7:
        right += 1
        if int(element[0].split(":")[1]) >= 1920 and int(element[0].split(":")[1]) <= 2002:
            if element[1].split(":")[1] in eyecolors:
                if int(element[2].split(":")[1]) >= 2020 and int(element[2].split(":")[1]) <= 2030:
                    if len(element[3].split(":")[1]) == 7:
                        if element[4].split(":")[1][-2:] == "cm" and int(element[4].split(":")[1][:-2]) >= 150 and int(element[4].split(":")[1][:-2]) <= 193:
                            if int(element[5].split(":")[1]) >= 2010 and int(element[5].split(":")[1]) <= 2020:
                                if len(element[6].split(":")[1]) == 9:
                                    i += 1
                                    #print(element)
                                    count[element[-1]] = count.get(element[-1], 0) + 1
                        if element[4].split(":")[1][-2:] == "in" and int(element[4].split(":")[1][:-2]) >= 59 and int(element[4].split(":")[1][:-2]) <= 76:
                            if int(element[5].split(":")[1]) >= 2010 and int(element[5].split(":")[1]) <= 2020: 
                                if len(element[6].split(":")[1]) == 9:
                                    i += 1
                                    #print(element)
                                    count[element[-1]] = count.get(element[-1], 0) + 1
    elif len(element) == 8:
        right += 1
        if int(element[0].split(":")[1]) >= 1920 and int(element[0].split(":")[1]) <= 2002:
            if element[2].split(":")[1] in eyecolors:
                if int(element[3].split(":")[1]) >= 2020 and int(element[3].split(":")[1]) <= 2030:
                    if len(element[4].split(":")[1]) == 7:
                        if element[5].split(":")[1][-2:] == "cm" and int(element[5].split(":")[1][:-2]) >= 150 and int(element[5].split(":")[1][:-2]) <= 193:
                            if int(element[6].split(":")[1]) >= 2010 and int(element[6].split(":")[1]) <= 2020:
                                if len(element[7].split(":")[1]) == 9:
                                    i += 1
                                    #print(element)
                                    count[element[-1]] = count.get(element[-1], 0) + 1
                        if element[5].split(":")[1][-2:] == "in" and int(element[5].split(":")[1][:-2]) >= 59 and int(element[5].split(":")[1][:-2]) <= 76:
                            if int(element[6].split(":")[1]) >= 2010 and int(element[6].split(":")[1]) <= 2020: 
                                if len(element[7].split(":")[1]) == 9:
                                    i += 1
                                    #print(element)
                                    count[element[-1]] = count.get(element[-1], 0) + 1 
    else:
        error += 1
        print(element)
print(i, "goal")
print(range, "range")
print(len(count))
print(error, "error")
print(right, "right")
