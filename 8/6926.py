from itertools import product

words = list(product('ЧИСТЫЙРАЗУМ', repeat=5))

ans = 0
for word in words:
    if word.count('Й') <= 1:
        ans += 1
print(ans)
