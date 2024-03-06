def f(start, end):
    if start == end:
        return 1
    if start < end  or start == 27:
        return 0
    if start > end:
        return f(start - 1, end) + f(start - 5, end)
    
print(f(32, 26) * f(26, 24) * f(24, 17))