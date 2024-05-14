from itertools import *
alph = '0123456789ABCDEF'

ans = 0
for n in product(alph, repeat=3):
    n = ''.join(n)
    if n[0] != '0':
        if len(set(n)) == len(n):
            if int(n[0], 16) % 2 == 0 and int(n[1], 16) % 2 != 0 and int(n[2], 16) % 2 == 0:
                ans += 1
            if int(n[0], 16) % 2 != 0 and int(n[1], 16) % 2 == 0 and int(n[2], 16) % 2 != 0:
                ans += 1

print(ans)
