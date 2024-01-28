def func(n):
    bin_n = bin(n)[2:]
    sum_1 = str(bin_n.count('1') % 2)
    new_bin_n = bin_n + sum_1
    sum_2 = str(new_bin_n.count('1') % 2)
    bin_r = new_bin_n + sum_2
    r = int(bin_r, 2)
    return r


for n in range(1, 1000):
    ans = func(n)
    if ans > 150:
        print(ans)
        break
