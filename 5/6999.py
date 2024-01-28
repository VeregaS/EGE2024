def func(N):
    bin_n = bin(N)[2:]
    if bin_n.rfind('0'):
        bin_r = f"{bin_n[:-1]}{bin_n[:2]}"
        new_bin_r = bin_r[::-1]
        return int(str(new_bin_r), 2)
    
    
for n in range(0, 1000):
    if func(n) == 123:
        print(n)
        break


a = '111000111101'
print(a.rfind("0"))
a = a[:10] + ' ABC ' + a[10 + 1:]
print(a)
