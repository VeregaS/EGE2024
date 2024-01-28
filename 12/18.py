def func(n):
    while '222' in n or '888' in n:
        if '222' in n:
            n = n.replace('222', '8', 1)
        else:
            n = n.replace('888', '2', 1)
    return n


print(func('8' * 68))
