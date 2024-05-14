import sys
from fnmatch import fnmatch

sys.setrecursionlimit(10**9)
def f(n):
    delit = set()
    for j in range(1, int((n ** 0.5)) + 1):
        if n % j == 0:
            delit.add(j)
            delit.add(n // j)
    return [len(delit), delit]


for n in range(311, 10**8, 311):
    if fnmatch(str(n), '12?5*5??'):
        a = f(n)
        if a[0] == 4:
            c = 0
            a[1].remove(n)
            for j in a[1]:
                if f(j)[0] == 2:
                    c += 1
            if c <= 3:
                print(n, n // 311)
            


# 2, 3, 5, 6, 7, 10, 11, 17, 

