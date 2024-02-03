# ((y + 3x) > a) or (x < 20) or (y < 50)

ans = []
for a in range(1, 1000):
    if all( ( ((y + 3 * x) > a) or (x < 20) or (y < 50) ) for x in range(1000) for y in range(1000)):
        ans.append(a)

print(max(ans))