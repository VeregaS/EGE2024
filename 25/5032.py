from fnmatch import fnmatch

for n in range(10**11, 10**12, int('ba', 16)):
    if fnmatch(str(hex(n)[2:]), '1?ded?baba'):
        print(n, n // int('ba', 16))