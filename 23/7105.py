def f(start, end):
    if start == end:
        return 1
    if start > end  or start == 18:
        return 0
    if start < end:
        return f(start * 3, end) + f(start + 2, end)
    
print(f(4, 46) * f(46, 52))
