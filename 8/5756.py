from itertools import product

words = product('АНТИУОПЯ*', repeat=7) # * - АНТИУТОПИЯ

ans = 0
for word in words:
    word = ''.join(word)
    if word.count('*') == 1:
        sogl = [i for i in word if i in 'НТП']
        gl = [i for i in word if i in 'АИУОЯ']
        if gl == sorted(gl) and sogl == sorted(sogl, reverse=True) and len(sogl) <= 2:
            ans += 1

print(ans)
