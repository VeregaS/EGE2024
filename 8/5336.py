from itertools import *

alph = '012345678'

ans = 0
for n in product(alph, repeat=5):
    n = ''.join(n)
    if n[0] != '0':
        if int(n[0], 9) % 2 == 0 and n[-1] != '1' and n[-1] != '8' and n.count('3') <= 1:
            ans += 1

print(ans)