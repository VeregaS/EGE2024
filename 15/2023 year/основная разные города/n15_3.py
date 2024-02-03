# ((x + 3 * y) > a) or (x < 30) or (y < 30)

ans = []
for a in range(1000):
    if all( (((x + 3 * y) > a) or (x < 30) or (y < 30))  for x in range(1000) for y in range(1000)):
        ans.append(a)
        
print(max(ans))