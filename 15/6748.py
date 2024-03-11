# (x * y < a) or (x < y) or (9 < x)

for a in range(10**3):
    if all ( ((x * y < a) or (x < y) or (9 < x)) for x in range(10**3) for y in range(10**3)):
        print(a)
        break
