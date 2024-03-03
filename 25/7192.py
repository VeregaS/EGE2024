from fnmatch import *

def all_delit_n(n):
    d = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return d


for n in range(2627, 10 ** 9, 2627):
    if fnmatch(str(n), '7*53?3*1'):
        sum_n = sum([int(i) for i in str(n)])
        if len(all_delit_n(sum_n)) == 2:
            print(n, n // 2627)
        

