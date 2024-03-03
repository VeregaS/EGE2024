from fnmatch import *

ans = []

for n in range(4546, 10**10, 4546):
    if fnmatch(str(n), '8*80*06'):
        ans.append([n, n // 4546])
        
for i in range(0, len(ans), 60):
    print(*ans[i])