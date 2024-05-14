from fnmatch import fnmatch

for n in range(2023, 10**9, 2023):
    if fnmatch(str(n), '1*1*1?'):
        if n % 2023 == 0 and n % 19 == 0 and n % 6 == 0:
            print(n, n // 2023)

