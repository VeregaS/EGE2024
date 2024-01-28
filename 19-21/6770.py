def f(s, n):
    if s >= 82:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [f(s + 2, n - 1), f(s + 4, n - 1), f(s * 3, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print('19) ', [s for s in range(1, 82) if f(s, 2)]) # all на any поменяй т.к "неудачного хода"
print('20) ', [s for s in range(1, 82) if f(s, 3) and not f(s, 1)])
print('21) ', [s for s in range(1, 82) if f(s, 4) and not f(s, 2)])