s = open('24/txts/24-2.txt').readline()
for i in range(100, 0, -1):
    s = s.replace('.'*i, '.')
s = s.split('.')

ans = []
for i in s:
    if s.count('A') >= 3:
        ans.append(len(i))
print(max(ans))
