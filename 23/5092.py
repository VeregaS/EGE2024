def f(start, end, counter):
    if start == end:
        return 1
    if start > end:
        return 0
    if start < end:
        if counter < 2: 
            if (start) % 2 == 0:
                return f(start + 2, end, counter) + f(start * 2, end, counter) + f(start * 2 + 1, end, counter + 1)
            if (start) % 2 != 0:
                return f(start + 2, end, counter + 1) + f(start * 2, end, counter) + f(start * 2 + 1, end, counter + 1)
        else:
            if (start) % 2 == 0:
                return f(start + 2, end, counter) + f(start * 2, end, counter)
            if (start) % 2 != 0:
                return f(start * 2, end, counter)
    

print(f(2, 35, 0))