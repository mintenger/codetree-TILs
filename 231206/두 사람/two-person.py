p1 = input().split(" ")
p1_age = int(p1[0])
p1_sex = str(p1[1])

p2 = input().split()
p2_age = int(p2[0])
p2_sex = str(p2[1])

if (p1_age >= 19 and p1_sex=="M") or (p2_age >= 19 and p2_sex=="M"):
    print(1)
else:
    print(0)