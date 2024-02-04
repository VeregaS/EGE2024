def f(n):
    bin_n = bin(n)[2:]
    if n % 3 == 0:
        bin_r = str(bin_n) + str(bin_n)[-3:]
    else:
        a = (n % 3) * 3
        bin_a = bin(a)[2:]        
        bin_r = str(bin_n) + str(bin_a)
    return int(bin_r, 2)

ans = []
for n in range(5000):
    res = f(n)
    if res <= 170:
        ans.append(res)
print(max(ans))