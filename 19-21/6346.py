def f(s1, s2, n):
    if (s1 + s2) >= 60:
        return n % 2 == 0
    if n == 0:
        return 0
    if s1 == s2:
        h = [f(s1 + 1, s2, n - 1), f(s1 + 2, s2, n - 1), f(s1 + 3, s2, n - 1), 
             f(s1, s2 + 1, n - 1), f(s1, s2 + 2, n - 1), f(s1, s2 + 3, n - 1)]
    if s1 > s2:
        h = [f(s1 + 1, s2, n - 1), f(s1 + 2, s2, n - 1), f(s1 + 3, s2, n - 1), f(s1, s2 * 2, n - 1)]
    if s2 > s1:
        h = [f(s1, s2 + 1, n - 1), f(s1, s2 + 2, n - 1), f(s1, s2 + 3, n - 1), f(s1 * 2, s2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


ans = []
for s1 in range(1, 100):
    for s2 in range(1, 100):
        if f(s1, s2, 1):
            ans.append(s1 + s2)
print('19)', min(ans))
print('20)', [s2 for s2 in range(1, 48) if f(12, s2, 3) and not f(12, s2, 1)])
print('21)', [s2 for s2 in range(1, 35) if not f(25, s2, 2) and f(25, s2, 4)])

