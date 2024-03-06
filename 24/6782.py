s = open('24/txts/24-264.txt').readline()

letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'

for i in range(len(s)):
    if s[i] in letters:
        s = s.replace(s[i], '*')
    if s[i] in numbers:
        s = s.replace(s[i], '_')

ans = []

for n in range(1, 10*3):
    s1 = '*_' * n
    s2 = '_*' * n
    if s1 in s or s2 in s:
        ans.append(n * 2)
    if (s1 + '*') in s or (s2 + '_') in s:
        ans.append(n * 2 + 1)

print(max(ans))