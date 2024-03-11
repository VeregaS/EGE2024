ans = []
for a in range(1, 1000):
    if all((not(x % a == 0)) <= ((x % 6 == 0) <= (not(x % 9 == 0))) for x in range(1, 1000)) is True:
        ans.append(a)
    
print(max(ans))
