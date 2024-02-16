from fnmatch import *

ans = []
for n in range(2023, 10 ** 10, 2023):
    if fnmatch(str(n), '1*1'):
        ans.append([n, sum([int(i) for i in str(n)])])

ans.sort(key=lambda x: -x[1])
# print(ans[:10]) видим max длинна равна 68 и это у a[0] и a[1]
print(ans[1][0], ans[1][0] // 2023)
print(ans[0][0], ans[0][0] // 2023)