date = open("input_5.txt")
lst = []
e = ""
counter = 0
total = 0
for a in date:
    counter += 1
    if a != "\n":
        e += a[:-1] + " "
    if a == "\n":
        quark = e[:-1].split(" ")
        quark.sort()
        e = ""
        lst.append(quark)
        continue

def byr(byr1):
    if int(byr1) >= 1920 and int(byr1) <= 2002:
        return True
    return False

def iyr(iyr1):
    if int(iyr1) >= 2010 and int(iyr1) <= 2020:
        return True
    return False

def eyr(eyr1):
    if int(eyr1) >= 2020 and int(eyr1) <= 2030:
        return True
    return False

def hgt(hgt1):
    if hgt1[-2:] == "cm" and int(hgt1[:-2]) >= 150 and int(hgt1[:-2]) <= 193:
        return True
    if hgt1[-2:] == "in" and int(hgt1[:-2]) >= 59 and int(hgt1[:-2]) <= 76:
        return True
    return False

def hcl(hcl1):
    lst_ = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    if len(hcl1) == 7:
        return True
    return False

def ecl(ecl1):
    eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl1 in eyecolors:
        return True
    return False

def pid(pid1):
    if len(pid1) == 9:
        return True
    return False

acv = 0
qdh = 0
error = 0
total = 0
lst2 = []

for element in lst:
    total += 1
    if element[1].split(":")[0] != "cid" and len(element) == 7:
        qdh += 1
        if byr(element[0].split(":")[1]) == True and ecl(element[1].split(":")[1]) == True:
            if eyr(element[2].split(":")[1]) == True and hcl(element[3].split(":")[1]) == True:
                if hgt(element[4].split(":")[1]) == True and iyr(element[5].split(":")[1]) == True: 
                    if pid(element[6].split(":")[1]) == True:
                        #print(element)
                        acv += 1
    elif len(element) == 8:
        qdh += 1
        if byr(element[0].split(":")[1]) == True and ecl(element[2].split(":")[1]) == True:
            if eyr(element[3].split(":")[1]) == True and hcl(element[4].split(":")[1]) == True:
                if hgt(element[5].split(":")[1]) == True and iyr(element[6].split(":")[1]) == True:
                    if pid(element[7].split(":")[1]) == True:
                        #print(element)
                        acv += 1
    else:
        error += 1
        print(element)
print(acv, "values")     
print(qdh, "limit")
print(error , "error")
print(total, "total")
print(counter)