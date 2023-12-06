a, b = map(int, input().split(" "))

if b >= 95 and a >= 90:
    print(100000)
elif b >= 90 and a >= 90:
    print(50000)
else:
    print(0)