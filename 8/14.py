from itertools import product

words = product('ПИР', repeat=5)

ans = 0
for word in words:
    word = ''.join(word)
    if word.count('П') == 1:
        ans += 1
print(ans)
