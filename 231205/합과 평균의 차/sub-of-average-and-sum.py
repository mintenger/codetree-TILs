a, b, c = map(int, input().split(" "))
arr = [a, b, c]
sol1 = sum(arr)
sol2 = sum(arr)/len(arr)
sol3 = sol1 - sol2
print(f"{sol1}\n{sol2:.0f}\n{sol3:.0f}")