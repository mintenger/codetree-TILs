h, w = map(float, input().split())
bmi = w * 100 * 100 // (h**2)
print("%.0f" % bmi)
if bmi > 25:
    print("Obesity")