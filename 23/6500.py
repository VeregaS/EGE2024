def f(start, end, count_1):
    if start == end:
        return 1
    if start > end or start == 11 or start == 35:
        return 0
    if start < end:
        if count_1 < 5:
            return f(start + 1, end, count_1 + 1) + f(start + 3, end, count_1) + f(start * 2, end, count_1)
        else:
            return f(start + 3, end, count_1) + f(start * 2, end, count_1)
        

print(f(2, 18, 0) * f(18, 40, 0))