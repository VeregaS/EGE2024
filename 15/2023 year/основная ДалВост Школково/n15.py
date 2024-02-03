#  ((x + 2 * y) > a) or (x > 13) or (y < 44)

ans = []
for a in range(1000):
    if all( (( (x + 2 * y) > a ) or (x > 13) or (y < 44)) for x in range(1000) for y in range(1000)):
        ans.append(a)

print(max(ans))