from fnmatch import *

nechet = '13579'
for n in range(133, 10**10, 133):
    if fnmatch(str(n), '1?2157*4'):  # A - ? - одно число //// B - * - последовательность
        n_a = int(str(n)[1])
        n_b = str(n)[6:len(str(n)) - 1]
        if n_a % 2 == 0:
            if all(int(i) % 2 != 0 for i in n_b):
                print(n, n // 133)
