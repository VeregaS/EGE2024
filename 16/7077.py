def g(n):
    if n < 10:
        return n
    elif n >= 10:
        return g(n - 2) + 1


def f(n):
    return g(n - 1)


ans = 0

for n in range(1, 101):
    a = f(n)
    if (a ** 0.5) % 1 == 0:
        ans += 1

print(ans)

