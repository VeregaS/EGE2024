from fnmatch import *


def perevod(n, ss):
    ans = ''
    while n > 0:
        ans += str(n % ss)
        n //= ss
    return ans[::-1]


for n in range(1, 2023 ** 3):
    if fnmatch(str(n), '*2*0'):
        a = perevod(n, 3)
        if str(a) == str(a)[::-1]:
            b = perevod(n, 7)
            if str(b) == str(b)[::-1]:
                c = str(perevod(n, 8))
                print(n, sum([int(i) for i in c]))
