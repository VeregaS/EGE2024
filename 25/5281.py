from fnmatch import fnmatch

def f(n):
    do_k = n ** 0.5
    delit = set()
    for i in range(1, int(do_k) + 1):
        if n % i == 0:
            delit.add(i)
            delit.add(n // i)
    return sum(delit)


c = 0
for n in range(3*7*8, 10**9, 3*7*8):
    if fnmatch(str(n), '?6*6*?6') and c != 7:
        c += 1
        print(n, f(n))