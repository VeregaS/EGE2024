from itertools import product

vars = product('ЕГЭ', repeat=5)

ans = 0
for i in vars:
    word = ''.join(i)
    if word[0] != 'Г':
        ans += 1
print(ans)
