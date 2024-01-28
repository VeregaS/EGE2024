def f(s, n):
    if s >= 100:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [f(s + 7, n - 1), f(s * 2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print('19) ', [s for s in range(1, 100) if f(s, 2)]) # all на any поменяй т.к "поддается"
# 20 не знаю
print('21) ', [s for s in range(1, 100) if f(s, 4)])