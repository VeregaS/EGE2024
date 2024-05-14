from fnmatch import fnmatch

f = [1, 2, 3, 5, 8]
for n in range(43, 10**9, 43):
    if len(str(n)) >= 9:
        if fnmatch(str(n), '73*5*486*') and int(str(n)[4]) in f and int(str(n)[8]) in f:
            print(n, n // 43)
        