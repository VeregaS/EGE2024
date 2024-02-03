# (x + y <= 22) or (y <= (x – 6)) or (y >= a)

ans = []
for a in range(1, 1000):
        if all(((x + y <= 22) or (y <= (x - 6)) or (y >= a)) for x in range(1, 1000) for y in range(1, 1000)) is True:
            ans.append(a)
            
print(max(ans))