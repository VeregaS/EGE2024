from itertools import product

words = product('УОА', repeat=5)

ans = []
for word in words:
    word = ''.join(word)
    ans.append(word)

print(ans[239])

