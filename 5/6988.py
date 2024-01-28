# Интересное задание !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def func(n):
    bin_n = bin(n)[2:]
    new_bin = bin_n.replace('1', '2').replace('0', '1').replace('2', '0')
    if new_bin.count('1') % 2 == 0:
        bin_r = new_bin + '0'
    else:
        bin_r = new_bin + '1'
        
    return int(bin_r, 2)


rs = []
for n in range(1, 1000):
    ans = func(n)
    if ans < 170:
        rs.append(ans)
print(max(rs))
