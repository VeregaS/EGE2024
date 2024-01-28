from itertools import product

words = product('АНДРЕЙ', repeat=7)

ans = 0
for word in words:
    word = ''.join(word)
    if word.count('А') == 1 and word.count('Й') == 1 and word[0] != 'Й':
        ans += 1
        
print(ans)
