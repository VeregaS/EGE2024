def f(s, n):
    if s == 0:
        return n % 2 == 0
    if n == 0:
        return 0
    if s % 2 == 0:
        h = [f(s - 5, n - 1), f(s - (s // 2), n - 1)]
    else:
        h = [f(s - 5, n - 1), f(s - ((s // 2) + 1), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print('1) ', [s for s in range(13, 1000) if f(s, 3) and not f(s, 1)])