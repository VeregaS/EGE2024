from fnmatch import fnmatch

def f(n):
    do_k = n ** 0.5
    delit = set()
    ans = []
    for i in range(1, int(do_k) + 1):
        if n % i == 0:
            delit.add(i)
            delit.add(n // i)
    for j in delit:
        ans.append(j)
    return ans

for n in range(10**4, 10**7):
    if fnmatch(str(n), '3*52?'):
        a = f(n)
        if len(a) % 2 != 0:
            a.remove(n)
            print(n, max(a))
        