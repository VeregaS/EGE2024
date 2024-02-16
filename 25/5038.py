from fnmatch import fnmatch

for n in range(17, 10**9, 17):
    if fnmatch(str(n), '12345?6?8'):
        print(n, n // 17)