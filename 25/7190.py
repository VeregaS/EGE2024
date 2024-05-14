from fnmatch import fnmatch

def f(n):
    delit = set()
    for j in range(1, int((n ** 0.5)) + 1):
        if n % j == 0:
            delit.add(j)
            delit.add(n // j)
    return len(delit)


for i in range(2273, 10**9, 2273):
    if fnmatch(str(i), "5*35?5*1"):
        sum_i = sum([int(j) for j in str(i)])
        if f(sum_i) == 2:
            print(i, i // 2273)