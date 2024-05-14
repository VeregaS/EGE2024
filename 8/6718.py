from itertools import product
alph = 'компьютер'

a =  product(alph, repeat=5)
a = sorted(a)

ans = []
for i in range(len(a)):
    n = "".join(a[i])
    if n[0] != 'ь' and n.count('к') == 2 and (i + 1) % 2 != 0:
        ans.append(i + 1)

print(max(ans))