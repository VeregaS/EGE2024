s = open('24/txts/24-181.txt').readline()
l,m,k = 0, 0, 0
for r in range(len(s)):
    if s[r] == '.': k += 1
    while k > 1:
        if s[l] == '.': k -= 1
        l += 1
    m = max(m, r - l + 1)

print(m)