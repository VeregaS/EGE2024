from fnmatch import fnmatch


for n in range(92, 10**8, 92):
    if fnmatch(str(n), '12*4*6?8') and int(str(n)[2]) % 2 == 0 and int(str(n)[4]) % 2 != 0:
        print(n, n // 92)

