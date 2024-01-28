# Интересное задание !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def func(n):
    bin_n = bin(n)[2:]
    new_bin_n = bin_n + bin_n[-1]
    if bin_n.count('1') % 2 == 0:
        new_bin_n += '0'
    else:
        new_bin_n += '1'
    if new_bin_n.count('1') % 2 != 0:
        new_bin_n += '1'
    return int(new_bin_n, 2)


for n in range(1, 1000):
    ans = func(n)
    if ans > 80:
        print(ans)
        break
