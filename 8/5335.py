from itertools import *

alph = '01234567'

ans = 0
for n in product(alph, repeat=5):
    n = ''.join(n)
    if n[0] != '0':
        if n.count('6') == 1:
            i_6 = n.index('6')
            
            if i_6 == 0:
                if int(n[i_6 + 1], 8) % 2 == 0:
                    ans += 1
            elif i_6 == 4:
                if int(n[i_6 - 1], 8) % 2 == 0:
                    ans += 1
            else:
                if int(n[i_6 - 1], 8) % 2 == 0 and int(n[i_6 + 1], 8) % 2 == 0:
                    ans += 1

print(ans)