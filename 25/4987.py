from fnmatch import fnmatch

for n in range(17, 10**9, 17):
    if fnmatch(str(n), '1?34567?9'):
        print(n, n // 17)
        