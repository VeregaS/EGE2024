def func(n):
    bin_n = bin(n)[2:]
    bin_r = bin_n + bin_n[-2] + bin_n[1]
    return int(bin_r, 2)


ans = 0
o = [i for i in range(150, 201)]
for n in range(2, 1000):
    r = func(n)
    if r in o:
        ans += 1
        
print(ans)
