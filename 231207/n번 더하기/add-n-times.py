a, n = map(int, input().split())
for i in range(a + n, a + ((n + 2) * a), n):
    print(i)