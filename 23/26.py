def f(curr, end):
    if curr == end:
        return 1
    if curr > end or curr == 25:
        return 0
    if curr < end:
        return f(curr * 2, end) + f(curr + 1, end)

print(f(2, 14) * f(14, 29))
