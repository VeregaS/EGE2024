from itertools import product
alph = 'мангуст'

a =  product(alph, repeat=6)
a = sorted(a)

ans = []
for i in range(len(a)):
    n = "".join(a[i])
    if n[0] != 'у' and n.count('м') == 2 and n.count('г') <= 1:
        ans.append(i + 1)

print(max(ans))