# Интересное задание !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def func(n):
    bin_n = bin(n)[2:]
    
    if bin_n.count('1') % 4 == 0:
        bin_n_1 = '10' + bin_n
    else:
        bin_n_1 = '11' + bin_n
        
    n1 = int(bin_n_1, 2)
    if n % 2 == 0:
        bin_r = bin_n_1 + '1'
    else:
        bin_r = bin_n_1 + '0'

    return int(bin_r, 2)


ns = []
for n in range(1, 1000):
    if func(n) <= 250:
        ns.append(n)
    else:
        break
    
print(max(ns))