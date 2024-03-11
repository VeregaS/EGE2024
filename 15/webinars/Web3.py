# (2x + y != 70) or (x < y) or (a < x)

ans = []
for a in range(1, 1000):
    if all(((2 * x + y != 70) or (x < y) or (a < x)) for x in range(1, 1000) for y in range(1, 1000)) is True:
        ans.append(a)
        
print(max(ans))
