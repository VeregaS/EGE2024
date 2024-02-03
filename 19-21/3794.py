def f(s, s2, m):
    if (s + s2) >= 64:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s + 1, s2, m - 1), f(s + s2, s2, m - 1), f(s, s2 + 1, m - 1), f(s, s2 + s, m -1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)

print('19) ', [s2 for s2 in range(1, 58) if f(6, s2, 2)])
print('20) ', [s2 for s2 in range(1, 58) if f(6, s2, 3) and not(f(6, s2, 1))])
print('21) ', [s2 for s2 in range(1, 58) if f(6, s2, 4) and not(f(6, s2, 2))])
