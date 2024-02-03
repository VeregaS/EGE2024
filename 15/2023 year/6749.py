# ((x + 2 * y) > a) or (y < x) or (x < 30)

ans = []
for a in range(0, 1000):
    if all( (((x + 2 * y) > a) or (y < x) or (x < 30))  for x in range(0, 1000) for y in range(0, 1000)):
        ans.append(a)
        
print(max(ans))