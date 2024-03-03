def f(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    if start < end:
        return f(start + 1, end) + f(start + 5, end) + f(start * 3, end)
    

for end in range(2, 10*3):
    if f(1, end) == 175:
        print(end)
