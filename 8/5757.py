from itertools import product

words = list(product('АНТИУОПЯ*', repeat=7)) # * - АНТИУТОПИЯ

ans = 0
for word in words:
    word = ''.join(word)
    if word.count('*') == 1:
        word = word.split('*')
        sogl_l = [i for i in word[0] if i in 'НТП']
        gl_l = [i for i in word[0] if i in 'АИУОЯ']
        
        sogl_r = [i for i in word[1] if i in 'НТП']
        gl_r = [i for i in word[1] if i in 'АИУОЯ']
        
        if sogl_r == sorted(sogl_r):
            if gl_r == sorted(gl_r, reverse=True):
                if sogl_l == sorted(sogl_l, reverse=True):
                    if gl_l == sorted(gl_l):
                        ans += 1

print(ans)
