def func(n):
    if n <= 3:
        return n
    else:
        if n % 2 == 0:
            return n + 3 + func(n - 1)
        else:
            return n * n + func(n - 2)

c = 0
for n in range(1, 1001):
    if func(n) % 7 == 0:
        c += 1
print(c)
