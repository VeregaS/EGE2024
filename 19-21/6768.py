def f(s, n):
    if s >= 59:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [f(s + 1, n - 1), f(s + 4, n - 1), f(s * 3, n -1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print('19) ', [s for s in range(1, 59) if f(s, 2)])
print('20) ', [s for s in range(1, 59) if not f(s, 1) and f(s, 3)])
print('21) ', [s for s in range(1, 59) if not f(s, 2) and f(s, 4)])