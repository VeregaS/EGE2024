from fnmatch import *

for n in range(2023, 10 ** 8, 2023):
    if fnmatch(str(n), '3?1*57'):
        print(n, n // 2023)