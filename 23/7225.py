def f(s, e, last_h):
    if s == e:
        return 1
    if s > e:
        return 0
    if last_h == "a":
        return f(s + 3, e, 'a') + f(s * 7, e, 'c')
    else:
        return f(s + 3, e, 'a') + f(s * 5, e, 'b') + f(s * 7, e, 'c')
    

print(f(1, 1000, ''))
