from itertools import *

alph = 'парус'

n = product(alph, repeat=5)

n = sorted(n)

for i in range(len(n)):
    s = ''.join(n[i])
    if s[0] == 'у' and 'аа' not in s:
        print(i + 1)
        break