item = list()
f = [cool for cool in range(1,1000) if cool > 10 for a in range(1,10) if cool%a==0]
print(f)