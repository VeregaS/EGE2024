from fnmatch import fnmatch

def preobr_v_ss(n, ss):
    ans = []
    while n > 0:
        ans.append(str(n % ss))
        n //= ss
    return ''.join(ans[::-1])

for n in range(333, 10**9, 333):
    if fnmatch(str(preobr_v_ss(n, 7)), '?213*5664'):
        print(n, n // 333)
        