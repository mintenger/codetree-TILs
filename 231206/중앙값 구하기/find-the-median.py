a, b, c = map(int, input().split(" "))
if a > b:
    if b > c:
        print(b)
    elif c > a:
        print(a)
    else:
        print(c)
else:
    if a > c:
        print(a)
    elif c > b:
        print(b)
    else:
        prit(c)