from fnmatch import fnmatch

def f(n):
    do_k = n ** 0.5
    delit = set()
    for i in range(1, int(do_k) + 1):
        if n % i == 0:
            delit.add(i)
            delit.add(n // i)
    return sum(delit)



for n in range(10*6, 10**7, 1):
    if fnmatch(str(n), '9?*55*7'):
        sum_n = sum([int(j) for j in str(n)])
        print(n, f(n) % 21)

