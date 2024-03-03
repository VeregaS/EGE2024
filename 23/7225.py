def f(start, end, last_h):
    if start == end:
        return 1
    if  start > end:
        return 0
    if start < end:
        if last_h != 'A':
            return f(start + 3, end, 'A') + f(start * 5, end, 'B') + f(start * 7, end, 'C')
        if last_h == 'A':
            return f(start + 3, end, 'A') + f(start * 7, end, 'C')

    

print(f(1, 1000, '')) 