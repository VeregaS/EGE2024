def f(s1, s2, n):
    if s1 < 10 or s2 < 10:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [f(s1 - 1, s2, n - 1), f(s1 - 3, s2, n - 1), f(s1, s2 - 1, n - 1), f(s1, s2 - 3, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print('19) ', [s for s in range(11, 1000) if f(s, s, 2) and not f(s, s, 1)])
print('20) ', [s2 for s2 in range(10, 1000) if f(13, s2, 3) and not f(13, s2, 1)])
print('21) ', [s2 for s2 in range(10, 1000) if f(13, s2, 4) and not f(13, s2, 2)])
