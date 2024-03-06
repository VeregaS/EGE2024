def f(start, end, counter_2):
    if start == end:
        return 1
    if start > end or counter_2 > 2:
        return 0
    if start < end:
        if start % 2 == 0:
            return f(start + 2, end, counter_2 + 1) + f(start * 2, end, counter_2 + 1) + f(start * 3, end, counter_2 + 1)
        if start % 2 != 0:
            return f(start + 2, end, counter_2) + f(start * 2, end, counter_2 + 1) + f(start * 3, end, counter_2)
    

print(f(1, 402, 0))